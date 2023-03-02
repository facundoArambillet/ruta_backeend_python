from fastapi import HTTPException
from fastapi.responses import JSONResponse
from models.user_entity import UserModel
from jwt_manager import create_token
class UserService():
    def __init__(self,db) -> None:
        self.db = db

    def get_users(self):
        result = self.db.query(UserModel).all()
        return result
    
    def get_user(self,id):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result

    def create_user(self,user):
        try:
            result = self.db
            if not (user.email and user.password):
                raise HTTPException(status_code= 400, content= {"message": "Valores de usuario invalidos"})
            else:
                new_user = UserModel(**user.dict()) #Alternativa mas obvia es hacer new_movie = MovieModel(title= movie.title, overview= movie.overview, year = movie.year, rating= movie.rating, category= movie.category)
                result.add(new_user)
                result.commit()                    
                return JSONResponse(status_code = 200, content = {"message": "Usuario Creado"})
        except HTTPException as error:
            return error

    def update_user(self,id,user):
        try:
            result = self.db
            if not (user.email and user.password):
                raise HTTPException(status_code= 400, content= {"message": "Valores de usuario invalidos"})
            else:
                data = result.query(UserModel).filter(UserModel.id == id).first()
                if(data):
                    data.email = user.email
                    data.password = user.password
                    result.commit()                    
                    return JSONResponse(status_code = 200, content = {"message": "Usuario Actualizado"})
                else:
                    raise HTTPException(status_code= 404, detail= {"message": "Usuario no encontrado"})
        except HTTPException as error:
            return JSONResponse(status_code= error.status_code, content= {"Error": error.detail})

    def delete_user(self,id):
        try:
            if(id):
                result = self.db
                data = result.query(UserModel).filter(UserModel.id == id).first()
                if(data):
                    result.delete(data)
                    result.commit() 
                    return JSONResponse(status_code= 200, content={"message": "Usuario eliminado"})
                else:
                    raise HTTPException(status_code= 404, detail= {"error": "Usuario no encontrado"})
            else:
                raise HTTPException(status_code=400, detail={"error": "Datos invalidos"})
        except HTTPException as error:
            return JSONResponse(status_code= error.status_code, content= {"error": error.detail})
    
    def login(self,user):
        try:
            if(user):
                result = self.db
                data = result.query(UserModel).filter(UserModel.email == user.email).first()
                print(data)
                if(data):
                    if(data.email == "test15@test.com" and data.password == "123456"):
                        token = create_token(user.dict())
                    return JSONResponse(status_code=200, content= token)
                else:
                    raise HTTPException(status_code= 404, detail= {"error": "Usuario no encontrado"})
            else:
                raise HTTPException(status_code=400, detail={"error": "Datos invalidos"})
        except HTTPException as error:
            return JSONResponse(status_code= error.status_code, content= {"error": error.detail})