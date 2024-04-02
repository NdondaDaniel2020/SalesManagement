import os
import json
import random
from src.gui.core.database import DataBase
from src.gui.core.absolute_path import AbsolutePath


def generate_barcode() -> str:
    codigo: str = ""

    db = DataBase(AbsolutePath().getPathDatabase())
    db.connectDataBase()
    query = db.executarFetchall("SELECT chave FROM produto")
    db.disconnectDataBase()

    while True:
        for _ in range(13):
            codigo += str(random.randint(0, 9))

        if not codigo in query:
            return codigo
        else:
            codigo = ''


def reduce_url(url: str) -> str:
    if len(url) > 24:
        url = os.path.normpath(url).split('\\')
        url = (*url[:4], '....', url[-1])
        url = '\\'.join(url)

        return url

    return url


def saveImageSettingInSizeSetting(produto: dict):
    json_file = AbsolutePath().getPathSettingSize()
    dados: dict = {}

    with open(json_file, 'r') as file:
        dados = json.load(file)

    if not produto['nome_produto'] in dados:
        nome = produto['nome_produto'].lower()
        dados[nome] = produto['size_image']

        with open(json_file, "w") as file:
            json.dump(dados, file)


def insertProductDataIntoTheDatabase(produto: dict):
    insert_produto = fr"""INSERT INTO produto (chave, nome, preco_venda, quantidade, unidade, categoria,linkImg,
                                        informacoes_adicionais)
                                VALUES ('{produto['chave']}', '{produto['nome_produto'].lower().strip()}', {produto['preco_venda']},
                                        {produto['quantidade']}, {produto['unidade']}, {produto['categoria']},
                                        '{produto['linkImg']}' , '{produto['informacoes_adicionais']}')
               """

    db = DataBase(AbsolutePath().getPathDatabase())
    db.connectDataBase()
    db.executarComand(insert_produto)

    if produto['data_de_expiracao']:
        id_produto = db.executarFetchone("SELECT id FROM produto ORDER By id DESC LIMIT 1")
        for dado in produto['data_de_expiracao']:
            insert_data_expiracao = fr"""INSERT INTO data_de_expiracao(data, id_produto, informacoes_de_expiracao)
                                                              VALUES ('{dado[0]}', {id_produto[0]}, '{dado[1]}')"""
            db.executarComand(insert_data_expiracao)

    db.disconnectDataBase()



if __name__ == '__main__':
    # produto = {'linkImg': 'C:\\Users\\Daniel\\Downloads\\barra_de_cera.png', 'size_image': {'image': (260, 260), 'icon_image': (30, 30)}, 'data_de_expiracao': [], 'unidade': 4, 'categoria': 2, 'nome_produto': 'barra de cera', 'preco_venda': 12000, 'chave': '8978885538803', 'quantidade': 12, 'informacoes_adicionais': '', 'data_de_expiracao': [('12/02/2025', 'primeira data de exipracao da barra de cera'), ('12/02/2026', 'segunda data de exipracao da barra de cera')]}
    ...

