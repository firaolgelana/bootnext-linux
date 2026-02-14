# 🚀 QuickBoot (Linux)

A lightweight, professional CLI utility to reboot directly into **Windows from Linux** using UEFI BootNext.

No more waiting to catch the GRUB menu.
No more manually selecting Windows during boot.

QuickBoot sets the **next boot entry safely and temporarily** using standard Linux tools.

---

## ✨ Features

* ⚡ **One-command reboot** into Windows
* 🔄 Switch back to Linux easily
* 🛡️ **Safe checks**:

  * UEFI detection
  * Secure Boot detection
  * Root privilege validation
* 🐧 Uses native `efibootmgr`
* 🖥️ Smart detection of:

  * Windows Boot Manager
  * Multiple Linux entries
  * Firmware entries
* 📦 Cross-distro support (Debian, Fedora, Arch)

---

## 📋 Requirements

* Linux (Ubuntu, Debian, Fedora, Arch, etc.)
* UEFI system (Legacy BIOS not supported)
* `efibootmgr`
* Python 3

---

# 📥 Installation

## Option A — Install via Package (Recommended)

Go to the **Releases** page:

👉 [https://github.com/firaolgelana/bootnext-linux/releases](https://github.com/firaolgelana/bootnext-linux/releases)

Download the package for your distribution.

---

## 🟠 Ubuntu / Debian / Linux Mint (`.deb`)

### Download & Install

```bash
wget https://github.com/firaolgelana/bootnext-linux/releases/latest/download/quickboot_1.0.0_all.deb
sudo apt install ./quickboot_1.0.0_all.deb
```

If dependencies are missing:

```bash
sudo apt install -f
```

---

## 🔵 Fedora (`.rpm`)

### Download & Install

```bash
wget https://github.com/firaolgelana/bootnext-linux/releases/latest/download/quickboot-1.0.0-1.noarch.rpm
sudo dnf install ./quickboot-1.0.0-1.noarch.rpm
```

---

## 🟣 Arch Linux (AUR)


### Download & Install

```bash
wget https://github.com/yourrepo/releases/download/v1.0.0/quickboot-1.0.0-1-any.pkg.tar.zst
sudo pacman -U quickboot-1.0.0-1-any.pkg.tar.zst

```

---

# 🖥 Usage

Switch next boot to Windows:

```bash
sudo quickboot windows
```


---

# 🔐 How It Works

QuickBoot wraps the standard Linux tool:

```
efibootmgr
```

It sets the **BootNext** variable in UEFI firmware.
This means:

* It does NOT permanently change boot order.
* It only affects the next reboot.
* After that, normal boot order resumes.

---

# 🗑 Uninstall

### Debian / Ubuntu

```bash
sudo apt remove quickboot
```

### Fedora

```bash
sudo dnf remove quickboot
```

### Arch

```bash
sudo pacman -R quickboot
```

---

# ⚠ Important Notes

* Only works on UEFI systems
* Requires root privileges
* Does not support Legacy BIOS
* Modifies EFI variables — use responsibly

---

# 🛠 Development

Clone repository:

```bash
git clone https://github.com/firaolgelana/bootnext-linux.git
cd bootnext-linux
```

---


