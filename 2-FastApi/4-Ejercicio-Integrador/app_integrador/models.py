from sqlalchemy.orm import Mapped , mapped_column , relationship 
from sqlalchemy import String,Integer,Float,DateTime , ForeignKey
from database import Base
from datetime import datetime

class Cliente(Base):
    __tablename__ = "Cliente"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    nombre:Mapped[str] = mapped_column(String(40))
    mail:Mapped[str] = mapped_column(String(40))
    #Relacion con pedidos
    pedidos:Mapped[list["Pedido"]]=relationship(back_populates="cliente" ,cascade="all, delete-orphan")

   

class Pedido(Base):
    __tablename__ = "Pedido"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    fecha:Mapped[datetime] = mapped_column(DateTime,default=datetime.now())
    
    #Relaciones con cliente
    cliente_id:Mapped[int] = mapped_column(ForeignKey("Cliente.id",ondelete="CASCADE"))
    cliente:Mapped["Cliente"] = relationship(back_populates="pedidos")
    
    #Relaciones con Detalles
    detalles_de_pedidos:Mapped[list["DetallePedido"]]=relationship(back_populates="pedido",cascade="all, delete-orphan")

    total:Mapped[float]=mapped_column(Float,default=0.0)

    def set_total(self):
        self.total = sum(detalle.subtotal for detalle in self.detalles_de_pedidos)

    def get_total(self):
        return self.total

class DetallePedido(Base):
    __tablename__ = "DetallePedido"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    #Relaciones con Pedido
    pedido_id:Mapped[int] = mapped_column(Integer,ForeignKey("Pedido.id",ondelete="CASCADE"))
    pedido:Mapped["Pedido"] = relationship(back_populates="detalles_de_pedidos")
    
    #Relaciones con Producto
    producto_id:Mapped[int] = mapped_column(Integer,ForeignKey("Producto.id"))
    producto:Mapped["Producto"] = relationship(back_populates="detalles_de_productos")
    
    cantidad:Mapped[int] = mapped_column(Integer,default=1)
    subtotal:Mapped[float]=mapped_column(Float,default=0.0)
    
    def set_subtotal(self):
        self.subtotal = self.cantidad * self.producto.precio
    
    def get_subtotal(self):
        return self.set_subtotal

class Producto(Base):
    __tablename__ = "Producto"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    nombre:Mapped[str] = mapped_column(String(40))

    precio:Mapped[float]=mapped_column(Float)
    
    detalles_de_productos:Mapped[list["DetallePedido"]]=relationship(back_populates="producto")
    
    categoria_id:Mapped[int]=mapped_column(Integer,ForeignKey("Categoria.id"))
    categoria:Mapped["Categoria"]=relationship(back_populates="productos")
    
    def get_precio(self):
        return self.precio
    

class Categoria(Base):
    __tablename__ = "Categoria"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    nombre:Mapped[str] = mapped_column(String(40))
    
    productos:Mapped[list["Producto"]]=relationship(back_populates="categoria")