from fastapi import APIRouter

from api.v1.endpoints import curso

# /api/v1/cursos
api_router = APIRouter()

api_router.include_router(curso.router, prefix="/cursos", tags=["Cursos"])