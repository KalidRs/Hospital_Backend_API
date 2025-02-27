from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.userrol import userrol
from routes.receta import receta
from routes.citas import cita
from routes.expediente import expediente


from routes.cirugia import cirugia_router
from routes.horarios import horarios
from routes.espacios import espacio
from routes.areas_medicas import area_medica
from routes.bitacora import bitacora
from routes.consumibles import consumible
from routes.departamentos import departamentos
from routes.dispensaciones import dispensacion
from routes.estudios import estudios
from routes.resultados_estudios import resultados_estudios
#from routes.resultadosEstudios import resultadosEstudios
from routes.lotes import lote
from routes.medicamentos import medicamento
from routes.personal_medico import personal_medico
from routes.puestos import puesto
from routes.puestos_departamentos import puesto_departamento
from routes.solicitudes import request
from routes.tbb_aprobaciones import tbb_aprobaciones
from routes.tbc_organos import tbc_organos
# from routes.Pediatria.nacimientos import baby
# from routes.Pediatria.viewCiudad import view1
# from routes.Pediatria.viewGenero import view2
#from routes.Pediatria.vacunas import vacuna
from routes.servicios_medicos import serviceM



app = FastAPI(
    title="HOSPITAL S.A. de C.V.",
    description="API para el almacenamiento de información de un hospital"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    #allow_origins=["*"],  # Permite todas las solicitudes de origen cruzado. Puedes especificar una lista de dominios permitidos.
    allow_credentials=True,
    allow_origins=["http://localhost:8080"], 
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)


app.include_router(user)
app.include_router(person)
app.include_router(serviceM)
app.include_router(rol)
app.include_router(userrol)
app.include_router(receta)
app.include_router(cita)
app.include_router(expediente)
print ("Hola bienvenido a mi backend")
app.include_router(cirugia_router)
app.include_router(horarios)
app.include_router(espacio)
app.include_router(area_medica)
app.include_router(bitacora)
app.include_router(consumible)
app.include_router(departamentos)
app.include_router(dispensacion)
app.include_router(estudios)
#app.include_router(resultadosEstudios)
app.include_router(resultados_estudios)
app.include_router(lote)
app.include_router(medicamento)
app.include_router(personal_medico)
app.include_router(puesto)
app.include_router(puesto_departamento)
app.include_router(request)
app.include_router(tbb_aprobaciones)
app.include_router(tbc_organos)
#app.include_router(baby, prefix="/pediatria")
#app.include_router(view1, prefix="/pediatria")
#app.include_router(view2, prefix="/pediatria")
#app.include_router(vacuna, prefix="/pediatria")

print("Hola, bienvenido a mi backend hospital")
