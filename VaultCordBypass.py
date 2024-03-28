import random
import string
import requests

# User inputs
access_code = input("Discord Oauth2 code: ")
vault_cord_verify_domain = input("VaultCord verify domain: ")
cloudflare_captcha_token = input("Cloudflare captcha token: ")

# Generate valid IP and random fingerprint
ip = '.'.join(str(random.randint(0, 255)) for _ in range(4))
fingerprint = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

print(f"IP: {ip}")
print(f"Fingerprint: {fingerprint}")

# Prepare POST request
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": f"https://{vault_cord_verify_domain}/",
    "Origin": f"https://{vault_cord_verify_domain}",
}
payload = {
    "code": access_code,
    "domain": vault_cord_verify_domain,
    "token": cloudflare_captcha_token,
    "ip": ip,
    "fingerprint": fingerprint,
}

# Make POST request
response = requests.post("https://api.vaultcord.com/servers/verify", headers=headers, json=payload)
body = response.json()
print(body)
