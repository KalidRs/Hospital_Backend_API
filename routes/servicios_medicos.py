from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.servicios_medicos, config.db, schemas.servicios_medicos, models.servicios_medicos
from typing import List

serviceM = APIRouter()

models.servicios_medicos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@serviceM.get("/servicios_medicos/", response_model=List[schemas.servicios_medicos.Service], tags=["Servicios Medicos"])
def read_servicesM(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    db_serviceM = crud.servicios_medicos.get_servicesM(db=db, skip=skip, limit=limit)
    return db_serviceM

@serviceM.get("/servicios_medicos/{ID}", response_model=schemas.servicios_medicos.Service, tags=["Servicios Medicos"])
def read_serviceM(ID: int, db: Session = Depends(get_db)):
    db_serviceM = crud.servicios_medicos.get_serviceM(db=db, ID=ID)
    if db_serviceM is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_serviceM

@serviceM.post("/servicios_medicos/", response_model=schemas.servicios_medicos.Service, tags=["Servicios Medicos"])
def create_serviceM(service: schemas.servicios_medicos.ServiceMCreate, db: Session = Depends(get_db)):
    db_serviceM = crud.servicios_medicos.get_serviceM_by_Nombre(db, Nombre=service.Nombre)
    if db_serviceM:
        raise HTTPException(status_code=400, detail="Servicio existente, intenta nuevamente")
    return crud.servicios_medicos.create_serviceM(db=db, service=service)

@serviceM.put("/servicios_medicos/{ID}", response_model=schemas.servicios_medicos.Service, tags=["Servicios Medicos"])
def update_serviceM(ID: int, service: schemas.servicios_medicos.ServiCeMUpdate, db: Session = Depends(get_db)):
    db_serviceM = crud.servicios_medicos.update_serviceM(db=db, ID=ID, service=service)
    if db_serviceM is None:
        raise HTTPException(status_code=404, detail="Servicio no existente, no se pudo actualizar")
    return db_serviceM

@serviceM.delete("/servicios_medicos/{ID}", response_model=schemas.servicios_medicos.Service, tags=["Servicios Medicos"])
def delete_serviceM(ID: int, db: Session = Depends(get_db)):
    db_serviceM = crud.servicios_medicos.delete_serviceM(db=db, ID=ID)
    if db_serviceM is None:
        raise HTTPException(status_code=404, detail="Servicio no existente, no se pudo eliminar")
    return db_serviceM

# Continuar con el ID 4 de servcios medicos