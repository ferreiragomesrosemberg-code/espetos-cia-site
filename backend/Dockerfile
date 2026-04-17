FROM python:3.11-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root

COPY ./app ./app

EXPOSE 8000

CMD ["poetry", "run", "python", "-m", "app.main"]
