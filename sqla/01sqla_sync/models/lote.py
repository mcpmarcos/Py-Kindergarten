import sqlalchemy as sa
from sqlalchemy.orm import Mapped

import sqlalchemy.orm as orm
from datetime import datetime

from models.model_base import ModelBase
from models.tipo_picole import TipoPicole


class Lote(ModelBase):
    __tablename__: str = "lotes"

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now)
    id_tipo_picole: int = sa.Column(sa.Integer, sa.ForeignKey("tipos_picole.id")) #tabela.campo
    tipo_picole: Mapped[TipoPicole]= orm.relationship("TipoPicole", lazy="joined")
    quantidade: int = sa.Column(sa.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"<Lote(nome='{self.id}')>" 