import subprocess
from core import parser
import config

# Add this function
def get_efibootmgr_output():
    """Returns the raw text output of efibootmgr."""
    try:
        result = subprocess.run(["efibootmgr"], stdout=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except Exception as e:
        print(f"Error running efibootmgr: {e}")
        return ""

def set_next_boot(boot_id):
    """Sets BootNext variable."""
    cmd = ["efibootmgr", "-n", boot_id]
    subprocess.run(cmd, check=True)

def reboot_system():
    subprocess.run(["reboot"])

