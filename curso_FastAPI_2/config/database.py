import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
sqlite_file_name = "../database.sqlite" #Nombre con el que se crea la BDD  de SQLite

base_dir = os.path.dirname(os.path.realpath(__file__))
#mysql_dir = 'mysql://root:123456789@localhost/database_mysql'
DB_USER = "root"
DB_PASSWORD = "123456789"
DB_HOST = "localhost"
DB_NAME = "database_mysql"

DATABASE_URL = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

database_url = f"sqlite:///{os.path.join(base_dir,sqlite_file_name)}"

engine = create_engine(database_url, echo=True)

engine_mysql = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind = engine)
Session_mysql = sessionmaker(bind = engine_mysql)

Base = declarative_base()