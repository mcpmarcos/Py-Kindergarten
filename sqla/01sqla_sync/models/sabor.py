import sqlalchemy as sa

from datetime import datetime

from models.model_base import ModelBase

class Sabor(ModelBase):
    __tablename__: str = "sabores"
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    nome: str = sa.Column(sa.String(45), unique=True, nullable=False)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"<Sabor(nome='{self.nome}')>"