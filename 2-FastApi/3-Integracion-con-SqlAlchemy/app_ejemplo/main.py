from fastapi import Depends , FastAPI , HTTPException
from sqlalchemy.orm import Session
import models , schemas , crud
from database import SessionLocal,engine

#Crear Tablas
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


#Funcion de dependencia para obteber sessiones de base de Datos

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/ping")
def ping():
    return {"ping": "pong"}
        
        
@app.get("/api")
def root():
    return {"msg":"Root"}


@app.post("/api/users",response_model=schemas.User)
def create_user(u:schemas.UserCreate,db:Session = Depends(get_db)):
    return crud.create_user(db=db,u=u)


@app.get("/api/users",response_model=list[schemas.User])
def get_users(db:Session=Depends(get_db)):
    return crud.get_users(db=db)

@app.get("/api/users/{id}",response_model=schemas.User)
def get_users_by_id(id:int,db:Session=Depends(get_db)):
    db_user_crud =  crud.get_user(db=db,id=id)
    if db_user_crud is None:
        raise HTTPException(status_code=404,detail="Usuario con id proporcionado no existe")
    return db_user_crud

@app.put("/api/items/{id}",response_model=schemas.Item)
def update_item_by_id(id:int,I:schemas.ItemCreate,db:Session=Depends(get_db)):
    item_db_crud = crud.update_item(db=db,id=id,I=I)
    if item_db_crud is None:
        raise HTTPException(status_code=404,detail="Item con el id proporcionado no existe")
    return item_db_crud

@app.get("/api/items",response_model=list[schemas.Item])
def get_items(db:Session=Depends(get_db)):
    return crud.get_items(db=db)

@app.get("/api/items/{id}",response_model=schemas.Item)
def get_items_by_id(id:int,db:Session=Depends(get_db)):
    item_db_crud = crud.get_item(db=db,id=id)
    if item_db_crud is None:
        raise HTTPException(status_code=404,detail="Item con id proporcionado no existe")
    return item_db_crud

@app.delete("/api/items/{id}",response_model=schemas.Item)
def delte_item_by_id(id:int,db:Session=Depends(get_db)):
    item_db_crud = crud.delete_item(db=db,id=id)
    if item_db_crud is None:
        raise HTTPException(status_code=404,detail="Item con id proporcionado no existe")
    return item_db_crud

@app.post("/api/users/{id}/items")
def post_user_item(id:int,I:schemas.ItemCreate,db:Session=Depends(get_db)):
    u = crud.get_user(db=db,id=id)
    if u is None:
        raise HTTPException(status_code=404,detail="User con id proporcionado no existe")
    return crud.create_user_item(I=I,db=db,id_user=id)