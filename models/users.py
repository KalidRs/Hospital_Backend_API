from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, text
from sqlalchemy.orm import relationship
from config.db import Base
import models.persons
import enum
from datetime import datetime

class MyEstatus(str, enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendido"

class User(Base):
    __tablename__ = "tbb_usuarios"

    ID = Column(Integer, primary_key=True, index=True)
    Persona_ID = Column(Integer, ForeignKey("tbb_personas.ID"), nullable=False)

    # ✅ Relación con Person
    persona = relationship("Person", back_populates="usuario")  # Relación 1 a 1
    Nombre_Usuario = Column(String(60), unique=True, nullable=False)
    Correo_Electronico = Column(String(100), unique=True, nullable=False)
    Contrasena = Column(String(255), nullable=False)  # Asegurar longitud suficiente para hashing
    Numero_Telefonico_Movil = Column(String(20), nullable=True)
    Estatus = Column(Enum(MyEstatus), default=MyEstatus.Activo, nullable=False)

    # ✅ Se genera automáticamente al crear un usuario
    Fecha_Registro = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

    # ✅ Se actualiza automáticamente al modificar el usuario
    Fecha_Actualizacion = Column(DateTime, nullable=True, onupdate=datetime.utcnow)

    # Relación con Person
    persona = relationship("Person", back_populates="usuario")

