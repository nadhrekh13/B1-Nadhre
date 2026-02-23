import json
from fastapi import FastAPI
from user_store import UserStore
from schema import User

app = FastAPI()
store = UserStore("users.txt")

@app.get("/users")
def get_users():
    return store.load()

@app.post("/users")
def create_user(user: User):
    users = store.load()
    new_user = user.dict()
    new_user["id"] = max([u.get("id", 0) for u in users], default=0) + 1
    users.append(new_user)
    store.save(users)
    return new_user

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return store.update_user(user_id, user.dict())

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return store.delete_user(user_id)