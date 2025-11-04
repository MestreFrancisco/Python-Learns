from usuarios import Usuarios , Base
from sqlalchemy.orm import Session
from sqlalchemy import  create_engine , select

engine = create_engine("sqlite:///user.db")
Base.metadata.create_all(engine)


with Session(engine) as session:
    
    #--SELECT GLOBAL---
    
    stmt_all = select(Usuarios)  # Selecciona todos los usuarios y todas sus columnas
    usuarios = session.scalars(stmt_all).all()  # Devuelve lista de objetos User
    
    print("SELECT GLOBAL")
    for u in usuarios:
        print(f"Nombre: {u.nombre} ,Edad:{u.edad}")
    
    stmt_column = select(Usuarios.id,Usuarios.nombre)
    filas = session.execute(stmt_column).all()  # Devuelve lista de Row objects
    print("SELECT DE COLUMNAS ESPECIFICAS")
    for fila in filas:
        """ 
        → Si llamamos e un parametro que no fue seleccionado dara un raise error
        
        print(fila) print(fila.nombre , fila.edad) 
        
        _key_not_found
        raise AttributeError(ke.args[0]) from ke
        AttributeError: id
        """
    
"""
- `select(User)` → trae toda la fila como objeto ORM `User`.
  
- `select(User.name, User.fullname)` → trae solo las columnas 
    especificadas y devuelve `Row` en lugar de objetos ORM.  
    
- `session.scalars()` se usa para extraer directamente los objetos de una consulta completa.
  
- `session.execute()` se usa para consultas más flexibles o columnas parciales.
"""