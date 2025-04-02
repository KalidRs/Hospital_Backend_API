# models/horarios.py

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, Time
from config.db import Base

class Horario(Base):
    __tablename__ = "tbc_horarios"

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    nombre = Column(String(100), nullable=False)  # Ej: "Turno Matutino"
    dia_semana = Column(String(20), nullable=False)  # Ej: "Lunes"
    hora_inicio = Column(Time, nullable=False)  # Hora como tipo TIME
    hora_fin = Column(Time, nullable=False)
    turno = Column(String(50), nullable=True)  # Opcional: "Matutino", "Vespertino", etc.
    estatus = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
