from pydantic import BaseModel
from typing import List,Optional

#Categoria
class CategoriaBase(BaseModel):
    nombre:str

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id:int
    
    class config:#orm
        orm_mode=True
        
#Producto
class ProductoBase(BaseModel):
    nombre:str
    
  
class ProductoCreate(ProductoBase):
    precio:float

class Producto(ProductoBase):
    id:int
    categoria_id:int
    precio:int
    
    class config: #orm
        orm_mode=True
        
# DetallePedido
class DetallePedidoBase(BaseModel):
    pass

class DetallePedidoCreate(DetallePedidoBase):
    pass


class DetallePedido(DetallePedidoBase):
    id:int
    producto_id:int
    pedido_id:int
    cantidad:int
    subtotal:float
    
    class config: #orm
        orm_mode=True

#Pedido
class PedidoBase(BaseModel):
    pass

class PedidoCreate(PedidoBase):
    pass

class Pedido(PedidoBase):
    id:int
    cliente_id:int
    detalles_de_pedidos:List[DetallePedido] = []
    total:float
    
    class config: #orm
        orm_mode=True

#Cliente
class ClienteBase(BaseModel):
    nombre:str
    mail:str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id:int
    pedidos:List[Pedido] = []
    
    class config: #orm
        orm_mode=True