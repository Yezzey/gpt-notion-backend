
import os
import time
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

NOTION_API_URL = "https://api.notion.com/v1/pages"
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_VERSION = "2022-06-28"

CACHE_FILE = "last_message.txt"

def get_latest_message():
    try:
        with open("test_message.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def get_cached_message():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    return None

def update_cache(message):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        f.write(message)

def send_to_notion(message):
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION,
    }

    data = {
        "parent": {"database_id": NOTION_DATABASE_ID},
        "properties": {
            "Czas": {"date": {"start": datetime.utcnow().isoformat()}},
            "Nadawca": {"title": [{"text": {"content": "Użytkownik"}}]},
            "Wiadomość": {"rich_text": [{"text": {"content": message}}]},
        }
    }

    response = requests.post(NOTION_API_URL, headers=headers, json=data)
    if response.status_code in [200, 201]:
        print("✅ Wiadomość zapisana do Notion")
    else:
        print(f"❌ Błąd zapisu: {response.status_code}\n{response.text}")

if __name__ == "__main__":
    print("📡 Start zapisu do Notion...")
    while True:
        latest = get_latest_message()
        cached = get_cached_message()

        if latest and latest != cached:
            send_to_notion(latest)
            update_cache(latest)

        time.sleep(30)
