#!/usr/bin/env python3
import sys
import config
from core import system, boot
from ui import cli

def main():
    # 1. Show Welcome
    cli.banner(config.APP_NAME, config.VERSION)

    # 2. Check System Requirements
    is_ready, msg = system.check_requirements()
    if not is_ready:
        cli.error(msg)
        sys.exit(1)

    # 3. Search for the OS
    cli.step("Scanning UEFI boot entries...")
    boot_id, label = boot.get_windows_entry()

    if not boot_id:
        cli.fail_search(config.WINDOWS_LABEL_KEYWORDS)
        sys.exit(1)

    # 4. Show Success and Ask Confirmation
    cli.success(label, boot_id)
    
    if cli.ask_reboot(label):
        cli.rebooting()
        try:
            boot.set_next_boot(boot_id)
            boot.reboot_system()
        except Exception as e:
            cli.error(f"Failed to set boot variable: {e}")
            sys.exit(1)
    else:
        cli.abort()

if __name__ == "__main__":
    main()