from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    SERVICE_NAME: str = "AI Fantasy Avatar Generator"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "postgresql://user:pass@localhost/fantasy_avatars"
    REDIS_URL: str = "redis://localhost:6379/0"
    S3_UPLOAD_BUCKET: str = "fantasy-avatar-uploads"
    S3_OUTPUT_BUCKET: str = "fantasy-avatar-outputs"
    REPLICATE_API_TOKEN: str = ""
    STRIPE_SECRET_KEY: str = ""
    STRIPE_WEBHOOK_SECRET: str = ""
    DATA_RETENTION_DAYS: int = 7
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    class Config:
        env_file = ".env"

settings = Settings()
