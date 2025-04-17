from pathlib import Path #Usado apenascasoo bancos ejsqlte 

from typing import Optional
from sqlalchemy.orm import sessionmaker

# principais importações que determinam se a utilização da orm e do banco de dados será síncrona ou assíncrona

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine
 
from models.model_base import ModelBase

__async_engine: Optional[AsyncEngine] = None


# Função para configurar a conexão como Banco de dados
def create_engine(sqlite: bool = False) -> AsyncEngine:

    global __async_engine

    if __async_engine:
        return __async_engine
    
    if sqlite:
        arquivo_db = 'db/picoles-async-refactor.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f'sqlite+aiosqlite:///{arquivo_db}'
        __async_engine = create_async_engine(url=conn_str, echo=False, future=True, connect_args={"check_same_thread": False})
    else:
        conn_str = 'postgresql+asyncpg://postgres:123456@localhost:5432/picoles-async-refactor'
        __async_engine = create_async_engine(url=conn_str, echo=False)
    return __async_engine 



# Função para criar uma sessão de conexão com o banco de dados
def create_session() -> AsyncSession:

    global __async_engine

    if not __async_engine:
        create_engine()
    __async_session: AsyncSession = sessionmaker(
        __async_engine, 
        expire_on_commit=False, 
        class_=AsyncSession
        )
    session: AsyncSession = __async_session()
    return session 


async def create_tables() -> None:
    
    global __async_engine

    if not __async_engine:
        create_engine()

    import models.__all_models
    async with __async_engine.begin() as conn:
        await conn.run_sync(ModelBase.metadata.drop_all) 
        await conn.run_sync(ModelBase.metadata.create_all)
