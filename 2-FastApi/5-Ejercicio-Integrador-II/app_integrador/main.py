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
        

@app.get("/")
def root():
    return {"msg":"Root"}


@app.get("/clientes",response_model=list[schemas.Cliente])
def get_clientes(db:Session=Depends(get_db)):
    return crud.get_clientes(db)
    

@app.get("/clientes/{id}",response_model=schemas.Cliente)
def get_cliente(id: int,db:Session=Depends(get_db)):
    return crud.get_cliente(db=db,id=id)


@app.post("/clientes",response_model=schemas.Cliente)
def post_cliente(cl:schemas.ClienteCreate,db:Session=Depends(get_db)):
    return crud.crear_cliente(db=db,cliente=cl)


@app.get("/detalles",response_model=list[schemas.Factura])
def get_detalles(db:Session=Depends(get_db)):
    return crud.get_facturas(db)
    

@app.get("/detalles/{id}",response_model=schemas.Factura)
def get_detalle(id: int,db:Session=Depends(get_db)):
    return crud.get_factura(db=db,id=id)


@app.post("/detalles/{cliente_id}",response_model=schemas.Factura)
def post_factura(fc:schemas.FacturaCreate,cliente_id: int,db: Session=Depends(get_db)):
    return crud.crearfacturas(db=db,cliente_id=cliente_id,detalle=fc)

@app.put("/detalles/{id}",response_model=schemas.Factura)
def get_detalle(id: int,factura:schemas.FacturaCreate,db:Session=Depends(get_db)):
    return crud.editar_factura(db=db,id=id,factura=factura)

@app.delete("/detalles/{id}",response_model=bool)#→Response bool
def delete_factura(id: int,db:Session=Depends(get_db)):
    return crud.eliminar_factura(db=db,id=id)