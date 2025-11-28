import schema, models
from fastapi import HTTPException
from sqlalchemy.orm import Session

#Cliente
def get_cliente_x_id(db:Session,id: int):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == id).first()
    if db_cliente is None:
        return {"msg":"No existe Cliente con tal ID"}
    return db_cliente

def get_cliente(db:Session):
    return db.query(models.Cliente).all()

def cr_cliente(db: Session,cl:schema.ClienteCreate):
    cliente = models.Cliente(nombre=cl.nombre,mail=cl.mail) 
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

def delete_cliente(db: Session,id:int):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == id).first()
    if db_cliente is None:
        return {"msg":"No existe Cliente con tal ID"}
    db.delete(db_cliente)
    db.commit()
    return True

#Pedido
def get_pedido_x_id(db:Session,id: int):
    db_pedido = db.query(models.Pedido).filter(models.Pedido.id == id).first()
    if db_pedido is None:
        return {"msg":"No existe Pedido con tal ID"}
    return db_pedido

def get_pedido(db:Session):
    return db.query(models.Pedido).all()

def cr_pedido(db: Session,id_cliente: int):
    pedido = models.Pedido(cliente_id=id_cliente) 
    db.add(pedido)
    db.commit()
    db.refresh(pedido)
    return pedido

#Producto
def get_producto_x_id(db:Session,id: int):
    db_producto = db.query(models.Producto).filter(models.Producto.id == id).first()
    if db_producto is None:
        return {"msg":"No existe Producto con tal ID"}
    return db_producto

def get_producto(db:Session):
    return db.query(models.Producto).all()

def cr_producto(db: Session,pr:schema.ProductoCreate,id_categoria: int):
    producto_db = models.Producto(nombre=pr.nombre,precio=pr.precio,categoria_id=id_categoria) 
    db.add(producto_db)
    db.commit()
    db.refresh(producto_db)
    return producto_db
    

#Categoria
def get_categoria_x_id(db:Session,id: int):
    db_categoria = db.query(models.Categoria).filter(models.Categoria.id == id).first()
    if db_categoria is None:
        return {"msg":"No existe Categoria con tal ID"}
    return db_categoria

def get_categoria(db:Session):
    return db.query(models.Categoria).all()

def cr_categoria(db: Session,ct:schema.CategoriaCreate):
    categoria = models.Categoria(nombre=ct.nombre) 
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria


#DetallePedido
def get_detallepedido_x_id(db:Session,id: int):
    db_detalle = db.query(models.DetallePedido).filter(models.DetallePedido.id == id).first()
    if db_detalle is None:
        return {"msg":"No existe Detalle con tal ID"}
    return db_detalle

def get_detallepedido(db:Session):
    return db.query(models.DetallePedido).all()

def cr_detallepedido(db: Session,id_producto:int,id_pedido:int):
    db_detalle = models.DetallePedido(producto_id=id_producto,pedido_id=id_pedido) 
    db.add(db_detalle)
    db.commit()
    db.refresh(db_detalle)
    return db_detalle