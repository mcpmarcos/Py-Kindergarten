from pytz import timezone

from typing import Optional, List
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from jose import jwt    

from model.usuario_model import UsuarioModel

from core.configs import settings

from core.security import verificar_senha

from pydantic import EmailStr

import os

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl = "os.getenv(API_V1_STR)/usuarios/login"
)

async def autenticar(email: EmailStr, senha: str, db: AsyncSession) -> Optional[UsuarioModel]:
    async with db  as session:
        # query = 
        result = await session.execute(select(UsuarioModel).filter(UsuarioModel.email == email))
        usuario: UsuarioModel = result.scalars().unique().one_or_none()
        if not usuario:
            return None
        if not verificar_senha(senha, usuario.senha):
            return None
        return usuario 
    

def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str ) -> str:
    
    # https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3
    
    payload = {}
    sp_timezone = timezone("America/Sao_Paulo")
    expire = datetime.now(tz=sp_timezone) + tempo_vida 

    # dados do payload (translate = carga útil)

    payload["type"] = tipo_token
    payload["exp"] = expire

    # iat >> issued at = "gerado em..."
    payload["iat"] = datetime.now(tz=sp_timezone)

    #subject
    payload["sub"] = str(sub)
 
    return jwt.encode(payload, settings.JWT_SECRET, algorithm= settings.ALGORITHM)

# https://jwt.io ==>> Para maiores informações
def criar_token_acesso(sub: str) -> str:
    return _criar_token(
        tipo_token = "access token",
        tempo_vida = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub = sub)