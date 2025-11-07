1) Usa la base de datos facturacion.db para abrir y hacer Consultas

```python

from sqlalchemy import create_engine , select , func
from sqlalchemy.orm import Session 
from tabla import Cliente , Factura

engine = create_engine("sqlite:///facturacion.db")
```

# Ejercicio A

1) Usa la funcion `Count()` para contar la cantidad de clientes  
2) Usa la funcion `Count()` para contar la cantidad de facturas 
3) Usa la funcion `Max()`   para traer la factura con el total mas alto

4) Haz un `Join()` entre ambas tablas y usa `Count()` Para mostrar cuantas facturas tiene cada __cliente__

5) Haz `Join()` entre ambas tablas y muestra aquellos clientes cuyo total de factura sea mayor a 100.000$

6) haz `Join()` entre ambas tablas y muestra aquellos clientes cuyo total de factura sea menor a 20.000$

