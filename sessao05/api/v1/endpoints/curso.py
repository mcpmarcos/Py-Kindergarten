from typing import List

from fastapi import (APIRouter,
                     status,
                     Depends,HTTPException,
                     Response
                     )

from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select

from models.curso_model import CursoModel

from core.deps import get_session

# Bypass warning from sqlmodel select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True # type: ignore

Select.inherit_cache = True # type: ignore

# Fim do bypass


router = APIRouter()

# post curso
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CursoModel)
async def post_curso(curso: CursoModel, db: AsyncSession = Depends(get_session)):
   novo_curso = CursoModel(titulo = curso.titulo, aulas = curso.aulas, horas = curso.horas)
   db.add(novo_curso)
   await db.commit()
   return novo_curso



# get cursos
@router.get("/", response_model=List[CursoModel])
async def get_cursos(db: AsyncSession = Depends(get_session)):
   async with db as session:
      #query = select(CursoModel)
      result = await session.execute(select(CursoModel))
      cursos: List[CursoModel] = result.scalars().all()
      return cursos
      

# get curso
@router.get("/{curso_id}")
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
   async with db as session:
      result = await session.execute(select(CursoModel).filter(CursoModel.id == curso_id))
      curso: CursoModel = result.scalar_one_or_none()

      if curso:
         return curso
      else:
         raise HTTPException(detail= "Curso não encontrado", status_code= status.HTTP_404_NOT_FOUND)



#put cursos
@router.put("/{curso_id}", response_model= CursoModel, status_code= status.HTTP_200_OK)
async def put_cursos(curso_id: int, curso: CursoModel, db: AsyncSession = Depends(get_session)):
    async with db as session:
       result = await session.execute(select(CursoModel).filter(CursoModel.id == curso_id))
       curso_up: CursoModel = result.scalar_one_or_none()

       if curso_up:
         curso_up.titulo = curso.titulo
         curso_up.aulas = curso.aulas
         curso_up.horas = curso.horas
         await session.commit()
         return curso_up
       else:
         raise HTTPException(detail= "Curso não encontrado", status_code= status.HTTP_404_NOT_FOUND)


#delete cursos
@router.delete("/{curso_id}", status_code= status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
       result = await session.execute(select(CursoModel).filter(CursoModel.id == curso_id))
       curso_del: CursoModel = result.scalar_one_or_none()

       if curso_del:
         await session.delete(curso_del)
         await session.commit()
         return HTTPException(status_code= status.HTTP_204_NO_CONTENT)
       else:
         raise HTTPException(detail= "Curso não encontrado", status_code= status.HTTP_404_NOT_FOUND)