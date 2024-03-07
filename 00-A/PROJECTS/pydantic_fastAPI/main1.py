from fastapi import FastAPI, HTTPException
from models import Item
from typing import List

app = FastAPI()

items = [
    Item(id=1, name="Item 1", description="This is item 1",
         price=19.99, is_offer=True),
    Item(id=2, name="Item 2", description="This is item 2",
         price=29.99, is_offer=False),
    Item(id=3, name="Item 3", description="This is item 3",
         price=39.99, is_offer=True),
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item


@app.get("/items/", response_model=List[Item])
async def read_items():
    return items


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    for index, existing_item in enumerate(items):
        if existing_item.id == item_id:
            items[index] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    for index, existing_item in enumerate(items):
        if existing_item.id == item_id:
            deleted_item = items.pop(index)
            return deleted_item
    raise HTTPException(status_code=404, detail="Item not found")


# uvicorn main1:app --reload
# curl -X PUT "http://127.0.0.1:8000/items/1" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\":5,\"name\":\"Updated Item\",\"description\":\"This is an updated item\",\"price\":29.99,\"is_offer\":false}"
# curl -X POST "http://127.0.0.1:8000/items/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\":5,\"name\":\"Updated Item\",\"description\":\"This is an updated item\",\"price\":29.99,\"is_offer\":false}"
# curl -X DELETE "http://127.0.0.1:8000/items/5"
# curl -X GET "http://127.0.0.1:8000/items/1" -H "accept: application/json"
# curl -X GET "http://127.0.0.1:8000/items" -H "accept: application/json"
