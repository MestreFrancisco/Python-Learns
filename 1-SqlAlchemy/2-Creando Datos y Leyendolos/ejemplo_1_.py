from usuarios import Usuarios , Base
from sqlalchemy.orm import Session
from sqlalchemy import  create_engine

engine = create_engine("sqlite:///user.db")
Base.metadata.create_all(engine)

with Session(engine) as session:
    fran = Usuarios(nombre="Francisco",edad=22) #Creamos un usuarios
    
    session.add_all(fran) #Lo pasamos como parametro
    session.commit() # Confirmamos el cambio y lo subimos en la base

    