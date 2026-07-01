from banner import show_banner
from modules.output import success
from modules.output import info

def main():
    show_banner()
    info("Initializing BugHunter Toolkit...")
    success("Toolkit Loaded Successfully")

if __name__ == "__main__":
    main()
