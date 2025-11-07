# SQLAlchemy con Python

SQLAlchemy es una librería de Python para trabajar con bases de datos relacionales (MySQL, PostgreSQL, SQLite, etc.) sin tener que escribir SQL manualmente todo el tiempo.

---

## Tabla de Contenidos

- [Instalación](#instalación)  
- [Configuración Inicial](#configuración-inicial)   
- [Como Crear Tablas?](#como-crear-tablas)   
- [Tipos Mapped y mapped_column](#tipos-mapped-y-mapped_column)  
- [Creación de la Base de Datos](#creación-de-la-base-de-datos)  
- [Resumen](#resumen)  

---

## Instalación

```bash
pip install sqlalchemy
```

## Configuración Inicial

Desde SQLAlchemy 2.0, se recomienda usar DeclarativeBase para definir la clase base de los modelos.
from sqlalchemy.orm import DeclarativeBase

```python
class Base(DeclarativeBase):
    pass
```

La clase Base contiene:
+ Un objeto MetaData necesario para crear las tablas.
+ La lógica interna del ORM para registrar las clases hijas.
+ Definición de Modelos 
---
## Como Crear Tablas
Para crear una tabla, defines una clase que herede de Base y defines el nombre de la tabla:

```python
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String

class User(Base):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True)   # AutoIncremental
    name = mapped_column(String(50), nullable=False) # Máximo 50 caracteres y obligatorio

```

```sql
Equivalente a SQL:

CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
```

## Tipos Mapped y mapped_column

Mapped es un tipo genérico que ayuda a los ides y linters a entender que un atributo está mapeado a una columna en la base de datos.

Osea: 
+ Mapped[`Tipo`] mapea el tipo de dato
+ `mapped_column()` mapea y crea una columna dentro de la base de datos

```python
#Ejemplo moderno:

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

```

Ventajas:

+ Menos código, SQLAlchemy infiere el tipo y la nullabilidad.

+ Mejor soporte para autocompletado y linters.

## Creación de la Base de Datos

Para crear la base de datos y las tablas:

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mydb.db")  # Tipo de DB y nombre
Base.metadata.create_all(engine)  # Crea todas las tablas definidas
```

## Resumen

+ Crear Base que hereda de DeclarativeBase.

+ Crear clases para cada tabla heredando de Base.

+ Definir __`__tablename__`__ = "NombreTabla" para nombrar la tabla.

+ Usar Mapped[Tipo] para mapear los tipos de datos.

+ Usar __`mapped_column()`__ para definir columnas de SQL.

+ Crear el engine y generar las tablas:

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mydb.db")
Base.metadata.create_all(engine)
```
---
De esta forma creamos bases de datos en SqlAlchemy
---

+ [Volver Arriba](#sqlalchemy-con-python)
+ [Ejercicios](python-sql-Ejercicio-1.md)
+ [Siguiente tema Creando Datos Y Leyendolos](../2-Creando%20Datos%20y%20Leyendolos/introduccion.py)