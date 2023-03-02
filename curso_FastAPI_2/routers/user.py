from typing import Optional
from pydantic import BaseModel
from fastapi import Path,Query,HTTPException, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session, engine, Base
from models.user_entity import UserModel
from jwt_manager import create_token
from services.user import UserService

class User(BaseModel):
    id: Optional[int] = None
    email: str
    password: str

    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "email": "test100@test.com",
                "password": "123456",

            }
        }

user_router = APIRouter()

@user_router.get("/users", tags= ["users"], response_model= list[User])
def get_users():
    db = Session()
    data = UserService(db).get_users()
    return data

@user_router.post("/users", tags=["users"],response_model= dict)
def create_user(user: User):
    db = Session()
    data = UserService(db).create_user(user)
    return data

@user_router.put("/users", tags=["users"],response_model= dict)
def update_user(id:int,user: User):
    db = Session()
    data = UserService(db).update_user(id,user)
    return data

@user_router.delete("/users", tags=["users"],response_model=dict)
def delete_user(id:int):
    db = Session()
    data = UserService(db).delete_user(id)
    return data


@user_router.post("/users/login", tags=["users"],response_model= str)
def login(user: User):
    db = Session()
    data = UserService(db).login(user)
    return data