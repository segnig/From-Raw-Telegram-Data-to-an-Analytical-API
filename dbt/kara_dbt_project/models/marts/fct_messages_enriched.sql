{{ config(materialized='table') }}

SELECT
    msg.id AS message_id,
    msg.channel,
    msg.date,
    det.detected_class,
    det.confidence,
    det.detected_at
FROM {{ ref('stg_telegram_messages') }} msg
JOIN {{ ref('stg_image_detections') }} det
  ON msg.id = det.message_id AND msg.channel = det.channel
