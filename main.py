import requests
import time
import os
from colorama import Fore, Style, init

# Initialize colorama for professional CLI styling
init(autoreset=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5"
}

def get_platform_list(username):
    # Expanded to 32 major global platforms across various categories
    return {
        # Social Media & Messaging
        "Instagram": f"https://www.instagram.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Twitter (X)": f"https://x.com/{username}",
        "Telegram": f"https://t.me/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Discord (Invite)": f"https://discord.com/invite/{username}",
        
        # Coding & Tech Development
        "GitHub": f"https://github.com/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "LeetCode": f"https://leetcode.com/{username}",
        "HackerRank": f"https://www.hackerrank.com/{username}",
        "Kaggle": f"https://www.kaggle.com/{username}",
        "StackOverflow": f"https://stackoverflow.com/users/{username}",
        
        # Gaming Platforms
        "Steam (ID)": f"https://steamcommunity.com/id/{username}",
        "Roblox": f"https://www.roblox.com/user.aspx?username={username}",
        "Xbox Gamertag": f"https://account.xbox.com/en-us/profile?gamertag={username}",
        
        # Portfolio, Design & Blogging
        "Linktree": f"https://linktr.ee/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "Behance": f"https://www.behance.net/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}",
        
        # Audio & Professional Music
        "Spotify": f"https://open.spotify.com/user/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Bandcamp": f"https://bandcamp.com/{username}",
        
        # Other Services
        "DailyMotion": f"https://www.dailymotion.com/{username}",
        "Vimeo": f"https://vimeo.com/{username}"
    }

def scan_username(username):
    print(Fore.CYAN + f"\n[+] Target Username: '{username}'")
    print(Fore.YELLOW + f"{'Platform':<20} | {'Status':<15} | {'Direct Profile Link':<40}")
    print(Style.BRIGHT + "-" * 85)

    websites = get_platform_list(username)
    found_profiles = []

    for name, url in websites.items():
        try:
            time.sleep(0.5) # 0.5 second delay to ensure speed while maintaining safety
            response = requests.get(url, headers=HEADERS, timeout=5, allow_redirects=False)
            
            if response.status_code == 200:
                print(f"📌 {Fore.GREEN + name:<18} | {Fore.GREEN}🟢 FOUND       {Style.RESET_ALL} | {Fore.LIGHTBLUE_EX + url}")
                found_profiles.append((name, url))
            elif response.status_code in [403, 429]:
                print(f"🔒 {Fore.YELLOW + name:<18} | {Fore.YELLOW}🟡 BLOCKED     {Style.RESET_ALL} | - (Protected)")
            else:
                print(f"❌ {Fore.RED + name:<18} | {Fore.RED}🔴 NOT FOUND   {Style.RESET_ALL} | {Fore.WHITE + url}")
                
        except requests.exceptions.Timeout:
            print(f"⏳ {Fore.YELLOW + name:<18} | {Fore.YELLOW}🟡 TIMEOUT     {Style.RESET_ALL} | -")
        except requests.exceptions.RequestException:
            print(f"🛑 {Fore.RED + name:<18} | {Fore.RED}🔴 CONN ERROR  {Style.RESET_ALL} | -")

    print(Style.BRIGHT + "-" * 85)
    print(Fore.CYAN + f"[+] Scan completed for '{username}'. Identified profiles: {len(found_profiles)}")
    
    # Save results to text file automatically if profiles are found
    if found_profiles:
        with open("results.txt", "a") as f:
            f.write(f"\n=== SCAN REPORT FOR USERNAME: {username} ===\n")
            for name, url in found_profiles:
                f.write(f"[{name}]: {url}\n")
        print(Fore.GREEN + "[+] Active links automatically saved to 'results.txt'")

def show_saved_results():
    print(Fore.MAGENTA + Style.BRIGHT + "\n=== HISTORICAL SAVED RESULTS ===")
    if os.path.exists("results.txt"):
        with open("results.txt", "r") as f:
            print(Fore.WHITE + f.read())
    else:
        print(Fore.RED + "[-] No saved results found yet! Run a scan first.")

def main_menu():
    while True:
        print(Fore.MAGENTA + Style.BRIGHT + "\n========================================")
        print(Fore.MAGENTA + Style.BRIGHT + "===   ADVANCED OSINT USER-FINDER     ===")
        print(Fore.MAGENTA + Style.BRIGHT + "========================================")
        print(Fore.BLUE + "[1] " + Fore.WHITE + "Scan Single Username")
        print(Fore.BLUE + "[2] " + Fore.WHITE + "Scan Multiple Usernames (Comma Separated)")
        print(Fore.BLUE + "[3] " + Fore.WHITE + "View All Saved Results (results.txt)")
        print(Fore.BLUE + "[4] " + Fore.WHITE + "Exit Tool")
        
        choice = input(Fore.YELLOW + "\nSelect an option [1-4]: " + Style.RESET_ALL).strip()
        
        if choice == "1":
            username = input(Fore.BLUE + "Enter username to scan: " + Style.RESET_ALL).strip()
            if username:
                scan_username(username)
            else:
                print(Fore.RED + "[-] Username cannot be empty!")
                
        elif choice == "2":
            raw_input = input(Fore.BLUE + "Enter usernames separated by commas (e.g. user1, user2): " + Style.RESET_ALL).strip()
            if raw_input:
                username_list = [name.strip() for name in raw_input.split(",") if name.strip()]
                print(Fore.CYAN + f"\n[+] Batch process started for {len(username_list)} targets...")
                for username in username_list:
                    scan_username(username)
            else:
                print(Fore.RED + "[-] Input cannot be empty!")
                
        elif choice == "3":
            show_saved_results()
            
        elif choice == "4":
            print(Fore.GREEN + "\n[+] Thank you for using User-Finder OSINT. Goodbye!\n")
            break
        else:
            print(Fore.RED + "[-] Invalid Choice! Please select between 1 and 4.")

if __name__ == "__main__":
    main_menu()
