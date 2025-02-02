from typing import Optional

from pydantic import BaseModel as scBaseModel


class CursoSchema(scBaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    class Config:
        orm_mode = True
