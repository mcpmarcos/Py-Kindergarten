from typing import List, Optional, Any

from fastapi import APIRouter, status, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from model.usuario_model import UsuarioModel
from schemas.usuario_schema import UsuarioSchemaBase, UsuarioSchemaCreate, UsuarioSchemaArtigos, UsuarioSchemaUp

from core.deps import get_session, get_current_user

from core.security import gerar_hash_senha
from core.auth import criar_token_acesso, autenticar

router = APIRouter()

# GET - Logado
@router.get("/logado", response_model=UsuarioSchemaBase)
def get_logado(usuario_logado: UsuarioModel = Depends(get_current_user)):
    return usuario_logado

# POST - Signup
@router.post("/signup", 
             status_code=status.HTTP_201_CREATED, 
             response_model=UsuarioSchemaBase)
async def post_signup(usuario: UsuarioSchemaCreate, 
                      db: AsyncSession = Depends(get_session)) -> Any:

    novo_usuario = UsuarioModel(nome=usuario.nome, 
                                sobrenome=usuario.sobrenome, 
                                email=usuario.email, 
                                senha=gerar_hash_senha(usuario.senha), 
                                isAdmin=usuario.is_admin)
    async with db as session:
        try:
            db.add(novo_usuario)
            await session.commit()

            return novo_usuario
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, 
                                detail="Usuário já cadastrado")

# GET - Usuários
@router.get("/", response_model=List[UsuarioSchemaBase])
async def get_usuarios(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel)
        result = await session.execute(query)
        usuarios: List[UsuarioModel] = result.scalars().unique().all()

        return usuarios
    

# GET - Usuário
@router.get("/{usuario_id}", response_model=UsuarioSchemaArtigos, status_code=status.HTTP_200_OK)
async def get_usuario(usuario_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario: UsuarioSchemaArtigos = result.scalars().unique().one_or_none()

        if usuario:
            return usuario
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
        

# PUT - Usuários
@router.put("/{usuario_id}", response_model=UsuarioSchemaBase, status_code=status.HTTP_202_ACCEPTED)
async def put_usuario(usuario_id: int, usuario: UsuarioSchemaUp, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario_up: UsuarioSchemaBase = result.scalars().unique().one_or_none()

        if usuario_up:
            if usuario.nome:
                usuario_up.nome = usuario.nome
            if usuario.sobrenome:
                usuario_up.sobrenome = usuario.sobrenome
            if usuario.email:
                usuario_up.email = usuario.email
            if usuario.is_admin:
                usuario_up.is_admin = usuario.is_admin
            if usuario.senha:
                usuario_up.senha = gerar_hash_senha(usuario.senha)
            await session.commit()
            return usuario_up
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
        

# DELETE - Usuário
@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_usuario(usuario_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario_del: UsuarioSchemaBase = result.scalars().unique().one_or_none()

        if usuario_del:
            await session.delete(usuario_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
        
# POST - Login
@router.post("/login", 
             response_model=UsuarioSchemaBase)
async def login(form_data : OAuth2PasswordRequestForm = Depends(), 
                db: AsyncSession = Depends(get_session)):
    
    usuario = await autenticar(email=form_data.username, 
                               senha=form_data.password, 
                               db=db)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Dados de acesso incorretos")
    return JSONResponse(content={"access_token": criar_token_acesso(sub=usuario.id), 
                                 "token_type": "bearer"},
                                 status_code=status.HTTP_200_OK)