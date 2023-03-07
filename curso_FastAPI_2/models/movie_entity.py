from config.database import Base
from sqlalchemy import Column, Integer, String, Float
class MovieModel(Base):

    __tablename__  = "movies"

    id = Column(Integer, primary_key= True, autoincrement= "auto")
    title = Column(String(50))
    overview = Column(String(50))
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String(50))