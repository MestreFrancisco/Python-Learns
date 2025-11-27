import schemas, models
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_user(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def get_users(db: Session, limit: int = 50):
    return db.query(models.User).limit(limit).all()


def create_user(db: Session, u: schemas.UserCreate):
    db_user = models.User(nombre=u.nombre)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_item(db: Session, id: int):
    return db.query(models.Item).filter(models.Item.id == id).first()


def get_items(db: Session, limit: int = 50):
    return db.query(models.Item).limit(limit).all()


def create_user_item(db: Session, I: schemas.ItemCreate, id_user: int):
    db_item = models.Item(
        titulo=I.titulo,
        descripcion=I.descripcion,
        user_id=id_user
    )

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, id: int, I: schemas.ItemCreate):
    item_filter = db.query(models.Item).filter(models.Item.id == id).first()

    if item_filter is None:
        raise HTTPException(status_code=404, detail="No existe el item")

    update_data = I.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(item_filter, key, value)

    db.commit()
    db.refresh(item_filter)
    return item_filter


def delete_item(db: Session, id: int):
    item_db = db.query(models.Item).filter(models.Item.id == id).first()

    if item_db is None:
        raise HTTPException(status_code=404, detail="No existe el item")

    db.delete(item_db)
    db.commit()
    return {"msg": "Item eliminado", "id": item_db.id}
