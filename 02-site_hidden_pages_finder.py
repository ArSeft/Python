import requests

target_url=input("Website url: ")

wordlist = ["admin", "backup", "login", "config", "uploads", "secret"]

print(f"Scanning {target_url} for directories...\n")

for word in wordlist:
    full_url = f"{target_url}/{word}/"
    response = requests.get(full_url)

    if response.status_code == 200:
        print(f"[+] Found: {full_url}")
    else:
        print(f"[-] Not found: {full_url}")
input()
