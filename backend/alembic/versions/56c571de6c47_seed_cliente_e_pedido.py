"""seed cliente, pedido e itens_pedido

Revision ID: 56c571de6c47
Revises: 4e176fd220d9
Create Date: 2026-04-24 11:29:42.685270
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
import datetime

# revision identifiers, used by Alembic.
revision: str = '56c571de6c47'
down_revision: Union[str, Sequence[str], None] = '4e176fd220d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Insere dados iniciais em clientes, pedidos e itens_pedido."""

    clientes_table = table(
        'clientes',
        column('id', sa.Integer),
        column('nome', sa.String),
        column('telefone', sa.String),
        column('endereco', sa.String),
    )
    op.bulk_insert(clientes_table, [
        {"id": 1, "nome": "Rosemberg", "telefone": "65999990001", "endereco": "Rua das Palmeiras, 123"},
        {"id": 2, "nome": "Maria", "telefone": "65999990002", "endereco": "Av. Brasil, 456"},
    ])

    pedidos_table = table(
        'pedidos',
        column('id', sa.Integer),
        column('cliente_id', sa.Integer),
        column('status', sa.String),
        column('data', sa.TIMESTAMP),
    )
    op.bulk_insert(pedidos_table, [
        {"id": 1, "cliente_id": 1, "status": "Em andamento", "data": datetime.datetime.now()},
        {"id": 2, "cliente_id": 2, "status": "Concluído", "data": datetime.datetime.now()},
    ])

    itens_pedido_table = table(
        'itens_pedido',
        column('id', sa.Integer),
        column('pedido_id', sa.Integer),
        column('nome_item', sa.String),
        column('quantidade', sa.Integer),
        column('preco', sa.Numeric(10, 2)),
    )
    op.bulk_insert(itens_pedido_table, [
        {"id": 1, "pedido_id": 1, "nome_item": "Espeto de Frango", "quantidade": 2, "preco": 8.50},
        {"id": 2, "pedido_id": 1, "nome_item": "Espeto de Carne", "quantidade": 1, "preco": 10.00},
        {"id": 3, "pedido_id": 2, "nome_item": "Espeto de Linguiça", "quantidade": 3, "preco": 7.00},
    ])


def downgrade() -> None:
    """Remove os dados inseridos em clientes, pedidos e itens_pedido."""
    op.execute("DELETE FROM itens_pedido WHERE id IN (1,2,3)")
    op.execute("DELETE FROM pedidos WHERE id IN (1,2)")
    op.execute("DELETE FROM clientes WHERE id IN (1,2)")
