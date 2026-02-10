import shutil
import os

def check_requirements():
    """Checks if the system is ready."""
    # 1. Check Root
    if os.geteuid() != 0:
        return False, "Root privileges required."
    
    # 2. Check tool existence
    if not shutil.which("efibootmgr"):
        return False, "efibootmgr is not installed."
        
    return True, "OK"