from usuarios import Usuarios , Base
from sqlalchemy.orm import Session
from sqlalchemy import  create_engine

engine = create_engine("sqlite:///user.db")
Base.metadata.create_all(engine)

listaDeUsuarios=[
    Usuarios(nombre="Franco",edad="31"),
    Usuarios(nombre="Martin",edad="21"),
    Usuarios(nombre="Nerina",edad="41"),
    Usuarios(nombre="Olga",edad="39"),
    Usuarios(nombre="Pablo",edad="22"),
    Usuarios(nombre="Quico",edad="25"),
]

with Session(engine) as session:
    
    session.add_all(listaDeUsuarios) # → Subimos varios objetos
    session.commit() # → Confirmamos el cambio y lo subimos en la base

    user = session.get(Usuarios,2) #Obtenemos el user con el id→2 (Pasar Clase e Id)
    session.delete(user) # Eliminar user obtenido
    
    session.commit()

    