from menu import Menu, MenuManager, MenuItemType

# Example callback functions
def noclip_toggle(enabled):
    print(f"\n[LOG] Noclip: {'ENABLED' if enabled else 'DISABLED'}")
    input("Press Enter to continue...")

def godmode_toggle(enabled):
    print(f"\n[LOG] God Mode: {'ENABLED' if enabled else 'DISABLED'}")
    input("Press Enter to continue...")

def speed_changed(value):
    print(f"\n[LOG] Player Speed: {value}%")
    input("Press Enter to continue...")

def fov_changed(value):
    print(f"\n[LOG] Field of View: {value}°")
    input("Press Enter to continue...")

def give_item():
    print(f"\n[LOG] Item given to player!")
    input("Press Enter to continue...")

def teleport_home():
    print(f"\n[LOG] Teleported to home!")
    input("Press Enter to continue...")

def kick_player():
    print(f"\n[LOG] Player kicked from server!")
    input("Press Enter to continue...")

def ban_player():
    print(f"\n[LOG] Player banned!")
    input("Press Enter to continue...")

def spawn_airdrop():
    print(f"\n[LOG] Airdrop spawned!")
    input("Press Enter to continue...")

def mute_player():
    print(f"\n[LOG] Player muted!")
    input("Press Enter to continue...")

def unmute_all():
    print(f"\n[LOG] All players unmuted!")
    input("Press Enter to continue...")

def wipe_server():
    print(f"\n[LOG] Server data wiped!")
    input("Press Enter to continue...")

def set_time(value):
    print(f"\n[LOG] Server Time: {value}:00")
    input("Press Enter to continue...")

def set_weather(value):
    weathers = ["Clear", "Rain", "Fog", "Storm"]
    print(f"\n[LOG] Weather: {weathers[value % len(weathers)]}")
    input("Press Enter to continue...")

# Create main menu
main_menu = Menu("OXIDE MOD MENU")

# Player Section
player_menu = main_menu.add_submenu("Player")
player_menu.add_label("--- Player Settings ---")
player_menu.add_toggle("Noclip", noclip_toggle)
player_menu.add_toggle("God Mode", godmode_toggle)
player_menu.add_slider("Speed Multiplier", speed_changed, min_val=50, max_val=200, default=100)
player_menu.add_slider("FOV", fov_changed, min_val=60, max_val=120, default=90)
player_menu.add_button("Give Item", give_item)
player_menu.add_button("Teleport Home", teleport_home)

# Admin Section
admin_menu = main_menu.add_submenu("Admin")
admin_menu.add_label("--- Admin Tools ---")
admin_menu.add_button("Kick Player", kick_player)
admin_menu.add_button("Ban Player", ban_player)
admin_menu.add_button("Mute Player", mute_player)
admin_menu.add_button("Unmute All", unmute_all)
admin_menu.add_button("Spawn Airdrop", spawn_airdrop)
admin_menu.add_button("Wipe Server", wipe_server)

# Server Section
server_menu = main_menu.add_submenu("Server")
server_menu.add_label("--- Server Settings ---")
server_menu.add_slider("Time (Hour)", set_time, min_val=0, max_val=23, default=12)
server_menu.add_slider("Weather", set_weather, min_val=0, max_val=3, default=0)
server_menu.add_label("")
server_menu.add_label("Current Players: 23/64")
server_menu.add_label("Server FPS: 60")

# Settings Section
settings_menu = main_menu.add_submenu("Settings")
settings_menu.add_label("--- Menu Settings ---")
settings_menu.add_toggle("Show Notifications", lambda x: None)
settings_menu.add_toggle("Show Keybinds", lambda x: None)
settings_menu.add_slider("Menu Opacity", lambda x: None, min_val=0, max_val=100, default=80)
settings_menu.add_label("")
settings_menu.add_label("Version: 1.0.0")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("  FPS MOD MENU - OXIDE STYLE")
    print("="*50)
    print("\nStarting menu system...")
    print("Controls:")
    print("  [W] - Move Up")
    print("  [S] - Move Down")
    print("  [E] - Select/Execute")
    print("  [Q] - Back")
    print("  [A] - Decrease Value (Sliders)")
    print("  [D] - Increase Value (Sliders)")
    print("\nPress Enter to start...\n")
    input()
    
    # Create and run the menu
    menu_manager = MenuManager(main_menu)
    menu_manager.open()
