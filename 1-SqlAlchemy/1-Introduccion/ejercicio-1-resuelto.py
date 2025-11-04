#Usa los siguientes import se libre de hacer el tuyo.
from sqlalchemy import create_engine, String, Integer, Float, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from sqlalchemy import create_engine

engine = create_engine("sqlite:///tienda.db")

class Base(DeclarativeBase):
    pass

#Producto
class Producto(Base):
    __tablename__ = "Productos"
    
    id :Mapped[int] = mapped_column(primary_key=True)
    
    nombre:Mapped[str] = mapped_column(String(100),nullable=False)
    precio:Mapped[float] = mapped_column(Float,nullable=False)
    stock:Mapped[int] = mapped_column(Integer,default=0)
    activo:Mapped[bool] = mapped_column(nullable=False)
    fecha_creacion:Mapped[datetime] = mapped_column(DateTime,default=datetime.now)
    
class Facturas(Base):
    __tablename__ = "Facturas"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    fecha_factura:Mapped[datetime] = mapped_column(DateTime,nullable=False)
    total:Mapped[float]=mapped_column(Float)
    metodo_pago:Mapped[str]=mapped_column(String(50),nullable=True)
    activo:Mapped[bool]=mapped_column()    

Base.metadata.create_all(engine)