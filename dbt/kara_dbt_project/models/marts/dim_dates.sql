{{ config(materialized='table') }};

WITH base AS (
    SELECT DISTINCT CAST(date AS DATE) AS date
    FROM {{ ref('stg_telegram_messages') }}
    WHERE date IS NOT NULL
)
SELECT
    date,
    EXTRACT(DAY FROM date) AS day,
    EXTRACT(MONTH FROM date) AS month,
    EXTRACT(YEAR FROM date) AS year,
    TO_CHAR(date, 'Day') AS weekday
FROM base;
