from sqlalchemy.orm import Session
import models.espacios
import schemas.espacios  # Asegúrate de que este archivo exista y esté en el lugar correcto

def get_espacio(db: Session, id: int):
    return db.query(models.espacios.Espacio).filter(models.espacios.Espacio.ID == id).first()

def get_espacios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.espacios.Espacio).offset(skip).limit(limit).all()

def create_espacio(db: Session, espacio: schemas.espacios):
    db_espacio = models.espacios.Espacio(
        Tipo=espacio.Tipo,
        Nombre=espacio.Nombre,
        Departamento_ID=espacio.Departamento_ID,
        Estatus=espacio.Estatus,
        Capacidad=espacio.Capacidad,
        Espacio_superior_ID=espacio.Espacio_superior_ID,
        tbc_espacioscol=espacio.tbc_espacioscol
    )
    db.add(db_espacio)
    try:
        db.commit()
        db.refresh(db_espacio)
    except Exception as e:
        db.rollback()
        raise e
    return db_espacio

def update_espacio(db: Session, id: int, espacio: schemas.espacios):
    db_espacio = db.query(models.espacios.Espacio).filter(models.espacios.Espacio.ID == id).first()
    if db_espacio:
        for var, value in vars(espacio).items():
            if value is not None:
                setattr(db_espacio, var, value)
        try:
            db.commit()
            db.refresh(db_espacio)
        except Exception as e:
            db.rollback()
            raise e
    return db_espacio

def delete_espacio(db: Session, id: int):
    db_espacio = db.query(models.espacios.Espacio).filter(models.espacios.Espacio.ID == id).first()
    if db_espacio:
        try:
            db.delete(db_espacio)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
    return db_espacio
