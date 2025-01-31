import sqlalchemy as sa

from datetime import datetime

from models.model_base import ModelBase

class TipoEmbalagem(ModelBase):
    __tablename__: str = "tipos_embalagem"
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    nome: str = sa.Column(sa.String(45), unique=True, nullable=False)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now)
   

    def __repr__(self) -> str:
        return f"<Tipo de Embalagem(nome='{self.nome}')>"