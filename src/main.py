# PACOTES NATIVOS
# NATIVE PACKAGES
import os
import sys
import json
import pathlib
import winsound

# INSTALLED PACKAGES
# PACOTES INSTALADOS
import cv2
from src.qt_core import *
from pyzbar.pyzbar import decode

# CUSTOM WIDGETS
# WIDGETS PERSONALIZADOS

from src.gui.widgets.py_grips.py_grips import PyGrips
from src.gui.widgets.py_menu.py_menu import PySaleMenu
from src.gui.widgets.py_left_menu.py_left_menu import LeftMenu
from src.gui.widgets.py_push_button.py_push_button import PyPushButton
from src.gui.widgets.py_sales_finisher.py_sales_finisher import PySalesFinisher
from src.gui.widgets.py_registration_list.py_registration_list import PyRegistrationList
from src.gui.widgets.py_product_registration.py_product_registration import PyProductRegistration
from src.gui.widgets.py_sale_registration_list.py_sale_registration_list import PySaleRegistrationList
from src.gui.widgets.py_painel_de_produtos_a_venda.py_painel_de_produtos_a_venda import PyProductSelectionPanel

# MAIN INTERFACE CODE
# CÓDIGO PRINCIPAL DA INTERFACE
from src.gui.ui.windows.main_window.ui_main_window import Ui_MainWindow
from src.gui.function.functions_main_window.functions_system import FunctionsSystem

# INTERFACE AUXILIARY CODE
# CÓDIGO AUXILIAR DA INTERFACE
from src.gui.ui.windows.main_window.setup_main_window import *
from src.gui.function.functions_main_window.functions_chart import ChartFunctions

# AUXILIARY CODE
# CÓDIGO AUXILIAR
from src.gui.core.database import DataBase
from src.gui.core.absolute_path import AbsolutePath
from src.gui.function.functions_main_window.static_functions import (saveImageSettingInSizeSetting,
                                                                     insertProductDataIntoTheDatabase,
                                                                     convert_str_in_float)

try:
    from ctypes import windll  # Only exists on Windows.

    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # /////////////////////////////////////////////////////////////////////////
        self.setWindowIcon(QIcon(AbsolutePath().getPathImage('icon_resimido.png')))

        self.setWindowTitle("Sales Management MX")
        self.setBaseSize(QSize(724, 621))

        # ////////////////////////////////////////////////////////////////////////
        self.set_title_bar = False
        self.menu_opcoes_de_venda: PySaleMenu = None
        self.registration_panel: PyProductRegistration = None
        self.painel_de_produto: PyProductSelectionPanel = None
        self.combo_box_sugestao_de_busca: QComboBox = None
        self.painel_sale_finisher: PySalesFinisher = None
        self.usuario = 'NdDaniel'  # adicionar apartir da tela de login

        # adicionar nas configuracoes do despositivo que sera usado para as leiruras
        # quando se mudar tambem tem que mudar no painel de cadastro de produto
        # 'http://192.168.43.1:8080/video'
        # "http://192.168.0.120:8080/video
        # "http://192.168.42.129:8080/video
        # self.cap = cv2.VideoCapture('http://192.168.43.1:8080/video')  # nas configuracoes escolher scanner
        self.cap = None
        self.timer_scan_bar_code = QTimer()
        self.timer_scan_bar_code.timeout.connect(self.scanBarCodeCam)
        self.timer_scan_bar_code.setInterval(1000)

        self.timer_show_scan_bar_code = QTimer()
        self.timer_show_scan_bar_code.timeout.connect(self.showScanBarCodeCam)  # adicionar no painel de configuacoes

        # self.lbl_camera = QLabel(self.ui.page_venda)  # adicionar no painel de configuacoes
        # self.lbl_camera.setGeometry(9, 9, 640, 179)

        # /////////////////////////////////////////////////////////////
        SetUpMainWindow.configIconPath(self)
        SetUpMainWindow.addControlWindow(self)
        SetUpMainWindow.configTableWidget(self)
        SetUpMainWindow.configSystem(self)

        # /////////////////////////////////////////////////////////////
        ChartFunctions.addInventoryChart(self)
        ChartFunctions.addHistoricBar(self)
        ChartFunctions.updatCircularProgress(self)
        ChartFunctions.addBarChartOnHomepage(self)
        ChartFunctions.connecoesHistoricoDeVenda(self)
        self.timer_dynamic_chart = ChartFunctions.addDynamicLineChart(self)
        # self.timer_dynamic_chart tem que ativar sempre que entrar nas na home
        # se o dinamic estiver ativo nas comfiguracoes

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.ui.frame_inventario.mousePressEvent = lambda e: self.ui.stacked_widget.setCurrentWidget(
            self.ui.page_inventario)
        self.ui.frame_venda.mousePressEvent = lambda e: self.ui.stacked_widget.setCurrentWidget(self.ui.page_venda)
        self.ui.frame_historico_de_venda.mousePressEvent = lambda e: self.ui.stacked_widget.setCurrentWidget(
            self.ui.page_historico_venda)

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # todas as iniciolizacoes tem que passa na tela de login
        self._iniLeftMenu_()
        self.initRegistrationPanel()
        self.insercaoAutomaticaDeProduto()

        # //////////////////////////////////////////////////////////////////////////////////
        self._connectingPages_()

        # //////////////////////////////// LEFT MENU //////////////////////////////////////
        self.btn_info_base.clicked.connect(lambda: FunctionsSystem.resizeLeftColumn(self))
        self.btn_info_float.clicked.connect(lambda: FunctionsSystem.resizeLeftColumn(self))

        self.btn_info_base.clicked.connect(self.left_menu.activeBtbInfo)
        self.btn_info_float.clicked.connect(self.left_menu.activeBtbInfo)

        self.ui.btn_pesquisa_produto.clicked.connect(lambda: FunctionsSystem.searchProduct(self))
        self.ui.line_edit_pesquisa_produto.returnPressed.connect(lambda: FunctionsSystem.searchProduct(self))

        self.ui.line_edit_pesquisa_produto_devenda.returnPressed.connect(self.irerirProdutosPelaChave)

        # ///////////////////////////////////////////// INVENTORY ///////////////////////////////////////////
        self.ui.btn_adicionar_produto.clicked.connect(lambda: self.showPainelDeRegistroDeProduto())
        self.ui.frame_criar_produto.mousePressEvent = lambda e: self.showPainelDeRegistroDeProduto()

        self.ui.btn_mais_opcoes_de_venda.clicked.connect(self.showMenuOpcoes)

    # falha na arquitetura
    def _activeBtbInfo_(self):
        # ////////////////////////////////////////////////////////////////////////////////
        if not self.btn_info_base.is_active:
            self.btn_info_base.set_style(is_active=True, btn_radius=8, text_padding=6)
            self.btn_info_float.set_style(is_active=True, btn_radius=8, text_padding=6)
        # ////////////////////////////////////////////////////////////////////////////////
        else:
            self.btn_info_base.set_style(is_active=False, btn_radius=8, text_padding=6)
            self.btn_info_float.set_style(is_active=False, btn_radius=8, text_padding=6)

    # falha na arquitetura
    def _iniLeftMenu_(self):

        # ADD LEFT MENU
        # ////////////////////////////////////////////////////////////////////////////////
        self.left_menu = LeftMenu(self.ui.frame_left_menu, self.ui.central_widget,
                                  self.geometry().height(), self.set_title_bar)

        # ADJUST BTN's
        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_back_base = self.left_menu.left_menu_base.btn_back
        self.btn_back_float = self.left_menu.left_menu_float.btn_back

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_home_base = self.left_menu.left_menu_base.btn_home
        self.btn_home_float = self.left_menu.left_menu_float.btn_home

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_compra_base = self.left_menu.left_menu_base.btn_compra
        self.btn_compra_float = self.left_menu.left_menu_float.btn_compra

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_venda_base = self.left_menu.left_menu_base.btn_venda
        self.btn_venda_float = self.left_menu.left_menu_float.btn_venda

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_inventario_base = self.left_menu.left_menu_base.btn_inventario
        self.btn_inventario_float = self.left_menu.left_menu_float.btn_inventario

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_relatorio_base = self.left_menu.left_menu_base.btn_relatorio
        self.btn_relatorio_float = self.left_menu.left_menu_float.btn_relatorio

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_service_base = self.left_menu.left_menu_base.btn_service
        self.btn_service_float = self.left_menu.left_menu_float.btn_service

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_fornecedor_base = self.left_menu.left_menu_base.btn_fornecedor
        self.btn_fornecedor_float = self.left_menu.left_menu_float.btn_fornecedor

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_cliente_base = self.left_menu.left_menu_base.btn_cliente
        self.btn_cliente_float = self.left_menu.left_menu_float.btn_cliente

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_agenda_base = self.left_menu.left_menu_base.btn_agenda
        self.btn_agenda_float = self.left_menu.left_menu_float.btn_agenda

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_copia_seguranca_base = self.left_menu.left_menu_base.btn_copia_seguranca
        self.btn_copia_seguranca_float = self.left_menu.left_menu_float.btn_copia_seguranca

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_recibo_base = self.left_menu.left_menu_base.btn_recibo
        self.btn_recibo_float = self.left_menu.left_menu_float.btn_recibo

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_setting_base = self.left_menu.left_menu_base.btn_setting
        self.btn_setting_float = self.left_menu.left_menu_float.btn_setting

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_info_base = self.left_menu.left_menu_base.btn_info
        self.btn_info_float = self.left_menu.left_menu_float.btn_info

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_user_base = self.left_menu.left_menu_base.btn_user
        self.btn_user_float = self.left_menu.left_menu_float.btn_user

    def _connectingPages_(self):

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_home_base.clicked.connect(self.changePage)
        self.btn_home_float.clicked.connect(self.changePage)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_compra_base.clicked.connect(self.changePage)
        self.btn_compra_float.clicked.connect(self.changePage)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_venda_base.clicked.connect(self.changePage)
        self.btn_venda_float.clicked.connect(self.changePage)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_inventario_base.clicked.connect(self.changePage)
        self.btn_inventario_float.clicked.connect(self.changePage)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_relatorio_base.clicked.connect(self.changePage)
        self.btn_relatorio_float.clicked.connect(self.changePage)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_service_base.clicked.connect(self.changePage)
        self.btn_service_float.clicked.connect(self.changePage)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_fornecedor_base.clicked.connect(self.changePage)
        self.btn_fornecedor_float.clicked.connect(self.changePage)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_cliente_base.clicked.connect(self.changePage)
        self.btn_cliente_float.clicked.connect(self.changePage)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_agenda_base.clicked.connect(self.changePage)
        self.btn_agenda_float.clicked.connect(self.changePage)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_copia_seguranca_base.clicked.connect(self.changePage)
        self.btn_copia_seguranca_float.clicked.connect(self.changePage)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_recibo_base.clicked.connect(self.changePage)
        self.btn_recibo_float.clicked.connect(self.changePage)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_setting_base.clicked.connect(self.changePage)
        self.btn_setting_float.clicked.connect(self.changePage)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_info_base.clicked.connect(self.changePage)
        self.btn_info_float.clicked.connect(self.changePage)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_user_base.clicked.connect(self.changePage)
        self.btn_user_float.clicked.connect(self.changePage)

    def changePage(self) -> None:
        name_btn = self.sender().objectName()

        if name_btn == 'btn_home':
            self.ui.stacked_widget.setCurrentWidget(self.ui.page_home)
            self.timer_dynamic_chart.start()

        elif name_btn == 'btn_inventario':
            self.ui.stacked_widget.setCurrentWidget(self.ui.page_inventario)
            self.timer_dynamic_chart.stop()

        elif name_btn == 'btn_venda':
            self.ui.stacked_widget.setCurrentWidget(self.ui.page_venda)
            self.timer_dynamic_chart.stop()
            self.ui.line_edit_pesquisa_produto_devenda.setFocus()

    ############################################## inventario ##############################################

    def initRegistrationPanel(self):
        self.registration_panel = PyProductRegistration(self.ui.central_widget)
        # self.registration_panel.countAvailableCameras()  # por nas configuracoes
        self.registration_panel.close()

    @Slot(None)
    def showPainelDeRegistroDeProduto(self) -> None:
        """
        ESTE MÉTODO É REPONSAVEL POR CENTRALIZAR MOSTRAR E AJUSTAR O PAINEL DE REGISTRO
        :return:
        """
        self.registration_panel.btn_ok.clicked.connect(self.cadastrarProduto)
        self.registration_panel.setGeometry(0, 0, self.width(), self.height())

        self.registration_panel.move((self.width() - self.registration_panel.width()) / 2,
                                     (self.height() - self.registration_panel.height()) / 2)
        self.registration_panel.show()

    def insercaoAutomaticaDeProduto(self):
        db = DataBase(AbsolutePath().getPathDatabase())
        db.connectDataBase()
        query = db.executarFetchall("SELECT chave, nome, quantidade, preco_venda, linkImg from produto")
        db.disconnectDataBase()

        json_file = AbsolutePath().getPathSettingSize()

        for dados in query:
            list_produto = PyRegistrationList()
            list_produto.setImage(dados[4])
            list_produto.setChave(dados[0][:4])
            list_produto.setQuantidade(dados[2])
            list_produto.setValorDeVenda(dados[3], True)
            list_produto.setName(dados[1].capitalize())

            with open(json_file, 'r') as file:
                dado = json.load(file)
                list_produto.setImageSize(*dado[dados[1]]["icon_image"])

            self.ui.vertical_layout_registro.insertWidget(0, list_produto)

    def cadastrarProduto(self):
        produto = self.registration_panel.getAllData()

        if produto:
            list_produto = PyRegistrationList()
            list_produto.setImage(produto['linkImg'])
            list_produto.setChave(produto['chave'][:4])
            list_produto.setQuantidade(produto['quantidade'])
            list_produto.setValorDeVenda(int(produto['preco_venda']))
            list_produto.setName(produto['nome_produto'].capitalize())
            list_produto.setImageSize(*produto['size_image']['icon_image'])

            self.ui.vertical_layout_registro.insertWidget(0, list_produto)
            self.registration_panel.cleanAndClose()
            self.registration_panel.close()

            saveImageSettingInSizeSetting(produto)
            insertProductDataIntoTheDatabase(produto)

            ChartFunctions.updateCircularProgress()

    ############################################## venda ##############################################

    def irerirProdutosPelaChave(self):

        chave = self.ui.line_edit_pesquisa_produto_devenda.text()

        if len(chave) >= 13 and chave.isnumeric():
            if len(chave) > 13 and chave.isnumeric():
                chave = chave[:13]
                self.ui.line_edit_pesquisa_produto_devenda.setText(chave)

            db = DataBase(AbsolutePath().getPathDatabase())
            db.connectDataBase()
            query = db.executarFetchall(f"""SELECT chave, nome, quantidade, preco_venda, linkImg 
                                                                                  FROM produto WHERE chave='{chave}'""")
            db.disconnectDataBase()

            json_file = AbsolutePath().getPathSettingSize()
            lista_de_produto_atuais = self.getSelectedProductsForSale()
            for dados in query:
                if not dados[1].capitalize() in lista_de_produto_atuais['nome']:
                    produto = PySaleRegistrationList()
                    produto.setImage(dados[4])
                    produto.setChave(dados[0])
                    produto.setQuantidade(dados[2])
                    produto.setPrecoDeVenda(dados[3])
                    produto.setName(dados[1].capitalize())
                    produto.let_quantidade.setText('1')

                    with open(json_file, 'r') as file:
                        dado = json.load(file)
                        produto.setImageSize(*dado[dados[1]]["icon_image"])

                    self.ui.vertical_layout_venda.insertWidget(0, produto)
                    self.ui.line_edit_pesquisa_produto_devenda.setText("")

                else:
                    produtos = self.ui.scroll_area_widget_contents_venda.findChildren(PySaleRegistrationList)
                    for produto in produtos:
                        if produto.chave_completa == chave:
                            quantidade = int(produto.let_quantidade.text()) + 1
                            produto.let_quantidade.setText(str(quantidade))
                            self.ui.line_edit_pesquisa_produto_devenda.setText("")

    Slot(None)
    def showMenuOpcoes(self):
        if not self.menu_opcoes_de_venda:
            self.menu_opcoes_de_venda = PySaleMenu(self.ui.page_venda)
            self.menu_opcoes_de_venda.move(self.size().width() - 272, 234)
            self.menu_opcoes_de_venda.show()

            self.menu_opcoes_de_venda.abrir_painel_de_produto.clicked.connect(self.showProductPainel)
            self.menu_opcoes_de_venda.limpar.clicked.connect(self.cleanProduct)

            def show_painel_sale_finished():
                self.showPanelSaleFinisher()
                self.menu_opcoes_de_venda.close()

            self.menu_opcoes_de_venda.finalizar.clicked.connect(show_painel_sale_finished)

            def start_timer():  # ajustar a opcao de abrir e fechar  o scaner da cemera
                self.timer_scan_bar_code.start()
                self.timer_show_scan_bar_code.start()
                self.menu_opcoes_de_venda.close()
                self.ui.line_edit_pesquisa_produto_devenda.setFocus()

            self.menu_opcoes_de_venda.scanner.clicked.connect(start_timer)

            def fechar_menu_de_opcoes(_):
                self.menu_opcoes_de_venda.close()
                self.ui.line_edit_pesquisa_produto_devenda.setFocus()

            self.ui.page_venda.mousePressEvent = fechar_menu_de_opcoes

            self.menu_opcoes_de_venda_opacity = QGraphicsOpacityEffect(self.menu_opcoes_de_venda)
            self.menu_opcoes_de_venda_opacity.setOpacity(0.0)
            self.menu_opcoes_de_venda.setGraphicsEffect(self.menu_opcoes_de_venda_opacity)

            self.AnimationMenuOpcoes()

        elif not self.menu_opcoes_de_venda.isVisible():
            self.menu_opcoes_de_venda.show()
            self.menu_venda_opacity_animation.start()

    def AnimationMenuOpcoes(self):

        self.menu_venda_opacity_animation = QPropertyAnimation(self.menu_opcoes_de_venda_opacity, b'opacity')
        self.menu_venda_opacity_animation.setStartValue(0.0)
        self.menu_venda_opacity_animation.setEndValue(0.9)
        self.menu_venda_opacity_animation.setDuration(400)
        self.menu_venda_opacity_animation.setEasingCurve(QEasingCurve.Type.InOutExpo)
        self.menu_venda_opacity_animation.start()

    def showProductPainel(self):
        self.menu_opcoes_de_venda.close()

        self.painel_de_produto = PyProductSelectionPanel(self.ui.central_widget)
        self.painel_de_produto.setGeometry(0, 0, self.width(), self.height())
        self.painel_de_produto.move((self.width() - self.registration_panel.width()) / 2,
                                    (self.height() - self.registration_panel.height()) / 2)

        self.painel_de_produto.btn_confirmar.clicked.connect(self.getProductsSelectedInThePanel)
        self.painel_de_produto.btn_deletar.clicked.connect(lambda:
                                                           self.ui.line_edit_pesquisa_produto_devenda.setFocus())

        self.painel_de_produto.show()

    def getSelectedProductsForSale(self):
        produtos_selecionados = {'chave': [], 'nome': [], 'quantidade': [], 'desconto': [], 'preco': [], 'subtotal': []}
        produtos = self.ui.scroll_area_widget_contents_venda.findChildren(PySaleRegistrationList)

        for produto in produtos:
            if int(produto.let_quantidade.text()) > 0:
                produtos_selecionados['chave'].append(produto.chave_completa)
                produtos_selecionados['nome'].append(produto.nome_produto.text())
                produtos_selecionados['quantidade'].append(int(produto.let_quantidade.text()))
                produtos_selecionados['desconto'].append(float(produto.let_desconto.text()))
                produtos_selecionados['preco'].append(produto.preco_contante)
                produtos_selecionados['subtotal'].append(convert_str_in_float(produto.lbl_subtotal_valor.text()))

        return produtos_selecionados

    def getProductsSelectedInThePanel(self):
        produtos = self.painel_de_produto.confirmProduct()
        json_file = AbsolutePath().getPathSettingSize()
        db = DataBase(AbsolutePath().getPathDatabase())
        lista_de_produto = []

        for produto in produtos:
            db.connectDataBase()
            query = db.executarFetchone(f"""SELECT chave, nome, quantidade, preco_venda, linkImg 
                                            from produto where nome='{produto.lower()}'""")
            lista_de_produto.append(query)
            db.disconnectDataBase()

        lista_de_produto_atuais = self.getSelectedProductsForSale()

        for dados in lista_de_produto:
            if not dados[1].capitalize() in lista_de_produto_atuais['nome']:
                produto = PySaleRegistrationList()
                produto.setImage(dados[4])
                produto.setChave(dados[0])
                produto.setQuantidade(dados[2])
                produto.setPrecoDeVenda(dados[3])
                produto.setName(dados[1].capitalize())
                produto.let_quantidade.setText('1')

                with open(json_file, 'r') as file:
                    dado = json.load(file)
                    produto.setImageSize(*dado[dados[1]]["icon_image"])

                self.ui.vertical_layout_venda.insertWidget(0, produto)
        self.painel_de_produto.close()

    def cleanProduct(self):
        produtos: list[PySaleRegistrationList] = self.ui.scroll_area_widget_contents_venda.findChildren(
            PySaleRegistrationList)
        self.menu_opcoes_de_venda.close()

        for produto in produtos:
            produto.deleteLater()
            del produto

        self.ui.line_edit_pesquisa_produto_devenda.setFocus()

    def scanBarCodeCam(self) -> None:
        # Read the frame from the video capture object
        ret, frame = self.cap.read()

        # Convert the frame to QImage
        try:
            for code in decode(frame):
                chave = code.data.decode('utf-8')

                if chave:
                    self.ui.line_edit_pesquisa_produto_devenda.setText(chave)
                    winsound.Beep(2500, 100)
                    self.ui.line_edit_pesquisa_produto_devenda.returnPressed.emit()
        except ImportError:
            pass

    def showScanBarCodeCam(self) -> None:
        # Read the frame from the video capture object
        ret, frame = self.cap.read()

        # Convert the frame to QImage
        try:
            height, width, channels = frame.shape
            bytes_per_line = channels * width
            qimg = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

            # rest = 0
            # if width > self.lbl_camera.width():
            #     rest = (width - self.lbl_camera.width()) / 2
            #     width = width - rest

            # Convert the QImage to QPixmap
            # pixmap = QPixmap.fromImage(qimg.copy(rest, 0, width - rest, height))

            # Set the pixmap to the label
            # self.lbl_camera.setPixmap(pixmap)  # por nas configuralcoes
        except ImportError:
            pass

    def showPanelSaleFinisher(self):

        self.painel_sale_finisher = PySalesFinisher(self.ui.central_widget)
        produtos_vendidos = self.getSelectedProductsForSale()

        if produtos_vendidos['chave']:
            width = self.painel_sale_finisher.width()
            height = self.painel_sale_finisher.height()

            self.painel_sale_finisher.btn_confirmar.clicked.connect(self.FinalizarVenda)
            self.painel_sale_finisher.lineEdit_pagamento_valor.returnPressed.connect(self.FinalizarVenda)

            self.painel_sale_finisher.move((self.width() - width) / 2, (self.height() - height) / 2)
            self.painel_sale_finisher.setGeometry(0, 0, self.width(), self.height())

            valor = sum(produtos_vendidos['subtotal'])
            self.painel_sale_finisher.lb_valor_pagamento.setText(f'{valor:,.2f}'.replace(',', '.'))

            self.painel_sale_finisher.show()

    def FinalizarVenda(self):  # modula depois de criar recibo
        produtos_vendidos = self.getSelectedProductsForSale()
        dados_fvenda = self.painel_sale_finisher.confirmar()

        data_atual = QDate.currentDate().toString("dd/MM/yyyy")
        hora_atual = QDateTime.currentDateTime().time().toString()

        # import pprint
        # pprint.pprint(produtos_vendidos)
        # pprint.pprint(dados_fvenda)
        # pprint.pprint(data_atual)

        if dados_fvenda['ok']:

            db = DataBase(AbsolutePath().getPathDatabase())
            db.connectDataBase()

            id_m_d_p = db.executarFetchone(f"""SELECT id FROM metodo_de_pagamento
                                                WHERE nome='{dados_fvenda['metodo_de_pagamento']}'""")
            id_cliente = db.executarFetchone(f"""SELECT id FROM cliente WHERE nome='{dados_fvenda['cliente']}'""")
            id_usuario = db.executarFetchone(f"""SELECT id FROM usuario WHERE nome='{self.usuario}'""")

            # print(id_usuario, id_cliente, id_m_d_p, dados_fvenda, self.usuario, produtos_vendidos)
            db.executarComand(f"""INSERT INTO venda(data, total, troco, usuario, metodo_de_pagamento, cliente)
                                VALUES ('{data_atual} {hora_atual}', {sum(produtos_vendidos['subtotal'])},
                                         {convert_str_in_float(dados_fvenda['troco'])}, {id_usuario[0]},
                                         {id_m_d_p[0]}, {id_cliente[0] if id_cliente else 'Null'})""")

            db.disconnectDataBase()

            for chave, _, quantidade, desconto, preco, _ in zip(*produtos_vendidos.values()):
                db.connectDataBase()
                id_venda = db.executarFetchone("SELECT id FROM venda ORDER BY id DESC LIMIT 1")
                id_produto = db.executarFetchone(f"SELECT ID FROM produto WHERE chave={chave}")

                db.executarComand(f"""INSERT INTO itens_vendido(id_venda, id_produto, quantidade, desconto, preco)
                                      VALUES ({id_venda[0]}, {id_produto[0]}, {quantidade},
                                              {desconto}, {preco})""")
                db.disconnectDataBase()

            self.cleanProduct()
            self.painel_sale_finisher.close()
            self.ui.line_edit_pesquisa_produto_devenda.setFocus()
            ChartFunctions.updateHistorico(self)
            ChartFunctions.updatCircularProgress(self)


    ######################################### historico de venda #########################################

    ############################################## eventos ##############################################
    def mousePressEvent(self, event):
        self._dragPos = event.globalPosition().toPoint()

    def resizeEvent(self, event):
        """
        WINDOW RESIZE EVENT
        EVENTO DE REDIMENSIONAMENTO DA JANELA
        :param event:
        :return:
        """
        # //////////////////////////////////////////////////////////////////////////////////
        SetUpMainWindow.resizeLeftMenu(self, event)
        SetUpMainWindow.resizeGrips(self)

        # //////////////////////////////////////////////////////////////////////////////////
        FunctionsSystem.resizeFrameChartWidth(self)

        # //////////////////////////////////////////////////////////////////////////////////
        if self.menu_opcoes_de_venda:
            self.menu_opcoes_de_venda.move(self.size().width() - 272, 234)

        # ///////////////////////////////////////////////////////////////////////////////////////
        if self.registration_panel:
            self.registration_panel.setGeometry(
                self.registration_panel.x(),
                self.registration_panel.y(),
                self.width(), self.height()
            )
            # //////////////////////////////////////////////////////////////////////////////////////
            self.registration_panel.move((self.width() - self.registration_panel.width()) / 2,
                                         (self.height() - self.registration_panel.height()) / 2)

        # ///////////////////////////////////////////////////////////////////////////////////////
        if self.painel_de_produto:
            self.painel_de_produto.setGeometry(
                self.painel_de_produto.x(),
                self.painel_de_produto.y(),
                self.width(), self.height())

            self.painel_de_produto.move((self.width() - self.painel_de_produto.width()) / 2,
                                        (self.height() - self.painel_de_produto.height()) / 2)

        # /////////////////////////////////////////////////////////////////////////////////////////
        if self.painel_sale_finisher:
            self.painel_sale_finisher.setGeometry(
                self.painel_sale_finisher.x(),
                self.painel_sale_finisher.y(),
                self.width(), self.height())

            self.painel_sale_finisher.move((self.width() - self.painel_sale_finisher.width()) / 2,
                                           (self.height() - self.painel_sale_finisher.height()) / 2)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11:
            FunctionsSystem.resizeFrameChart(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
