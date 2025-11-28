# Ejercicio Integrador I FastAPI

El siguiente ejercicio tiene como objetivo reforzar lo aprendido en las secciones anteriores de fastpi y sqlalchemy

## 1) Crear un proyecto FastAPI con SQLAlchemy siguiendo la siguiente estructura

Debe respetarse:

```plaintext
app/
 ├── main.py
 ├── models.py
 ├── schemas.py
 ├── crud.py
 ├── database.py
 
```

## 2) Crear el siguiente modelo Relacional

Usar este diagrama:

```mermaid
erDiagram
    CATEGORIA {
        int id PK
        string nombre
    }

    PRODUCTO {
        int id PK
        string nombre
        float precio
        int categoria_id FK
    }

    CLIENTE {
        int id PK
        string nombre
        string email
    }

    PEDIDO {
        int id PK
        date fecha
        int cliente_id FK
        float total
    }

    DETALLE_PEDIDO {
        int id PK
        int pedido_id FK
        int producto_id FK
        int cantidad
        float subtotal
    }

    CATEGORIA ||--o{ PRODUCTO : tiene
CLIENTE ||--o{ PEDIDO : realiza
PEDIDO ||--o{ DETALLE_PEDIDO : contiene
PRODUCTO ||--o{ DETALLE_PEDIDO : aparece_en
```

+ Crea los modelos teniendo en cuenta que si un cliente se elimina todos sus pedidos y detalles pedido se eliminaran tambien , no deben eliminarse los productos.

#### Cliente
```py
pedidos: Mapped[list["Pedido"]] = Relationship(
    back_populates="cliente",
    cascade="all, delete-orphan"
)
```
#### Pedido
```py
cliente_id: Mapped[int] = mapped_column(
    ForeignKey("cliente.id", ondelete="CASCADE")
)

```
+ Eventualmente debes hacer lo mismo para detalles


## 3) Creacion de Schemas

ModelBase → ModelCreate → Model (con orm_mode=True)

## 4) Crear archivo CRUD

CRUD completo para:

+ ####  Categoría
    + READ , CREATE
+ #### Producto
    + READ , CREATE
+ #### Cliente
    + READ , DELETE , CREATE
+ #### Pedido
    + READ , CREATE
+ #### DetallePedido
    + READ , CREATE
## 5) Crear endpoints en main.py 

### CATEGORIAS

+ POST /categorias

+ GET /categorias

### PRODUCTOS

+ POST /productos

+ GET /productos

+ GET /productos/{id}

### CLIENTES

+ POST /clientes

+ GET /clientes

+ GET /clientes/{id}

+ DELET /clientes/{id}

### PEDIDOS

+ POST /pedidos (solo fecha + cliente)

+ POST /pedidos/{id_pedido}/detalles (agrega detalles)

+ GET /pedidos/{id} (incluye detalles)