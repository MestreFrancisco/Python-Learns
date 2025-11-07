## Ejercicio A:
1) Crea una base de datos llamada tienda.db , con su tabla producto.
2) Crea una Session.
3) Crea 4 productos con parametros propios.
4) Crea almenos 1 producto con stock por default.
5) Crea almenos 1 producto con fecha_creacion por default.
6) Crea tambien un usuario , from usuarios import Usuarios.
7) Subelo a la base de Datos.
8) haz un select de la columna id,nombre,precio,stock e imprimelo


---
### Producto

| Columna        | Tipo de dato  | Descripción                         |
|----------------|----------------|-------------------------------------|
| id             | Integer (Primary Key) | Identificador único del producto |
| nombre         | String(100)    | No puede ser nulo                 |
| precio         | Float          | No puede ser nulo                 |
| stock          | Integer        | Valor default   |
| activo         | Boolean        | No puede ser nulo |
| fecha_creacion | DateTime       | no puede ser nulo debe tener valor default |



```python
# Imports utiles
from sqlalchemy import create_engine, String, Integer, Float, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column , Session
from datetime import datetime
from sqlalchemy import  create_engine , select 
from usuarios import Base , Usuarios
```


## Ejercicio B:

1) Crea la base de datos biblioteca.db y crea la tabla libros

---
### Producto

| Columna        | Tipo de dato  | Descripción                         |
|----------------|----------------|-------------------------------------|
| id             | Integer (Primary Key) | Identificador único del producto |
| nombre         | String(100)    | No puede ser nulo                 |
| precio         | Float          | No puede ser nulo                 |
| cantida_hojas          | Integer        | Valor default   |
| fecha_publicacion | DateTime       | no puede ser nulo debe tener valor default |

---

2) Crea objetos Libros y agregalos a esta lista 

```python

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
```

3) Sube esta lista a la base de datos
4) haz un select global y guarda los datos
5) imprime solo los libros que tengan mas de 1000 paginas y cuesten menos de 4000$
