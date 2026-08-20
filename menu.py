import os
import sys
from enum import Enum

class MenuItemType(Enum):
    BUTTON = 1
    TOGGLE = 2
    SLIDER = 3
    SUBMENU = 4
    LABEL = 5

class MenuItem:
    def __init__(self, label, item_type, callback=None, value=None, min_val=0, max_val=100):
        self.label = label
        self.item_type = item_type
        self.callback = callback
        self.value = value
        self.min_val = min_val
        self.max_val = max_val
        self.children = []

class Menu:
    def __init__(self, title="Mod Menu"):
        self.title = title
        self.items = []
        self.selected_index = 0
        self.is_open = False
        self.parent_menu = None

    def add_button(self, label, callback):
        """Add a button that executes a callback"""
        item = MenuItem(label, MenuItemType.BUTTON, callback=callback)
        self.items.append(item)
        return item

    def add_toggle(self, label, callback, default=False):
        """Add a toggle (on/off) option"""
        item = MenuItem(label, MenuItemType.TOGGLE, callback=callback, value=default)
        self.items.append(item)
        return item

    def add_slider(self, label, callback, min_val=0, max_val=100, default=50):
        """Add a slider option"""
        item = MenuItem(label, MenuItemType.SLIDER, callback=callback, value=default, min_val=min_val, max_val=max_val)
        self.items.append(item)
        return item

    def add_submenu(self, label):
        """Add a submenu"""
        submenu = Menu(label)
        submenu.parent_menu = self
        item = MenuItem(label, MenuItemType.SUBMENU, value=submenu)
        self.items.append(item)
        return submenu

    def add_label(self, label):
        """Add a label (text only)"""
        item = MenuItem(label, MenuItemType.LABEL)
        self.items.append(item)
        return item

    def select_next(self):
        """Move selection down"""
        self.selected_index = (self.selected_index + 1) % len(self.items)

    def select_prev(self):
        """Move selection up"""
        self.selected_index = (self.selected_index - 1) % len(self.items)

    def get_selected_item(self):
        """Get currently selected menu item"""
        if 0 <= self.selected_index < len(self.items):
            return self.items[self.selected_index]
        return None

    def execute_selected(self):
        """Execute the selected item"""
        item = self.get_selected_item()
        if not item:
            return

        if item.item_type == MenuItemType.BUTTON:
            if item.callback:
                item.callback()

        elif item.item_type == MenuItemType.TOGGLE:
            item.value = not item.value
            if item.callback:
                item.callback(item.value)

        elif item.item_type == MenuItemType.SUBMENU:
            return item.value  # Return the submenu to open it

        return None

    def increase_slider(self):
        """Increase slider value"""
        item = self.get_selected_item()
        if item and item.item_type == MenuItemType.SLIDER:
            item.value = min(item.value + 1, item.max_val)
            if item.callback:
                item.callback(item.value)

    def decrease_slider(self):
        """Decrease slider value"""
        item = self.get_selected_item()
        if item and item.item_type == MenuItemType.SLIDER:
            item.value = max(item.value - 1, item.min_val)
            if item.callback:
                item.callback(item.value)

    def render(self):
        """Render the menu to console"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print("\n" + "=" * 50)
        print(f"  {self.title.upper()}")
        print("=" * 50 + "\n")

        for i, item in enumerate(self.items):
            prefix = "> " if i == self.selected_index else "  "
            
            if item.item_type == MenuItemType.BUTTON:
                print(f"{prefix}[{i}] {item.label}")
            
            elif item.item_type == MenuItemType.TOGGLE:
                state = "ON" if item.value else "OFF"
                print(f"{prefix}[{i}] {item.label}: {state}")
            
            elif item.item_type == MenuItemType.SLIDER:
                bar_length = 20
                filled = int((item.value / item.max_val) * bar_length)
                bar = "█" * filled + "░" * (bar_length - filled)
                print(f"{prefix}[{i}] {item.label}: [{bar}] {item.value}/{item.max_val}")
            
            elif item.item_type == MenuItemType.SUBMENU:
                print(f"{prefix}[{i}] {item.label} →")
            
            elif item.item_type == MenuItemType.LABEL:
                print(f"     {item.label}")

        print("\n" + "-" * 50)
        print("  [W] Up  [S] Down  [E] Select  [Q] Back")
        print("-" * 50 + "\n")

class MenuManager:
    def __init__(self, root_menu):
        self.root_menu = root_menu
        self.current_menu = root_menu
        self.running = True

    def open(self):
        """Open the menu"""
        self.current_menu.is_open = True
        self.run()

    def close(self):
        """Close the menu"""
        self.running = False

    def go_back(self):
        """Go back to parent menu"""
        if self.current_menu.parent_menu:
            self.current_menu = self.current_menu.parent_menu

    def handle_input(self, key):
        """Handle user input"""
        key = key.lower()

        if key == 'w':
            self.current_menu.select_prev()
        elif key == 's':
            self.current_menu.select_next()
        elif key == 'e':
            result = self.current_menu.execute_selected()
            if result and isinstance(result, Menu):
                self.current_menu = result
        elif key == 'q':
            self.go_back()
        elif key == 'a':
            self.current_menu.decrease_slider()
        elif key == 'd':
            self.current_menu.increase_slider()

    def run(self):
        """Main menu loop"""
        while self.running:
            self.current_menu.render()
            
            try:
                user_input = input("Input: ").strip()
                if not user_input:
                    continue
                
                self.handle_input(user_input)
                
                if self.current_menu == self.root_menu and not self.current_menu.parent_menu:
                    # At root level, can exit
                    pass
            
            except KeyboardInterrupt:
                print("\n\nMenu closed.")
                self.close()
            except Exception as e:
                print(f"Error: {e}")
                input("Press Enter to continue...")
