from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor


# 1 Aditivo Nutritivo
def insert_aditivo_nutritivo() -> None:
    print('Cadastrando aditivo nutritivo')

    nome:str = input('Informe o nome do aditivo nutritivo: ')

    formula_quimica:str = input('Informe a fórmula química do aditivo nutritivo: ')

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)
        session.commit()

    print(f'Aditivo Nutritivo {an.nome} cadastrado com sucesso!')
    print(f'ID do aditivo nutritivo: {an.id}')

    print(f'Fórmula química: {an.formula_quimica}')
    print(f'Data de criação: {an.data_criacao}')


# 2 Sabor
def insert_sabor() -> None:
    print('Cadastrando sabor')

    nome:str = input('Informe o nome do sabor: ')

    sabor: Sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(sabor)
        session.commit()

    print(f'Sabor {sabor.nome} cadastrado com sucesso!')

    print(f'ID do sabor: {sabor.id}')

    print(f'Data de criação: {sabor.data_criacao}')


# 3 tipos_embalagem
def insert_tipos_embalagem() -> None:
    print('Cadastrando tipo deembalagem')

    nome:str = input('Informe o nome do tipo de embaagem: ')

    tipo_embalagem: TipoEmbalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(tipo_embalagem)
        session.commit()

    print(f'Tipo de embalagem {tipo_embalagem.nome} cadastrado com sucesso!')

    print(f'ID do tipo de embalagem: {tipo_embalagem.id}')

    print(f'Data de criaçãodo tipo de embalagem: {tipo_embalagem.data_criacao}')


# 4 tipos_picole
def insert_tipo_picole() -> None:
    print('Cadastrando tipo de picolé')

    nome:str = input('Informe o nome do tipo de picolé: ')

    tipo_picole: TipoPicole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(tipo_picole)
        session.commit()

    print(f'Tipo de picolé {tipo_picole.nome} cadastrado com sucesso!')

    print(f'ID do tipo de picolé: {tipo_picole.id}')

    print(f'Data de criaçãodo do tipode picolé: {tipo_picole.data_criacao}')

# 5 ingredientes
def insert_ingrediente() -> None:
    print('Cadastrando ingrediente')

    nome:str = input('Informe o nome do ingrediente: ')

    ingrediente: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ingrediente)
        session.commit()

    print(f'Ingrediente {ingrediente.nome} cadastrado com sucesso!')

    print(f'ID do ingrediente: {ingrediente.id}')

    print(f'Data de criaçãodo do ingrediente: {ingrediente.data_criacao}')

# 6 conservantes
def insert_conservante() -> None:
    print('Cadastrando conservante')

    nome:str = input('Informe o nome do conservante: ')
    descricao:str = input('Descreva o conservante: ')

    conservante: Conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(conservante)
        session.commit()

    print(f'Conservante {conservante.nome} cadastrado com sucesso!')

    print(f'ID do conservante: {conservante.id}')

    print(f'Data de criaçãodo do conservante: {conservante.data_criacao}')

# 7 revendedor
def insert_revendedor() -> Revendedor:
    print('Cadastrando revendedor')

    cnpj:str = input('Informe o cnpj do revendedor: ')
    razao_social:str = input('Informe a razão social: ')
    contato:str = input('Informe o contato: ')

    revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(revendedor)
        session.commit()

    return revendedor
    

if __name__ == '__main__':

    # 1 Aditivo Nutritivo
    #insert_aditivo_nutritivo()

    # 2 Sabor
    #insert_sabor() 

    # 3 tipos_embalagem
    # insert_tipos_embalagem()

    # 4 tipos_picole
    # insert_tipo_picole()

    # 5 ingredientes
    # insert_ingrediente()

    # 6 conservantes
    # insert_conservante()

    # 7 revendedor
    rev = insert_revendedor()
    print(f'Revendedor {rev} cadastrado com sucesso!')