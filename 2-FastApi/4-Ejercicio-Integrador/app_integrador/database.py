from sqlalchemy.orm import DeclarativeBase , sessionmaker
from sqlalchemy import create_engine 
from pathlib import Path
from sqlalchemy import create_engine

# Ruta absoluta hacia la carpeta del script
db_path = Path(__file__).parent / "integrador.db"

# Crear engine con SQLite apuntando a esa ruta

#clase Base → DeclarativeBase
class Base(DeclarativeBase):
    pass

engine = create_engine(f"sqlite:///{db_path}",connect_args={"check_same_thread":False},echo=True)

# Crear una session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

from sqlalchemy import event

@event.listens_for(engine, "connect")
def enable_sqlite_fk(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()