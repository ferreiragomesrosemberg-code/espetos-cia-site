FROM python:3.11-slim

# Dependências do sistema necessárias para compilar extensões e psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia arquivos de dependências primeiro para aproveitar cache de camadas
COPY pyproject.toml poetry.lock* /app/

# Instala Poetry
RUN pip install --no-cache-dir poetry

# Configura Poetry para não criar virtualenvs e instala dependências do projeto
ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1
RUN poetry install --no-root --no-interaction --no-ansi

# Copia o código da aplicação
COPY . /app

# Porta exposta
EXPOSE 8000

# Comando de execução (uvicorn com reload para desenvolvimento)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
