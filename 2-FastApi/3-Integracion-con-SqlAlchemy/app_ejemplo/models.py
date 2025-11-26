from sqlalchemy.orm import mapped_column , Mapped ,Relationship
from sqlalchemy import String , DateTime , Boolean , ForeignKey
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "User"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    nombre:Mapped[str] = mapped_column(String(40))
    activo:Mapped[bool]=mapped_column(Boolean,default=True)
    creado_el:Mapped[datetime]=mapped_column(DateTime,default=datetime.now())
    
    #Relaciones
    items:Mapped[list["Item"]]=Relationship(back_populates="user")
    
class Item(Base):
    __tablename__ = "Item"
    
    id:Mapped[int]=mapped_column(primary_key=True)
    
    titulo:Mapped[str]=mapped_column(String(50))
    descripcion:Mapped[str]=mapped_column(String(50))
    
    #Relaciones
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    user:Mapped["User"] = Relationship(back_populates="items")