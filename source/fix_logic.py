import subprocess
import os
import time
from utils.system_check import get_local_adb_path

def wait_for_device(adb):
    """Wait until a device is connected and authorized."""
    print("[*] Waiting for device... (Ensure USB Debugging is ON)")
    while True:
        result = subprocess.run([adb, "get-state"], capture_output=True, text=True)
        if "device" in result.stdout:
            print("[✔] Device connected and authorized.")
            break
        elif "unauthorized" in result.stderr or "unauthorized" in result.stdout:
            print("[!] Device unauthorized! Please accept the prompt on your phone screen.", end="\r")
        else:
            print("[?] Looking for device... Make sure Developer Options are enabled.", end="\r")
        time.sleep(2)

def run_patch():
    adb = get_local_adb_path()
    if not os.path.exists(adb): adb = "adb"
    
    wait_for_device(adb)
    
    print("[*] Applying Softfix (Disabling Logkit)...")
    try:
        cmd = [adb, "shell", "pm", "disable-user", "--user", "0", "com.nothing.logkit"]
        subprocess.run(cmd, check=True)
        print("[✔] Done! Logkit has been disabled.")
    except Exception as e:
        print(f"[✘] Failed to patch: {e}")
    input("\nPress Enter to return to menu...")

def run_unpatch():
    adb = get_local_adb_path()
    if not os.path.exists(adb): adb = "adb"
    
    wait_for_device(adb)
    
    print("[*] Reverting Fix (Enabling Logkit)...")
    try:
        cmd = [adb, "shell", "pm", "enable", "--user", "0", "com.nothing.logkit"]
        subprocess.run(cmd, check=True)
        print("[✔] Done! Logkit has been enabled.")
    except Exception as e:
        print(f"[✘] Failed to unpatch: {e}")
    input("\nPress Enter to return to menu...")