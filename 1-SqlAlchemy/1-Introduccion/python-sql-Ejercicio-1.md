## Ejercicio A:
Crea una base de datos llamada tienda.db , con su tabla producto y su tabla facturas

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

### Facturas

| Columna         | Tipo de dato        | Descripción                                |
|-----------------|---------------------|--------------------------------------------|
| id              | Integer (Primary Key) | Identificador único de la factura          |
| fecha_factura   | DateTime            | Fecha y hora de la factura, no puede ser nulo |
| total           | Float               | Total de la factura, no puede ser nulo     |
| metodo_pago     | String(50)          | Método de pago (Ej. "tarjeta", "efectivo"), no puede ser nulo |
| activo          | Boolean             | --- |


## Ejercicio B:
Crea una base de datos llamada **escuela.db**, con su tabla **alumnos**, su tabla **cursos** y su tabla **profesores**.

---

### Alumnos

| Columna        | Tipo de dato         | Descripción                                   |
|----------------|----------------------|-----------------------------------------------|
| id             | Integer (Primary Key) | Identificador único del alumno                |
| nombre         | String(100)          | No puede ser nulo                             |
| apellido       | String(100)          | No puede ser nulo                             |
| edad           | Integer              | No puede ser nulo                             |
| promedio       | Float                | Valor default (por ejemplo, 0.0)              |
| activo         | Boolean              |  no puede ser nulo |
| fecha_ingreso  | DateTime             | No puede ser nulo, debe tener valor default   |

---

### Cursos

| Columna        | Tipo de dato         | Descripción                                   |
|----------------|----------------------|-----------------------------------------------|
| id             | Integer (Primary Key) | Identificador único del curso                 |
| nombre         | String(100)          | No puede ser nulo                             |
| descripcion    | String(200)          | Puede ser nulo                                |
| duracion_horas | Integer              | No puede ser nulo                             |
| costo          | Float                | No puede ser nulo                             |
| activo         | Boolean              | no puede ser nulo |

---

### Profesores

| Columna        | Tipo de dato         | Descripción                                   |
|----------------|----------------------|-----------------------------------------------|
| id             | Integer (Primary Key) | Identificador único del profesor              |
| nombre         | String(100)          | No puede ser nulo                             |
| apellido       | String(100)          | No puede ser nulo                             |
| materia        | String(100)          | No puede ser nulo                             |
| salario        | Float                | No puede ser nulo                             |
| fecha_contratacion | DateTime         | No puede ser nulo, debe tener valor default   |
| activo         | Boolean              | no puede ser nulo |

---

```python
# Usa los siguientes import o crea los tuyos propios.
from sqlalchemy import create_engine, String, Integer, Float, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from sqlalchemy import create_engine

#Ejemplo
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
Base.metadata.create_all(engine)```
```
---
Algunos Posibles errores de compilacion pueden ser:
 - No pusiste ```__tablename__```
 - No pusiste un primary_key
 - Confundiste el tipo de dato
 - No pasaste como parametro el engine.