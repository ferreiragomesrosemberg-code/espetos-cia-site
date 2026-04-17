import os

class Settings:
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
    ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS", "*").split(",")

settings = Settings()
