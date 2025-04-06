from typing import Optional

from conf.db_session import create_session

from models.revendedor import Revendedor
from models.picole import Picole


# Buscar registro no banco
# Deletar o registro encontrado
# Registrar no banco a deleção do registro


def deletar_picole(id_picole: int) -> None:
    with create_session() as session:
        
        # Buscar registro no banco
        picole: Optional[Picole] = session.query(Picole).filter(Picole.id == id_picole).one_or_none()
        
        if picole:
            # Deletar o registro encontrado
            session.delete(picole)
            # Registrar no banco a deleção do registro
            session.commit()
            print(f'Picolé {picole.id} deletado com sucesso.')
        else:
            print(f"Picolé {picole.id} não encontrado.")


def select_filtro_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()

        if revendedor:
            print(f"ID: {revendedor.id}")
            print(f"Razão Social: {revendedor.razao_social}")
            print("----------------------------------------")
        else:
            print(f"Não foi encontrado nenhum revendedor com id {id_revendedor}")
            print("----------------------------------------")


def deletar_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()

        if revendedor:
            session.delete(revendedor)
            session.commit()
            print(f"Revendedor {id_revendedor} deletado com sucesso.")

        else:
            print(f"Não foi encontrado nenhum revendedor com id {id_revendedor}")
            print("----------------------------------------")
        


if __name__ == "__main__":
    # from update_main import select_filtro_picole

    # id_picole = 22

    # select_filtro_picole(id_picole)

    # deletar_picole(id_picole)

    # select_filtro_picole(id_picole)

#######################################################

    # Como a tabela de revendedor está relacionada a de notas, eu só posso deletar um revendedor que não esteja relacionado a uma nota

    # Caso eu tenha tentado deletar um revendedor vinculado a uma nota fiscal, vai dar erro

    
    id_revendedor_vinculado = 1
    id_revendedor_nao_vinculado = 2

    select_filtro_revendedor(id_revendedor_vinculado)

    deletar_revendedor(id_revendedor_vinculado)

    select_filtro_revendedor(id_revendedor_vinculado)

######################################################
