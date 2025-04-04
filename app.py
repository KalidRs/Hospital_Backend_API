from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 🔹 Importar configuración de la BD
from config.db import Base, engine
import models  # 🔹 Importa todos los modelos desde __init__.py

# 🔹 INICIALIZAR FASTAPI
app = FastAPI(
    title="HOSPITAL S.A. de C.V.",
    description=(
        "API RESTful para la gestión operativa de un hospital, "
        "construida con FastAPI y SQLAlchemy."
    ),
)

# 🔹 Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["http://localhost:8080"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 IMPORTAR RUTAS ACTIVAS
from routes.users import users_router
from routes.persons import persons_router
from routes.servicios_medicos import serviceM
from routes.servicios_medicos_espacios import router as servicios_espacios_router
from routes.servicios_medicos_consumibles import servicios_medicos_consumibles
from routes.espacios import espacio
from routes.consumibles import consumible
from routes.areas_medicas import area_medica
from routes.rol import rol
from routes.userrol import userrol
from routes.departamentos import departamentos

# 🔹 IMPORTAR RUTAS DOCUMENTADAS (NO USADAS POR AHORA)
# from routes.receta import receta
# from routes.citas import cita
# from routes.expediente import expediente
# from routes.cirugia import cirugia_router
from routes.horarios import horarios_router
# from routes.bitacora import bitacora
# from routes.dispensaciones import dispensacion
# from routes.estudios import estudios
# from routes.resultados_estudios import resultados_estudios
# from routes.lotes import lote
# from routes.medicamentos import medicamento
# from routes.personal_medico import personal_medico
from routes.puestos import puestos_router
# from routes.puestos_departamentos import puesto_departamento
# from routes.solicitudes import request
# from routes.tbb_aprobaciones import tbb_aprobaciones
# from routes.tbc_organos import tbc_organos
from routes.especialidades import especialidades_router
from routes.personal import personal_router


# 🔹 INCLUIR RUTAS ACTIVAS
app.include_router(users_router)
app.include_router(persons_router)
app.include_router(serviceM)
app.include_router(servicios_espacios_router)
app.include_router(servicios_medicos_consumibles)
app.include_router(espacio)
app.include_router(consumible)
app.include_router(area_medica)
app.include_router(rol)
app.include_router(userrol)
app.include_router(departamentos)
app.include_router(puestos_router)
app.include_router(horarios_router)
app.include_router(especialidades_router)
app.include_router(personal_router)




# 🔹 CREAR LAS TABLAS **DESPUÉS DE REGISTRAR LAS RUTAS**
print("🔄 Creando las tablas en MySQL si no existen...")
Base.metadata.create_all(bind=engine)
print("✅ Tablas creadas exitosamente en MySQL")
