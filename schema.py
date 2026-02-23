from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


class Item(BaseModel):
    id: int
    title: str
    description: str = None
    owner_id: int


class Order(BaseModel):
    id: int
    item_id: int
    user_id: int
    quantity: int
