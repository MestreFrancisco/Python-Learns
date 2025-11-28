from fastapi import Depends , FastAPI , HTTPException
from sqlalchemy.orm import Session
import models , schema , crud
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
        

@app.get("/")
def root():
    return {"msg":"Root"}


@app.get("/clientes",response_model=list[schema.Cliente])
def get_clientes(db: Session=Depends(get_db)):
    return crud.get_cliente(db=db)

@app.get("/clientes/{id}",response_model=schema.Cliente)
def get_clientes_x_id(id: int,db: Session=Depends(get_db)):
    db_cliente = crud.get_cliente_x_id(id=id,db=db)
    if db_cliente is None:
        raise HTTPException(status_code=404,detail="Cliente con id proporcionado no existe")
    return db_cliente

@app.delete("/clientes/{id}",response_model=schema.Cliente)
def get_clientes_x_id(id: int,db: Session=Depends(get_db)):
    db_cliente = crud.delete_cliente(id=id,db=db)
    if db_cliente is None:
        raise HTTPException(status_code=404,detail="Cliente con id proporcionado no existe")
    return db_cliente

@app.post("/clientes",response_model=schema.Cliente)
def post_cliente(cl:schema.ClienteCreate,db: Session=Depends(get_db)):
    db_cliente = crud.cr_cliente(db=db,cl=cl)
    return db_cliente

#---Pedido
@app.get("/pedidos",response_model=list[schema.Pedido])
def get_pedidos(db: Session=Depends(get_db)):
    return crud.get_pedido(db=db)

@app.get("/pedidos/{id}",response_model=schema.Pedido)
def get_pedidos_x_id(id:int,db: Session=Depends(get_db)):
    db_pedido = crud.get_pedido_x_id(id=id,db=db)
    if db_pedido is None:
        raise HTTPException(status_code=404,detail="Pedido con id proporcionado no existe")
    return db_pedido

@app.post("/pedidos/{id_cliente}", response_model=schema.Pedido)
def post_pedido(id_cliente: int, db: Session = Depends(get_db)):
    db_cliente = crud.get_cliente_x_id(db, id_cliente)
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente no existe")
    db_pedido = crud.cr_pedido(db=db, id_cliente=id_cliente)
    return db_pedido

#---DetalleProducto
@app.get("/detalles",response_model=list[schema.DetallePedido])
def get_detalles(db: Session=Depends(get_db)):
    return crud.get_detallepedido(db=db)

@app.get("/detalles/{id}",response_model=schema.DetallePedido)
def get_detalles_x_id(id:int,db: Session=Depends(get_db)):
    db_detalle = crud.get_detallepedido_x_id(id=id,db=db)
    if db_detalle is None:
        raise HTTPException(status_code=404,detail="Detalle con id proporcionado no existe")
    return db_detalle

@app.post("/detalles/{id_pedido}/{id_producto}",response_model=schema.DetallePedido)
def post_pedido(id_producto:int,id_pedido:int,db: Session=Depends(get_db)):
    db_pedido = crud.cr_detallepedido(id_pedido=id_pedido,id_producto=id_producto,db=db)
    return db_pedido

#---Producto
@app.get("/productos",response_model=list[schema.Producto])
def get_productos(db: Session=Depends(get_db)):
    return crud.get_producto(db=db)

@app.get("/productos/{id}",response_model=schema.Producto)
def get_productos_x_id(id:int,db: Session=Depends(get_db)):
    db_producto = crud.get_producto_x_id(id=id,db=db)
    if db_producto is None:
        raise HTTPException(status_code=404,detail="Producto con id proporcionado no existe")
    return db_producto

@app.post("/productos/{id_categoria}",response_model=schema.Producto)
def post_producto(pr:schema.ProductoCreate,id_categoria: int,db: Session=Depends(get_db)):
    db_pedido = crud.cr_producto(db=db,pr=pr,id_categoria=id_categoria)
    return db_pedido

#---Categoria
@app.get("/categorias",response_model=list[schema.Categoria])
def get_categorias(db: Session=Depends(get_db)):
    return crud.get_categoria(db=db)

@app.get("/categorias/{id}",response_model=schema.Producto)
def get_categorias_x_id(id:int,db: Session=Depends(get_db)):
    db_categoria = crud.get_categoria_x_id(id=id,db=db)
    if db_categoria is None:
        raise HTTPException(status_code=404,detail="Categoria con id proporcionado no existe")
    return db_categoria

@app.post("/categorias",response_model=schema.Categoria)
def post_producto(c:schema.CategoriaCreate,db: Session=Depends(get_db)):
    db_categoria = crud.cr_categoria(db=db,ct=c)
    return db_categoria