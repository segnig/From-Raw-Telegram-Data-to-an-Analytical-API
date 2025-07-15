from dagster import job
from dagster_pipeline.ops import (
    scrape_telegram_data,
    load_raw_to_postgres,
    run_dbt_transformations,
    run_yolo_enrichment,
)

@job
def telegram_pipeline():
    raw_data = scrape_telegram_data()
    loaded = load_raw_to_postgres(start=raw_data)  # Dependency without data
    transformed = run_dbt_transformations(start=loaded)
    run_yolo_enrichment(start=transformed)