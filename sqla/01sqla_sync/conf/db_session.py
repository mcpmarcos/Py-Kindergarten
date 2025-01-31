import sqlalchemy as sa

from sqlalchemy.orm import sessionmaker

from pathlib import Path #Usado apenascasoo bancos ejsqlte 
from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine

from models.model_base import ModelBase

__engine: Optional[Engine] = None

# Função para configurar a conexão como Banco de dados
def create_engine(sqlite: bool = False) -> Engine:

    global __engine

    if __engine:
      return

    if sqlite:
        arquivo_db = "db/picole.sqlite"
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(url=conn_str, echo=False, connect_args={"check_same_thread": False})

    else:
        conn_str = 'postgresql://postgres:123456@localhost:5432/picoles'
        __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


# Função para criar uma sessão de conexão com o banco de dados
def create_session() -> Session:
    global __engine


    if not __engine:
        create_engine()                 # caso o banco seja o postgresql
        # create_engine(sqlite=True)    # caso o banco seja o sqlite
    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    
    session: Session = __session()
    
    return session


def create_tables() -> None:
    global __engine

    if not __engine:
        create_engine()                  # caso o banco seja o postgresql
        # create_engine(sqlite=True)     # caso o banco seja o sqlite
    import models.__all_models
    ModelBase.metadata.drop_all(__engine) 
    ModelBase.metadata.create_all(__engine) 