import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def lookup_username(username):
    print(Fore.CYAN + f"\n[+] Searching direct profile links for username: '{username}'...\n")
    print(Fore.YELLOW + f"{'Platform':<20} | {'Status':<15} | {'Direct Profile Link':<40}")
    print(Style.BRIGHT + "-" * 85)

    # List of 12 major platforms
    websites = {
        "Instagram": f"https://www.instagram.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "GitHub": f"https://github.com/{username}",
        "Telegram": f"https://t.me/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Twitter (X)": f"https://x.com/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    found_count = 0

    for name, url in websites.items():
        try:
            # Checking if the URL is valid/exists
            response = requests.get(url, headers=headers, timeout=5, allow_redirects=False)
            
            if response.status_code == 200:
                print(f"📌 {Fore.GREEN + name:<18} | {Fore.GREEN}🟢 FOUND       {Style.RESET_ALL} | {Fore.LIGHTBLUE_EX + url}")
                found_count += 1
            else:
                print(f"❌ {Fore.RED + name:<18} | {Fore.RED}🔴 NOT FOUND   {Style.RESET_ALL} | {Fore.WHITE + url}")
                
        except requests.exceptions.RequestException:
            print(f"⚠️ {Fore.YELLOW + name:<18} | {Fore.YELLOW}🟡 ERROR       {Style.RESET_ALL} | -")

    print(Style.BRIGHT + "-" * 85)
    print(Fore.CYAN + f"\n[+] Search completed! Total {found_count} profiles identified.")

if __name__ == "__main__":
    print(Fore.MAGENTA + Style.BRIGHT + "=== ADVANCED DIRECT USER-FINDER ===")
    user_input = input(Fore.BLUE + "Enter username to scan: " + Style.RESET_ALL).strip()
    if user_input:
        lookup_username(user_input)
    else:
        print(Fore.RED + "Please enter a valid username!")
