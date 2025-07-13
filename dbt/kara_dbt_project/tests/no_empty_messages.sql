-- Messages without text and no media are considered "empty"
SELECT *
FROM {{ ref('stg_telegram_messages') }}
WHERE COALESCE(text, '') = '' AND has_media = FALSE
