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
    db: DataBase = DataBase(AbsolutePath().getPathDatabase())
    db.connectDataBase()
    query = db.executarFetchall(f"SELECT DISTINCT * FROM vw_historico_de_venda")
    db.disconnectDataBase()

# database = database("../ControleFinanceiro")
# database.connect_database()
# database.executarComand("""
# INSERT INTO Categoria (nome) values ('Compra')
# """)
# database.close_connection_database()
