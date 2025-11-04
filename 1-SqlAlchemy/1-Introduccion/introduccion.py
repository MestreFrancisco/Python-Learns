"""
El Resumen esta debajo de todo.

SQLAlchemy es una librería de Python 
para trabajar con bases de datos relacionales (MySQL, PostgreSQL, SQLite, etc.) 
sin tener que escribir SQL manualmente todo el tiempo."""

"""Para empezar a trabajar con sqlalchemy se debe crear clase llamada Base
la cual extiende de DeclarativeBase

Antes, se usaba declarative_base() para crear una "base" de la que heredan todas las clases que representan tablas.
Desde SQLAlchemy 2.0, se usa una forma más moderna:
""" 

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

"""
Esto crea una clase Base que contiene:
- Un objeto MetaData (necesario para crear las tablas).(Los meta datos describen como se debe crear)
- La lógica interna del ORM para registrar las clases hijas.
- Luego defines tus modelos (tablas) heredando de Base: """

class User(Base): #→ Hereda de Base → Base hereda de DeclarativeBase
    __tablename__ = "User"  # nombre de la tabla en la base de datos , usamos __tablename__ = "NombreTabla"

"""mapped_column() define una columna en la tabla, 
y además le dice al ORM que se debe mapear al atributo de tu clase."""

from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String

class User(Base):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True) #→ AutoIncremental
    name = mapped_column(String(50), nullable=False) # → maximo 50 caracteres y no puede estar vacio
    
"""
Esto genera una tabla equivalente a:

CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
"""

"""
¿Qué es Mapped[]?

Mapped es un tipo genérico que se usa con anotaciones de tipo (type hints de Python).
Sirve para que el IDE (PyCharm, VSCode, Mypy) entienda que ese atributo es una columna mapeada.

Ejemplo moderno:"""

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

"""
Ventajas:

Menos código (si solo pones Mapped[str], SQLAlchemy infiere tipo y nullabilidad).

Mejor soporte de autocompletado y linters."""

"""
Crear la base de datos:
"""

from sqlalchemy import create_engine #Importamos el engine

engine = create_engine("sqlite:///mydb.db") #Ruta , Tipo de base de dato y nombre 
Base.metadata.create_all(engine) #Crea las tablas de todo lo que extienda de Base.

"""
En resumen: 
1-se crea Base que hereda DeclarativeBase 
2-creas una clase con el nombre de la talba y la heredas de Base
3-con __tablename__  = "Nombre Tabla" , le das el nombre a tu tabla
4-usas Mapped[str] para el mapear el tipo de dato
5-usas mapped_column() para mapear este dato como una columna dentro de sql.
6-creas el engine con el codigo de abajo

from sqlalchemy import create_engine 

engine = create_engine("sqlite:///mydb.db")
Base.metadata.create_all(engine)

"""
