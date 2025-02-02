from core.configs import settings
from core.database import engine


async def create_tables() -> None:
    import models.__all_models
    print("Criando as tabelas no banco de dados")

    # Pesquisar comandos que o begin(), o run(),

    # fazem e o que os comandos abaixo fazem

    async with engine.begin() as conn:
        await conn.run_sync(settings.dbBaseModel.metadata.drop_all)
        await conn.run_sync(settings.dbBaseModel.metadata.create_all)
    print("Tabelas criadas com sucesso")


if __name__ == "__main__":
    import asyncio

    asyncio.run(create_tables())
    