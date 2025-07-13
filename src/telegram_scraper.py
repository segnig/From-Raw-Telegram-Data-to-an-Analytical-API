import os
import json
import logging
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()
API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")

# Channels to scrape
CHANNELS = [
    "lobelia4cosmetics",
    "tikvahpharma"
]

# Setup directories
BASE_DIR = "data/raw/telegram_messages"
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Logging config
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "scrape.log"),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# Initialize client session (user login)
client = TelegramClient("scraper_session", API_ID, API_HASH)


def scrape_channel(channel_username: str, limit: int = 1000):
    today = datetime.now().strftime("%Y-%m-%d")
    save_dir = os.path.join(BASE_DIR, today)
    media_dir = os.path.join(save_dir, "media")
    os.makedirs(save_dir, exist_ok=True)
    os.makedirs(media_dir, exist_ok=True)

    file_path = os.path.join(save_dir, f"{channel_username}.json")
    messages_list = []

    try:
        logging.info(f"🔍 Scraping channel: {channel_username}")

        for message in client.iter_messages(channel_username, limit=limit):
            msg_data = {
                "id": message.id,
                "date": message.date.isoformat() if message.date else None,
                "text": message.text,
                "sender_id": message.sender_id,
                "has_photo": isinstance(message.media, MessageMediaPhoto),
                "has_document": isinstance(message.media, MessageMediaDocument),
                "file_name": None
            }

            # Media download logic
            if message.media:
                try:
                    filename = None

                    if msg_data["has_document"]:
                        # Extract original file name if available
                        for attr in message.media.document.attributes:
                            if hasattr(attr, "file_name"):
                                filename = f"{channel_username}_{message.id}_{attr.file_name}"
                                break
                        if not filename:
                            filename = f"{channel_username}_{message.id}_document"
                    
                    elif msg_data["has_photo"]:
                        filename = f"{channel_username}_{message.id}_photo.jpg"

                    media_path = client.download_media(
                        message, file=os.path.join(media_dir, filename)
                    )

                    if media_path:
                        msg_data["file_name"] = os.path.basename(media_path)

                except Exception as media_err:
                    logging.warning(f"⚠️ Media download failed for message {message.id} in {channel_username}: {media_err}")

            messages_list.append(msg_data)

        # Save scraped messages to JSON
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(messages_list, f, indent=2, ensure_ascii=False)

        logging.info(f"✅ Scraped {len(messages_list)} messages from {channel_username}")

    except Exception as e:
        logging.error(f"❌ Error scraping {channel_username}: {e}")


def main():
    with client:
        for channel in CHANNELS:
            scrape_channel(channel)


if __name__ == "__main__":
    main()
