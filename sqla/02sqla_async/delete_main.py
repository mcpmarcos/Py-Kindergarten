from typing import Optional

from conf.db_session import create_session

from models.revendedor import Revendedor
from models.picole import Picole

import asyncio
from sqlalchemy.future import select

# Buscar registro no banco
# Deletar o registro encontrado
# Registrar no banco a deleção do registro


async def select_filtro_revendedor(id_revendedor: int) -> None:
    async with create_session() as session:
        
        query = select(Revendedor).filter(Revendedor.id == id_revendedor)
        result = await session.execute(query)
        revendedor: Optional[Revendedor] = result.scalars().unique().one_or_none()

        if revendedor:
            print(f"ID: {revendedor.id}")
            print(f"Razão Social: {revendedor.razao_social}")
            print("----------------------------------------")
        else:
            print(f"Não foi encontrado nenhum revendedor com id {id_revendedor}")
            print("----------------------------------------")

async def deletar_picole(id_picole: int) -> None:
    async with create_session() as session:
        
        # Buscar registro no banco
        query = select(Picole).filter(Picole.id == id_picole)
        result = await session.execute(query)
        picole: Optional[Picole] = result.scalars().unique().one_or_none()
        
        if picole:
            # Deletar o registro encontrado
            await session.delete(picole)
            # Registrar no banco a deleção do registro
            await session.commit()
            print(f'Picolé {picole.id} deletado com sucesso.')
        else:
            print(f"Picolé {picole.id} não encontrado.")

async def deletar_revendedor(id_revendedor: int) -> None:
    async with create_session() as session:
        
        query = select(Revendedor).filter(Revendedor.id == id_revendedor)
        result = await session.execute(query)
        revendedor: Optional[Revendedor] = result.scalars().unique().one_or_none()

        if revendedor:
            await session.delete(revendedor)
            await session.commit()
            print(f"Revendedor {id_revendedor} deletado com sucesso.")

        else:
            print(f"Não foi encontrado nenhum revendedor com id {id_revendedor}")
            print("----------------------------------------")
        

async def delete_revendedor():
    
    # Fazer consulta na tabelade notas fiscais para saber quais IDs de revendedor estão vincularos ou não
    
    id_revendedor_vinculado = 6
    id_revendedor_nao_vinculado = 3

    # await select_filtro_revendedor(id_revendedor_vinculado)

    await deletar_revendedor(id_revendedor_nao_vinculado)

    # await select_filtro_revendedor(id_revendedor_vinculado)

async def delete_picole():
        
        from update_main import select_filtro_picole

        id_picole = 22
    
        await select_filtro_picole(id_picole)
    
        await deletar_picole(id_picole)
    
        await select_filtro_picole(id_picole)

if __name__ == "__main__":

    asyncio.run(delete_revendedor())
    # asyncio.run(delete_picole())

#######################################################

    # Como a tabela de revendedor está relacionada a de notas, eu só posso deletar um revendedor que não esteja relacionado a uma nota

    # Caso eu tenha tentado deletar um revendedor vinculado a uma nota fiscal, vai dar erro   

######################################################
