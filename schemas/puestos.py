# schemas/puestos.py

from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID

class PuestoBase(BaseModel):
    nombre: str = Field(..., example="Jefe de Enfermería")
    descripcion: Optional[str] = Field(None, example="Responsable del personal de enfermería")
    departamento_id: UUID = Field(..., example="0c1d2e3f-4a5b-6789-0abc-def123456789")
    estatus: Optional[bool] = Field(True, example=True)
    fecha_registro: Optional[datetime] = Field(None, example="2025-04-01T10:00:00.000Z")
    fecha_actualizacion: Optional[datetime] = Field(None, example="2025-04-01T11:00:00.000Z")

class PuestoCreate(PuestoBase):
    pass

class PuestoUpdate(BaseModel):
    nombre: Optional[str] = Field(None, example="Jefe de Quirófano")
    descripcion: Optional[str] = Field(None, example="Encargado del área quirúrgica")
    departamento_id: Optional[UUID] = Field(None, example="f3e1b2d7-4b9d-4a3e-9f61-48e8b7d4a5e3")
    estatus: Optional[bool] = Field(None, example=False)
    fecha_actualizacion: Optional[datetime] = Field(None, example="2025-04-01T11:00:00.000Z")

class Puesto(PuestoBase):
    id: UUID = Field(..., example="a1b2c3d4-e5f6-7890-1234-56789abcdef0")

    class Config:
        orm_mode = True
