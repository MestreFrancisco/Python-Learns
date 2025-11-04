from sqlalchemy.orm import DeclarativeBase , Mapped,mapped_column
from sqlalchemy import String , Integer


class Base(DeclarativeBase):
    pass

class Usuarios(Base):
    __tablename__ = "Usuarios"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    nombre:Mapped[str] = mapped_column(String(50),nullable=False)
    edad:Mapped[int] = mapped_column(Integer())
    
    