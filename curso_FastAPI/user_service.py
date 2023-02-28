from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from jwt_manager import create_token
from User import User
app = FastAPI()

users = [
    {
    "id": 1,
    "email": "test@test.com",
    "password": "123456789"
    },
    {
    "id": 2,
    "email": "test2@test2.com",
    "password": "123456789"
    }
]


def get_users():
    try:
        if(len(users) == 0):
            raise HTTPException(status_code=405, detail="No hay usuarios registrados")
        else:
            return users
    except HTTPException as error:
        return error

def create_user(new_user: User):
    try:
        if(new_user):
            users.append(new_user)
            return JSONResponse(content= {"message": "Usuario creado"})
        else:
            raise HTTPException(status_code= 400, detail= "Parametros de usuario invalido")
    except HTTPException as error:
        return error


def update_user(id: int, new_user: User):
    try:
        id_exist = 0
        for element in users:
            if (int(element.get("id")) == id):
                id_exist = id
        if (id_exist):
            users[id - 1] = new_user
            return JSONResponse(content = {"message": "Usuario Modificado"})
        else:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
    except HTTPException as error:
        return error

def delete_user(id: int):
    try:
        for element in users:
            if (int(element.get("id")) == id):
                users.remove(element)
                return JSONResponse(content = {"message": "Usuario Eliminado"})
            else:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
    except HTTPException as error:
        return error

def login(user: User):
    try:
        id_exist = 0
        for element in users:
            if (int(element.get("id")) == user.id):
                id_exist = user.id
                print(id_exist)
        if (id_exist != 0):
            if(user.email == "test@test.com" and user.password == "123456789"):
                token: str = create_token(user.dict())
                return JSONResponse(status_code=200, content= token)
        else:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
    except HTTPException as error:
        return error