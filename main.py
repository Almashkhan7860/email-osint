import asyncio
from holehe import core
from colorama import Fore, Style, init

# कलर को इनिशियलाइज करें
init(autoreset=True)

async def lookup_email(email):
    print(Fore.CYAN + f"\n[+] {email} के लिए सोशल मीडिया अकाउंट्स खोजे जा रहे हैं...")
    modules = core.import_submodules("holehe.modules")
    results = []
    
    for module in modules:
        try:
            await module(email, results)
        except Exception:
            continue

    print(Fore.YELLOW + f"\n{'(Website)':<25} | {'(Status)':<20}")
    print(Style.BRIGHT + "-" * 50)
    
    account_found = False
    for res in results:
        if res.get("exists"):
            account_found = True
            print(f"📌 {Fore.GREEN + res.get('name'):<22} | {Fore.GREEN}🟢 ACCOUNT FOUND")
            
    if not account_found:
        print(Fore.RED + "[-] No account associated with this email was found on any major social media platform.।")

if __name__ == "__main__":
    email = input(Fore.BLUE + "Enter your Email: " + Style.RESET_ALL)
    asyncio.run(lookup_email(email))
