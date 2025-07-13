SELECT *
FROM {{ ref('fct_image_detections') }}
WHERE detected_class IS NULL OR detected_class = ''
