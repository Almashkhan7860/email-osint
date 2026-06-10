import asyncio
from holehe import core

async def lookup_email(email):
    print(f"\n[+] {email} के लिए सोशल मीडिया अकाउंट्स खोजे जा रहे हैं...\n")
    modules = core.import_submodules("holehe.modules")
    results = []
    
    for module in modules:
        try:
            await module(email, results)
        except Exception:
            continue

    print(f"{'वेबसाइट (Website)':<25} | {'अकाउंट स्थिति (Status)':<20}")
    print("-" * 50)
    
    account_found = False
    for res in results:
        if res.get("exists"):
            account_found = True
            print(f"📌 {res.get('name'):<22} | 🟢 ACCOUNT FOUND")
            
    if not account_found:
        print("[-] किसी भी प्रमुख सोशल मीडिया पर इस ईमेल से जुड़ा अकाउंट नहीं मिला।")

if __name__ == "__main__":
    target_email = input("कृपया जांचने के लिए ईमेल आईडी दर्ज करें: ")
    asyncio.run(lookup_email(target_email))
