import os
import shutil

def get_local_adb_path():
    """Returns the path where the installer puts ADB."""
    ext = ".exe" if os.name == "nt" else ""
    return os.path.abspath(os.path.join(os.getcwd(), "platform-tools", f"adb{ext}"))

def is_adb_installed():
    if shutil.which("adb"):
        return True
    return os.path.exists(get_local_adb_path())