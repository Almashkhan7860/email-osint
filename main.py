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
    # Massive database of 65 major global platforms
    return {
        # Social Media, Forums & Messaging
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
        "Quora": f"https://www.quora.com/profile/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "Vimeo": f"https://vimeo.com/{username}",
        "DailyMotion": f"https://www.dailymotion.com/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}",
        "VK (Vkontakte)": f"https://vk.com/{username}",
        "Ok.ru": f"https://ok.ru/{username}",
        "Imgur": f"https://imgur.com/user/{username}",
        
        # Coding, Devs & Technical (With Scraper Support)
        "GitHub": f"https://github.com/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "LeetCode": f"https://leetcode.com/{username}",
        "HackerRank": f"https://www.hackerrank.com/{username}",
        "Kaggle": f"https://www.kaggle.com/{username}",
        "StackOverflow": f"https://stackoverflow.com/users/{username}",
        "CodePen": f"https://codepen.io/{username}",
        "Dev.to": f"https://dev.to/{username}",
        "DockerHub": f"https://hub.docker.com/u/{username}",
        "PyPI (Python Pack)": f"https://pypi.org/user/{username}",
        "NPM (JS Packages)": f"https://www.npmjs.com/~{username}",
        "BitBucket": f"https://bitbucket.org/{username}/",
        
        # Cybersecurity, OSINT & Hacking
        "HackTheBox": f"https://forum.hackthebox.com/u/{username}",
        "TryHackMe": f"https://tryhackme.com/p/{username}",
        "Bugcrowd": f"https://bugcrowd.com/{username}",
        "HackerOne": f"https://hackerone.com/{username}",
        "Exploit-DB": f"https://www.exploit-db.com/profiles/{username}",
        
        # Gaming Networks
        "Steam (ID)": f"https://steamcommunity.com/id/{username}",
        "Roblox": f"https://www.roblox.com/user.aspx?username={username}",
        "Xbox Gamertag": f"https://account.xbox.com/en-us/profile?gamertag={username}",
        "PlayStation Net": f"https://psnprofiles.com/{username}",
        "Minecraft (Namemc)": f"https://namemc.com/profile/{username}",
        "Chess.com": f"https://www.chess.com/member/{username}",
        
        # Freelancing & Business Portfolio
        "Fiverr": f"https://www.fiverr.com/{username}",
        "Upwork": f"https://www.upwork.com/freelancers/~{username}",
        "Behance": f"https://www.behance.net/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Linktree": f"https://linktr.ee/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Patreon": f"https://www.patreon.com/{username}",
        "About.me": f"https://about.me/{username}",
        
        # Audio, Podcasts & Music
        "Spotify": f"https://open.spotify.com/user/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Bandcamp": f"https://bandcamp.com/{username}",
        "Mixcloud": f"https://www.mixcloud.com/{username}",
        
        # Financial & Crypto
        "TradingView": f"https://www.tradingview.com/u/{username}",
        "BuyMeACoffee": f"https://www.buymeacoffee.com/{username}",
        "CoinMarketCap": f"https://coinmarketcap.com/community/profile/{username}"
    }

def fetch_profile_details(name, username):
    # Live Scraper Logic for GitHub API to fetch real identity
    if name == "GitHub":
        try:
            api_url = f"https://api.github.com/users/{username}"
            res = requests.get(api_url, headers=HEADERS, timeout=3)
            if res.status_code == 200:
                data = res.json()
                real_name = data.get("name") or "Not Available"
                bio = data.get("bio") or "Not Available"
                location = data.get("location") or "Not Available"
                followers = data.get("followers") or 0
                return f" [Identity -> Name: {real_name} | Bio: {bio} | Loc: {location} | Followers: {followers}]"
        except Exception:
            pass
    return ""

def scan_username(username):
    print(Fore.CYAN + f"\n[+] Target Username: '{username}'")
    print(Fore.YELLOW + f"{'Platform':<20} | {'Status':<15} | {'Direct Profile Link / Scraped Details':<40}")
    print(Style.BRIGHT + "-" * 95)

    websites = get_platform_list(username)
    found_profiles = []

    for name, url in websites.items():
        try:
            time.sleep(0.4)
            response = requests.get(url, headers=HEADERS, timeout=5, allow_redirects=True)
            
            if response.status_code == 200 and url in response.url:
                # Trigger Profile Scraper for details
                details = fetch_profile_details(name, username)
                display_text = f"{url}{Fore.LIGHTMAGENTA_EX + details if details else ''}"
                
                print(f"📌 {Fore.GREEN + name:<18} | {Fore.GREEN}🟢 FOUND       {Style.RESET_ALL} | {display_text}")
                found_profiles.append((name, url, details))
            elif response.status_code in [403, 429]:
                print(f"🔒 {Fore.YELLOW + name:<18} | {Fore.YELLOW}🟡 BLOCKED     {Style.RESET_ALL} | - (Protected)")
            else:
                print(f"❌ {Fore.RED + name:<18} | {Fore.RED}🔴 NOT FOUND   {Style.RESET_ALL} | {Fore.WHITE + url}")
                
        except requests.exceptions.Timeout:
            print(f"⏳ {Fore.YELLOW + name:<18} | {Fore.YELLOW}🟡 TIMEOUT     {Style.RESET_ALL} | -")
        except requests.exceptions.RequestException:
            print(f"🛑 {Fore.RED + name:<18} | {Fore.RED}🔴 CONN ERROR  {Style.RESET_ALL} | -")

    print(Style.BRIGHT + "-" * 95)
    print(Fore.CYAN + f"[+] Scan completed for '{username}'. Identified profiles: {len(found_profiles)}")
    
    if found_profiles:
        with open("results.txt", "a") as f:
            f.write(f"\n=== SCAN REPORT FOR USERNAME: {username} ===\n")
            for name, url, details in found_profiles:
                f.write(f"[{name}]: {url} {details if details else ''}\n")
        print(Fore.GREEN + "[+] Active links and scraped metadata saved to 'results.txt'")

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
        print(Fore.MAGENTA + Style.BRIGHT + "===   MEGA OSINT + SCRAPER (65+)    ====")
        print(Fore.MAGENTA + Style.BRIGHT + "========================================")
        print(Fore.BLUE + "[1] " + Fore.WHITE + "Scan Single Username (With Profile Scraper)")
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
            raw_input = input(Fore.BLUE + "Enter usernames separated by commas: " + Style.RESET_ALL).strip()
            if raw_input:
                username_list = [name.strip() for name in raw_input.split(",") if name.strip()]
                print(Fore.CYAN + f"\n[+] Mega Batch process started for {len(username_list)} targets...")
                for username in username_list:
                    scan_username(username)
            else:
                print(Fore.RED + "[-] Input cannot be empty!")
                
        elif choice == "3":
            show_saved_results()
            
        elif choice == "4":
            print(Fore.GREEN + "\n[+] Thank you for using Mega User-Finder OSINT. Goodbye!\n")
            break
        else:
            print(Fore.RED + "[-] Invalid Choice! Please select between 1 and 4.")

if __name__ == "__main__":
    main_menu()
