import os
import uvicorn
from fastapi import FastAPI
from app.core.middleware import setup_middlewares
from app.core.logging import logger
from app.core.exceptions import register_exception_handlers
from app.routers import cardapio, promocao, contato, pedidos, clientes

app = FastAPI(
    title="Espetos & Cia API",
    description="API para gerenciar cardápio, promoções, contato e pedidos do restaurante",
    version="1.0.0"
)

# Configura middlewares
setup_middlewares(app)

# Registra handlers de exceção (global, SQLAlchemy, validação)
register_exception_handlers(app)

# Inclui routers com prefixos e tags
app.include_router(cardapio.router, prefix="/cardapio", tags=["Cardápio"])
app.include_router(promocao.router, prefix="/promocoes", tags=["Promoções"])
app.include_router(contato.router, prefix="/contato", tags=["Contato"])
app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
app.include_router(pedidos.router, prefix="/pedidos", tags=["Pedidos"])

# Rotas utilitárias
@app.get("/")
def root():
    logger.debug("Rota raiz '/' chamada")
    return {"message": "Bem-vindo à API Espetos & Cia"}

@app.get("/health")
def healthcheck():
    return {"status": "ok"}

if __name__ == "__main__":
    log_level = os.getenv("LOG_LEVEL", "info").lower()
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, log_level=log_level)
