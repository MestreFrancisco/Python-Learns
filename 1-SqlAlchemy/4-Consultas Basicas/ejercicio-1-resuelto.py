from sqlalchemy import create_engine , select , func
from sqlalchemy.orm import Session 
from tabla import Cliente , Factura

engine = create_engine("sqlite:///facturacion.db")

with Session(engine) as session:
    
    #EJERCICIO 1
    smtm = select(func.count(Cliente.id))
    total_cliente = session.scalar(smtm)
    print("Total Clientes: ",total_cliente) 
    
    
    #EJERCICIO 2
    smtm = select(func.count(Factura.id))
    total_facturas = session.scalar(smtm)
    print("Total Facturas: ",total_facturas)
    
    #EJERCICIO3
    smtm = select(func.max(Factura.total).label("total_max"),Factura.id)
    rta = session.execute(smtm).all()
    for i in rta:
        print(f"Factura Id: {i.id} - Total: {i.total_max}") 
    
    #EJERCICIO4
    smtm = select(
        Cliente.nombre,
        func.count(Factura.cliente_id).label("total_factura")
        ).join(Factura).group_by(Cliente.nombre)
    
    rta = session.execute(smtm).all()
    for r in rta:
        print(f"- Cliente: {r.nombre},Cantidad Facturas →: {r.total_factura}")
        print(f"-------------------------------------------------------------")
        
    #EJERCICIO 5
    smtm = select(Cliente.nombre,Factura.total).where(Factura.total >= 100_000).join(Factura).group_by(Cliente.nombre)
    rta = session.execute(smtm).all()
    for r in rta:
        print(f"- Cliente: {r.nombre}, Total Factura →: {r.total}")

    print("\nEjercicio 6\n")
    #EJERCICIO 6
    smtm = select(Cliente.nombre,Factura.total).where(Factura.total <= 20_000).join(Factura).group_by(Cliente.nombre)
    rta = session.execute(smtm).all()
    for r in rta:
        print(f"- Cliente: {r.nombre}, Total Factura →: {r.total}")