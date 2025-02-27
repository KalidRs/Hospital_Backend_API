from sqlalchemy import func, Column, Integer, String, Boolean, DateTime, Enum, Date, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base



class Departamentos(Base):
    __tablename__ = "tbc_departamentos"

    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(100))
    AreaMedica_ID= Column(Integer, ForeignKey("tbb_personas.ID"))
    DepartamentoSuperior_ID = Column(Integer, ForeignKey("tbc_departamentos.ID"))
    Responsable_ID = Column(Integer)
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
