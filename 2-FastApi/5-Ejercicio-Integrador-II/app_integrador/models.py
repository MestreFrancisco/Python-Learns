from sqlalchemy.orm import Mapped , mapped_column , relationship
from sqlalchemy import ForeignKey , String , Float
from database import Base

class Cliente(Base):
    __tablename__ = "Cliente"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    nombre:Mapped[str] = mapped_column(String(40))
    total_facturado:Mapped[float] = mapped_column(Float,default=0)
    lista_de_facturas:Mapped[list["DetalleFactura"]]=relationship(
        back_populates="cliente", 
        cascade="all, delete-orphan")


class DetalleFactura(Base):
    __tablename__ = "DetalleFactura"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    descripcion:Mapped[str] = mapped_column(String(40))
    monto:Mapped[float] = mapped_column(Float)
    
    cliente_id:Mapped[int] = mapped_column(ForeignKey(
        "Cliente.id",
        ondelete="CASCADE"))
    
    cliente:Mapped["Cliente"] = relationship(back_populates="lista_de_facturas")
    
    