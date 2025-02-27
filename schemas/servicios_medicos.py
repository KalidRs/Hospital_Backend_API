from typing import List,Union
from pydantic import BaseModel
from datetime import datetime

class ServiceMBase(BaseModel):
    Nombre: str
    Descripcion: str
    Observaciones: str
    Fecha_Registro:datetime
    Fecha_Actualizacion:datetime

    
class ServiceMCreate(ServiceMBase):
    pass
class ServiCeMUpdate(ServiceMBase):
    pass
class Service(ServiceMBase):
    ID: int

    class Config:
        from_attributes = True