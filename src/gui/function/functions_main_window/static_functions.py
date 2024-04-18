import os
import json
import socket
import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from src.gui.core.database import DataBase
from src.gui.core.absolute_path import AbsolutePath


def convert_str_in_float(value: str) -> float:
    if ' ' in value:
        value = value.split(' ')[-1]

    value = value.split('.')
    value.insert(-1, '.')
    value = float(''.join(value))

    return value


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

    if produto.get('size_image'):
        json_file = AbsolutePath().getPathSettingSize()

        with open(json_file, 'r') as file:
            dados = json.load(file)

        if not produto['nome'] in dados:
            nome = produto.get('nome').lower()
            dados[nome] = produto.get('size_image')

            with open(json_file, "w") as file:
                json.dump(dados, file)


def insertProductDataIntoTheDatabase(produto: dict):
    insert = fr"""INSERT INTO produto (chave, nome, preco_venda, preco_compra, quantidade, unidade, categoria,linkImg,
                                        informacoes_adicionais)
                        VALUES ('{produto['chave']}', '{produto['nome'].lower().strip()}', {produto['preco_venda']},
                                 {produto['preco_compra']}, {produto['quantidade']}, {produto['unidade']},
                                 {produto['categoria']},'{produto['linkImg']}' , '{produto['informacoes_adicionais']}')
               """

    db = DataBase(AbsolutePath().getPathDatabase())
    db.connectDataBase()
    db.executarComand(insert)

    if produto['data_de_expiracao']:
        id_produto = db.executarFetchone("SELECT id FROM produto ORDER By id DESC LIMIT 1")
        for dado in produto['data_de_expiracao']:
            insert_data_expiracao = fr"""INSERT INTO data_de_expiracao(data, id_produto, informacoes_de_expiracao)
                                                              VALUES ('{dado[0]}', {id_produto[0]}, '{dado[1]}')"""
            db.executarComand(insert_data_expiracao)

    db.disconnectDataBase()


def verificar_acessibilidade_de_ip(e_ip: str, porta_ip: int) -> bool:
    # Cria um objeto socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Define um timeout para a conexão (em segundos)
        s.settimeout(0)
        # Tenta conectar ao IP na porta específica
        s.connect((e_ip, porta_ip))
        return True
    except Exception as _:
        return False
    finally:
        # Fecha a conexão
        s.close()



def gerar_recibo(data):
    # Calcula a altura da página com base na quantidade de produtos
    page_height = 28 * (len(data['nome']) + 8)  # Estimativa da altura da página

    # Cria o arquivo PDF
    pdf_filename = "recibo_venda.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=(220, page_height))

    c.setFont('Helvetica-Bold', 15)
    c.drawString(50, page_height - 40, f"Recibo de venda")

    c.setFont('Helvetica', 10)
    c.drawString(86, page_height - 63, f"{data['empresa']}")
    c.drawString(58, page_height - 76, f"{data['email']}")

    c.line(10, page_height - 90, 210, page_height - 90)

    # Adiciona os detalhes do cabeçalho
    c.setFont('Helvetica', 10)
    c.drawString(10, page_height - 148, f"Método de Pagamento: {data['metodo_de_pagamento'].capitalize()}")
    c.drawString(10, page_height - 134, f"Data: {data['data']}")
    c.drawString(10, page_height - 121, f"Cliente: {data['cliente'].capitalize()}")
    c.drawString(10, page_height - 108, f"Status: {data['status'].capitalize()}")

    c.line(10, page_height - 170, 210, page_height - 170)
    c.line(10, page_height - 169, 210, page_height - 169)

    # # Adiciona a tabela de itens vendidos
    width_font = c.stringWidth("Nome")
    c.drawString(10, page_height - 190, "Nome")
    c.drawString(20 + (width_font * 2), page_height - 190, "Preço")
    c.drawString(5 + (width_font * 4), page_height - 190, "Quantidade")
    c.drawString(40 + (width_font * 5), page_height - 190, "Subtotal")

    c.line(10, page_height - 200, 210, page_height - 200)
    c.line(10, page_height - 199, 210, page_height - 199)

    c.setFont('Helvetica', 8.8)
    y = page_height - 203
    for i in range(len(data['nome'])):
        y -= 14
        c.drawString(10, y, data['nome'][i].capitalize())
        c.drawString(20 + (width_font * 2), y, f"{data['preco'][i]:,.2f}".replace(',', '.'))
        c.drawString(30 + (width_font * 4), y, str(data['quantidade'][i]))
        c.drawString(40 + (width_font * 5), y, f"{data['subtotal'][i]:,.2f}".replace(',', '.'))


    c.line(10, y - 14, 210, y - 14)
    # c.line(10, y - 13, 210, y - 13)

    # # Adiciona o total da venda
    c.setFont('Helvetica', 9.8)
    c.drawString(10, y - 30, f"Total: {data['total']:,.2f} Kz".replace(',', '.'))

    c.line(10, y - 50, 210, y - 50)

    # c.drawImage('some_qr.PNG', 70, y - 160, 90, 90)

    # Salva o PDF
    c.save()




if __name__ == '__main__':
    # produto = {'linkImg': 'C:\\Users\\Daniel\\Downloads\\barra_de_cera.png', 'size_image': {'image': (260, 260),
    # 'icon_image': (30, 30)}, 'data_de_expiracao': [], 'unidade': 4, 'categoria': 2, 'nome_produto': 'barra de cera',
    # 'preco_venda': 12000, 'chave': '8978885538803', 'quantidade': 12, 'informacoes_adicionais': '',
    # 'data_de_expiracao': [('12/02/2025', 'primeira data de exipracao da barra de cera'),
    # ('12/02/2026', 'segunda data de exipracao da barra de cera')]}
    ...
    # Exemplo de uso
    # ip = '192.168.0.120'
    # porta = 8080
    # print(verificar_acessibilidade_de_ip(ip, porta))
    ...
dados_recibo = {
    'nome': ['Barra de cera', 'Mousse', 'area'],
    'preco': [12000.0, 15000.0, 200.0],
    'quantidade': [2, 4, 1],
    'subtotal': [24000.0, 30000.0, 200],
    'desconto': [0.0, 0.0],
    'data': '27/04/2024',
    'total': 54200.0,
    'metodo_de_pagamento': 'em dinheiro',
    'status': 'pago',
    'cliente': 'Mauro',
    'empresa': 'MissXtrela',
    'email': 'missxtrela@gmail.com'
}