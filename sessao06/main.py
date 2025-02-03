from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title="CursoAPI - Segurança")
app.include_router(api_router, prefix=settings.API_V1_STR)


# if __name__ == "__main__":
#     import uvicorn
#     import asyncio
#     import create_tables
#     asyncio.run(create_tables)
#     uvicorn.run("main:app", 
#                 host="0.0.0.0", 
#                 port=8000, 
#                 log_level="info", 
#                 reload=True) 
    

if __name__ == "__main__":
    import uvicorn
    import asyncio
    from create_tables import create_tables

    async def main():
        await create_tables()
        uvicorn.run("main:app", 
                    host="0.0.0.0", 
                    port=8000, 
                    log_level="info", 
                    reload=True)

    asyncio.run(main())