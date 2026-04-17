from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Contato(Base):
    __tablename__ = "contato"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    mensagem = Column(String, nullable=False)
