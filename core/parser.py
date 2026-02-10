import re

def parse_boot_entries(efibootmgr_output):
    """
    Returns a dictionary of { 'Label': 'ID' }
    Example output: {'Windows Boot Manager': '0001', 'Ubuntu': '0000'}
    """
    entries = {}
    # Regex to capture BootXXXX and the Name
    regex = r"Boot([0-9A-F]+)\*?\s+(.*)"
    
    lines = efibootmgr_output.splitlines()
    for line in lines:
        match = re.search(regex, line)
        if match:
            boot_id = match.group(1)
            label = match.group(2).strip()
            entries[label] = boot_id
            
    return entries

def find_windows_id(entries_dict, keywords):
    """Finds the ID matching one of the keywords."""
    for label, boot_id in entries_dict.items():
        for keyword in keywords:
            if keyword.lower() in label.lower():
                return boot_id, label
    return None, None