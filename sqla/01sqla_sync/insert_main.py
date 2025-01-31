from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo


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

if __name__ == '__main__':
    insert_aditivo_nutritivo()