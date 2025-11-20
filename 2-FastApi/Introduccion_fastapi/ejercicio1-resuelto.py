from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Producto(BaseModel):
    id:int    
    nombre:str
    costo:float
    
 
productos_list = [
    Producto(id=1,nombre="Coca-cola",costo=2250.50),
    Producto(id=2,nombre="Pepsi-cola",costo=1200.50),
    Producto(id=3,nombre="Sprite",costo=950.50),
    Producto(id=4,nombre="Fanta",costo=980.50),
    Producto(id=5,nombre="Coto-cola",costo=400.50),
    Producto(id=6,nombre="Leche",costo=1700.20),
    Producto(id=7,nombre="Fernet",costo=6000.50),
    ]   
    
    
@app.get("/")
async def root():
    return {"msg":"Hola Mundo"}

@app.get("/productos")
async def get_productos():
    return productos_list

@app.get("/productos/mascaro")
async def get_productos_rango_id():
    return mas_caro()

@app.get("/productos/ordenar")
async def get_productos_rango_id(orden: str):
    return ordenar(orden)

@app.get("/productos/rango_id")
async def get_productos_rango_id(min:int,max: int):
    return min_max_id(min,max)

@app.get("/productos/caros")
async def get_productos_caros(min: float):
    return precio_min(min)

@app.get("/productos/buscar")
async def get_productos_buscar(nombre: str):
    return buscar_por_nombre(nombre)


@app.get("/productos/{id}")
async def get_productos(id: int):
    return buscar_id(id)


##Ejerciocio B)
def buscar_id(id: int):
    result = next((u for u in productos_list if u.id == id),None)
    if result is None:
        return {"error":"Producto no encontrado"}
    else:
        return result

#EJERCICIO C)
def buscar_por_nombre(nombre: str):
    productos_filtrados = filter(lambda u: u.nombre.lower().startswith(nombre.lower()), productos_list)
    resultado = list(productos_filtrados)
    return resultado

#EJERCICIO D)
def precio_min(min: float):
    productos_filtrados = filter(lambda u: u.costo >= min, productos_list)
    resultado = list(productos_filtrados)
    return resultado

#EJERCICIO E)
def min_max_id(min:int=1,max:int=4):
    productos_filtrados = filter(lambda u: u.id >= min and u.id <= max , productos_list)
    resultado = list(productos_filtrados)
    return resultado

#EJERCICIO F)
def ordenar(orden:str="asc"):
    if orden == "desc":
        ordenar = sorted(productos_list,key=lambda p: p.nombre,reverse=True)
        result = list(ordenar)
        return result
    else: 
        ordenar = sorted(productos_list,key=lambda p: p.nombre,reverse=False)
        result = list(ordenar)
        return result

#EJERCICIO G)
def mas_caro():
    maxProducto = max(productos_list,key=lambda p: p.costo)
    return maxProducto