CREATE SCHEMA IF NOT EXISTS raw;

CREATE TABLE IF NOT EXISTS raw.telegram_messages (
    id INT,
    date TIMESTAMP,
    text TEXT,
    sender_id BIGINT,
    has_photo BOOLEAN,
    has_document BOOLEAN,
    file_name TEXT,
    channel TEXT,
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_telegram_message UNIQUE (id, channel)
);
