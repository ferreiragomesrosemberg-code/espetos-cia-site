import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL do banco de dados (vem do .env ou usa padrão local)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://user:password@localhost:5432/espetos"
)

# Cria o engine
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Cria a factory de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
