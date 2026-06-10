import streamlit as st
import requests
import time
import os

# Page Configuration for Title and Layout
st.set_page_config(page_title="Mega OSINT User-Finder", page_icon="🔍", layout="wide")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}

# Import the massive platform list
from main import get_platform_list, fetch_profile_details

# Beautiful Header
st.title("🔍 Mega OSINT + Profile Scraper Dashboard")
st.markdown("---")

# Sidebar for options
st.sidebar.header("⚙️ Control Panel")
mode = st.sidebar.radio("Select Scan Mode:", ["Single Username Scan", "View Saved Results"])

if mode == "Single Username Scan":
    st.subheader("👤 Single Target Intelligence Gathering")
    
    # Input box for username
    username = st.text_input("Enter target username to hunt:", "").strip()
    
    if st.button("🚀 Start Mega Scan"):
        if username:
            st.info(f"Scanning 65+ global networks for: '{username}'... Please wait.")
            
            # Progress bar setup
            progress_bar = st.progress(0)
            websites = get_platform_list(username)
            total_sites = len(websites)
            
            found_profiles = []
            
            # Table Header for live display
            col1, col2, col3 = st.columns([2, 2, 5])
            with col1: st.bold("Platform")
            with col2: st.bold("Status")
            with col3: st.bold("Direct Link / Scraped Metadata")
            st.markdown("---")
            
            for index, (name, url) in enumerate(websites.items()):
                # Update progress bar
                progress_bar.progress((index + 1) / total_sites)
                
                try:
                    time.sleep(0.3)
                    response = requests.get(url, headers=HEADERS, timeout=4, allow_redirects=True)
                    
                    c1, c2, c3 = st.columns([2, 2, 5])
                    
                    if response.status_code == 200 and url in response.url:
                        details = fetch_profile_details(name, username)
                        found_profiles.append((name, url, details))
                        
                        with c1: st.success(name)
                        with c2: st.success("🟢 FOUND")
                        with c3: st.write(f"[Open Profile]({url}) " + (f" | 🆔 {details}" if details else ""))
                        
                    elif response.status_code in [403, 429]:
                        with c1: st.warning(name)
                        with c2: st.warning("🔒 BLOCKED")
                        with c3: st.write("Protected by Website Security")
                    else:
                        # We don't flood the UI with NOT FOUND to keep it clean
                        pass
                        
                except Exception:
                    pass
            
            st.success(f"🎯 Scan completed! Total {len(found_profiles)} profiles identified.")
            
            # Save to history automatically
            if found_profiles:
                with open("results.txt", "a") as f:
                    f.write(f"\n=== GUI SCAN REPORT FOR USERNAME: {username} ===\n")
                    for name, url, details in found_profiles:
                        f.write(f"[{name}]: {url} {details if details else ''}\n")
        else:
            st.error("Please enter a valid username first!")

elif mode == "View Saved Results":
    st.subheader("📂 Historical OSINT Reports")
    if os.path.exists("results.txt"):
        with open("results.txt", "r") as f:
            st.text_area("Saved Database Logs:", f.read(), height=400)
    else:
        st.error("No intelligence reports found in database yet.")
