import urllib.request
import urllib.parse
import json

WEBHOOK_URL = "https://discord.com/api/webhooks/1513870002267095182/pT0s6b7sZdumysbJzOPJYfEeWIWA-AiglR8nndNm7wpHwu1ftX510g_m63OtdWqyvz0R"

def send_discord_message(message):
    payload = json.dumps({"content": message}).encode("utf-8")
    req = urllib.request.Request(
        WEBHOOK_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req) as response:
        print(f"Message sent! Status: {response.status}")

if __name__ == "__main__":
    send_discord_message("Hello from Python!")
