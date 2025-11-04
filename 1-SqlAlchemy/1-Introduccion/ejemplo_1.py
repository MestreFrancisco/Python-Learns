"""Recomiendo Usar Db browser Sqlite para ver la base"""

from sqlalchemy.orm import DeclarativeBase #Importamos DeclarativeBase
from sqlalchemy.orm import Mapped,mapped_column #Importamos esto para mapear datos y mapear columnas
from sqlalchemy import String , Integer
from sqlalchemy import create_engine #Importamos el engine


class Base(DeclarativeBase): #Extendemos
    pass

class User(Base):
    __tablename__ = "Usuarios"
    
    id:Mapped[int]=mapped_column(primary_key=True)
    
    nombre: Mapped[str] = mapped_column(String(30))
    apellido: Mapped[str] = mapped_column(String(30)) 
    edad: Mapped[int] = mapped_column(Integer)
    pais: Mapped[str] = mapped_column(String(15))
    
engine = create_engine("sqlite:///mydb.db") #Ruta , Tipo de base de dato y nombre 
Base.metadata.create_all(engine) #Crea las tablas de todo lo que extienda de Base.

"""Ya que Sabemos crear Una Tabla ahora veamos como subir los Datos"""