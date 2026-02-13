#!/usr/bin/env python3
import sys
import config
from core import system, boot, parser # Ensure parser is imported
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
    
    # Get raw output
    raw_output = boot.get_efibootmgr_output() # You might need to add this getter to boot.py
    parsed_entries = parser.parse_boot_entries(raw_output)
    
    # Find matches
    targets = parser.find_target_entries(parsed_entries, config.WINDOWS_LABEL_KEYWORDS)

    selected_target = None

    if len(targets) == 0:
        cli.fail_search(config.WINDOWS_LABEL_KEYWORDS)
        sys.exit(1)
        
    elif len(targets) == 1:
        # Easy case: only one found
        selected_target = targets[0]
        
    else:
        # Complex case: Multiple found -> Show Menu
        selected_target = cli.ask_selection(targets)

    # 4. Show Success and Ask Confirmation
    # Unpack the dictionary
    boot_id = selected_target['id']
    label = selected_target['label']

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