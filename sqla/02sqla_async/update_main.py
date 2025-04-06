from conf.db_session import create_session
from models.sabor import Sabor
from models.picole import Picole


def select_filtro_picole(id_picole: int) -> None:
    with create_session() as session:
 
        picole: Picole = session.query(Picole).where(Picole.id == id_picole).one_or_none()
        
        if picole:
            print(f'ID: {picole.id}')
            print(f'Nome: {picole.sabor.nome}')
            print(f'Preço: {picole.preco}')
            print('--------------------------------------')
        else:
            print("Picolé não encontrado.")
            print('--------------------------------------')

# Buscar registro no banco
# Fazer alterações no registro
# Atualizar/Salvar o registro no banco

def atualizar_sabor(id__sabor: int, novo_nome: str) -> None:
    with create_session() as session:

        # Buscar registro no banco
        sabor = session.query(Sabor).filter(Sabor.id == id__sabor).one_or_none()
        if sabor:
            # Fazer alterações no registro
            sabor.nome = novo_nome
            # Atualizar/Salvar o registro no banco
            print("Sabor {sabor.nome} atualizado com sucesso.")
            session.commit()
        else:

            print("Sabor não encontrado.")


def atualizar_picole(id__picole: int, novo_preco: float, novo_sabor: int = None) -> None:
    with create_session() as session:

        # Buscar registro no banco
        picole = session.query(Picole).filter(Picole.id == id__picole).one_or_none()

        # Fazer alterações no registro
        if picole:
            picole.preco = novo_preco

            if novo_sabor:
                picole.id_sabor = novo_sabor

            # Atualizar/Salvar o registro no banco
            print("Picolé atualizado com sucesso.")
            session.commit()
        else:
            print("Picolé não encontrado.")

if __name__ == "__main__":
    
    # from select_main import select_filtro_sabor

    # id_sabor = 42
    # novo_nome = "Limão com mel"
    # select_filtro_sabor(id_sabor)

    # atualizar_sabor(id_sabor, novo_nome)
    
    # select_filtro_sabor(id_sabor)

    #############################################
    id_picole = 22
    novo_preco = 7.99
    id_novo_sabor = 42
    
    select_filtro_picole(id_picole)

    atualizar_picole(id_picole, novo_preco, id_novo_sabor)

    select_filtro_picole(id_picole)

