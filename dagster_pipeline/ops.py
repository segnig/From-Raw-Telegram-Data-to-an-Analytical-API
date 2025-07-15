from dagster import op, In, Out, Nothing
import subprocess

@op(out=Out(Nothing))
def scrape_telegram_data():
    subprocess.run(["python", "scripts/telegram_scraper.py"], check=True)

@op(ins={"start": In(Nothing)}, out=Out(Nothing))
def load_raw_to_postgres():
    subprocess.run(["python", "scripts/load_to_postgres.py"], check=True)

@op(ins={"start": In(Nothing)}, out=Out(Nothing)) 
def run_dbt_transformations():
    subprocess.run(["dbt", "run", "--project-dir", "dbt/kara_dbt_project"], check=True)

@op(ins={"start": In(Nothing)}, out=Out(Nothing))
def run_yolo_enrichment():
    subprocess.run(["python", "scripts/detect_objects.py"], check=True)