from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    is_offer: Optional[bool] = None

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Item 1",
                "description": "This is item 1",
                "price": 19.99,
                "is_offer": True
            }
        }
