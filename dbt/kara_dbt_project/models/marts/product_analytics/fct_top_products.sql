-- models/marts/product_analytics/fct_top_products.sql
SELECT
    detected_class as product,
    COUNT(*) AS mention_count
FROM {{ ref('stg_image_detections') }}
GROUP BY detected_class
