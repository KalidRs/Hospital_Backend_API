from config.db import Base  # 🔹 Importar Base para definir la clase correctamente
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from models.servicios_medicos_espacios import ServiciosMedicosEspacios  

class ServiceM(Base):
    __tablename__ = "tbc_servicios_medicos"

    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(255))
    Descripcion = Column(String(250))
    Observaciones = Column(String(250))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

    espacios = relationship("ServiciosMedicosEspacios", back_populates="servicio")
