from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
import models.departamentos
from portadortoken import Portador
import models.departamentos, config.db, schemas.departamentos
from typing import List

departamentos = APIRouter()

models.departamentos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()