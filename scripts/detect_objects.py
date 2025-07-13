import os
import json
import logging
from pathlib import Path
from ultralytics import YOLO
from datetime import datetime

# Setup
media_base = "data/raw/telegram_messages"
output_path = "data/processed/detections.json"
model = YOLO('yolov8n.pt')  # Small model, fast for testing
results_list = []

def scan_images():
    for root, _, files in os.walk(media_base):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                full_path = os.path.join(root, file)
                results = model(full_path)[0]
                for box in results.boxes:
                    cls = results.names[int(box.cls[0])]
                    conf = round(float(box.conf[0]), 4)
                    message_id = Path(file).stem.split("_")[1]
                    channel_name = Path(file).stem.split("_")[0]
                    results_list.append({
                        "message_id": int(message_id),
                        "channel": channel_name,
                        "detected_class": cls,
                        "confidence": conf
                    })

    with open(output_path, "w") as f:
        json.dump(results_list, f, indent=2)
    print(f"✅ Saved {len(results_list)} detections to {output_path}")

if __name__ == "__main__":
    scan_images()
