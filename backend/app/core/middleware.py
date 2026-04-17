import time
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from app.core.logging import logger
from app.core.config import settings

def setup_middlewares(app):
    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOW_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Logging de requisições
    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        logger.debug(f"{request.method} {request.url.path} → {response.status_code} ({duration:.4f}s)")
        return response
