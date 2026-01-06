import os
import urllib.request
import zipfile
import platform

def install_adb():
    system = platform.system()
    urls = {
        "Windows": "https://dl.google.com/android/repository/platform-tools-latest-windows.zip",
        "Darwin": "https://dl.google.com/android/repository/platform-tools-latest-darwin.zip",
        "Linux": "https://dl.google.com/android/repository/platform-tools-latest-linux.zip"
    }
    if system not in urls: return False
    try:
        print("[*] Downloading ADB...")
        urllib.request.urlretrieve(urls[system], "adb.zip")
        with zipfile.ZipFile("adb.zip", 'r') as zip_ref:
            zip_ref.extractall(".")
        os.remove("adb.zip")
        return True
    except:
        return False