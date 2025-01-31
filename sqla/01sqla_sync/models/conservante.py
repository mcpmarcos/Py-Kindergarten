import sqlalchemy as sa

from datetime import datetime

from models.model_base import ModelBase

class Conservante(ModelBase):
    __tablename__: str = "conservantes"
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    nome: str = sa.Column(sa.String(45), unique=True, nullable=False)
    descricao: str = sa.Column(sa.String(45), nullable=False)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now)
   

    def __repr__(self) -> str:
        return f"<Conservante(nome='{self.nome}')>"