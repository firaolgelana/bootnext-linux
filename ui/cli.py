import sys

# ANSI Colors
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"

def banner(app_name, version):
    print(f"{BOLD}{CYAN}--- {app_name} v{version} ---{RESET}")

def error(message):
    print(f"{RED}❌ Error: {message}{RESET}")

def warning(message):
    print(f"{YELLOW}⚠️  Warning: {message}{RESET}")

def step(message):
    print(f"{BOLD}🔹 {message}{RESET}")

def success(label, boot_id):
    print(f"{GREEN}✅ Found Target: {BOLD}{label}{RESET}{GREEN} (ID: {boot_id}){RESET}")

def fail_search(keywords):
    print(f"{RED}❌ Could not find any boot entry matching: {keywords}{RESET}")

def ask_reboot(label):
    """Returns True if user says 'y'"""
    try:
        choice = input(f"\n🚀 Reboot to {BOLD}{label}{RESET} now? (y/n): ").lower().strip()
        return choice == 'y'
    except KeyboardInterrupt:
        print("\n")
        return False

def rebooting():
    print(f"\n{GREEN}👋 Rebooting system... See you on the other side!{RESET}")

def abort():
    print(f"{YELLOW}🛑 Operation cancelled.{RESET}")