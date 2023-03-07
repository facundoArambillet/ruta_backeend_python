from fastapi import FastAPI,Depends,Body,Path,Query,HTTPException
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.encoders import jsonable_encoder

#JWT
from jwt_manager import create_token
from jwt_bearer import JWTBearer
from middlewares.error_handler import ErrorHandler

#IMPORTACION BDD
from config.database import Session, engine,engine_mysql, Base

#IMPORTACION DE ROUTERS
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
# Para cambiar el nombre de la aplicacion
app.title = "Mi aplicacion con FastAPI"

# Para cambiar la version de la aplicacion
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

#UTILIZACION DE ROUTERS
app.include_router(movie_router)
app.include_router(user_router)

#CONEXION CON LA BDD
Base.metadata.create_all(bind= engine) #BDD SQLite
Base.metadata.create_all(bind= engine_mysql) #BDD MYSQL

@app.get("/", tags=['home'])
def message():
    return HTMLResponse("<h1>Hello World</h1>")


# movies = [
#     {
#         'id': 1,
#         'title': 'Avatar',
#         'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
#         'year': '2009',
#         'rating': 7.8,
#         'category': 'Accion'
#     },
#     {
#         'id': 2,
#         'title': 'Avatar',
#         'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
#         'year': '2009',
#         'rating': 7.8,
#         'category': 'Accion'
#     }
# ]

# users = [
#     {
#     "id": 1,
#     "email": "test@test.com",
#     "password": "123456789"
#     }
# ]

# los tags nos permite agrupar las rutas de la aplicacion

# USUARIOS
