from typing import List

from sqlalchemy import func # funções de agregação

from conf.helpers import formata_data
from conf.db_session import create_session

# select simples

from models.aditivo_nutritivo import AditivoNutritivo
from models.picole import Picole
from models.sabor import Sabor
from models.revendedor import Revendedor

# select composto / complexo


## Select Simples -> select * from nome-da-tabela
def select_todos_aditivos_nutritivos() -> None:
    with create_session() as session:
        # forma 1
        #aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo)

        # forma 2
        aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo).all()
        
        for a in aditivos_nutritivos:
            print(f'ID: {a.id}')
            print(f'Data de Criação: {formata_data(a.data_criacao)}')
            print(f'Nome: {a.nome}')
            print(f'Fórmula Química: {a.formula_quimica}')

def select_filtro_sabor(id_sabor: int) -> None:
    with create_session() as session:
        #forma 1 
        #sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).first()
        
        #forma 2 (recomendado)
        #sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()
        
        #forma 3 (Retorna uma exception exec.NoResult)
        # sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one()
        
        #forma 4 usando where() ao invés de filter(), e com eleé possível usar o one(), one_or_none() e first()
        sabor: Sabor = session.query(Sabor).where(Sabor.id == id_sabor).one()

        print(f'ID: {sabor.id}')
        print(f'Nome: {sabor.nome}')
        print(f'Data: {formata_data(sabor.data_criacao)}')


def select_complexo_picole() -> None:
    with create_session() as session:
        # select * from sabor where id = 21
        picoles: List[Picole] = session.query(Picole).all()
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

if __name__ == '__main__':
    #select_todos_aditivos_nutritivos()
    #select_filtro_sabor(21)
    select_complexo_picole()
