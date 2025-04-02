import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener la URL de conexión desde .env
database_url = os.getenv("SQLALCHEMY_DATABASE_URL")

if not database_url:
    raise ValueError("No se encontró la variable SQLALCHEMY_DATABASE_URL en el archivo .env")

# Crear motor SQLAlchemy (sin SSL)
engine = create_engine(database_url)

# Crear la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos ORM
Base = declarative_base()
