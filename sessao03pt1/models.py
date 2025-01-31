from typing import Optional

from pydantic import (
    BaseModel,
    validator
)

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    # para o validator funcionar, ele precisa estar dentro da classe Curso
    @validator("titulo")
    def validar_titulo(cls, value: str):
        palavras = value.split(' ')
        #validação 1
        if len(palavras) < 3:
            raise ValueError('O título deve ter peo menos 3 palavras.')
        #validação 2
        if value.islower():
             raise ValueError("O título deve ser capitalizado(em letras maiúsculas)")
        return value



cursos = [
    Curso(
        id=1, 
        titulo= "Programação em Java", 
        aulas= 117,
        horas= 58 ),
    Curso(
        id=2, 
        titulo= "Lógica e Algotirmos", 
        aulas= 65,
        horas= 30 )
        ]
   