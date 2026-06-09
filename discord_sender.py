import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1513875044202188930/dw8gsAdUGilAB9kqqafinDfc0JozomWSYErp8HOJcEKeBfLJ5oBW6IPCZd-6NDKFiArm"

def send_discord_message(message):
    response = requests.post(WEBHOOK_URL, json={"content": message})
    print(f"Message sent! Status: {response.status_code}")

if __name__ == "__main__":
    send_discord_message("Hello from Python!")
