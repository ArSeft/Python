import requests

# Prompt user to input the base URL of the target website
target_url = input("Website url: ")

# List of common directory names to test against the target URL
wordlist = ["admin", "backup", "login", "config", "uploads", "secret"]

print(f"Scanning {target_url} for directories...\n")

# Iterate through the wordlist and send GET requests to each potential directory
for word in wordlist:
    full_url = f"{target_url}/{word}/"
    response = requests.get(full_url)

    # Check HTTP status code to determine if the directory exists
    if response.status_code == 200:
        print(f"[+] Found: {full_url}")
    else:
        print(f"[-] Not found: {full_url}")

# Wait for user input to prevent terminal from closing immediately
input()
