from pydantic import BaseModel,Field
from typing import Optional

class MovieModel(BaseModel):
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