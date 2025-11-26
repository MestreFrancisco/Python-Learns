from pydantic import BaseModel
from typing import List , Optional
from datetime import datetime

class ItemModel(BaseModel):
    titulo:str
    descripcion:Optional[str]
    
class ItemCreate(ItemModel):
    pass

class Item(ItemModel):
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
        