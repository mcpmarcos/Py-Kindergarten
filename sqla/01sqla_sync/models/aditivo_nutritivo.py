import sqlalchemy as sa

from datetime import datetime

from models.model_base import ModelBase

class AditivoNutritivo(ModelBase):
    __tablename__: str = "aditivos_nutritivos"

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now)

    nome: str = sa.Column(sa.String(45), unique=True, nullable=False)
    formula_quimica: str = sa.Column(sa.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"<AditivoNutritivo(nome='{self.nome}')>"