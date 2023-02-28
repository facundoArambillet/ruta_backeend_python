from fastapi import FastAPI,Depends,Body,Path,Query,HTTPException
from fastapi.responses import HTMLResponse,JSONResponse
from Movie import Movie
from User import User
import user_service
from jwt_manager import create_token
from jwt_bearer import JWTBearer
app = FastAPI()
# Para cambiar el nombre de la aplicacion
app.title = "Mi aplicacion con FastAPI"

# Para cambiar la version de la aplicacion
app.version = "0.0.1"

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


@app.get("/movies", tags=['movies'], response_model= list[Movie], dependencies=[Depends(JWTBearer())])
def get_movies() -> list[Movie]:
    return movies


@app.get("/movies/{id}", tags=['movies'], response_model= Movie)
def get_movie(id: int = Path(ge= 1)) -> Movie:
    for movie in movies:
        if (int(movie.get("id")) == id):
            return movie
        else:
            return "El id de la pelicula es invalido"


# Importante barra horizontal al final de '/movies/' para parametro query
@app.get('/movies/', tags=['movies'], response_model= list[Movie])
def get_movies_by_category(category: str = Query(min_length= 5)) -> list[Movie]:
    data = [movie for movie in movies if movie.get("category") == category.title()]
    return JSONResponse(content = data)


@app.post("/movies", tags=['movies'], response_model= dict)
def create_movies(movie: Movie) -> dict:
    try:
        print(movie.id)
        if (movie.id and movie.title and movie.overview and movie.year and movie.rating and movie.category):
            movies.append(movie)
            return JSONResponse(content = {"message": "Pelicula Agregada"})
        else:
            raise Exception("Valores de pelicula invalidos")
    except Exception as error:
        return error


@app.put("/movies/{id}", tags=['movies'], response_model= dict)
def update_movie(id: int, movie: Movie) -> dict:
    try:
        id_exist = 0
        for element in movies:
            if (int(element.get("id")) == id):
                id_exist = id
        if (id_exist):
            movies[id - 1] = movie
            return JSONResponse(content = {"message": "Pelicula Modificada"})
        else:
            raise HTTPException(status_code=404, detail="Movie not found")
    except HTTPException as error:
        return error


@app.delete("/movies/{id}", tags=['movies'], response_model= dict)
def delete_movie(id: int) -> dict:
    try:
        for element in movies:
            if (int(element.get("id")) == id):
                movies.remove(element)
                return JSONResponse(content = {"message": "Pelicula Eliminada"})
            else:
                raise HTTPException(status_code=404, detail="Movie not found")
    except HTTPException as error:
        return error


# USUARIOS
@app.get("/users", tags=["users"], response_model= list[User])
def get_users():
    return user_service.get_users()


@app.post("/users", tags=["users"],response_model= dict)
def create_user(new_user: User):
    return user_service.create_user(new_user)

@app.put("/users", tags=["users"], response_model= dict)
def update_user(id: int, new_user: User):
    return user_service.update_user(id,new_user)

@app.delete("/users", tags=["users"], response_model= dict)
def delete_user(id: int):
    return user_service.delete_user(id)

@app.post("/users/", tags=["users"], response_model= str)
def login(user: User):
    return user_service.login(user)