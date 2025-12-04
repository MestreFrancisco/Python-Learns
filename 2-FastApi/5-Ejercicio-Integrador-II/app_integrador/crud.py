import models,schemas
from sqlalchemy.orm import Session
from sqlalchemy import func

def get_clientes(db:Session):
    clientes = db.query(models.Cliente).all()
    return clientes

def get_cliente(db: Session,id:int):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == id).first()
    if cliente is None:
        return {"No existe"}
    
    return cliente

def crear_cliente(db: Session,cliente:schemas.ClienteCreate):
    cl = models.Cliente(nombre = cliente.nombre)
    
    db.add(cl)
    db.commit()
    db.refresh(cl)
    
    return cl

##---

def get_facturas(db:Session):
    factura = db.query(models.DetalleFactura).all()
    return factura

def get_factura(db: Session,id:int):
    detalle = db.query(models.DetalleFactura).filter(models.DetalleFactura.id == id).first()
    if detalle is None:
        return {"No existe"}
    
    return detalle

def crearfacturas(db: Session,cliente_id:int,detalle:schemas.FacturaCreate):
    fc = models.DetalleFactura(descripcion=detalle.descripcion,monto=detalle.monto,cliente_id=cliente_id)
    
    db.add(fc)
    db.commit()
    db.refresh(fc)
    recalcular_total_cliente(db=db,cliente_id=cliente_id)
        
    return fc

#CALCULO PARA RECALCULAR 
def recalcular_total_cliente(db: Session, cliente_id: int):
    total = db.query( # Abrimos una query
        func.sum(models.DetalleFactura.monto)#llamamos a la funcion suma
        ).filter(models.DetalleFactura.cliente_id == cliente_id #Luego filtramos la factura mediante el id del cliente pasado por parametro
    ).scalar() or 0

    #Luego Filtramos por id de cliente y le asignamos el total que obtuvimos previamente en la query
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    cliente.total_facturado = total

    db.commit()#Commit
    db.refresh(cliente)#Refrescamos el cliente
    return cliente


def editar_factura(db: Session,id: int,factura:schemas.FacturaCreate):
    detalle = db.query(models.DetalleFactura).filter(models.DetalleFactura.id == id).first()
    if detalle is None:
        return {"No existe"}

    update_data = factura.dict(exclude_unset=True)
    for key,value in update_data.items():
        setattr(detalle,key,value)
        
    db.commit()
    db.refresh(detalle)
    recalcular_total_cliente(db=db,cliente_id=detalle.cliente_id)
    return detalle


def eliminar_factura(db: Session,id: int):
    detalle = db.query(models.DetalleFactura).filter(models.DetalleFactura.id==id).first()
    cliente_id = detalle.cliente_id 
    
    db.delete(detalle)
    recalcular_total_cliente(db=db,cliente_id=cliente_id) #Siempre debemos llamar a la funcion que recalcula 😀
    
    db.commit()
  
    return True
    
    