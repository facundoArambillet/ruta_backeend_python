from fastapi import HTTPException
from fastapi.responses import JSONResponse
from models.movie_entity import MovieModel
class MovieService():
    def __init__(self,db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie(self,id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result

    def get_by_category(self,category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result

    def create_movie(self,movie):
        try:
            result = self.db
            if not (movie.title and movie.overview and movie.year and movie.rating and movie.category):
                raise HTTPException(status_code= 400, content= {"message": "Valores de pelicula invalidos"})
            else:
                new_movie = MovieModel(**movie.dict()) #Alternativa mas obvia es hacer new_movie = MovieModel(title= movie.title, overview= movie.overview, year = movie.year, rating= movie.rating, category= movie.category)
                result.add(new_movie)
                result.commit()                    
                return JSONResponse(status_code = 200, content = {"message": "Pelicula Agregada"})
        except HTTPException as error:
            return error

    def update_movie(self,id,movie):
        try:
            result = self.db
            if not (movie.title and movie.overview and movie.year and movie.rating and movie.category):
                raise HTTPException(status_code= 400, content= {"message": "Valores de pelicula invalidos"})
            else:
                data = result.query(MovieModel).filter(MovieModel.id == id).first()
                if(data):
                    data.title = movie.title
                    data.overview = movie.overview
                    data.year = movie.year
                    data.rating = movie.rating
                    data.category = movie.category
                    result.commit()                    
                    return JSONResponse(status_code = 200, content = {"message": "Pelicula Actualizada"})
                else:
                    raise HTTPException(status_code= 404, detail= {"message": "Pelicula no encontrada"})
        except HTTPException as error:
            return JSONResponse(status_code= error.status_code, content= {"Error": error.detail})

    def delete_movie(self,id):
        try:
            if(id):
                result = self.db
                data = result.query(MovieModel).filter(MovieModel.id == id).first()
                if(data):
                    result.delete(data)
                    result.commit() 
                    return JSONResponse(status_code= 200, content={"message": "Pelicula eliminada"})
                else:
                    raise HTTPException(status_code= 404, detail= {"error": "Pelicula no encontrada"})
            else:
                raise HTTPException(status_code=400, detail={"error": "Datos invalidos"})
        except HTTPException as error:
            return JSONResponse(status_code= error.status_code, content= {"error": error.detail})