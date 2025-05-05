
import asyncio


# insert pt 1
from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor

# insert pt 2
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole



# 1 Aditivo Nutritivo
async def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print('Cadastrando aditivo nutritivo')

    nome:str = input('Informe o nome do aditivo nutritivo: ')

    formula_quimica:str = input('Informe a fórmula química do aditivo nutritivo: ')

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    async with create_session() as session:
        session.add(an)
        await session.commit()

    print(f'Aditivo Nutritivo {an.nome} cadastrado com sucesso!')
    print(f'ID do aditivo nutritivo: {an.id}')

    print(f'Fórmula química: {an.formula_quimica}')
    print(f'Data de criação: {an.data_criacao}')

    return an


# 2 Sabor
async def insert_sabor() -> None:
    print('Cadastrando sabor')

    nome:str = input('Informe o nome do sabor: ')

    sabor: Sabor = Sabor(nome=nome)

    async with create_session() as session:
        session.add(sabor)
        await session.commit()

    print(f'Sabor {sabor.nome} cadastrado com sucesso!')

    print(f'ID do sabor: {sabor.id}')

    print(f'Data de criação: {sabor.data_criacao}')

    return sabor


# 3 tipos_embalagem
async def insert_tipos_embalagem() -> None:
    print('Cadastrando tipo deembalagem')

    nome:str = input('Informe o nome do tipo de embaagem: ')

    tipo_embalagem: TipoEmbalagem = TipoEmbalagem(nome=nome)

    async with create_session() as session:
        session.add(tipo_embalagem)
        await session.commit()

    print(f'Tipo de embalagem {tipo_embalagem.nome} cadastrado com sucesso!')

    print(f'ID do tipo de embalagem: {tipo_embalagem.id}')

    print(f'Data de criaçãodo tipo de embalagem: {tipo_embalagem.data_criacao}')


# 4 tipos_picole
async def insert_tipo_picole() -> None:
    print('Cadastrando tipo de picolé')

    nome:str = input('Informe o nome do tipo de picolé: ')

    tipo_picole: TipoPicole = TipoPicole(nome=nome)

    async with create_session() as session:
        session.add(tipo_picole)
        await session.commit()

    print(f'Tipo de picolé {tipo_picole.nome} cadastrado com sucesso!')

    print(f'ID do tipo de picolé: {tipo_picole.id}')

    print(f'Data de criaçãodo do tipode picolé: {tipo_picole.data_criacao}')


# 5 ingredientes
async def insert_ingrediente() -> Ingrediente:
    print('Cadastrando ingrediente')

    nome:str = input('Informe o nome do ingrediente: ')

    ingrediente: Ingrediente = Ingrediente(nome=nome)

    async with create_session() as session:
        session.add(ingrediente)
        await session.commit()

    print(f'Ingrediente {ingrediente.nome} cadastrado com sucesso!')

    print(f'ID do ingrediente: {ingrediente.id}')

    print(f'Data de criaçãodo do ingrediente: {ingrediente.data_criacao}')

    return ingrediente


# 6 conservantes
async def insert_conservante() -> Conservante:
    print('Cadastrando conservante')

    nome:str = input('Informe o nome do conservante: ')
    descricao:str = input('Descreva o conservante: ')

    conservante: Conservante = Conservante(nome=nome, descricao=descricao)

    async with create_session() as session:
        session.add(conservante)
        await session.commit()

    print(f'Conservante {conservante.nome} cadastrado com sucesso!')

    print(f'ID do conservante: {conservante.id}')

    print(f'Data de criaçãodo do conservante: {conservante.data_criacao}')

    return conservante


# 7 revendedor
async def insert_revendedor() -> Revendedor:
    print('Cadastrando revendedor')

    cnpj:str = input('Informe o cnpj do revendedor: ')
    razao_social:str = input('Informe a razão social: ')
    contato:str = input('Informe o contato: ')

    revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    async with create_session() as session:
        session.add(revendedor)
        await session.commit()

    return revendedor


# 8 lote
async def insert_lote() -> Lote:
    print('Cadastrando lote')

    # foi necessário fazer cast para a funçaõint()
    quantidade:int = int(input('Informe a quantidade do lote: '))
    id_tipo_picole:int = int(input('Informe o ID do tipo de picolé: '))
    
    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    async with create_session() as session:
        session.add(lote)
        await session.commit()

    return lote


# 9 nota_fiscal
async def insert_nota_fiscal() -> None:
    print('Cadastrando nota fiscal')

    valor:float = float(input('Informe o valor da nota fiscal: '))
    numero_serie:str = input('Informe número de série: ')
    descricao:str = input('Informe a descricao: ')
    id_revendedor:int = int(input('Informe o ID do revendedor: '))

    nota_fiscal: NotaFiscal = NotaFiscal(valor=valor, 
    numero_serie=numero_serie, 
    descricao=descricao, 
    id_revendedor=id_revendedor)

    lote = await insert_lote()
    nota_fiscal.lotes.append(lote)
   
    lote1 = await insert_lote() 
    nota_fiscal.lotes.append(lote1)
    
    async with create_session() as session:
        session.add(nota_fiscal)
        await session.commit()
        await session.refresh(nota_fiscal)


    return nota_fiscal


# 10 picole   
async def insert_picole() -> None:

    print('Cadastrando picolé:')

    preco:float = float(input('Informe o preço do picolé: '))
    id_sabor:int = int(input('Informe ID do sabor: '))
    id_tipo_embalagem:int = int(input('Informe ID do tipo de embalagem: '))
    id_tipo_picole:int = int(input('Informe o ID do tipo de picolé: '))

    # Criar/instanciar sabor
    
    picole: Picole = Picole(preco=preco, 
                            id_sabor=id_sabor, 
                            id_tipo_embalagem=id_tipo_embalagem, 
                            id_tipos_picole=id_tipo_picole)

    ingrediente1 = await insert_ingrediente()
    picole.ingredientes.append(ingrediente1) 

    ingrediente2 = await insert_ingrediente()
    picole.ingredientes.append(ingrediente2) 

    conservante = await insert_conservante()
    picole.conservantes.append(conservante)

    aditivo_nutritivo = await insert_aditivo_nutritivo()
    
    picole.aditivos_nutritivos.append(aditivo_nutritivo)

    async with create_session() as session:
        session.add(picole)
        await session.commit()
        await session.refresh(picole)

    return picole


if __name__ == '__main__':

    # 1 Aditivo Nutritivo
    # print('Cadastrando aditivo nutritivo')
    # print(asyncio.run(insert_aditivo_nutritivo()))
    # print('------------------------------')

    # asyncio.run(insert_aditivo_nutritivo())

    # 2 Sabor
    # asyncio.run(insert_sabor())

    # 3 tipos_embalagem
    # asyncio.run(insert_tipos_embalagem())

    # 4 tipos_picole
    # asyncio.run(insert_tipo_picole())

    # 5 ingredientes
    # asyncio.run(insert_ingrediente())

    # 6 conservantes
    # asyncio.run(insert_conservante())

    # 7 revendedor
    # rev = asyncio.run(insert_revendedor())
    # print(f'Revendedor {rev} cadastrado com sucesso!')
    
    # 8 lote
    # lote = asyncio.run(insert_lote()) 
    # print(f'Lote {lote} cadastrado com sucesso!')

    # 9 nota_fiscal
    # nf = asyncio.run(insert_nota_fiscal())
    # print(f'Nota fiscal {nf}cadastrada com sucesso!')

    # 10 picole
    # picole = asyncio.run(insert_picole()) 
    # print(f'Picolé {picole}cadastrado com sucesso!')  

    ...       