# Integracion FastApi con SqlAlchemy

Estructura de un proyecto FastApi con SqlAlchemy

```console
my_project/
│
├── app/
│   ├── __init__.py            # Inicialización del paquete
│   ├── main.py                # Archivo principal donde se corre la app FastAPI
│   ├── models.py              # Modelos de la base de datos con SQLAlchemy
│   ├── crud.py                # Funciones CRUD (Create, Read, Update, Delete)
│   ├── schemas.py             # Esquemas de Pydantic para validación
│   ├── api.py                 # Rutas de la API
│   └── database.py            # Configuración de la base de datos con SQLAlchemy
│
├── requirements.txt           # Dependencias del proyecto
├── .env                       # Variables de entorno (Base de datos, secreto, etc)
└── README.md                  # Documentación del proyecto
```

## Empezando

Comenzamos creando la estructura del proyecto para organizarlo , ahora lo ponemos en archivos python, pero lo ideal seria que tuvieras una carpeta para cada casi cada archivo , almenos para **Models** y **Schemas** 

---
## 1) **Database** 
en esta seccion crearemos la configuracion para la base de datos con **sqlalchemy** usaremos la forma de crearla de sqlachemy 2.0

```python
from sqlalchemy.orm import DeclarativeBase , sessionmaker
from sqlalchemy import create_engine 

#clase Base → DeclarativeBase
class Base(DeclarativeBase):
    pass

#Crear el engine
engine = create_engine("sqlite:///facturacion.db",connect_args={"check_same_thread":False})

# Crear una session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
```
---
## 2) **Models**

En la carpeta o archivo models , modelamos la tabla exacatamente igual a como la modelariamos normalmente , lo unico que cambia es que importamos la clase Base desde el archivo **database.py**

```python
from sqlalchemy.orm import mapped_column , Mapped ,Relationship
from sqlalchemy import String , DateTime , Boolean , ForeignKey
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "User"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    nombre:Mapped[str] = mapped_column(String(40))
    activo:Mapped[bool]=mapped_column(Boolean,default=True)
    creado_el:Mapped[datetime]=mapped_column(DateTime,default=datetime.now())
    
    #Relaciones
    items:Mapped[list["Item"]]=Relationship(back_populates="user")
    
class Item(Base):
    __tablename__ = "Item"
    
    id:Mapped[int]=mapped_column(primary_key=True)
    
    titulo:Mapped[str]=mapped_column(String(50))
    descripcion:Mapped[str]=mapped_column(String(50))
    
    #Relaciones
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    user:Mapped["User"] = Relationship(back_populates="items")
```

## 3) **Schemas**

Los esquemas de pydantic son un validador de datos de tu tabla creada con sqlalchmey , donde se define como se muestran y validan tus datos

+ Los schemas NO son modelos de la base de datos.
+ No crean tablas. No guardan datos.
+ Solo validan y definen estructura.

el schema controla los datos que muestra tu api , por ejemplo si en tu base de datos tienes contraseñas , con el schema podemos mostrar solo el nombre reduciendo la info de salida.

```py
from pydantic import BaseModel
from typing import List , Optional
from datetime import datetime

class ItemModel(BaseModel):#Datos Comunes
    titulo:str
    descripcion:Optional[str]
    
class ItemCreate(ItemModel):#Datos Necesarios para crear un Item
    pass

class Item(ItemModel):#Clase con los datos que se muestran en pantalla
    id:int
    user_id:int
    
    class config:
        orm_mode=True

#---°---°---°---°---°---°---

class UserModel(BaseModel):
    nombre:str

class UserCreate(UserModel):
    pass

class User(UserModel):
    id:int
    activo:bool
    creado_el:datetime
    items:List[Item] = []
    
    class config:
        orm_mode=True
        
```
---
Creamos Tres esquemas distintos para distintas cosas , el primero es de datos comunes , el segundo que es el create , pondremos los datos que necesitamos para crear el objeto y finalmente el ultimo es la clase que usaremos para mostrar la informacion en pantalla

## 4) **CRUD**

En la seccion del crud controlaremos las funciones basicas de la base de dato , crear , leer , editar y eliminar datos , usaremos la base de datos , los modelos y los schemas para esto. Crearemos las funciones necesarias para usarlas luego para hacer los metodos en la Api

