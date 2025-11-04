"""
Sessions:

las sesiones son el puente entre Python y la base de datos
basicamente con las sesion podremos hacer consultas sql y manipular
los datos que en ella se encuentran

 → podemos crear datos
 → eliminar datos
 → editar datos
 → leer datos
 
es decir las operaciones crud basicas 

Cada objeto que cargas o agregas al Session se guarda en una estructura llamada identity map.
Esta estructura asegura que solo haya una instancia de un objeto por clave primaria.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg2://usuario:pass@localhost/db")

"""
Usando context manager, se cierra automáticamente

with Session(engine) as session:
    session.add(objetos) → aqui iria una instancia de algun objeto
    session.commit()  → Opcional si no hay cambios
    
Como podemos ver se usara el engine para abrir la session.
Dentro de esta carpeta estaran algunos metodos para usar con session
no estan todos los metodos , por lo que puedes averiguar alguno por tu cuenta 

→ mira los ejemplos de como usarlos.

→ ejemplo_1.py Explica como abrir session y hacer un add
→ ejemplo_2.py Explica como añadir varios objetos , traer por id y eliminar.
→ ejemplo_3.py Explica como hacer un select global y como hacer un select por columna

"""

