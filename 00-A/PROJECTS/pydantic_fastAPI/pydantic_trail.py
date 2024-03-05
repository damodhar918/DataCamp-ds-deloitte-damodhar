from pydantic import BaseModel, validator
from typing import List, Dict, Optional
from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from pydantic import BaseSettings
from pydantic_settings import BaseSettings
from sqlalchemy.orm import declarative_base
# from pydantic import BaseSettings





class User(BaseModel):
    username: str
    password: str

    @validator('password')
    def password_must_meet_criteria(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isupper() for char in v):
            raise ValueError(
                'Password must contain at least one uppercase letter')
        if not any(char.islower() for char in v):
            raise ValueError(
                'Password must contain at least one lowercase letter')
        return v


# Integrating with FastAPI for API Development
app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.post("/items/")
async def create_item(item: Item):
    return item

# Using Pydantic with SQLAlchemy for ORM
Base = declarative_base()


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


class UserModelSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

# Handling Complex Nested Models with Lists and Dictionaries


class Product(BaseModel):
    name: str
    price: float


class Order(BaseModel):
    id: int
    products: List[Product]
    customer_info: Dict[str, str]


# Example usage
order = Order(
    id=1,
    products=[
        Product(name="Laptop", price=1200.0),
        Product(name="Mouse", price=20.0)
    ],
    customer_info={"name": "Alice", "email": "alice@example.com"}
)

# Using Pydantic for Environment Variable Configuration


        
class Settings(BaseSettings):
    database_url: str
    debug: bool = False

    class Config:
        env_prefix = "app_"
        from_attributes = True  # Use from_attributes instead of orm_mode
# Advanced Data Validation with Custom Validators



Base = declarative_base()


# This will read the settings from environment variables prefixed with "app_"
settings = Settings()
print(settings.database_url)
print(settings.debug)

# Running FastAPI app (comment out if not running as a script)
import uvicorn
uvicorn.run(app, host="0.0.0.0", port=8000)
