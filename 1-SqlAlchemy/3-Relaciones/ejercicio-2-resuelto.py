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
    
    pasaporte:Mapped["Pasaporte"] = relationship(back_populates="cliente",uselist=False)
    nombre:Mapped[str] = mapped_column(String(50))
    edad:Mapped[int] = mapped_column(Integer)
    
class Pasaporte(Base):
    __tablename__="Pasaporte"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    cliente_id:Mapped[int]=mapped_column(ForeignKey("Cliente.id"),unique=True)
    numero:Mapped[str]=mapped_column(String(4),nullable=False)
    cliente:Mapped["Cliente"]=relationship(back_populates="pasaporte")
    
engine = create_engine("sqlite:///gestion.db")
Base.metadata.create_all(engine)

cl1 = Cliente(nombre="Franco",edad=20)
cl2 = Cliente(nombre="Luciana",edad=23)
cl3 = Cliente(nombre="Mariana",edad=26)

ps1 = Pasaporte(numero="ARG3") 
ps2 = Pasaporte(numero="BRA7") 
ps3 = Pasaporte(numero="PAR4") 


cl1.pasaporte = ps3
cl2.pasaporte = ps1
cl3.pasaporte = ps2

with Session(engine) as session:
    
    session.add(cl1)
    session.add(cl2)
    session.add(cl3)
    
    session.commit()
    
    smtm = select(Cliente)
    
    clientes_q = session.scalars(smtm).all()
    
    for cl in clientes_q:
        
        print(f"Nombre:{cl.nombre} Id{cl.id}, Pasaporte Numero:{cl.pasaporte.numero}")