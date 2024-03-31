import sqlite3
from src.gui.core.absolute_path import AbsolutePath

class DataBase():
    def __init__(self, name: str='banco') -> None:
        if '.db' in name:
            self.name = name
        else:
            self.name = name+'.db'

    def connectDataBase(self) -> None:
        self.connection = sqlite3.connect(self.name)

    def disconnectDataBase(self) -> None:
        try:
            self.connection.commit() ## commit salva os dados no banco
            self.connection.close()
        except:
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
    db = DataBase(AbsolutePath().getPathDatabase())
    db.connectDataBase()
    query = db.executarFetchall("SELECT chave, nome, quantidade, preco_venda, linkImg from produto")
    db.disconnectDataBase()

# data.executarComand("""
# CREATE TABLE IF NOT EXISTS Usuario(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    nome varchar(20) NOT NULL UNIQUE,
#    password varchar(50) NOT NULL,
#    admin TEXT CHECK( admin IN ('T','F')) DEFAULT 'F' NOT NULL
# );""")
# data.executarComand("""
# INSERT INTO Usuario (nome, password, admin) values ('Nd Daniel','123456', 'T'), ('Daniel','1234', 'F'),
# ('Ndonda Daniel','1234567', 'F')
# """)
# user = data.executarFetchall(f"SELECT * FROM Usuario")
# CREATE TABLE IF NOT EXISTS UltimoUsuario(
# idUltimo integer PRIMARY KEY AUTOINCREMENT,
# Data dete NOT NULL,
# UltimoUsuario integer,
# CONSTRAINT UsuUlus FOREIGN KEY (UltimoUsuario) REFERENCES Usuario (id)
# )
# INSERT INTO UltimoUsuario (Data, UltimoUsuario)values('2022-10-22','6')
# INSERT INTO Categoria (nome) values ('Compra')
#
# database = database("../ControleFinanceiro")
# database.connect_database()
# database.executarComand("""
# INSERT INTO Categoria (nome) values ('Compra')
# """)
# database.close_connection_database()
# database = database("../ControloFinaceiro.db")
# database.connect_database()
# database.executarComand("""
# INSERT INTO Fornecedor (nome, telefone, email, cidade, categoria)
# values
# ('Luciano Luzembo', '923442065', 'lucianoluzembo@gmail.com', 'Lunada', '1')
# """)
# database.close_connection_database()

#  select * from relacionamento_de_compra rc
#  join cliente cl on rc.id_relacionamento_cliente = cl.id_cliente
#  join curso cu on  rc.id_relacionamento_livro = cu.id_curso
#  join equipamento eq on rc.id_relacionamento_equipamento = eq.id_equipamento
#  join servico sv on rc.id_relacionamento_servico = sv.id_servico
#  join ebook eb on rc.id_relacionamento_livro = eb.id_livro;

# UPDATE ReceberConta SET valorPago = '0' WHERE id ='2';

# /* ReceberConta.id, ReceberConta.dataEmissao, categoria.nome, Cliente.nome,
# ReceberConta.dataVencimento, ReceberConta.valorPago, Status.nome*/

# /*SELECT ReceberConta.id FROM ReceberConta rc  JOIN Categoria c ON rc.categoria = c.id
# JOIN cliente cl ON rc.cliente = cl.id JOIN status st ON rc.status = st.id;

#  rc.id, rc.dataEmissao, c.nome, cl.nome, rc.dataVencimento, rc.valorPago, st.nome

# SELECT rc.id, rc.dataEmissao, c.nome, rc.dataVencimento, rc.valorPago, st.nome
# FROM ReceberConta rc
# JOIN Categoria c ON rc.categoria = c.id
# JOIN cliente cl ON rc.cliente = cl.id
# JOIN Status st ON rc.status = st.id;

# SELECT * FROM ReceberConta rc  JOIN Categoria c ON rc.categoria = c.id JOIN cliente cl ON rc.cliente = cl.id JOIN status st ON rc.status = st.id;
# select data, sum(valor), tranzacao from MovimentacaoFinanceira WHERE tranzacao = 'saida' GROUP by data;
