from sqlalchemy import inspect
from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from databases import Database
# pip install sqlalchemy databases[sqlite]


# DATABASE_URL = "sqlite:///test.db"
DATABASE_URL = "sqlite:///./test.db"

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, index=True)
#     price = Column(Integer)
#     is_offer = Column(Boolean, default=False)

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer)
    is_offer = Column(Boolean, default=False)

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()
# Debugging: Print the database URL to ensure it's correct
# print(f"Database URL: {DATABASE_URL}")

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Debugging: Check if the table exists after creation
inspector = inspect(engine)
if inspector.has_table("items"):
    print("Tables:", inspector.get_table_names())
else:
    print("Table does not exist")

# @app.post("/items/", response_model=Item)
# async def create_item(item: Item, db: Session = Depends(get_db)):
#     db_item = Item(**item.dict())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item


# Pydantic model for Item

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    is_offer: Optional[bool] = False

# SQLAlchemy model remains unchanged


# Modify the endpoint to use the Pydantic model

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/items/", response_model=ItemBase)
async def create_item(item: ItemBase, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/items/{item_id}", response_model=ItemBase)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.get("/items/", response_model=ItemBase)
async def read_item(db: Session = Depends(get_db)):
    db_item = db.query(Item).all()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.put("/items/{item_id}", response_model=ItemBase)
async def update_item(item_id: int, item: ItemBase, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.delete("/items/{item_id}", response_model=ItemBase)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item
