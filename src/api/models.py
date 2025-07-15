from sqlalchemy import Column, Integer, String, Float
from database import Base

class FctMessage(Base):
    __tablename__ = "fct_messages"
    id = Column(Integer, primary_key=True, index=True)
    channel = Column(String)
    text = Column(String)

class FctTopProduct(Base):
    __tablename__ = "fct_top_products"
    product = Column(String, primary_key=True)
    mention_count = Column(Integer)

class ChannelActivity(Base):
    __tablename__ = "fct_channel_activity"
    channel = Column(String, primary_key=True)
    post_count = Column(Integer)
    avg_message_length = Column(Float)
