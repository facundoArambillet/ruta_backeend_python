from config.database import Base
from sqlalchemy import Column, Integer, String
class UserModel(Base):

    __tablename__  = "users"

    id = Column(Integer, primary_key= True, autoincrement= "auto")
    email = Column(String)
    password = Column(String)