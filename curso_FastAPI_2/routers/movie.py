from pydantic import BaseModel,Field
from typing import Optional
from fastapi import Depends, Path,Query,HTTPException, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from config.database import Session, engine, Base
from jwt_bearer import JWTBearer
from models.movie_entity import MovieModel


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length= 5, max_length=20)
    overview: str = Field(min_length= 20, max_length=100)
    year: int = Field(le = 2022)
    rating: float = Field(ge = 1, le=10)
    category: str = Field(min_length = 5)

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

@movie_router.get("/movies", tags=['movies'],response_model= List[Movie], dependencies=[Depends(JWTBearer())]) #dependencies=[Depends(JWTBearer())]
def get_movies() -> List[Movie]:
    db = Session()
    data = db.query(MovieModel).all()
    return JSONResponse(status_code= 200, content= jsonable_encoder(data))


@movie_router.get("/movies/{id}", tags=['movies'], response_model= Movie)
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
@movie_router.get('/movies/', tags=['movies'], response_model= Movie)
def get_movies_by_category(category: str = Query(min_length= 5)) -> Movie:
    #data = [movie for movie in movies if movie.get("category") == category.title()]
    db = Session()
    data = db.query(MovieModel).filter(MovieModel.category == category).all()
    if(data != []):
        return JSONResponse(status_code= 200, content = jsonable_encoder(data))
    else:
        return JSONResponse(status_code= 404, content = {"message": "No hay peliculas de esa categoria"})


@movie_router.post("/movies", tags=['movies'], response_model= dict)
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


@movie_router.put("/movies/{id}", tags=['movies'], response_model= dict)
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


@movie_router.delete("/movies/{id}", tags=['movies'], response_model= dict)
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

