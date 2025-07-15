from fastapi import FastAPI, HTTPException
from typing import List
import crud, schemas

app = FastAPI(title="Telegram Analytics API")

@app.get("/api/reports/top-products", response_model=List[schemas.TopProduct])
def top_products(limit: int = 10):
    results = crud.get_top_products(limit)
    return results

@app.get("/api/channels/{channel_name}/activity", response_model=schemas.ChannelActivity)
def channel_activity(channel_name: str):
    result = crud.get_channel_activity(channel_name)
    if not result:
        raise HTTPException(status_code=404, detail="Channel not found")
    return result

@app.get("/api/search/messages", response_model=List[schemas.SearchResult])
def search_messages(query: str):
    results = crud.search_messages(query)
    return results