# dagster_pipeline/repository.py
from dagster import Definitions
from dagster_pipeline.pipeline import telegram_pipeline 

defs = Definitions(
    jobs=[telegram_pipeline]  
)