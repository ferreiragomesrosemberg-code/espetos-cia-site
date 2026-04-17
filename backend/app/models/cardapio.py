from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Cardapio(Base):
    __tablename__ = "cardapio"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Float, nullable=False)
