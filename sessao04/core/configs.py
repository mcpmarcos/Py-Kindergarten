from pydantic_settings import BaseSettings


from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base


# from fastapi import FastAPI


class Settings(BaseSettings):
    
    """
    Configurações gerais usadas na aplicação
    """         
    
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:123456@localhost:5432/sessao04"
    # DB_URL: str = "sqlite+aiosqlite:///./dev.db"
    
    # função que herda osrecursosdosql alchemy para os models
    dbBaseModel: DeclarativeMeta = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings() 

