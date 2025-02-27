import models.servicios_medicos
import schemas.servicios_medicos
from sqlalchemy.orm import Session

def get_serviceM(db:Session, ID:int):
    return db.query(models.servicios_medicos.ServiceM).filter(models.servicios_medicos.ServiceM.ID == ID).first()

def get_serviceM_by_Nombre(db: Session, Nombre: str):
    return db.query(models.servicios_medicos.ServiceM).filter(models.servicios_medicos.ServiceM == Nombre).first()

def get_servicesM(db: Session, skip:int=0,limit:int=10):
    return db.query(models.servicios_medicos.ServiceM).offset(skip).limit(limit).all()

def create_serviceM(db: Session, service:schemas.servicios_medicos.ServiceMCreate):
    db_serviceM = models.servicios_medicos.ServiceM(Nombre=service.Nombre, Descripcion=service.Descripcion, Observaciones=service.Observaciones, Fecha_Registro=service.Fecha_Registro,Fecha_Actualizacion=service.Fecha_Actualizacion )
    db.add(db_serviceM)
    db.commit()
    db.refresh(db_serviceM)
    return db_serviceM

def update_serviceM(db: Session, ID: int, service: schemas.servicios_medicos.ServiCeMUpdate):
    db_serviceM = db.query(models.servicios_medicos.ServiceM).filter(models.servicios_medicos.ServiceM.ID == ID).first()
    if db_serviceM:
        for var, value in vars(service).items():
            setattr(db_serviceM, var, value) if value else None
        db.commit()
        db.refresh(db_serviceM)
    return db_serviceM

def delete_serviceM(db: Session, ID: int):
    db_serviceM = db.query(models.servicios_medicos.ServiceM).filter(models.servicios_medicos.ServiceM.ID == ID).first()
    if  db_serviceM:
        db.delete(db_serviceM)
        db.commit()
    return db_serviceM