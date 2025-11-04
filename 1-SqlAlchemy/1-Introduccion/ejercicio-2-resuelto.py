from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase
from sqlalchemy import String,DateTime,Float,Integer,Boolean
from datetime import datetime
from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass


class Alumnos(Base):
    __tablename__="Alumnos"


    id:Mapped[int]=mapped_column(primary_key=True)
    
    nombre:Mapped[str]=mapped_column(String(100),nullable=False)
    apellido:Mapped[str]=mapped_column(String(100),nullable=False)
    edad:Mapped[str]=mapped_column(Integer,nullable=False)
    promedio:Mapped[float]=mapped_column(Float,default=0.0)
    activo:Mapped[bool]=mapped_column(Boolean,nullable=False)
    fecha_ingreso:Mapped[datetime] = mapped_column(DateTime,default=datetime.now)
    

class Cursos(Base):
    __tablename__="Cursos"

    
    id:Mapped[int]=mapped_column(primary_key=True)

    nombre:Mapped[str]=mapped_column(String(100),nullable=False)
    descripcion:Mapped[str]=mapped_column(String(200),nullable=False)
    duracion_horas:Mapped[int]=mapped_column(Integer,nullable=False)
    costo:Mapped[float]=mapped_column(Float,nullable=False)
    activo:Mapped[bool]=mapped_column(Boolean,nullable=False)
    
    
class Profesores(Base):
    __tablename__="Profesores"
    
    id:Mapped[int]=mapped_column(primary_key=True)

    nombre:Mapped[str]=mapped_column(String(100),nullable=False)
    apellido:Mapped[str]=mapped_column(String(100),nullable=False)
    materia:Mapped[str]=mapped_column(String(100),nullable=False)
    salario:Mapped[str]=mapped_column(Float,nullable=False)
    fecha_contratacion:Mapped[datetime]=mapped_column(DateTime,nullable=False,default=datetime.now)
    activo:Mapped[bool]=mapped_column(Boolean)

engine = create_engine("sqlite:///escuela.db")
Base.metadata.create_all(engine)