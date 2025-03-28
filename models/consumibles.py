# pylint: disable=too-few-public-methods
"""Modelo ORM para representar los consumibles médicos del hospital."""

import uuid
from enum import Enum
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Enum as SqlEnum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config.db import Base


class TipoConsumibleEnum(str, Enum):
    Guantes = "Guantes"
    Jeringas = "Jeringas"
    Gasas = "Gasas"
    Vendas = "Vendas"
    Algodón = "Algodón"
    Cubrebocas = "Cubrebocas"
    Bata_desechable = "Bata desechable"
    Suero = "Suero"
    Agua_inyectable = "Agua inyectable"
    Material_de_curacion = "Material de curación"
    Tubos_de_recoleccion = "Tubos de recolección"
    Catéter = "Catéter"
    Jabón_antibacterial = "Jabón antibacterial"
    Bolsas_biológicas = "Bolsas biológicas"
    Lubricante = "Lubricante"
    Toallas_desechables = "Toallas desechables"
    Soluciones_antisépticas = "Soluciones antisépticas"
    Agujas = "Agujas"
    Cinta_microporosa = "Cinta microporosa"
    Material_de_limpieza = "Material de limpieza"


class Consumible(Base):
    """
    Representa un consumible o insumo médico utilizado dentro del hospital,
    como guantes, jeringas, medicamentos, etc.
    """

    __tablename__ = "tbc_consumibles"

    id = Column(
        String(36),
        primary_key=True,
        index=True,
        default=lambda: str(uuid.uuid4())
    )
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=False)
    tipo = Column(SqlEnum(TipoConsumibleEnum), nullable=False)
    departamento_id = Column(String(36), nullable=False)
    cantidad_existencia = Column(Integer, nullable=False)
    detalle = Column(Text, nullable=True)
    fecha_registro = Column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )
    fecha_actualizacion = Column(
        DateTime,
        nullable=True,
        onupdate=func.now()
    )
    estatus = Column(Boolean, nullable=True)
    observaciones = Column(Text, nullable=True)
    espacio_medico = Column(String(50), nullable=True)

    servicios = relationship(
        "ServiciosMedicosConsumibles",
        back_populates="consumible"
    )
