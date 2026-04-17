from loguru import logger
from app.core.config import settings

logger.remove()
logger.add(
    "logs/espetos.log",
    rotation="1 day",
    retention="7 days",
    compression="zip",
    level=settings.LOG_LEVEL,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>"
)
