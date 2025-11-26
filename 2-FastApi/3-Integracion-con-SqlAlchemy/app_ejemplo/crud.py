import schemas,models
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_user(db:Session,id: int):
    
    return db.query(models.User).filter(models.User.id==id).first()


def get_users(db: Session,limit:int):
    return db.query(models.User).limit(limit).all()


def create_user(db: Session,u:schemas.UserCreate):
    
    db_user = models.User(nombre=u.nombre)
    db.add(db_user)
    db.commit(db_user)
    return db_user

