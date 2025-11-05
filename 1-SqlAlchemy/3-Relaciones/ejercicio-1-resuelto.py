# Imports utiles
from sqlalchemy import create_engine, String, Integer, Float, Boolean, DateTime , ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column , Session ,relationship 
from datetime import datetime
from sqlalchemy import  create_engine , select 


class Base(DeclarativeBase):
    pass

class Cliente(Base):
    __tablename__ = "Cliente"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    facturas:Mapped[list["Factura"]] = relationship(back_populates="cliente")
    nombre:Mapped[str] = mapped_column(String(50))
    edad:Mapped[int] = mapped_column(Integer)
    
class Factura(Base):
    __tablename__ = "Factua"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    id_cliente:Mapped[int] = mapped_column(ForeignKey("Cliente.id"))
    cliente:Mapped["Cliente"] = relationship(back_populates="facturas")
    total:Mapped[float] = mapped_column(Float,nullable=False)
    

engine = create_engine("sqlite:///facturacion.db")
Base.metadata.create_all(engine)

# 2) CREACION DE CLIENTE Y FACTURA

cl1 = Cliente(nombre="Francisco",edad=22)
cl2 = Cliente(nombre="Nicolas",edad=25)

fc1 = Factura(total=2500.24)
fc2 = Factura(total=5500.84)
fc3 = Factura(total=30.14)
fc4 = Factura(total=15500.84)


cl1.facturas = [fc1,fc2]
cl2.facturas = [fc3,fc4]

with Session(engine) as session:
    
   session.add(cl1) 
   session.add(cl2)
   
   session.commit()
   
   smtm = select(Cliente)
   
   clientes = session.scalars(smtm).all()
   
   for cl in clientes:
          
       print(f"Nombre {cl.nombre} , Id Cliente:{cl.id}\n-→ Total Factura:{cl.facturas[0].total+cl.facturas[1].total}") 
    
## Por supuesto esto funciona por que sabemos que ambos tienen solo dos facturas si no fuese el caso daria error