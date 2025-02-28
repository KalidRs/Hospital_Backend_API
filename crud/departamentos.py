from sqlalchemy.orm import Session
import models.departamentos as models
import schemas.departamentos as schemas
from datetime import datetime

# 🔹 Obtener un departamento por ID
def get_departamento(db: Session, departamento_id: int):
    return db.query(models.Departamentos).filter(models.Departamentos.ID == departamento_id).first()

# 🔹 Obtener todos los departamentos con paginación
def get_departamentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Departamentos).offset(skip).limit(limit).all()

# 🔹 Crear un nuevo departamento
def create_departamento(db: Session, departamento: schemas.DepartamentoCreate):
    db_departamento = models.Departamentos(
        Nombre=departamento.Nombre,
        AreaMedica_ID=departamento.AreaMedica_ID,
        DepartamentoSuperior_ID=departamento.DepartamentoSuperior_ID,
        Responsable_ID=departamento.Responsable_ID,
        Estatus=departamento.Estatus,
        Fecha_Registro=datetime.utcnow()
    )
    db.add(db_departamento)
    try:
        db.commit()
        db.refresh(db_departamento)
    except Exception as e:
        db.rollback()
        raise e
    return db_departamento

# 🔹 Actualizar un departamento por ID
def update_departamento(db: Session, departamento_id: int, departamento_data: schemas.DepartamentoUpdate):
    db_departamento = db.query(models.Departamentos).filter(models.Departamentos.ID == departamento_id).first()
    if db_departamento:
        for var, value in departamento_data.dict(exclude_unset=True).items():
            if value is not None:
                setattr(db_departamento, var, value)
        db_departamento.Fecha_Actualizacion = datetime.utcnow()
        try:
            db.commit()
            db.refresh(db_departamento)
        except Exception as e:
            db.rollback()
            raise e
    return db_departamento

# 🔹 Eliminar un departamento por ID
def delete_departamento(db: Session, departamento_id: int):
    db_departamento = db.query(models.Departamentos).filter(models.Departamentos.ID == departamento_id).first()
    if db_departamento:
        try:
            db.delete(db_departamento)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
    return db_departamento
