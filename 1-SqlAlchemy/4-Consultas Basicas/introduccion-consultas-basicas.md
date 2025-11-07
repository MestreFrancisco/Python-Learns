## Consultas Basicas Sqlachemy 2.0

En este apartado se explican las consultas basicas de sql
[Regresar](../../README.MD)

## Indice


1. [Consultas Básicas SQLAlchemy 2.0](#consultas-basicas-sqlalchemy-20)
   - [WHERE](#where)
   - [ORDER BY](#order-by)
   - [LIMIT](#limit)
   - [COUNT](#count)
   - [Join One-To-Many](#join-one-to-many)
     - [Inner Join](#inner-join)
     - [Left Join](#left-join-one-to-many)
   - [UPDATE](#update)
   - [DELETE](#delete)
   - [Funciones de Agregación](#tabla-funciones-de-agregacion)
  
---

### WHERE

```python
stmt = select(Cliente).where(Cliente.edad > 30) #Filtra Clientes cuya edad sean mayores a 30
result = session.scalars(stmt).all()
```

### ORDER BY

```python
stmt = select(Cliente).order_by(Cliente.nombre.desc()) #Ordena de forma decendiente
result = session.scalars(stmt).all()
```

### LIMIT

```python
stmt = select(Cliente).limit(5) #el limite de registros es 5
result = session.scalars(stmt).all()
```

### COUNT

```python
from sqlalchemy import func

stmt = select(func.count(Cliente.id))
total = session.scalar(stmt)
```

### Join One-To-Many

Por defecto, join() en SQLAlchemy hace un INNER JOIN (el más común).
O sea __solo devuelve filas que tienen coincidencias en ambas tablas__.

En este caso:

+ Muestra clientes que tienen al menos una factura.

+ Si hay un cliente sin facturas, no aparece en el resultado.

```python
stmt = select(Cliente.nombre, Factura.total).join(Factura)
result = session.execute(stmt).all()
```

---

```sql
SELECT cliente.nombre, factura.total
FROM cliente
JOIN factura ON cliente.id = factura.cliente_id;
```
---
El resultado esperado seria este , ahora es importante seleccionar que columnas queremos traer en el select.

| nombre | total |
| ------ | ----- |
| Ana    | 100.0 |
| Ana    | 250.0 |
| Juan   | 300.0 |

### Left Join One-To-Many

#### Python left join
```python
stmt = select(Cliente.nombre, Factura.total).join(Factura, isouter=True)
```
---
#### SQL left join
```sql
SELECT cliente.nombre, factura.total
FROM cliente
LEFT JOIN factura ON cliente.id = factura.cliente_id;
```

---
| Concepto                | Descripción                         |
| ----------------------- | ----------------------------------- |
| `join(Factura)`         | INNER JOIN por defecto              |
| Requiere relación       | `cliente.id` ↔ `factura.cliente_id` |
| Resultado               | Solo clientes con facturas          |
| LEFT JOIN en SQLAlchemy | `join(Factura, isouter=True)`       |


### UPDATE

Actualiza Registros

```python
from sqlalchemy import update

stmt = update(Cliente).where(Cliente.id == 1).values(edad=35)
session.execute(stmt)
session.commit()
```

### DELETE

Elimina Registros

```python
from sqlalchemy import delete

stmt = delete(Cliente).where(Cliente.id == 3)
session.execute(stmt)
session.commit()
```

### Tabla Funciones De Agregacion

| Función           |  SQLAlchemy 2.0                                                                  | SQL Equivalente                                                                                                          | Ejemplo práctico               |
| -------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **COUNT**            | `select(func.count(Cliente.id))`                                                     | SELECT COUNT(id) FROM cliente;                                                                                              | Contar clientes totales        |
| **COUNT con JOIN**   | `select(func.count(Factura.id)).join(Factura)`                                       | SELECT COUNT(factura.id) FROM cliente JOIN factura ON cliente.id = factura.cliente_id;                                      | Contar facturas por cliente    |
| **SUM**              | `select(func.sum(Factura.total))`                                                    | SELECT SUM(total) FROM factura;                                                                                             | Total facturado                |
| **SUM con GROUP BY** | `select(Cliente.nombre, func.sum(Factura.total)).join(Factura).group_by(Cliente.id)` | SELECT cliente.nombre, SUM(factura.total) FROM cliente JOIN factura ON cliente.id = factura.cliente_id GROUP BY cliente.id; | Total facturado por cliente    |
| **AVG**              | `select(func.avg(Factura.total))`                                                    | SELECT AVG(total) FROM factura;                                                                                             | Promedio de facturas           |
| **AVG con GROUP BY** | `select(Cliente.nombre, func.avg(Factura.total)).join(Factura).group_by(Cliente.id)` | SELECT cliente.nombre, AVG(factura.total) FROM cliente JOIN factura ON cliente.id = factura.cliente_id GROUP BY cliente.id; | Promedio facturado por cliente |
| **MAX**              | select(func.max(Factura.total))                                                    | SELECT MAX(total) FROM factura;                                                                                             | Factura más alta               |
| **MAX con GROUP BY** | `select(Cliente.nombre, func.max(Factura.total)).join(Factura).group_by(Cliente.id)` | SELECT cliente.nombre, MAX(factura.total) FROM cliente JOIN factura ON cliente.id = factura.cliente_id GROUP BY cliente.id; | Máxima factura por cliente     |
| **MIN**              | `select(func.min(Factura.total))`                                                    | SELECT MIN(total) FROM factura;                                                                                             | Factura más baja               |
| **MIN con GROUP BY** | `select(Cliente.nombre, func.min(Factura.total)).join(Factura).group_by(Cliente.id)` | SELECT cliente.nombre, MIN(factura.total) FROM cliente JOIN factura ON cliente.id = factura.cliente_id GROUP BY cliente.id; | Mínima factura por cliente     |

[VOLVER ARRIBA ↑](#indice)
[Ejercicios](python-sql-Ejercicios-4.md)

Si hiciste todos los ejercicios estas listo para rendir el Integrador __intenta no usar chatGpt para la resolucion Directa__
[Integrador](../5-Ejercicio-Integrador/python-sql-Integrador-1.md)
