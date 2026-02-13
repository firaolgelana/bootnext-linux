import re

def parse_boot_entries(efibootmgr_output):
    """
    Parses efibootmgr output into a structured list.
    Returns: [{'id': '0001', 'label': 'Windows Boot Manager'}, ...]
    """
    entries = []
    # Regex to capture BootXXXX and the Name
    # Matches: Boot0001* Windows Boot Manager
    regex = r"^Boot([0-9A-F]+)\*?\s+(.*)$"
    
    lines = efibootmgr_output.splitlines()
    for line in lines:
        match = re.search(regex, line)
        if match:
            entries.append({
                'id': match.group(1),
                'label': match.group(2).strip()
            })
            
    return entries

def find_target_entries(entries_list, keywords):
    """
    Returns a LIST of matching entries.
    """
    matches = []
    for entry in entries_list:
        for keyword in keywords:
            if keyword.lower() in entry['label'].lower():
                # Avoid duplicates if multiple keywords match same entry
                if entry not in matches:
                    matches.append(entry)
                break
    return matches