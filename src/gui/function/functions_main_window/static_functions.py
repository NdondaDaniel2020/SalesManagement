import os
import json
import socket
import random
import webbrowser
import urllib.request

from src.qt_core import QBarSet, QColor

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, TableStyle

from src.gui.core.database import DataBase
from src.gui.core.absolute_path import AbsolutePath


meses_do_ano = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}
cores_contraste_do_grafico = ['#A9A9A9', '#FFDAB9', '#FFEFD5', '#696969',
                              '#F0F0F0', '#FAEBD7', '#B0C4DE', '#FAFAFA',
                              '#FFF5EE', '#F0F8FF', '#ADD8E6', '#FFE4C4',
                              '#F5FFFA', '#00BFFF', '#B0E0E6', '#FFFFF0',
                              '#FFEBCD', '#FAFAD2', '#FFFAFA', '#FFE4B5',
                              '#D3D3D3', '#FFF8DC', '#E6E6FA', '#808080',
                              '#FFFFE0', '#F5F5F5', '#FFDEAD', '#FFFFFF',
                              '#FFFACD', '#F5F5DC', '#708090', '#FFF0F5',
                              '#FFE4E1', '#C0C0C0', '#FAF0E6', '#F0FFF0',
                              '#87CEFA', '#778899', '#87CEEB', '#F0FFFF']



def converter_data_para_ano_mes_dia(data) -> str:
    data = data.split('/')
    data.reverse()
    return '-'.join(data)


def converter_data_para_dia_mes_ano(data_completa) -> str:
    """
    tratar data no formato portugues
    :param data_completa: 
    :return: 
    """
    data_completa = str(data_completa)
    data_completa = data_completa.split(' ')
    data = data_completa[0]
    data = data.split('-')
    data.reverse()
    return '/'.join(data)+' ' + data_completa[1]


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


def verificar_acessibilidade_de_pagina_camera(url):
    try:
        urllib.request.urlopen(url)
    except Exception as _:
        return False
    else:
        return True


def mesclar_dados_de_venda(dados_fvenda: dict, produtos_vendidos: dict,
                           data_atual: str,
                           email: str,
                           nome_empresa: str,
                           usuario: str) -> dict:

    dados_estaticos = {'empresa': nome_empresa, 'email': email, 'data': data_atual, 'usuario': usuario}
    dados_da_venda = dados_fvenda | produtos_vendidos | dados_estaticos

    return dados_da_venda


def gerar_recibo(dados: dict) -> None:
    # Calcula a altura da página com base na quantidade de produtos
    page_height = 28 * (len(dados['nome']) + 8)  # Estimativa da altura da página

    # Cria o arquivo PDF
    json_file = AbsolutePath().getPathSetting()
    with open(json_file, 'r') as file:
        folder = json.load(file)

    pdf_filename = f"/recibo de venda {dados['data'].replace('/', '-').replace(':', '-')}.pdf"
    file_path = folder['registration_panel']['image_path'] + pdf_filename
    pdf_filename = os.path.normpath(file_path)

    c = canvas.Canvas(pdf_filename, pagesize=(220, page_height))

    c.setFont('Helvetica-Bold', 15)
    c.drawString(50, page_height - 40, f"Recibo de venda")

    c.setFont('Helvetica', 10)
    c.drawString(86, page_height - 63, f"{dados['empresa']}")
    c.drawString(58, page_height - 76, f"{dados['email']}")

    c.line(10, page_height - 90, 210, page_height - 90)

    # Adiciona os detalhes do cabeçalho
    c.setFont('Helvetica', 10)
    c.drawString(10, page_height - 148, f"Método de Pagamento: {dados['metodo_de_pagamento'].capitalize()}")
    c.drawString(10, page_height - 134, f"Data: {dados['data']}")
    c.drawString(10, page_height - 121, f"Cliente: {dados['cliente'].capitalize()}")
    c.drawString(10, page_height - 108, f"Status: {dados['status']}")

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
    for i in range(len(dados['nome'])):
        y -= 14
        c.drawString(10, y, dados['nome'][i].capitalize())
        c.drawString(20 + (width_font * 2), y, f"{dados['preco'][i]:,.2f}".replace(',', '.'))
        c.drawString(30 + (width_font * 4), y, str(dados['quantidade'][i]))
        c.drawString(40 + (width_font * 5), y, f"{dados['subtotal'][i]:,.2f}".replace(',', '.'))


    c.line(10, y - 14, 210, y - 14)
    # c.line(10, y - 13, 210, y - 13)

    # # Adiciona o total da venda
    c.setFont('Helvetica', 9.8)
    c.drawString(10, y - 30, f"Total: {sum(dados['subtotal']):,.2f} Kz".replace(',', '.'))

    c.line(10, y - 50, 210, y - 50)

    # Salva o PDF
    c.save()

    # webbrowser.open(pdf_filename)


def enviar_dados_de_venda_na_base_de_dados(dados_da_venda: dict) -> None:
    db = DataBase(AbsolutePath().getPathDatabase())
    db.connectDataBase()

    id_m_d_p = db.executarFetchone(f"""SELECT id FROM metodo_de_pagamento
                                        WHERE nome='{dados_da_venda['metodo_de_pagamento']}'""")
    id_cliente = db.executarFetchone(f"""SELECT id FROM cliente WHERE nome='{dados_da_venda['cliente']}'""")
    id_usuario = db.executarFetchone(f"""SELECT id FROM usuario WHERE nome='{dados_da_venda['usuario']}'""")

    db.executarComand(f"""INSERT INTO venda(data, total, troco, usuario, metodo_de_pagamento, cliente)
                        VALUES ('{dados_da_venda['data']}', {sum(dados_da_venda['subtotal'])},
                                 {convert_str_in_float(dados_da_venda['troco'])}, {id_usuario[0]},
                                 {id_m_d_p[0]}, {id_cliente[0] if id_cliente else 'Null'})""")

    db.disconnectDataBase()

    precos = dados_da_venda.get('preco')
    chaves = dados_da_venda.get('chave')
    descontos = dados_da_venda.get('desconto')
    quantidades = dados_da_venda.get('quantidade')

    for chave, quantidade, desconto, preco in zip(chaves, quantidades, descontos, precos):
        db.connectDataBase()
        id_venda = db.executarFetchone("SELECT id FROM venda ORDER BY id DESC LIMIT 1")
        id_produto = db.executarFetchone(f"SELECT id FROM produto WHERE chave='{chave}'")
        db.executarComand(f"""INSERT INTO itens_vendido(id_venda, id_produto, quantidade, desconto, preco)
                              VALUES ({id_venda[0]}, {id_produto[0]}, {quantidade}, {desconto}, {preco})""")
        db.disconnectDataBase()

    if dados_da_venda['recibo']:
        dados_da_venda['status'] = 'Pago'
        gerar_recibo(dados_da_venda)


def criar_pedido_de_compra(data: str, items: dict, total: float) -> None:

    json_file = AbsolutePath().getPathSetting()
    with open(json_file, 'r') as file:
        folder = json.load(file)

    nome_do_arquivo = f"/pedido de compra {data.replace('/', '-').replace(':', '-')}.pdf"
    file_path = folder['registration_panel']['image_path'] + nome_do_arquivo
    nome_do_arquivo = os.path.normpath(file_path)

    def create_receipt_header(corpo_local, data_do_arquivo):
        corpo_local.setFont("Helvetica-Bold", 14)
        corpo_local.drawString(30, 730, "PEDIDO DE COMPRA")
        corpo_local.setFont("Helvetica", 12)
        corpo_local.drawString(30, 700, f"Data: {data_do_arquivo}")

    # Função para criar a tabela de itens vendidos
    def create_item_table(c, items_da_tabela: dict):
        # Define os dados da tabela
        dados = [["Nome", "Preço", "Quantidade", "Subtotal"]]
        for nome, preco, quantidade, subtotal in zip(*items_da_tabela.values()):
            dados.append([nome, preco, quantidade, subtotal])

        # Cria a tabela de itens
        table = Table(dados, colWidths=[138, 138, 138, 138])

        # Define o estilo da tabela
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.transparent),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.transparent),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])
        table.setStyle(style)

        # Adiciona a tabela ao canvas
        table.wrapOn(c, 400, 200)
        table.drawOn(c, 30, 590 - (17 * len(items_da_tabela['nome'])))

    # Função para criar a tabela do total
    def create_total_table(c, total_de_produto, tamanho_itens):
        # Define os dados da tabela do total
        dados = [["Total", f"Kz {total_de_produto}"]]

        # Cria a tabela do total
        table = Table(dados, colWidths=[276, 276], rowHeights=17)

        # Define o estilo da tabela do total
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.transparent),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 3),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])
        table.setStyle(style)

        # Adiciona a tabela do total ao canvas
        table.wrapOn(c, 400, 200)
        table.drawOn(c, 30, (560 - (17 * tamanho_itens + 1)))  # 455

    # criar o recibo de venda
    corpo = canvas.Canvas(nome_do_arquivo, pagesize=letter)
    create_receipt_header(corpo, data)
    create_item_table(corpo, items)
    create_total_table(corpo, total, len(items))
    corpo.save()

    # webbrowser.open(nome_do_arquivo)


def get_dados_do_relatorio_categoria_char() -> dict:
    global cores_contraste_do_grafico
    db = DataBase(AbsolutePath().getPathDatabase())

    db.connectDataBase()
    query_categoria = db.executarFetchall(f"SELECT DISTINCT categoria FROM vw_historico_de_venda")
    valor_total_dos_meses = max(
        db.executarFetchall("SELECT count(categoria) AS quantidade FROM vw_historico_de_venda GROUP by categoria"))

    lista_de_bar_series = {}
    lista_de_dados = {}
    for item_categoria, cor in zip(query_categoria, cores_contraste_do_grafico):
        lista_de_dados[item_categoria[0]] = []
        bar = QBarSet(item_categoria[0])
        bar.setColor(QColor(cor))
        bar.setLabelColor(QColor(255, 255, 255))
        lista_de_bar_series[item_categoria[0]] = bar
    db.disconnectDataBase()

    for i in range(1, 13):
        db.connectDataBase()
        query = db.executarFetchall(f"""SELECT categoria, count(categoria) AS quantidade FROM vw_historico_de_venda
                                            WHERE data like '%-{i:02}-%' GROUP by categoria""")
        categorias = db.executarFetchall(f"SELECT DISTINCT categoria FROM vw_historico_de_venda")
        if query:
            for item in query:
                lista_de_dados[item[0]].append(item[1])

            for categoria in categorias:
                if not categoria[0] in str(query):
                    lista_de_dados[categoria[0]].append(0)
        else:
            for key in lista_de_dados.keys():
                lista_de_dados[key].append(0)

        db.disconnectDataBase()

    for key in lista_de_bar_series.keys():
        lista_de_bar_series[key].append(lista_de_dados[key])

    return lista_de_bar_series, valor_total_dos_meses[0]



if __name__ == '__main__':
    get_dados_do_relatorio_categoria_char()
