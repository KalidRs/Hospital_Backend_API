from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class ServiceM(Base):
    __tablename__ = "tbc_servicios_medicos"
    
    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(255))
    Descripcion = Column(String(250))
    Observaciones = Column(String(250))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
