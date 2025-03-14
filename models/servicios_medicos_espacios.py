from sqlalchemy import Column, Integer, ForeignKey, String, Enum, DateTime
from sqlalchemy.orm import relationship
from config.db import Base
import enum
import datetime

# Enumeración para el estatus de aprobación
class EstatusAprobacionEnum(str, enum.Enum):
    Pendiente = 'Pendiente'
    Aprobado = 'Aprobado'
    Rechazado = 'Rechazado'

# Enumeración para el estatus general
class EstatusEnum(str, enum.Enum):
    Activo = 'Activo'
    Inactivo = 'Inactivo'

class ServiciosMedicosEspacios(Base):
    __tablename__ = 'tbc_servicios_medicos_espacios'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fk_servicio = Column(Integer, ForeignKey("tbc_servicios_medicos.ID", ondelete="CASCADE"), nullable=False, index=True)
    fk_espacio = Column(Integer, ForeignKey("tbc_espacios.id"), nullable=False, index=True)
    observaciones = Column(String(255), nullable=True)
    estatus_aprobacion = Column(Enum(EstatusAprobacionEnum), nullable=False, default=EstatusAprobacionEnum.Pendiente)
    estatus = Column(Enum(EstatusEnum), nullable=False, default=EstatusEnum.Activo)
    fecha_registro = Column(DateTime, default=datetime.datetime.utcnow)
    fecha_inicio = Column(DateTime, nullable=True)
    fecha_termino = Column(DateTime, nullable=True)
    fecha_ultima_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.datetime.utcnow)

    # Relaciones opcionales (si necesitas cargar datos relacionados)
    servicio = relationship("ServiceM", back_populates="espacios")
    espacio = relationship("Espacio", back_populates="servicios_medicos")
