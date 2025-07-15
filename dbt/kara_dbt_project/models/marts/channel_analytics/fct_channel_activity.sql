-- models/marts/channel_analytics/fct_channel_activity.sql
SELECT
    channel,
    COUNT(*) AS post_count,
    AVG(LENGTH(text))::FLOAT AS avg_message_length
FROM {{ ref('stg_telegram_messages') }}
GROUP BY channel
