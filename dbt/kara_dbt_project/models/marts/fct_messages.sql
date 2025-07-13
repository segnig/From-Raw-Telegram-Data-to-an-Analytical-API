{{ config(materialized='table') }};

SELECT
    stg.id,
    stg.message_date,
    stg.message_length,
    stg.has_media,
    stg.text,
    stg.sender_id,
    stg.channel,
    stg.file_name,
    ch.channel_name,
    dt.date AS date_key
FROM {{ ref('stg_telegram_messages') }} stg
LEFT JOIN {{ ref('dim_channels') }} ch ON stg.channel = ch.channel_name
LEFT JOIN {{ ref('dim_dates') }} dt ON stg.message_date = dt.date;
