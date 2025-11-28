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


## INDICE

+ 1-[Database](#1-database)
+ 2-[Models](#2-models)
+ 3-[Schemas](#3-schemas)
+ 4-[Crud](#4-crud)
+ 5-[Main](#5-mainpy)
+ 6-[Extras](#extras)

---
## 1) **Database** 
en esta seccion crearemos la configuracion para la base de datos con **sqlalchemy** usaremos la forma de crearla de sqlachemy 2.0

```python
from sqlalchemy.orm import DeclarativeBase , sessionmaker
from sqlalchemy import create_engine 
from pathlib import Path
from sqlalchemy import create_engine

# Ruta absoluta hacia la carpeta del script
db_path = Path(__file__).parent / "mi_base.db"

# Crear engine con SQLite apuntando a esa ruta

#clase Base → DeclarativeBase
class Base(DeclarativeBase):
    pass

engine = create_engine(f"sqlite:///{db_path}",connect_args={"check_same_thread":False},echo=True)

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

```python
import schemas, models
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_user(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def get_users(db: Session, limit: int = 50):
    return db.query(models.User).limit(limit).all()


def create_user(db: Session, u: schemas.UserCreate):
    db_user = models.User(nombre=u.nombre)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_item(db: Session, id: int):
    return db.query(models.Item).filter(models.Item.id == id).first()


def get_items(db: Session, limit: int = 50):
    return db.query(models.Item).limit(limit).all()


def create_user_item(db: Session, I: schemas.ItemCreate, id_user: int):
    db_item = models.Item(
        titulo=I.titulo,
        descripcion=I.descripcion,
        user_id=id_user
    )

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, id: int, I: schemas.ItemCreate):
    item_filter = db.query(models.Item).filter(models.Item.id == id).first()

    if item_filter is None:
        raise HTTPException(status_code=404, detail="No existe el item")

    update_data = I.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(item_filter, key, value)

    db.commit()
    db.refresh(item_filter)
    return item_filter


def delete_item(db: Session, id: int):
    item_db = db.query(models.Item).filter(models.Item.id == id).first()

    if item_db is None:
        raise HTTPException(status_code=404, detail="No existe el item")

    db.delete(item_db)
    db.commit()
    return {"msg": "Item eliminado", "id": item_db.id}

```
## 5) **main.py**

Finalmente en el main llamaremos al engine para crear la base de datos , tambien crearemos una session para poder subir los datos a la base de datos y crearemos los distintos endpoints

+ Es importante mencionar el hecho de que no se usa async en sqlite 

```python
from fastapi import Depends , FastAPI , HTTPException
from sqlalchemy.orm import Session
import models , schemas , crud
from database import SessionLocal,engine

#Crear Tablas
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


#Funcion de dependencia para obteber sessiones de base de Datos

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/ping")
def ping():
    return {"ping": "pong"}
        
        
@app.get("/api")
def root():
    return {"msg":"Root"}


@app.post("/api/users",response_model=schemas.User)
def create_user(u:schemas.UserCreate,db:Session = Depends(get_db)):
    return crud.create_user(db=db,u=u)


@app.get("/api/users",response_model=list[schemas.User])
def get_users(db:Session=Depends(get_db)):
    return crud.get_users(db=db)

@app.get("/api/users/{id}",response_model=schemas.User)
def get_users_by_id(id:int,db:Session=Depends(get_db)):
    db_user_crud =  crud.get_user(db=db,id=id)
    if db_user_crud is None:
        raise HTTPException(status_code=404,detail="Usuario con id proporcionado no existe")
    return db_user_crud

@app.put("/api/items/{id}",response_model=schemas.Item)
def update_item_by_id(id:int,I:schemas.ItemCreate,db:Session=Depends(get_db)):
    item_db_crud = crud.update_item(db=db,id=id,I=I)
    if item_db_crud is None:
        raise HTTPException(status_code=404,detail="Item con el id proporcionado no existe")
    return item_db_crud

@app.get("/api/items",response_model=list[schemas.Item])
def get_items(db:Session=Depends(get_db)):
    return crud.get_items(db=db)

@app.get("/api/items/{id}",response_model=schemas.Item)
def get_items_by_id(id:int,db:Session=Depends(get_db)):
    item_db_crud = crud.get_item(db=db,id=id)
    if item_db_crud is None:
        raise HTTPException(status_code=404,detail="Item con id proporcionado no existe")
    return item_db_crud

@app.delete("/api/items/{id}",response_model=schemas.Item)
def delte_item_by_id(id:int,db:Session=Depends(get_db)):
    item_db_crud = crud.delete_item(db=db,id=id)
    if item_db_crud is None:
        raise HTTPException(status_code=404,detail="Item con id proporcionado no existe")
    return item_db_crud

@app.post("/api/users/{id}/items")
def post_user_item(id:int,I:schemas.ItemCreate,db:Session=Depends(get_db)):
    u = crud.get_user(db=db,id=id)
    if u is None:
        raise HTTPException(status_code=404,detail="User con id proporcionado no existe")
    return crud.create_user_item(I=I,db=db,id_user=id)
```

## Extras
si no te carga el server usar para killear el server

```bash
taskkill /PID 12868 /F
```

para ver la lista de puertos usar

```bash
netstat -ano | findstr :8000
  TCP    127.0.0.1:8000         0.0.0.0:0              LISTENING       12868
  TCP    127.0.0.1:8000         127.0.0.1:52776        ESTABLISHED     12868
```
