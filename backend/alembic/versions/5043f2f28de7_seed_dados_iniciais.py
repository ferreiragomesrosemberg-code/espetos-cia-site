"""seed dados iniciais

Revision ID: 5043f2f28de7
Revises: ab5352d7c140
Create Date: 2026-04-14 19:57:04.670294
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '5043f2f28de7'
down_revision: Union[str, Sequence[str], None] = 'ab5352d7c140'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Usuário admin
    op.execute("INSERT INTO users (id, name) VALUES (1, 'Admin')")

    # Cardápio inicial
    op.execute("INSERT INTO cardapio (id, nome, descricao, preco) VALUES (1, 'Espeto de frango', 'Espeto de frango temperado', 10.00)")
    op.execute("INSERT INTO cardapio (id, nome, descricao, preco) VALUES (2, 'Espeto de carne', 'Espeto de carne bovina', 12.00)")
    op.execute("INSERT INTO cardapio (id, nome, descricao, preco) VALUES (3, 'Espeto misto', 'Frango e carne juntos', 15.00)")

    # Promoções iniciais
    op.execute("INSERT INTO promocao (id, titulo, desconto) VALUES (1, 'Promoção de segunda', 20)")
    op.execute("INSERT INTO promocao (id, titulo, desconto) VALUES (2, 'Happy Hour', 10)")

    # Contatos iniciais
    op.execute("INSERT INTO contato (id, nome, mensagem) VALUES (1, 'Cliente Teste', 'Gostei muito dos espetos!')")
    op.execute("INSERT INTO contato (id, nome, mensagem) VALUES (2, 'Outro Cliente', 'Quais os horários de funcionamento?')")

def downgrade() -> None:
    op.execute("DELETE FROM users WHERE id=1")
    op.execute("DELETE FROM cardapio WHERE id IN (1,2,3)")
    op.execute("DELETE FROM promocao WHERE id IN (1,2)")
    op.execute("DELETE FROM contato WHERE id IN (1,2)")
