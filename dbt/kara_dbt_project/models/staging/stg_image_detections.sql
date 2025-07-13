{{ config(materialized='view') }}

SELECT
    message_id,
    channel,
    detected_class,
    confidence,
    detected_at
FROM raw.fct_image_detections
