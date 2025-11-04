# Usa los siguientes import o crea los tuyos propios.
from sqlalchemy import create_engine, String, Integer, Float, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column , Session
from datetime import datetime
from sqlalchemy import  create_engine , select 
from usuarios import Base , Usuarios



"A)Crea la tabla"
class Libro(Base):
    __tablename__="Libro"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    nombre:Mapped[str] = mapped_column(String(100),nullable=False)
    precio:Mapped[float] = mapped_column(Float,nullable=False)
    cantidad_hojas:Mapped[int]=mapped_column(Integer,default=50)
    fecha_creacion:Mapped[datetime]=mapped_column(DateTime,default=datetime.now)


lista_libros=[
    Libro(nombre="Leyenda de Ang",
             precio=4000.13,
             cantidad_hojas=500,
             fecha_creacion=datetime(1999,10,5)),
    
    Libro(nombre="Papilas Gustativas",
             precio=14000.93,
             cantidad_hojas=5200,
             fecha_creacion=datetime(1998,10,5)),
    
    Libro(nombre="Avatar 34",
             precio=1000.33,
             cantidad_hojas=2500,
             fecha_creacion=datetime(2019,10,5)),
    
    Libro(nombre="Sinsajos",
             precio=12000,
             cantidad_hojas=4000.33,
             fecha_creacion=datetime(2019,10,5)),
    Libro(nombre="Diluvio",
             precio=400.03,
             cantidad_hojas=200,
             fecha_creacion=datetime(2000,12,6)),
    Libro(nombre="Francos Insufribles",
             precio=400.03,
             cantidad_hojas=5000,
             fecha_creacion=datetime(2000,10,26)),
    
]

engine = create_engine("sqlite:///biblioteca.db")
Base.metadata.create_all(engine)

with Session(engine) as session:
    
    session.add_all(lista_libros)
    
    session.commit()
    
    "SELECT"
    
    stmt = select(Libro)
    
    libros = session.scalars(stmt).all()
    
    for l in libros:
        if l.precio < 4000 and l.cantidad_hojas >= 1000:
            print(f"ID:{l.id},NOMBRE:{l.nombre},PRECIO:{l.precio},HOJAS:{l.cantidad_hojas},FECHA:{l.fecha_creacion}") 
        else:
            pass