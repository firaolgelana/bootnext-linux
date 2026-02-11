# 🚀 QuickBoot (Linux)

A lightweight Python utility to reboot directly into Windows from Linux using UEFI variables.
No more waiting at the GRUB menu!

## Features
- ⚡ **One-click reboot** into Windows
- 🛡️ **Safe**: Checks for UEFI support and Root privileges
- 🐧 **Native**: Uses `efibootmgr` (standard Linux tool)

## Requirements
- Linux (Ubuntu, Fedora, Arch, etc.)
- UEFI System (Legacy BIOS not supported)
- `efibootmgr` installed

## Installation

```bash
git clone https://github.com/https://github.com/firaolgelana/quickboot-linux.git
cd quickboot-linux
sudo bash install.sh