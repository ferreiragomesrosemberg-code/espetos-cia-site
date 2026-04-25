from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# URL de conexão com o banco (pegando do .env ou variável de ambiente)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:197822@db:5432/espetos")

# Cria engine
engine = create_engine(DATABASE_URL)

# Cria sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os models
Base = declarative_base()

# Dependência para injeção de sessão nos endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
