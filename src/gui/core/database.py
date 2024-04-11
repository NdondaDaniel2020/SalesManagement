import sqlite3
from src.gui.core.absolute_path import AbsolutePath


class DataBase:
    def __init__(self, name: str = 'banco') -> None:
        if '.db' in name:
            self.name = name
        else:
            self.name = name+'.db'

    def connectDataBase(self) -> None:
        self.connection = sqlite3.connect(self.name)

    def disconnectDataBase(self) -> None:
        try:
            self.connection.commit()  # commit salva os dados no banco
            self.connection.close()
        except ImportError:
            print('Nenhuma conexão detetada')
            raise "No connection detected"

    def executarComand(self, comand: str) -> None:
        cursor = self.connection.cursor()
        cursor.execute(comand)

    # retorna todos
    def executarFetchall(self, fetchall) -> list:
        cursor = self.connection.cursor()
        cursor.execute(fetchall)
        dados = cursor.fetchall()
        return dados

    # retorna 1
    def executarFetchone(self, fetchall) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute(fetchall)
        dados = cursor.fetchone()
        return dados

    def __str__(self) -> str:
        return 'Class para criares o teu banco de dados'


if __name__ == "__main__":
    from pprint import pprint
    from src.qt_core import *

    lista_do_dado: dict = dict()
    atribustos: list = ['id', 'nome', 'unidade', 'categoria', 'metodo_de_pagamento', 'vendedor', 'cliente']
    db: DataBase = DataBase(AbsolutePath().getPathDatabase())

    for atributo in atribustos:
        db.connectDataBase()
        query = db.executarFetchall(f"SELECT DISTINCT {atributo} FROM vw_historico_de_venda")
        lista_do_dado[f'{atributo}'] = query
        db.disconnectDataBase()

    txt = '1'

    select = 'SELECT * FROM vw_historico_de_venda'
    padrao = QRegularExpression(r"^[0-9]{2}\/[0-9]{2}\/[0-9]{4}")
    if txt:
        if txt in str(lista_do_dado['id']):
            select = f"{select} WHERE id='{txt}';"
        elif padrao.match(txt).hasMatch():
            select = f"{select} WHERE data LIKE '{txt}%';"
        elif txt in str(lista_do_dado['nome']):
            select = f"{select} WHERE nome='{txt}';"
        elif txt in str(lista_do_dado['unidade']):
            select = f"{select} WHERE unidade='{txt}';"
        elif txt in str(lista_do_dado['metodo_de_pagamento']):
            select = f"{select} WHERE metodo_de_pagamento='{txt}';"
        elif txt in str(lista_do_dado['vendedor']):
            select = f"{select} WHERE vendedor='{txt}';"
        elif txt in str(lista_do_dado['cliente']):
            select = f"{select} WHERE cliente='{txt}';"


    print(select, str(lista_do_dado['nome']))
# database = database("../ControleFinanceiro")
# database.connect_database()
# database.executarComand("""
# INSERT INTO Categoria (nome) values ('Compra')
# """)
# database.close_connection_database()
