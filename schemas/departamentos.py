from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class DepartamentoBase(BaseModel):
    Nombre: str
    AreaMedica_ID: Optional[int] = None
    DepartamentoSuperior_ID: Optional[int] = None
    Responsable_ID: Optional[int] = None
    Estatus: Optional[bool] = True
    Fecha_Registro: Optional[datetime] = None
    Fecha_Actualizacion: Optional[datetime] = None

class DepartamentoCreate(DepartamentoBase):
    pass  # Se usa la misma estructura de DepartamentoBase

class DepartamentoUpdate(BaseModel):
    Nombre: Optional[str] = None
    AreaMedica_ID: Optional[int] = None
    DepartamentoSuperior_ID: Optional[int] = None
    Responsable_ID: Optional[int] = None
    Estatus: Optional[bool] = None
    Fecha_Actualizacion: Optional[datetime] = None

class Departamento(DepartamentoBase):
    ID: int

    class Config:
        orm_mode = True
