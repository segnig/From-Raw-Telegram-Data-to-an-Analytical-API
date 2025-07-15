from pydantic import BaseModel
from typing import List


class TopProduct(BaseModel):
    product: str
    mention_count: int


class ChannelActivity(BaseModel):
    channel: str
    post_count: int
    avg_message_length: float


class SearchResult(BaseModel):
    message: str
    channel: str
    timestamp: str  # or datetime if formatted properly