import os
from utils.input_handler import get_single_key
from utils.system_check import is_adb_installed
from utils.install_adb import install_adb
import fix_logic

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print("==========================================")
    print("      NothingOS Logkit Softfix Tool       ")
    print("==========================================")
    
    # Check for ADB
    if not is_adb_installed():
        print("[!] ADB not found. It is required for this tool.")
        print("Download and install ADB automatically? (y/n)")
        while True:
            choice = get_single_key().lower()
            if choice == 'y':
                if install_adb(): 
                    print("[✔] ADB Installed.")
                    break
                else: exit("[✘] Failed to install ADB.")
            elif choice == 'n': exit("[!] Exiting...")

    while True:
        clear_screen()
        print("==========================================")
        print("      NothingOS Logkit Softfix Tool       ")
        print("==========================================")
        print("SELECT AN OPTION:")
        print(" [1] Patch (Disable Logkit)")
        print(" [2] Unpatch (Enable Logkit - Use after OS Update)")
        print(" [Q] Quit")
        
        choice = get_single_key().lower()
        if choice == '1':
            fix_logic.run_patch()
        elif choice == '2':
            fix_logic.run_unpatch()
        elif choice == 'q':
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()