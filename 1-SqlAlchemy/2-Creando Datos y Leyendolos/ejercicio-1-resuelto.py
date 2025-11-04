# Usa los siguientes import o crea los tuyos propios.
from sqlalchemy import create_engine, String, Integer, Float, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column , Session
from datetime import datetime
from sqlalchemy import  create_engine , select 
from usuarios import Base , Usuarios



"A)Crea la tabla"
class Productos(Base):
    __tablename__="Productos"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    nombre:Mapped[str] = mapped_column(String(100),nullable=False)
    precio:Mapped[float] = mapped_column(Float,nullable=False)
    stock:Mapped[int]=mapped_column(Integer,default=0)
    activo:Mapped[bool]=mapped_column(Boolean,nullable=False)
    fecha_creacion:Mapped[datetime]=mapped_column(DateTime,default=datetime.now)
    
#Creando engine
engine = create_engine("sqlite:///tienda.db")
Base.metadata.create_all(engine)

"B) ABRE UNA SESSION"
with Session(engine) as session:
    
    "C) CRANDO OBJETOS"
    #producto-1
    coca_cola = Productos(
            nombre="Coca-cola",
            precio=2000.0,
            stock=4,
            activo=True,
            fecha_creacion=datetime(2025,11,2),
            )
    #producto-2
    papas = Productos(
            nombre="Papas",
            precio=1000.50,
            stock=3,
            activo=True,
            fecha_creacion=datetime(2025,11,1),
            )
    #producto-stock-default
    pollo = Productos(
            nombre="Pollo",
            precio=1440.66,
            activo=True,
            fecha_creacion=datetime(2025,10,2),
            )
    #producto-fecha-default
    lechuga = Productos(
            nombre="Lechuga",
            precio=1440.66,
            stock=2,
            activo=True,
            )
    #Usuario
    session.add(Usuarios(nombre="Francisco",edad=24))
    
    session.add(coca_cola)
    session.add(papas)
    session.add(pollo)
    session.add(lechuga)
    
    session.commit()
    
    select_productos = select(Productos.id,
                              Productos.nombre,
                              Productos.stock,
                              Productos.precio)
    
    filas = session.execute(select_productos).all()
    
    for fila in filas:
        print(fila)