from typing import List, ClassVar

from pydantic_settings import BaseSettings

from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    
    API_V1_STR:str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:123456@localhost:5432/sessao06"

    DBBaseModel: ClassVar[str] = declarative_base()


    """
    No terminal digitar:

    python

    import secrets

    token: str = secrets.token_urlsafe(32)
    
    """



    JWT_SECRET: str = "VTzb_5xHp-BaNrspXhLSOUviGrN7mL1eoSajtHeL_TA" 
    ALGORITHM: str = "HS256" 

    # >> 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24*7

    class Config:
        case_sensitive = True

settings: Settings = Settings()