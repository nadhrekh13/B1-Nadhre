from fastapi import FastAPI
from user_store import UserStore
from schema import User

app = FastAPI()
store = UserStore("users.db")

@app.get("/users")
def get_users():
    users = store.load()
    return [{"id": u[0], "name": u[1], "email": u[2]} for u in users]

@app.post("/users")
def create_user(user: User):
    store.save(user.dict())
    return {"status": "success", "user": user}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return store.update_user(user_id, user.dict())

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    store.delete_user(user_id)
    return {"status": "success", "user_id": user_id}