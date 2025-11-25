# Ejercicios I

## Ejercicio (A)

1) Dada la clase la producto

```py

class Producto():
    id:int
    nombre:str
    costo:float
```

crea 5 productos añadelos a una lista y muestralos mediante un get via FastApi, recuerda usar BaseModel y asignar `FastApi()` a una variable.

resultado esperado:

```json
[
    {
        "id": 1,
        "nombre": "Coca-cola",
        "costo": 250.5
    },
    {
        "id": 2,
        "nombre": "Pepsi-cola",
        "costo": 250.5
    },
    {
        "id": 3,
        "nombre": "Sprite",
        "costo": 250.5
    },
    {
        "id": 4,
        "nombre": "Fanta",
        "costo": 250.5
    },
    {
        "id": 5,
        "nombre": "coto-cola",
        "costo": 250.5
    }
]
```

## Ejercicio (B)


Crea un endpoint GET que devuelva un producto según su id, usando next() para buscar el primer producto que coincida.

Resultado esperado (si existe el producto con id 3):

```json
{
    "id": 3,
    "nombre": "Sprite",
    "costo": 250.5
}
```


Si NO existe, retorna:
```json
{
    "error": "Producto no encontrado"
}
```

### Ejercicio (C)

Crea un endpoint GET /productos/buscar que reciba un parámetro de query llamado nombre.

Debe devolver todos los productos cuyo nombre empiece con lo escrito, usando filter() o list comprehension.

Ejemplo de llamada:

GET /productos/buscar?nombre=co

```json
Resultado esperado:

[
    { "id": 1, "nombre": "Coca-cola", "costo": 250.5 },
    { "id": 5, "nombre": "coto-cola", "costo": 250.5 }
]
```

### Ejercicio (D)

Crea un endpoint GET /productos/caros que devuelva todos los productos cuyo costo sea mayor a un número enviado por query.

Ejemplo:

`GET /productos/caros?min=200`


Usa:

`filter()`

comparación numérica

### Ejercicio (E)

Crea un endpoint GET `/productos/rango` que devuelva los productos cuyo id esté entre un rango dado:

`GET /productos/rango?min=2&max=4`


Debe devolver solo productos con id 2, 3 y 4.


### Ejercicio (F)

Crea un endpoint GET /productos/mascaro
Debe retornar el producto más caro usando:

`max()`

`key=lambda p: p.costo`

Resultado esperado:
```json
{
    "id": 4,
    "nombre": "Fanta",
    "costo": 250.5
}
```