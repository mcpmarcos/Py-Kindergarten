from conf.db_session import create_session
from models.sabor import Sabor
from models.picole import Picole

from sqlalchemy.future import select
import asyncio

async def select_filtro_picole(id_picole: int) -> None:
    async with create_session() as session:
 
        query = select(Picole).where(Picole.id == id_picole)
        result = await session.execute(query)
        picole = result.unique().scalar_one_or_none()
        
        if picole:
            print(f'ID: {picole.id}')
            print(f'Sabor: {picole.sabor.nome}')
            print(f'Preço: {picole.preco}')
            print('--------------------------------------')
        else:
            print("Picolé não encontrado.")
            print('--------------------------------------')

# Buscar registro no banco
# Fazer alterações no registro
# Atualizar/Salvar o registro no banco

async def atualizar_sabor(id__sabor: int, novo_nome: str) -> None:
    async with create_session() as session:

        # Buscar registro no banco
        query = select(Sabor).filter(Sabor.id == id__sabor)
        result = await session.execute(query)
        sabor = result.unique().scalar_one_or_none()
        
        if sabor:
            # Fazer alterações no registro
            sabor.nome = novo_nome
            # Atualizar/Salvar o registro no banco
            print("Sabor {sabor.nome} atualizado com sucesso.")
            await session.commit()
        else:
            print("Sabor não encontrado.")


async def atualizar_picole(id__picole: int, novo_preco: float, novo_sabor: int = None) -> None:
    async with create_session() as session:

        # Buscar registro no banco
        query = select(Picole).filter(Picole.id == id__picole)
        result = await session.execute(query)
        picole = result.unique().scalar_one_or_none()

        # Fazer alterações no registro
        if picole:
            picole.preco = novo_preco

            if novo_sabor:
                picole.id_sabor = novo_sabor

            # Atualizar/Salvar o registro no banco
            print("Picolé atualizado com sucesso.")
            await session.commit()
        else:
            print("Picolé não encontrado.")


async def update_sabor():
    from select_main import select_filtro_sabor

    id_sabor = 42
    novo_nome = "Ciriguela e Mutuca"
    
    await select_filtro_sabor(id_sabor)

    await atualizar_sabor(id_sabor, novo_nome)
    
    await select_filtro_sabor(id_sabor)


async def update_picole():

    id_picole = 22
    novo_preco = 7.99
    id_novo_sabor = 42
    
    await select_filtro_picole(id_picole)

    await atualizar_picole(id_picole, novo_preco, id_novo_sabor)

    await select_filtro_picole(id_picole)


if __name__ == "__main__":
    
    # asyncio.run(update_sabor())
    asyncio.run(update_picole())

