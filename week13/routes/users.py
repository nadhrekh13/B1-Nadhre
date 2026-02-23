from fastapi import APIRouter, HTTPException
from schema import User

router = APIRouter()
users_db = []


@router.post("/users")
def create_user(user: User):
    users_db.append(user)
    return {"message": "User created", "user": user}


@router.get("/users")
def get_all_users():
    return users_db


@router.get("/users/search")
def search_users(q: str):
    return [u for u in users_db if q.lower() in u.name.lower()]


@router.get("/users/{user_id}")
def get_user(user_id: int):
    for u in users_db:
        if u.id == user_id:
            return u
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    for i, u in enumerate(users_db):
        if u.id == user_id:
            users_db[i] = user
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, u in enumerate(users_db):
        if u.id == user_id:
            users_db.pop(i)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
