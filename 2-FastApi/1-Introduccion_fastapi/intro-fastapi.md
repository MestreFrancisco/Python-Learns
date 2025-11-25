# Intro Fast Api

FastAPI es un framework web moderno, rápido (de alto rendimiento), para construir APIs con Python basado en las anotaciones de tipos estándar de Python.

## Índice


1. [Introducción a FastAPI](#intro-fast-api)
2. [Empezando](#empezando)
3. [Configuración Inicial](#importamos-fastapi-desde-fastapi)
4. [GET Simple](#get-simple)
5. [GET Parámetros](#get-parametros)
   - [Path](#path)
   - [Query](#query)



## Empezando

Una vez instalado fastapi y uvicorn

```bash

pip install fastapi
pip install uvicorn["standard"]

```

---
Importamos FastApi desde fastapi
---

```python

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

```

## GET SIMPLE

FastApi retorna json en la web para ejecutar el servidor usamos:
`uvicorn main:app --reload` donde main es el nombre del archivo


```py
@app.get("/")
async def root():
    return {"message":"Hola Wacho"}
```

## GET PARAMETROS 


### PATH
Puedes declarar el tipo de un parámetro de path en la función, usando anotaciones de tipos estándar de Python:


```py
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

En este caso, item_id se declara como un int.

### QUERY
---
Tambien tenemos la opcion de meter queries en el buscador buscariamos algo asi:



```py
@app.get("/users")
async def get_users(id: int | None = None):
    if id is None:
        return u_list
    return search_by_user(id)


def search_by_user(id:int):
    result = next((u for u in u_list if u.id == id), None)
    return result if result else {"error": "Usuario no encontrado"}

#Usamos Next ya que este solo trae el primer valor coincidente que encuentra y como el id es unico es mejor para esta ocasion.

```

## Siguiente

1) [Ejercicios-1.md](#fast-ejercicio1.md)
2) [POST,UPDATE](intro-fastapi.md)

---

3. [Explicaciones Extras para filtrar](#explicaciones-extras-para-filtrar)
   + 3.1 [next()](#1-next)
   + 3.2 [Expresión Generadora](#2-expresión-generadora)
   + 3.3 [next() y la expresión generadora juntas](#3-next-y-la-expresión-generadora-juntas)
4. [Cómo funciona filter()?](#cómo-funciona-filter)
   + 4.1 [Filtrando usuarios cuyo nombre empieza con "fr"]( #filtrando-usuarios-cuyo-nombre-empieza-con-fr)
   + 4.2 [Explicación del código filter()](#explicación-filter-codigo)
5. [Uso de filter() vs. Bucle](#por-qué-usar-filter-en-lugar-de-un-bucle)
6. [Alternativa con List Comprehension](#alternativa-con-list-comprehension)

--- 
### Explicaciones Extras para filtrar

#### 1. `next()`

La función `next()` es una función integrada de Python que obtiene el siguiente valor de un iterador. Si el iterador se agota y no se encuentra más valores, se puede pasar un valor predeterminado que se retornará en lugar de lanzar una excepción StopIteration.

#### 2. Expresión Generadora 
```py
(u for u in u_list if u.id == id)
```

Esta parte es una expresión generadora. Funciona como un generador que crea valores de uno en uno, similar a una lista, pero de manera más eficiente en términos de memoria porque no se almacenan todos los elementos de una vez.

#### Desglosada:

`for u in u_list`: Este es un bucle que itera sobre cada usuario u dentro de la lista u_list.

`if u.id == id`: Este es un filtro que solo selecciona aquellos elementos de u_list cuyo campo id coincide con el valor id que se pasa a la función.


Entonces, la expresión generadora:

```py
(u for u in u_list if u.id == id)
```

crea un generador que recorre la lista de usuarios y filtra aquellos cuya propiedad id coincida con el valor de id que se pasa.

#### 3. next() y la expresión generadora juntas

La función `next()` toma un iterador (en este caso, el generador) y devuelve el primer valor que encuentre. Si no encuentra nada (es decir, si la expresión generadora no produce ningún valor), la función `next()` devuelve un valor por defecto, que en este caso es None.

Por lo tanto, el código completo:

```py
result = next((u for u in u_list if u.id == id), None)
```

hace lo siguiente:

+ Busca el primer usuario en u_list cuyo id coincida con el valor de id.

+ Si lo encuentra, lo asigna a result.

+ Si no encuentra ningún usuario con ese id, asigna None a result.

### Cómo funciona filter()?

La función `filter()` en Python recibe dos argumentos:

Una función que evalúa si un elemento cumple o no con la condición (por ejemplo, si el nombre empieza con "fr").

Un iterable sobre el cual se aplicará la función.

`filter()` devuelve un iterador que contiene solo los elementos que cumplen con la condición de la función.

Ejemplo para buscar usuarios cuyos nombres comienzan con `"fr"`

Supongamos que tienes la siguiente lista u_list de usuarios:
```py
u_list = [
    User(id=1, name="Fran", surname="Mestre", age=22),
    User(id=2, name="Franco", surname="Mendez", age=26),
    User(id=3, name="Juliana", surname="Serrano", age=22),
    User(id=4, name="Fernando", surname="Gomez", age=30),
    User(id=5, name="Ana", surname="Lopez", age=25)
]
```

Y quieres encontrar todos los usuarios cuyo nombre comience con "fr". Podrías hacer lo siguiente:

### Filtrando usuarios cuyo nombre empieza con "fr"
```py
filtered_users = filter(lambda u: u.name.lower().startswith("fr"), u_list)
```
### Convertimos el filtro en una lista para ver los resultados
```py
filtered_users_list = list(filtered_users)
```
### Mostramos los resultados
```py
for user in filtered_users_list:
    print(user.name)
```
### Explicación Filter codigo:

```py
lambda u: u.name.lower().startswith("fr"):
```

Esta es una función anónima `(lambda)` que toma cada usuario (u) y verifica si el nombre del usuario (u.name) empieza con "fr" (sin importar si la letra está en mayúsculas o minúsculas, por eso usamos `lower()`).

`filter()` aplica esta función a todos los elementos de u_list. Solo devuelve aquellos usuarios para los cuales la condición es verdadera.

`list(filtered_users)` convierte el resultado de `filter()` (que es un iterador) en una lista para poder ver los resultados.

 Resultado:

El código anterior imprimirá:
```bash
Fran
Franco
Fernando
```
¿Por qué usar `filter()` en lugar de un **bucle**?

Más conciso y elegante: `filter()` te permite aplicar una condición de manera muy directa.

**Limpieza de código**: No necesitas escribir explícitamente un bucle for para filtrar los elementos, lo cual puede hacer tu código más legible y corto.

**Mejor rendimiento en iterables grandes**: Si estás trabajando con grandes cantidades de datos, el uso de un iterador en lugar de generar toda la lista al mismo tiempo puede ser más eficiente.

Alternativa con list comprehension (también muy común)


### Usando list comprehension
```py
filtered_users_list = [user for user in u_list if user.name.lower().startswith("fr")]
```

### Mostramos los resultados
```py
for user in filtered_users_list:
    print(user.name)
```
Resultado: igual que con filter()

Ambos enfoques logran lo mismo, y la elección depende de tus preferencias y el estilo de tu código.

Resumen:

+ filter() es ideal cuando necesitas filtrar elementos de una lista (o cualquier iterable) de acuerdo a una condición.

+ Si tu condición involucra strings, como en este caso, puedes usar métodos como startswith() junto con filter().

+ List comprehension también es una excelente opción si prefieres una sintaxis más familiar y concisa.

