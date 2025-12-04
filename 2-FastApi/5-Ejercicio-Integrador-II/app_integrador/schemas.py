from pydantic import BaseModel
from typing import List


class ClienteBase(BaseModel):
    nombre:str
    

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id:int
    total_facturado:float
    
    class config:#orm
        orm_mode=True
    
class FacturaBase(BaseModel):
    descripcion:str
    monto:float

class FacturaCreate(FacturaBase):
    pass
    
class Factura(FacturaBase):
    id:int
    cliente_id:int
    
    class config:
        orm_mode=True
        
