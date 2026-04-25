from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import datetime
from decimal import Decimal

from app import schemas
from app.db.database import get_db
from app.models.pedido import Pedido, ItemPedido

router = APIRouter()

@router.post("/", response_model=schemas.PedidoResponse)
def criar_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(get_db)):
    try:
        novo_pedido = Pedido(
            cliente_id=pedido.cliente_id,
            status=pedido.status,
            data=datetime.datetime.utcnow()
        )
        db.add(novo_pedido)
        db.flush()  # gera o ID sem commit

        itens = [
            ItemPedido(
                pedido_id=novo_pedido.id,
                nome_item=item.nome_item,
                quantidade=item.quantidade,
                preco=Decimal(str(item.preco))
            )
            for item in pedido.itens
        ]
        db.add_all(itens)
        db.commit()
        db.refresh(novo_pedido)
        return novo_pedido
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro ao criar pedido")

@router.get("/{pedido_id}", response_model=schemas.PedidoResponse)
def get_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido

@router.patch("/{pedido_id}/status", response_model=schemas.StatusResponse)
def atualizar_status(pedido_id: int, status_update: schemas.StatusUpdate, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    pedido.status = status_update.status
    db.commit()
    return {"id": pedido.id, "status": pedido.status}
