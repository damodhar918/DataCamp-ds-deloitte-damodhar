# models.py

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, index=True)
#     price = Column(Integer)
#     is_offer = Column(Boolean, default=False)


class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float
    is_offer: bool = None

# curl -X POST "http://127.0.0.1:8000/items/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\":1,\"name\":\"New Item\",\"description\":\"This is a new item\",\"price\":19.99,\"is_offer\":true}"
