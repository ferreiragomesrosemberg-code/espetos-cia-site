from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Promocao(Base):
    __tablename__ = "promocao"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    desconto = Column(Float, nullable=False)
