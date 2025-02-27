from typing import List,Union
from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal


class DepartamentosBase(BaseModel):
    ID: int
    Nombre : str
    AreaMedica_ID: int
    DepartamentoSuperior_ID: int
    Responsable_ID: int
    Especialidad: str
    Fecha_Registro: datetime
    Fecha_Actualiacion: datetime


    
    
class PersonalMedicoCreate(DepartamentosBase):
    pass
class PersonalMedicoUpdate(DepartamentosBase):
    pass
class PersonalMedico(DepartamentosBase):
    AreaMedica_ID: int
    DepartamentoSuperior_ID: int
    class Config:
        orm_mode = True