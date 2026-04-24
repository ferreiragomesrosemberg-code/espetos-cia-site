"""seed dados iniciais

Revision ID: 7f9a1b2c3d4e
Revises: 266d3b54311a
Create Date: 2026-04-23 01:10:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '7f9a1b2c3d4e'
down_revision = '266d3b54311a'
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Tabela users
    users_table = table(
        'users',
        column('id', sa.Integer),
        column('name', sa.String),
    )
    op.bulk_insert(users_table, [
        {"id": 1, "name": "Admin"},
        {"id": 2, "name": "Cliente"},
    ])

    # Tabela cardapio
    cardapio_table = table(
        'cardapio',
        column('id', sa.Integer),
        column('nome', sa.String),
        column('descricao', sa.String),
        column('preco', sa.Float),
    )
    op.bulk_insert(cardapio_table, [
        {"id": 1, "nome": "Espeto de Frango", "descricao": "Frango temperado na brasa", "preco": 8.50},
        {"id": 2, "nome": "Espeto de Carne", "descricao": "Carne bovina suculenta", "preco": 10.00},
    ])

    # Tabela contato
    contato_table = table(
        'contato',
        column('id', sa.Integer),
        column('nome', sa.String),
        column('mensagem', sa.String),
    )
    op.bulk_insert(contato_table, [
        {"id": 1, "nome": "João", "mensagem": "Gostei muito do atendimento!"},
        {"id": 2, "nome": "Maria", "mensagem": "Quero saber sobre promoções."},
    ])

    # Tabela promocao
    promocao_table = table(
        'promocao',
        column('id', sa.Integer),
        column('titulo', sa.String),
        column('desconto', sa.Float),
    )
    op.bulk_insert(promocao_table, [
        {"id": 1, "titulo": "Promoção de Sexta", "desconto": 15.0},
        {"id": 2, "titulo": "Combo Família", "desconto": 20.0},
    ])


def downgrade() -> None:
    op.execute("DELETE FROM users WHERE id IN (1,2)")
    op.execute("DELETE FROM cardapio WHERE id IN (1,2)")
    op.execute("DELETE FROM contato WHERE id IN (1,2)")
    op.execute("DELETE FROM promocao WHERE id IN (1,2)")
