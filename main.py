import sys
from core import system, boot
import config

# Simple CLI entry for now to test logic
def main():
    print(f"--- {config.APP_NAME} v{config.VERSION} ---")
    
    # 1. System Check
    is_ready, msg = system.check_requirements()
    if not is_ready:
        print(f"❌ Error: {msg}")
        sys.exit(1)

    # 2. Find Windows
    print("🔍 Scanning for Windows...")
    boot_id, label = boot.get_windows_entry()
    
    if boot_id:
        print(f"✅ Found: {label} (ID: {boot_id})")
        
        # 3. User Confirmation
        confirm = input("Reboot to Windows now? (y/n): ")
        if confirm.lower() == 'y':
            print("🚀 Setting boot target...")
            boot.set_next_boot(boot_id)
            print("👋 Rebooting...")
            boot.reboot_system()
        else:
            print("Aborted.")
    else:
        print("❌ Could not find a Windows boot entry.")

if __name__ == "__main__":
    main()