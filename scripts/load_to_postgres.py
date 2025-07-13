import os
import json
import psycopg2
from dotenv import load_dotenv
from glob import glob

load_dotenv()

DB_PARAMS = {
    "host": os.getenv("PG_HOST"),
    "port": os.getenv("PG_PORT"),
    "user": os.getenv("PG_USER"),
    "password": os.getenv("PG_PASSWORD"),
    "dbname": os.getenv("PG_DBNAME")
}

def load_messages(json_file, channel_name):
    with open(json_file, encoding="utf-8") as f:
        messages = json.load(f)

    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()

    for msg in messages:
        cur.execute("""
            INSERT INTO raw.telegram_messages (id, date, text, sender_id, has_photo, has_document, file_name, channel)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id, channel) DO NOTHING;
        """, (
            msg["id"],
            msg["date"],
            msg["text"],
            msg["sender_id"],
            msg["has_photo"],
            msg["has_document"],
            msg["file_name"],
            channel_name
        ))

    conn.commit()
    cur.close()
    conn.close()

def main():
    base_path = "data/raw/telegram_messages"
    for date_folder in os.listdir(base_path):
        full_path = os.path.join(base_path, date_folder)
        for json_file in glob(os.path.join(full_path, "*.json")):
            channel_name = os.path.basename(json_file).replace(".json", "")
            load_messages(json_file, channel_name)

if __name__ == "__main__":
    main()
