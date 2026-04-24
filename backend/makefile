# Comandos para facilitar migrações e seeds com Alembic

# Aplica todas as migrações até a última versão
migrate:
    docker compose exec backend poetry run alembic upgrade head

# Cria uma nova revisão automática com mensagem personalizada
revision:
    docker compose exec backend poetry run alembic revision --autogenerate -m "nova revisao"

# Cria uma revisão manual para inserir seeds
seed:
    docker compose exec backend poetry run alembic revision -m "seed dados iniciais"

# Faz downgrade de uma versão (volta uma migração)
downgrade:
    docker compose exec backend poetry run alembic downgrade -1

# Reseta completamente o banco (remove volumes e recria containers)
reset-db:
    docker compose down -v
    docker compose up -d

# Lista todas as tabelas do banco
show-tables:
    docker compose exec db psql -U postgres -d espetos -c "\dt"
