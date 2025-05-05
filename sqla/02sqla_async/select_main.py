from typing import List

from sqlalchemy import func # funções de agregação
from sqlalchemy.future import select # para fazer selects de forma assíncrona

import asyncio


from conf.helpers import formata_data
from conf.db_session import create_session

# select simples

from models.aditivo_nutritivo import AditivoNutritivo
from models.picole import Picole
from models.sabor import Sabor
from models.revendedor import Revendedor

# select composto / complexo

## Select Simples -> select * from nome-da-tabela
async def select_todos_aditivos_nutritivos() -> None:
    async with create_session() as session:
        
        query = select(AditivoNutritivo)
        result: List[AditivoNutritivo] = await session.execute(query)
        aditivos_nutritivos = result.scalars().all()
        
        """
        Outra forma de escrever a query aioma:

        aditivos_nutritivos: List[AditivoNutritivo] = (await session.execute(select(AditivoNutritivo))).scalars().all()

        """


        for a in aditivos_nutritivos:
            print(f'ID: {a.id}')
            print(f'Data de Criação: {formata_data(a.data_criacao)}')
            print(f'Nome: {a.nome}')
            print(f'Fórmula Química: {a.formula_quimica}')
            print('--------------------------------------')

async def select_filtro_sabor(id_sabor: int) -> None:
    async with create_session() as session:

        # Ambos funcionam:
        query = select(Sabor).filter(Sabor.id == id_sabor)
        # query = select(Sabor).where(Sabor.id == id_sabor)

        result: Sabor = await session.execute(query)
        
        # Forma 1: Retorna None caso não encontrado
        sabor = result.scalars().first()

        # Forma 2: Retorna None caso não encontrado
        # sabor: Sabor = result.scalars().one_or_none() # Recomendado


        # Forma 3: Retorna "exec.NoResultFound" caso não encontrado
        # sabor: Sabor = result.scalars().one()

        # Forma 4: Retorna None caso não encontrado
        # sabor: Sabor = result.scalar_one_or_none() # Recomendado


        print(f'ID: {sabor.id}')
        print(f'Nome: {sabor.nome}')
        print(f'Data: {formata_data(sabor.data_criacao)}')
        print('--------------------------------------')

async def select_complexo_picole() -> None:
    async with create_session() as session:
        
        query = select(Picole)
        result: List[Picole] = await session.execute(query)
        picoles = result.scalars().unique().all()

        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Preço: {picole.preco}')
            print(f'Data de Criação: {formata_data(picole.data_criacao)}')

            print(f'ID Sabor: {picole.sabor.id}')
            print(f'Sabor: {picole.sabor.nome}')

            print(f'ID Embalagem: {picole.id_tipo_embalagem}')
            print(f'Embalagem: {picole.tipo_embalagem.nome}')

            print(f'id tipo_picole: {picole.id_tipos_picole}')
            print(f'Tipo Picolé: {picole.tipos_picole.nome}')

            print(f'Ingredientes: {picole.ingredientes}')
            print(f'Aditivos Nutritivos: {picole.aditivos_nutritivos}')
            print(f'Conseervantes: {picole.conservantes}')

            print('--------------------------------------')

async def select_order_by_sabor() -> None:
    async with create_session() as session:
        
        query = select(Sabor).order_by(Sabor.data_criacao.desc())
        result: List[Sabor] = await session.execute(query)
        sabores = result.scalars().all()

        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Nome: {sabor.nome}')
            print('--------------------------------------')

async def select_group_by_picole() -> None:
    async with create_session() as session:
        
        query = select(Picole).group_by(Picole.id, Picole.id_tipos_picole)
        result: List[Picole] = await session.execute(query)
        picoles = result.scalars().unique().all()

        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Preço: {picole.preco}')
            print(f'Sabor: {picole.sabor.nome}')
            print(f'id tipo_picole: {picole.id_tipos_picole}')
            print('--------------------------------------')

async def select_limit() -> None:
    async with create_session() as session:
        query = select(Sabor).limit(25)
        result: List[Sabor] = await session.execute(query)
        sabores = result.scalars().all()
        
        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Nome: {sabor.nome}')
            print('--------------------------------------')

async def select_count() -> None:
    async with create_session() as session:
        
        query = select(func.count(Revendedor.id))
        result: List = await session.execute(query)
        qtd: int  = result.scalar()

        
        
        print(f'Quantidade de revendedores: {qtd}')
        print('--------------------------------------')

async def select_agregacao() -> None:
    async with create_session() as session:
        
        
        query = select(
            func.sum(Picole.preco).label('soma'),
            func.avg(Picole.preco).label('media'),
            func.min(Picole.preco).label('minimo'), 
            func.max(Picole.preco).label('maximo')
            
        )
        
        returned: List = await session.execute(query)
        result = returned.all()

        
        print(f'A soma de todos os picolés é: {result[0][0]}')
        print(f'A média de todos os picolés é: {result[0][1]}')
        print(f'O menor preço de todos os picolés é: {result[0][2]}')
        print(f'O maior preço de todos os picolés é: {result[0][3]}')

        print('--------------------------------------')

        print(f'Resultado: {result}')

        print('--------------------------------------')



if __name__ == '__main__':
    # asyncio.run(select_todos_aditivos_nutritivos())
    # asyncio.run(select_filtro_sabor(21))
    # asyncio.run(select_complexo_picole())
    # asyncio.run(select_order_by_sabor())
    # asyncio.run(select_group_by_picole())
    # asyncio.run(select_limit())
    # asyncio.run(select_count())
    asyncio.run(select_agregacao())

    
    