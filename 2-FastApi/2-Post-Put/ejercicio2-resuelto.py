from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Definimos el modelo Autor para la respuesta simplificada
class AutorResponse(BaseModel):
    nombre: str
    nacionalidad: str
    libros: List["LibroResponse"] = []  # Usamos una lista de libros simplificados

    class Config:
        json_encoders = {
            'LibroResponse': lambda v: {'id': v.id, 'titulo': v.titulo}  # Simplificamos la respuesta del libro
        }

# Definimos el modelo Libro para la respuesta simplificada
class LibroResponse(BaseModel):
    id: int
    titulo: str

    class Config:
        json_encoders = {
            'Autor': lambda v: {'id': v.id, 'nombre': v.nombre}  # Simplificamos la respuesta del autor
        }

# Definimos los modelos originales
class Autor(BaseModel):
    nombre: str
    nacionalidad: str
    libros: List["Libro"] = []

    class Config:
        json_encoders = {
            'Libro': lambda v: {'id': v.id, 'titulo': v.titulo}  # Evitamos que los libros se conviertan recursivamente
        }

class Libro(BaseModel):
    id: int
    titulo: str
    autor: Optional["Autor"] = None

    class Config:
        json_encoders = {
            'Autor': lambda v: {'id': v.id, 'nombre': v.nombre}  # Evitamos la recursión infinita al mostrar el autor
        }

# Creamos la aplicación FastAPI
app = FastAPI()

# Ejemplo de autores y libros en memoria
au1 = Autor(nombre="Francisco", nacionalidad="Argentino")
lib1 = Libro(id=2, titulo="Pallaringas")

# Relacionamos el autor con el libro y viceversa
au1.libros.append(lib1)
lib1.autor = au1

# Listas de autores y libros para simular una base de datos en memoria
lista_autores = [au1]
lista_libros = [lib1]

# Ruta principal (root)
@app.get("/")
async def root():
    return {"msg": "Root"}

# Ruta para obtener todos los autores
@app.get("/Autores", response_model=List[AutorResponse])
async def get_autores():
    return lista_autores  # Devolvemos la lista de autores

# Ruta para obtener todos los libros
@app.get("/Libros", response_model=List[LibroResponse])
async def get_libros():
    return lista_libros  # Devolvemos la lista de libros


@app.post("/Autores")
async def post_autor(autor: Autor):
    lista_autores.append(autor)
    return autor


@app.post("/Libros")
async def post_autor(libro: Libro):
    lista_libros.append(libro)
    return libro