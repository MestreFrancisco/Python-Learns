from sqlalchemy.orm import DeclarativeBase , sessionmaker
from sqlalchemy import create_engine 

#clase Base → DeclarativeBase
class Base(DeclarativeBase):
    pass

#Crear el engine
engine = create_engine("sqlite:///facturacion.db",connect_args={"check_same_thread":False})

# Crear una session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
