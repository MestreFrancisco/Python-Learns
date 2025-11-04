| Método                 | Qué hace / Para qué sirve                                   |
|------------------------|------------------------------------------------------------|
| `Session()`            | Crea una nueva sesión (trabajo con la DB)                 |
| `add(obj)`             | Agrega un objeto nuevo o lo re-asocia con la sesión       |
| `add_all([obj1, ...])` | Agrega varios objetos a la sesión a la vez                |
| `commit()`             | Guarda todos los cambios pendientes en la base de datos   |
| `rollback()`           | Revierte los cambios de la sesión si algo falla           |
| `delete(obj)`          | Marca un objeto para eliminación en la DB                |
| `execute(stmt)`        | Ejecuta un SQL o consulta ORM (select, insert, update...) |
| `scalars(stmt)`        | Ejecuta una consulta y devuelve solo la primera columna de cada fila |
| `flush()`              | Envía los cambios pendientes al DB sin hacer commit       |
| `get(Entity, pk)`      | Recupera un objeto por su clave primaria                  |
| `refresh(obj)`         | Recarga un objeto desde la base de datos                  |
| `expire(obj)`          | Marca el objeto como "caducado", para que se recargue al acceder |
| `close()`              | Cierra la sesión y libera la conexión a la DB             |
| `begin()`              | Inicia un bloque de transacción explícito                 |
| `no_autoflush`         | Context manager para desactivar autoflush temporalmente   |


# Ejemplo básico de Session en SQLAlchemy

```python
from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# 1. Crear Base y Engine
class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///usuarios.db")

# 2. Definir tabla de usuarios
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

Base.metadata.create_all(engine)

# 3. Abrir sesión, agregar usuario y hacer commit
with Session(engine) as session:
    # Crear un nuevo usuario
    nuevo_usuario = User(name="Ana")
    
    # Agregar el usuario a la sesión
    session.add(nuevo_usuario)
    
    # Guardar los cambios en la base de datos
    session.commit()
