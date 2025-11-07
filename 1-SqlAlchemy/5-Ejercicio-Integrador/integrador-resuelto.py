from sqlalchemy.orm import DeclarativeBase , Mapped , mapped_column ,relationship ,Session 
from sqlalchemy import select , String , DateTime, Integer , Float , ForeignKey ,create_engine , func 
from sqlalchemy.orm import Session 
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Cliente(Base):
    __tablename__="Cliente"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    nombre:Mapped[str]=mapped_column(String(50)) 
    email:Mapped[str]=mapped_column(String(50)) 
    telefono:Mapped[str]=mapped_column(String(50))
    facturas:Mapped[list["Factura"]]=relationship(back_populates="cliente")
    
class Factura(Base):
    __tablename__="Factura"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    cliente_id:Mapped[int] = mapped_column(ForeignKey("Cliente.id"))
    cliente:Mapped["Cliente"] = relationship(back_populates="facturas")
    
    monto_total:Mapped[float] = mapped_column(Float,default=0)
    fecha:Mapped[datetime] = mapped_column(DateTime,default=datetime.now)
    
    detalles_facturas:Mapped[list["DetalleFactura"]]=relationship(back_populates="")
    
    #METODOS
    def add_detalle_factura(self,DetalleFactura):
        self.detalles_facturas.append(DetalleFactura)
        self.monto_total=0.0
        for detalle in self.detalles_facturas:
            self.monto_total += detalle.monto
    
class DetalleFactura(Base):
    __tablename__="DetalleFactura"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    factura_id:Mapped[int] = mapped_column(ForeignKey("Factura.id"))
    producto_id:Mapped[int] = mapped_column(ForeignKey("Producto.id"))
    
    cantidad:Mapped[int] = mapped_column(Integer,default=0)
    monto:Mapped[float] = mapped_column(Float,default=0)
    producto:Mapped["Producto"] = relationship(back_populates="detalle_factura")
    factura:Mapped["Factura"]=relationship(back_populates="detalles_facturas")

    #Metodos
    def add_producto(self,Producto,cantidad):
        print(f"[DEBUG] {type(Producto),cantidad}")
        self.producto = Producto
        self.cantidad = cantidad
        print(f"[DEBUG] {self.cantidad}")
        print(f"[DEBUG] {self.producto.precio}")
        self.monto = self.producto.precio * self.cantidad

class Producto(Base):
    __tablename__="Producto"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    
    nombre:Mapped[str]=mapped_column(String(50))
    precio:Mapped[float]=mapped_column(Float)
    
    detalle_factura:Mapped["DetalleFactura"] = relationship(back_populates="producto")
    
    #Metodos
    def get_precio(self):
        return self.precio
   

## Instanciando Objetos

cl1 = Cliente(nombre="Francisco",email="mestre2@yahoo.com",telefono="2613075476")
cl2 = Cliente(nombre="Lorenzo",email="f224lopez2@gmail.com",telefono="3013075476")
cl3 = Cliente(nombre="Akira",email="akr2ira@yahoo.com",telefono="5613075476")

p1 = Producto(nombre="lata pepsi 250 ml",precio=950.50)
p2 = Producto(nombre="lata coca  333 ml",precio=1250.50)
p3 = Producto(nombre="lata sprite 250 ml",precio=960.50)
p4 = Producto(nombre="papas fritas 500gr",precio=3020.50)
p5 = Producto(nombre="Cebolla Picada",precio=500.24)
p6 = Producto(nombre="Bacon",precio=1500.50)
p7 = Producto(nombre="medallon de carne 200gr",precio=2000.10)
p8 = Producto(nombre="Feta Cheddar",precio=800.20)
p9 = Producto(nombre="Pan de Papa",precio=1600)
p9 = Producto(nombre="Pan de hamburgesa comun",precio=1000)

fc1 = Factura()
fc2 = Factura()
fc3 = Factura()
fc4 = Factura()
fc5 = Factura()

dfc1 = DetalleFactura()
dfc2 = DetalleFactura()
dfc3 = DetalleFactura()
dfc4 = DetalleFactura()
dfc5 = DetalleFactura()
dfc6 = DetalleFactura()
dfc7 = DetalleFactura()
dfc8 = DetalleFactura()
dfc9 = DetalleFactura()
dfc10 = DetalleFactura()
dfc11 = DetalleFactura()
dfc12 = DetalleFactura()

## Setenado Datos

dfc1.add_producto(p1,1) ,  fc1.add_detalle_factura(dfc1)
dfc2.add_producto(p2,5) ,  fc1.add_detalle_factura(dfc2)
dfc3.add_producto(p3,3) ,  fc2.add_detalle_factura(dfc3)
dfc4.add_producto(p4,10) ,  fc2.add_detalle_factura(dfc4)
dfc5.add_producto(p5,6) ,  fc3.add_detalle_factura(dfc5)
dfc6.add_producto(p6,5) ,  fc3.add_detalle_factura(dfc6)
dfc7.add_producto(p7,2) ,  fc4.add_detalle_factura(dfc7)
dfc8.add_producto(p8,3) ,  fc4.add_detalle_factura(dfc8)
dfc9.add_producto(p9,2) ,  fc5.add_detalle_factura(dfc9)
dfc10.add_producto(p7,2) ,  fc5.add_detalle_factura(dfc10)
dfc11.add_producto(p8,2) ,  fc5.add_detalle_factura(dfc11)
dfc12.add_producto(p9,4) ,  fc5.add_detalle_factura(dfc12)

cl1.facturas=[fc1,fc2]
cl2.facturas=[fc4,fc5]
cl3.facturas=[fc3]

engine = create_engine("sqlite:///tienda.db")
Base.metadata.create_all(engine)

with Session(engine) as session:
    
    session.add(cl1)
    session.add(cl2)
    session.add(cl3)

    session.commit()
    
    #1-Consultas
    
    smtm = select(Cliente.nombre,func.sum(Factura.monto_total).label("total_de_facturas")
                  ).join(Factura).group_by(Cliente.nombre)
    
    respuesta = session.execute(smtm).all()
    
    for r in respuesta:
        print(f"Cliente {r.nombre} Monto Total de sus Facturas {r.total_de_facturas}")
        
    #2-Consulta
    
    smtm_1 = select(Cliente)
    respuesta = session.scalars(smtm_1).all()
    
    for r in respuesta:
        print(f"-({r.nombre}):")
        for i in r.facturas:
            for j in i.detalles_facturas:
                print(f" |-Producto-[{j.producto.nombre}]")
                print(f"   |-Cantidad →{j.cantidad}")
                print(f"   |-Monto Total →{j.monto}")
           
                