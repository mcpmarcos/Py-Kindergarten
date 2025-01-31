from typing import (
    List, 
    Optional, 
    Any, 
    Dict
    )

from fastapi import (
    FastAPI, 
    HTTPException, 
    status, 
    Query,
    Path, 
    Header,
    Depends
    )

from models import Curso, cursos

from fastapi.responses import Response

from time import sleep


app = FastAPI(title="MCP API", version="0.0.1", description="API para estudo do framawork FastAPI")

def fake_db():
    try:
        print("Abrindo conexão como banco de dados...")
        sleep(1)
    finally:
        print("Fechando conexão como banco de dados...")
        sleep(1)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app",
        host="0.0.0.0",
        port=8000,
        reload= True)
    
 
@app.get("/cursos", 
description="Retorna lista de cursos ou lista vazia.", 
summary="Retorna todos os cursos",
response_model=List[Curso], response_description="Cursos encontrados com sucesso.")
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@app.get("/cursos/{curso_id}", description="Retorna curso referente ao ID passado comoparâmetro.", 
summary="Retorna o curso requisitado",
response_model= Curso)
async def get_curso(curso_id: int = Path(title="ID do curso", description="Deve ser entre 1 e 2",lt=3), db: Any = Depends(fake_db)):
    try:
        return cursos[curso_id]
    except IndexError:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND, 
            detail="Curso não encontrado")
    

@app.post("/cursos", status_code=status.HTTP_201_CREATED,
description="Retorna o JSON do curso inserido no banco de dados.", 
summary="Retorna o curso inserido.",
response_model= Curso)
async def post_curso(curso: Curso,):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    #del curso.id
    cursos.append(curso) # insere o curso na lista
    return curso


@app.put('/cursos', status_code= status.HTTP_202_ACCEPTED,
description="Retorna o JSON do curso atualizado no banco de dados.", 
summary="Retorna o curso atualizado.",
response_model= Curso)
async def update_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        curso.id = curso_id
        cursos[curso_id] = curso
        del curso.id
        return cursos
    else:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND, 
            detail="O curso {curso_id} não encontrado")
    

@app.delete('/cursos/{curso_id}',
description="Deleta o curso referente ao ID passado comoparâmetro.", 
summary="Deleta um curso existente.",
#response_model= "Curso deletado com sucesso." ->> response_modelnãoaceita string
)
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del(cursos[curso_id])
        return Response(
            status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND, 
            detail=f"O curso {curso_id} não encontrado")



@app.get("/calculadora")
async def calcular(a: int = Query(gt=5), b: Optional[int] = None, x_geek = Header(), c: int = Query(gt= 5)):
    result = a + b
    if c: 
        result = result + c
        print(f"X-GEEK:{x_geek}")
    return {"resultado", result}



    