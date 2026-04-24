from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    status = Column(String, default="Aguardando entrega")
    data = Column(TIMESTAMP, default=datetime.utcnow)

    cliente = relationship("Cliente", backref="pedidos")
    itens = relationship("ItemPedido", back_populates="pedido")

class ItemPedido(Base):
    __tablename__ = "itens_pedido"
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    nome_item = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco = Column(Numeric(10,2), nullable=False)

    pedido = relationship("Pedido", back_populates="itens")
