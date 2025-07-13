import json
import psycopg2
import os
# Load environment variables
from dotenv import load_dotenv

load_dotenv()

with open("data/processed/detections.json", "r") as f:
    detections = json.load(f)

conn = psycopg2.connect(
    dbname=os.getenv("PG_DBNAME"),
    user=os.getenv("PG_USER"),
    password=os.getenv("PG_PASSWORD"),
    host=os.getenv("PG_HOST"),
    port=os.getenv("PG_PORT")
)
cur = conn.cursor()

for det in detections:
    cur.execute("""
        INSERT INTO raw.fct_image_detections (message_id, channel, detected_class, confidence)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
    """, (
        det["message_id"],
        det["channel"],
        det["detected_class"],
        det["confidence"],
    ))

conn.commit()
cur.close()
conn.close()
print("✅ Detections inserted successfully.")
