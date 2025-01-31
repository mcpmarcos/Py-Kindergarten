import sqlalchemy as sa
import sqlalchemy.orm as orm


from datetime import datetime

from models.model_base import ModelBase
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.aditivo_nutritivo import AditivoNutritivo
from typing import List, Optional

from sqlalchemy.orm import Mapped

# Um picolé pode ter vários ingredientes
ingrediente_picole = sa.Table(
    "ingrediente_picole",
    ModelBase.metadata,
    sa.Column("id_picole", sa.Integer, sa.ForeignKey("picoles.id")),
    sa.Column("id_ingrediente", sa.Integer, sa.ForeignKey("ingredientes.id"))
    )

# Um picolé pode ter vários conservantes
conservantes_picoles = sa.Table(
    "conservantes_picoles",
    ModelBase.metadata,
    sa.Column("id_picole", sa.Integer, sa.ForeignKey("picoles.id")),
    sa.Column("id_conservante", sa.Integer, sa.ForeignKey("conservantes.id"))
    )

# Um picolé pode ter vários aditivos nutritivos
aditivos_nutritivos_picole = sa.Table(
    "aditivos_nutritivos_picole",
    ModelBase.metadata,
    sa.Column("id_picole", sa.Integer, sa.ForeignKey("picoles.id")),
    sa.Column("id_aditivos_nutritivos", sa.Integer, sa.ForeignKey("aditivos_nutritivos.id"))
    )

class Picole(ModelBase):
    __tablename__: str = "picoles"
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    preco: float = sa.Column(sa.DECIMAL(8,2), nullable=False)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now)
   
    id_sabor: int = sa.Column(sa.Integer, sa.ForeignKey("sabores.id"))
    sabor: Mapped[Sabor] = orm.relationship("Sabor", lazy="joined")
    
    id_tipo_embalagem: int = sa.Column(sa.Integer, sa.ForeignKey("tipos_embalagem.id"))
    tipo_embalagem: Mapped[TipoEmbalagem] = orm.relationship("TipoEmbalagem", lazy="joined")
    
    id_tipos_picole: int = sa.Column(sa.Integer, sa.ForeignKey("tipos_picole.id"))
    tipos_picole: Mapped[TipoPicole] = orm.relationship("TipoPicole", lazy="joined")

    # Um picolé pode ter vários ingredientes
    ingredientes: Mapped[List[Ingrediente]] = orm.relationship("Ingrediente", secondary=ingrediente_picole, backref="ingredientes", lazy="joined")

    # Um picolé pode ter vários conservantes
    conservantes: Mapped[Optional[List[Conservante]]] = orm.relationship("Conservante", secondary=conservantes_picoles, backref="conservantes", lazy="joined")

    # Um picolé pode ter vários aditivos nutritivos
    aditivos_nutritivos: Mapped[Optional[List[AditivoNutritivo]]] = orm.relationship("AditivoNutritivo", secondary=aditivos_nutritivos_picole, backref="aditivos_nutritivos", lazy="joined")

    def __repr__(self) -> str:
        return f"<Picolé(nome='{self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}')>"