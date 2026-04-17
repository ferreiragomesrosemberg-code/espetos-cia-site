from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from sqlalchemy.exc import SQLAlchemyError
from app.core.logging import logger

def register_exception_handlers(app):
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.error(f"Erro inesperado em {request.url.path}: {exc}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Erro interno do servidor. Tente novamente mais tarde."}
        )

    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
        logger.error(f"Erro de banco em {request.url.path}: {exc}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Erro ao acessar o banco de dados. Tente novamente mais tarde."}
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        logger.warning(f"Erro de validação em {request.url.path}: {exc.errors()}")
        return JSONResponse(
            status_code=422,
            content={
                "detail": "Os dados enviados são inválidos.",
                "errors": exc.errors()
            }
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        logger.info(f"Erro HTTP {exc.status_code} em {request.url.path}: {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail or "Recurso não encontrado."}
        )
