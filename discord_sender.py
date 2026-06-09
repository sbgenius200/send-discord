import urllib.request
import urllib.parse
import json

WEBHOOK_URL = "https://discord.com/api/webhooks/1513872994706133003/gUNngshQj5JSW7jMOlmlY0s4t9ZRfGLPVmdDc7DDFsttLcW-rUS4nMlk-ghs4PvMBPzW"

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
