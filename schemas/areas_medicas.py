from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class EstatusEnum(str, Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"

class AreaMedicaBase(BaseModel):
    Nombre: str
    Descripcion: Optional[str] = None
    Estatus: EstatusEnum = EstatusEnum.Activo
    Fecha_Registro: Optional[datetime] = None
    Fecha_Actualizacion: Optional[datetime] = None

class AreaMedicaCreate(AreaMedicaBase):
    pass

class AreaMedicaUpdate(AreaMedicaBase):
    pass

class AreaMedica(AreaMedicaBase):
    ID: str  

    class Config:
        from_attributes = True
