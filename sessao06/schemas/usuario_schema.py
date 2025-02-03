from typing import List, Optional

from pydantic import BaseModel, EmailStr

from schemas.artigo_schema import ArtigoSchema


class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome:str
    email: EmailStr
    is_admin: bool = False

    class Config:
        orm_mode = True  

class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str

class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]

class UsuarioSchemaUp(UsuarioSchemaBase):
    sobrenome:Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    is_admin: Optional[bool]

    