# NothingOS Logkit Softfix Tool

**Created by: KunaiBox**

This is a portable Python-based utility designed to manage the Logkit package on NothingOS devices. It helps users apply a "softfix" by toggling the system package state without needing to manually install ADB or configure system environment variables.

---

## Technical Overview

The tool is designed to be completely portable. On the first run, it checks for the presence of ADB (Android Debug Bridge). If it isn't found, the tool downloads the official Google Platform Tools directly into the project folder. This ensures your computer's system files remain clean and untouched.

---

## From Compiled Exe
1. Download the [Latest Release](https://github.com/kunaibox/NothingOS-Logkit-Softfix/releases/latest) (`v1.0.0`).
2. Run the exe and follow the on-screen instructions.
> [!NOTE]
> This tool is portable. To completely uninstall it, simply delete the `.exe` and the `platform-tools` folder that it creates in your directory.

## From source
### Prerequisites
1. **Python 3.10 or higher**: Ensure Python is installed and added to your system PATH.
2. **Nothing Phone**: A device running NothingOS with a USB data cable.

### Installation and Execution
1. Download the repository as a ZIP and extract it to a folder.
2. python main.py
> [!NOTE]
> This tool is portable. To completely uninstall it, simply delete the folder.
---

## How to Enable USB Debugging

For the tool to communicate with your phone, you must enable Developer Options:

1. Open **Settings** on your phone.
2. Go to **About phone** > **NOTHING OS(Wide image)**.
3. Tap **Build number** exactly 7 times.
4. Go back to **Settings** > **System** > **Developer options**.
5. Find **USB Debugging** and turn it **ON**.
6. Connect the phone to your PC. If a prompt appears on the phone asking to "Allow USB Debugging," select "Always allow" and tap **Allow**.



---

## Usage Guide

### 1. Patch (Disable Logkit)
This option runs the command to disable the Logkit package for the main user. This is the primary "softfix" action.
* **Command:** `adb shell pm disable-user --user 0 com.nothing.logkit`

### 2. Unpatch (Enable Logkit)
This option restores the Logkit package. 
* **Command:** `adb shell pm enable --user 0 com.nothing.logkit`
* **Important:** You must perform this action before installing any official NothingOS OTA (System) updates to ensure the update process finishes correctly.

---

## Important Disclaimer
Using this tool to modify system packages is done at your own risk. The author is not responsible for any software issues or data loss. Always ensure you have a backup of important data before performing system-level modifications.

---

## License
This project is licensed under the MIT License.
