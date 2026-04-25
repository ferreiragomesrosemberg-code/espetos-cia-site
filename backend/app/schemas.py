from typing import List, Literal
from pydantic import BaseModel, conint, condecimal, constr, field_validator
from datetime import datetime

# -------------------
# Cliente
# -------------------
class ClienteBase(BaseModel):
    nome: constr(min_length=2, max_length=100)
    telefone: constr(pattern=r'^\+?\d{8,15}$')  # aceita números com ou sem +
    endereco: str

    @field_validator("nome")
    def validar_nome(cls, v):
        if not v.strip():
            raise ValueError("Nome não pode ser vazio")
        return v

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id: int
    class Config:
        from_attributes = True


# -------------------
# Item do Pedido
# -------------------
class ItemPedidoBase(BaseModel):
    nome_item: constr(min_length=2)
    quantidade: conint(gt=0)  # maior que zero
    preco: condecimal(gt=0, max_digits=10, decimal_places=2)

class ItemPedidoCreate(ItemPedidoBase):
    pass

class ItemPedidoResponse(ItemPedidoBase):
    id: int
    pedido_id: int
    class Config:
        from_attributes = True


# -------------------
# Pedido
# -------------------
class PedidoBase(BaseModel):
    cliente_id: int
    status: Literal["pendente", "em andamento", "finalizado"]

class PedidoCreate(PedidoBase):
    itens: List[ItemPedidoCreate]

    @field_validator("itens")
    def validar_itens(cls, v):
        if not v or len(v) == 0:
            raise ValueError("Pedido deve conter pelo menos um item")
        return v

class PedidoResponse(PedidoBase):
    id: int
    data: datetime
    itens: List[ItemPedidoResponse] = []
    class Config:
        from_attributes = True


# -------------------
# Status do Pedido
# -------------------
class StatusUpdate(BaseModel):
    status: Literal["pendente", "em andamento", "finalizado"]

class StatusResponse(BaseModel):
    id: int
    status: str

    class Config:
        from_attributes = True
