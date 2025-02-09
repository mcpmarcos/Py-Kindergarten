from typing import Optional

from sqlmodel import Field, SQLModel

class CursoModel(SQLModel,  table=True):
    __tablename__: str = "cursos"

    id: Optional[int] = Field(default=True, primary_key=True)
    titulo: str
    aulas: int
    horas: int