import subprocess
from core import parser
import config

def get_windows_entry():
    """Runs efibootmgr and finds Windows."""
    try:
        result = subprocess.run(["efibootmgr"], stdout=subprocess.PIPE, text=True, check=True)
        entries = parser.parse_boot_entries(result.stdout)
        
        # Use keywords from config
        boot_id, label = parser.find_windows_id(entries, config.WINDOWS_LABEL_KEYWORDS)
        return boot_id, label
    except Exception as e:
        print(f"Error scanning boot entries: {e}")
        return None, None

def set_next_boot(boot_id):
    """Sets BootNext variable."""
    cmd = ["efibootmgr", "-n", boot_id]
    subprocess.run(cmd, check=True)

def reboot_system():
    subprocess.run(["reboot"])