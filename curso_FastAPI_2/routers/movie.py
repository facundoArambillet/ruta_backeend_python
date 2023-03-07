from pydantic import BaseModel, Field
from typing import Optional
from fastapi import Depends, Path, Query, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from config.database import Session,Session_mysql, engine, Base
from jwt_bearer import JWTBearer
from models.movie_entity import MovieModel

from services.movie import MovieService


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=20)
    overview: str = Field(min_length=20, max_length=100)
    year: int = Field(le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Titulo",
                "overview": "Descripcion de la pelicula",
                "year": 2022,
                "rating": 8,
                "category": "Accion",
            }
        }


movie_router = APIRouter()


# dependencies=[Depends(JWTBearer())]
@movie_router.get("/movies", tags=['movies'], response_model=List[Movie], dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    data = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(data))


@movie_router.get("/movies/{id}", tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1)) -> Movie:
    db = Session()
    data = MovieService(db).get_movie(id)
    if (data != []):
        return JSONResponse(status_code=200, content=jsonable_encoder(data))
    else:
        return JSONResponse(status_code=404, content={"message": "Pelicula no encontrada"})
    # for movie in movies:
    #     if (int(movie.get("id")) == id):
    #         return movie
    #     else:
    #         return "El id de la pelicula es invalido"


# Importante barra horizontal al final de '/movies/' para parametro query
@movie_router.get('/movies/', tags=['movies'], response_model=Movie)
def get_movies_by_category(category: str = Query(min_length=5)) -> Movie:
    # data = [movie for movie in movies if movie.get("category") == category.title()]
    db = Session()
    data = MovieService(db).get_by_category(category)
    if (data != []):
        return JSONResponse(status_code=200, content=jsonable_encoder(data))
    else:
        return JSONResponse(status_code=404, content={"message": "No hay peliculas de esa categoria"})


@movie_router.post("/movies", tags=['movies'], response_model=dict)
def create_movies(movie: Movie) -> dict:
    db = Session()
    db_mysql = Session_mysql()
    new_movie = MovieService(db).create_movie(movie)
    new_movie = MovieService(db_mysql).create_movie(movie)
    return new_movie


@movie_router.put("/movies/{id}", tags=['movies'], response_model=dict)
def update_movie(id: int, movie: Movie) -> dict:

    db = Session()
    data = MovieService(db).update_movie(id, movie)
    return data
    # id_exist = 0
    # for element in movies:
    #     if (int(element.get("id")) == id):
    #         id_exist = id
    # if (id_exist):
    #     movies[id - 1] = movie
    #     return JSONResponse(content = {"message": "Pelicula Modificada"})
    # else:
    #     raise HTTPException(status_code=404, detail="Movie not found")


@movie_router.delete("/movies/{id}", tags=['movies'], response_model=dict)
def delete_movie(id: int) -> dict:

    db = Session()
    data = MovieService(db).delete_movie(id)
    return data
    # for element in movies:
    #     if (int(element.get("id")) == id):
    #         movies.remove(element)
    #         return JSONResponse(content = {"message": "Pelicula Eliminada"})
    #     else:
    #         raise HTTPException(status_code=404, detail="Movie not found")
