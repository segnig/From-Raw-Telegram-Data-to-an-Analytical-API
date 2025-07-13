{{ config(materialized='view') }};

SELECT
    id,
    date,
    CAST(date AS DATE) AS message_date,
    LENGTH(COALESCE(text, '')) AS message_length,
    sender_id,
    text,
    has_photo,
    has_document,
    CASE WHEN has_photo OR has_document THEN TRUE ELSE FALSE END AS has_media,
    file_name,
    channel,
    loaded_at
FROM raw.telegram_messages
WHERE
    -- Filter out messages with no text AND no media
    (text IS NOT NULL AND TRIM(text) <> '')
    OR has_photo = TRUE
    OR has_document = TRUE;
