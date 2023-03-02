from fastapi import FastAPI,Depends,Body,Path,Query,HTTPException
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List, Any
# from User import User
# import user_service
from Movie import Movie
from jwt_manager import create_token
from jwt_bearer import JWTBearer
from middlewares.error_handler import ErrorHandler

from config.database import Session, engine, Base
from models.movie_entity import MovieModel

app = FastAPI()
# Para cambiar el nombre de la aplicacion
app.title = "Mi aplicacion con FastAPI"

# Para cambiar la version de la aplicacion
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

Base.metadata.create_all(bind=engine)

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Accion'
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Accion'
    }
]

# users = [
#     {
#     "id": 1,
#     "email": "test@test.com",
#     "password": "123456789"
#     }
# ]

# los tags nos permite agrupar las rutas de la aplicacion
@app.get("/", tags=['home'])
def message():
    # return "hola mundo"
    return HTMLResponse("<h1>Hello World</h1>")


@app.get("/movies", tags=['movies'],response_model= List[Movie]) #dependencies=[Depends(JWTBearer())]
def get_movies() -> List[Movie]:
    db = Session()
    data = db.query(MovieModel).all()
    return JSONResponse(status_code= 200, content= jsonable_encoder(data))


@app.get("/movies/{id}", tags=['movies'], response_model= Movie)
def get_movie(id: int = Path(ge= 1)) -> Movie:
    db = Session()
    data = db.query(MovieModel).filter(MovieModel.id == id).first()
    if(data != []):
        return JSONResponse(status_code= 200, content= jsonable_encoder(data))
    else:
        return JSONResponse(status_code= 404, content= {"message": "Pelicula no encontrada"})
    # for movie in movies:
    #     if (int(movie.get("id")) == id):
    #         return movie
    #     else:
    #         return "El id de la pelicula es invalido"


# Importante barra horizontal al final de '/movies/' para parametro query
@app.get('/movies/', tags=['movies'], response_model= Movie)
def get_movies_by_category(category: str = Query(min_length= 5)) -> Movie:
    #data = [movie for movie in movies if movie.get("category") == category.title()]
    db = Session()
    data = db.query(MovieModel).filter(MovieModel.category == category).all()
    if(data != []):
        return JSONResponse(status_code= 200, content = jsonable_encoder(data))
    else:
        return JSONResponse(status_code= 404, content = {"message": "No hay peliculas de esa categoria"})


@app.post("/movies", tags=['movies'], response_model= dict)
def create_movies(movie: Movie) -> dict:
    try:
        if not (movie.title and movie.overview and movie.year and movie.rating and movie.category):
            raise HTTPException(status_code= 400, content= {"message": "Valores de pelicula invalidos"})
        else:
            db = Session()
            new_movie = MovieModel(**movie.dict()) #Alternativa mas obvia es hacer new_movie = MovieModel(title= movie.title, overview= movie.overview, year = movie.year, rating= movie.rating, category= movie.category)
            db.add(new_movie)
            db.commit()
            return JSONResponse(status_code = 200, content = {"message": "Pelicula Agregada"})
    except HTTPException as error:
        return error


@app.put("/movies/{id}", tags=['movies'], response_model= dict)
def update_movie(id: int, movie: Movie) -> dict:
    try:
        db = Session()
        data = db.query(MovieModel).filter(MovieModel.id == id).first()
        if not data:
            raise HTTPException(status_code= 404, detail= {"message": "Pelicula no encontrada"})
        else:
            data.title = movie.title
            data.overview = movie.overview
            data.year = movie.year
            data.rating = movie.rating
            data.category = movie.category
            db.commit()
            # db.refresh(data)
            return JSONResponse(status_code= 200, content={"message": "Pelicula actualizada"})
        # id_exist = 0
        # for element in movies:
        #     if (int(element.get("id")) == id):
        #         id_exist = id
        # if (id_exist):
        #     movies[id - 1] = movie
        #     return JSONResponse(content = {"message": "Pelicula Modificada"})
        # else:
        #     raise HTTPException(status_code=404, detail="Movie not found")
    except HTTPException as error:
        return error


@app.delete("/movies/{id}", tags=['movies'], response_model= dict)
def delete_movie(id: int) -> dict:
    try:
        db = Session()
        data = db.query(MovieModel).filter(MovieModel.id == id).first()
        if not data:
            raise HTTPException(status_code= 404, detail= {"message": "Pelicula no encontrada"})
        else:
            db.delete(data)
            db.commit()
            return JSONResponse(status_code= 200, content= {"message": "Pelicula eliminada"})
        # for element in movies:
        #     if (int(element.get("id")) == id):
        #         movies.remove(element)
        #         return JSONResponse(content = {"message": "Pelicula Eliminada"})
        #     else:
        #         raise HTTPException(status_code=404, detail="Movie not found")
    except HTTPException as error:
        return error


# USUARIOS
# @app.get("/users", tags=["users"], response_model= list[User])
# def get_users():
#     return user_service.get_users()


# @app.post("/users", tags=["users"],response_model= dict)
# def create_user(new_user: User):
#     return user_service.create_user(new_user)

# @app.put("/users", tags=["users"], response_model= dict)
# def update_user(id: int, new_user: User):
#     return user_service.update_user(id,new_user)

# @app.delete("/users", tags=["users"], response_model= dict)
# def delete_user(id: int):
#     return user_service.delete_user(id)

# @app.post("/users/", tags=["users"], response_model= str)
# def login(user: User):
#     return user_service.login(user)