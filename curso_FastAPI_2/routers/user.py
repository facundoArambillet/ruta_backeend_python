from pydantic import BaseModel
from fastapi import Path,Query,HTTPException, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session, engine, Base
from models.user_entity import UserModel
from jwt_manager import create_token

class User(BaseModel):
    id: int
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
    data = db.query(UserModel).all()
    return JSONResponse(status_code= 200, content= jsonable_encoder(data))

@user_router.post("/users", tags=["users"],response_model= dict)
def create_user(user: User):
    try:
        if(user.email and user.password):
            db = Session()
            new_user = UserModel(**user.dict())
            db.add(new_user)
            db.commit()
            return JSONResponse(status_code= 200, content={"message": "Usuario agregado"})
        else:
            raise HTTPException(status_code= 400, detail= {"error": "Datos de usuarios invalidos"})
    except HTTPException as error:
        return error

@user_router.put("/users", tags=["users"],response_model= dict)
def update_user(id:int,user: User):
    try:
        if(id and user):
            db = Session()
            data = db.query(UserModel).filter(UserModel.id == id).first()
            if(data):
                data.email = user.email
                data.password = user.password
                db.commit()
                return JSONResponse(status_code= 200, content={"message": "Usuario Actualizado"})
        else:
            raise HTTPException(status_code= 400, detail= {"error": "Usuario no encontrado"})
    except HTTPException as error:
        return error

@user_router.delete("/users", tags=["users"],response_model=dict)
def delete_user(id:int):
    try:
        if(id):
            db = Session()
            data = db.query(UserModel).filter(UserModel.id == id).first()
            if(data):
                db.delete(data)
                db.commit()
                return JSONResponse(status_code= 200, content={"message": "Usuario Eliminado"})
        else:
            raise HTTPException(status_code= 400, detail= {"error": "Usuario no encontrado"})
    except HTTPException as error:
        return error


@user_router.post("/users/", tags=["users"],response_model= str)
def login(user: User):
    try:
        if(user.email == "test@test15.com" and user.password == "123456"):
            token: str = create_token(user.dict())
            return JSONResponse(status_code=200, content= token)
        else:
            raise HTTPException(status_code= 400, detail= "Email o contrasenia invalida")
    except HTTPException as error:
       return JSONResponse(status_code=error.status_code, content={"message": error.detail}) #ASI NO ME TIRA ERROR PYDANTIC
    
