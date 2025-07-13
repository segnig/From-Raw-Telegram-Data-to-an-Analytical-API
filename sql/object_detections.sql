CREATE TABLE IF NOT EXISTS raw.fct_image_detections (
    message_id INT,
    channel TEXT,
    detected_class TEXT,
    confidence FLOAT,
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (message_id, channel) REFERENCES raw.telegram_messages(id, channel)
);
