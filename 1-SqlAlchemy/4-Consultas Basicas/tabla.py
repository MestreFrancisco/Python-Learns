from sqlalchemy.orm import DeclarativeBase , Mapped , mapped_column ,relationship ,Session
from sqlalchemy import select , String , Integer , Float , ForeignKey ,create_engine 
import random as r

class Base(DeclarativeBase):
    pass 

#TABLA CLIENTE
class Cliente(Base):
    __tablename__="Cliente"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    nombre:Mapped[str] = mapped_column(String(30),nullable=False)
    apellido:Mapped[str] = mapped_column(String(30),nullable=False)
    
    facturas:Mapped[list["Factura"]] = relationship(back_populates="cliente")

#TABLA FACTURA
class Factura(Base):
    __tablename__="Factura"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    cliente_id:Mapped[int]=mapped_column(ForeignKey("Cliente.id"))
    
    total:Mapped[float]=mapped_column(Float)
    tipo_factura:Mapped[str]=mapped_column(String(1),nullable=False)
    
    
    cliente:Mapped["Cliente"]=relationship(back_populates="facturas")
    

#engine=create_engine("sqlite:///facturacion.db")
#Base.metadata.create_all(engine)


lista_cliente=[
     Cliente(nombre="Francisco",apellido="Mestre"),
     Cliente(nombre="Franco",apellido="Mendez"),
     Cliente(nombre="Camila",apellido="Balbontin"),
     Cliente(nombre="Julieta",apellido="Mestre"),
     Cliente(nombre="Nicolas",apellido="Avellaneda"),
     Cliente(nombre="Carlos",apellido="Quintero"),
]

for i in lista_cliente:
    
    cantidad_factura = r.randint(2,5)    
    lista_facturas=[]
    for j in range(cantidad_factura):
        fc = Factura(
                    total=round(r.uniform(10.5,126_000),2),
                    tipo_factura=r.choice(["A","B","C"]))
        
        lista_facturas.append(fc)
        
    #EXIT
    i.facturas = lista_facturas

#with Session(engine) as session:
    #session.add_all(lista_cliente)
    #session.commit()