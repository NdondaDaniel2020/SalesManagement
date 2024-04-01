
# PACOTES NATIVOS
# NATIVE PACKAGES
import os
import sys
import json
import pathlib

# INSTALLED PACKAGES
# PACOTES INSTALADOS
from src.qt_core import *

# CUSTOM WIDGETS
# WIDGETS PERSONALIZADOS
from src.gui.widgets.py_grips.py_grips import PyGrips
from src.gui.widgets.py_left_menu.py_left_menu import LeftMenu
from src.gui.widgets.py_push_button.py_push_button import PyPushButton
from src.gui.widgets.py_registration_list.py_registration_list import PyRegistrationList
from src.gui.widgets.py_product_registration.py_product_registration import PyProductRegistration
from src.gui.widgets import SaleMenu
# from src.gui.widgets.py_flow_layout.py_flow_layout import PyFlowLayout

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
                                                                     insertProductDataIntoTheDatabase)

#
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
        self.menu_opcoes_de_venda: SaleMenu = None
        self.registration_panel: PyProductRegistration = None

        # /////////////////////////////////////////////////////////////
        SetUpMainWindow.configIconPath(self)
        SetUpMainWindow.addControlWindow(self)
        SetUpMainWindow.configSystem(self)

        # /////////////////////////////////////////////////////////////
        ChartFunctions.addInventoryChart(self)
        ChartFunctions.configCircularProgress(self)
        ChartFunctions.addBarChartOnHomepage(self)
        self.timer_dynamic_chart = ChartFunctions.addDynamicLineChart(self)
        # self.timer_dynamic_chart ativar

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.ui.frame_inventario.mousePressEvent = lambda e: self.ui.stacked_widget.setCurrentWidget(
                                                                                                self.ui.page_inventario)
        self.ui.frame_venda.mousePressEvent = lambda e: self.ui.stacked_widget.setCurrentWidget(self.ui.page_venda)

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # todas as iniciolizacoes tem que passa na tela de login
        self._iniLeftMenu_()
        self.initRegistrationPanel()
        self.automaticProductInsertion()

        # //////////////////////////////////////////////////////////////////////////////////
        self._connectingPages_()

        # //////////////////////////////// LEFT MENU //////////////////////////////////////
        self.btn_info_base.clicked.connect(lambda: FunctionsSystem.resizeLeftColumn(self))
        self.btn_info_float.clicked.connect(lambda: FunctionsSystem.resizeLeftColumn(self))

        self.btn_info_base.clicked.connect(self.left_menu.activeBtbInfo)
        self.btn_info_float.clicked.connect(self.left_menu.activeBtbInfo)

        # self.btn_back_base.clicked.connect(lambda: print(self.size(), self.ui.frame_chart_bar.size()))

        self.ui.btn_pesquisa_produto.clicked.connect(lambda: FunctionsSystem.searchProduct(self))
        self.ui.line_edit_pesquisa_produto.returnPressed.connect(lambda: FunctionsSystem.searchProduct(self))

        # ///////////////////////////////////////////// INVENTORY ///////////////////////////////////////////
        self.ui.btn_adicionar_produto.clicked.connect(lambda: self.showRegistrationPanel())
        self.ui.frame_criar_produto.mousePressEvent = lambda e: self.showRegistrationPanel()

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



    ############################################## inventario ###########################################

    def initRegistrationPanel(self):
        self.registration_panel = PyProductRegistration(self.ui.central_widget)
        self.registration_panel.countAvailableCameras()
        self.registration_panel.close()

    @Slot(None)
    def showRegistrationPanel(self) -> None:
        """
        ESTE MÉTODO É REPONSAVEL POR CENTRALIZAR MOSTRAR E AJUSTAR O PAINEL DE REGISTRO
        :return:
        """

        self.registration_panel.btn_ok.clicked.connect(self.registerProduct)

        self.registration_panel.move((self.width() - self.registration_panel.width()) / 2,
                                     (self.height() - self.registration_panel.height()) / 2)

        if self.registration_panel.isHidden():
            self.registration_panel.setGeometry(0, 0, self.width(), self.height())

            self.registration_panel.show()

    def automaticProductInsertion(self):
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


    def registerProduct(self):
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



    ################################################## venda #####################################################

    def showMenuOpcoes(self):
        if not self.menu_opcoes_de_venda:
            self.menu_opcoes_de_venda = SaleMenu(self.ui.page_venda)
            self.menu_opcoes_de_venda.move(456, 234)
            self.menu_opcoes_de_venda.show()

            self.ui.page_venda.mousePressEvent = lambda e: self.menu_opcoes_de_venda.close()

            self.menu_opcoes_de_venda_opacity = QGraphicsOpacityEffect(self.menu_opcoes_de_venda)
            self.menu_opcoes_de_venda_opacity.setOpacity(0.0)
            self.menu_opcoes_de_venda.setGraphicsEffect(self.menu_opcoes_de_venda_opacity)

            self.menu_venda_opacity_animation = QPropertyAnimation(self.menu_opcoes_de_venda_opacity, b'opacity')
            self.menu_venda_opacity_animation.setStartValue(0.0)
            self.menu_venda_opacity_animation.setEndValue(0.9)
            self.menu_venda_opacity_animation.setDuration(400)

            self.pos_animation_menu_venda = QPropertyAnimation(self.menu_opcoes_de_venda, b'pos')
            self.pos_animation_menu_venda.setStartValue(QPoint(456, 240))
            self.pos_animation_menu_venda.setEndValue(QPoint(456, 234))
            self.pos_animation_menu_venda.setDuration(400)
            self.pos_animation_menu_venda.setEasingCurve(QEasingCurve.Type.InOutCirc)

            self.group_animation_menu_vendas = QParallelAnimationGroup()
            self.group_animation_menu_vendas.addAnimation(self.menu_venda_opacity_animation)
            self.group_animation_menu_vendas.addAnimation(self.pos_animation_menu_venda)
            self.group_animation_menu_vendas.start()

        elif not self.menu_opcoes_de_venda.isVisible():
            self.menu_opcoes_de_venda.show()
            self.group_animation_menu_vendas.start()

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

        FunctionsSystem.resizeFrameChartWidth(self)
        # //////////////////////////////////////////////////////////////////////////////////
        if self.registration_panel:
            self.registration_panel.setGeometry(
                self.registration_panel.x(),
                self.registration_panel.y(),
                self.width(), self.height()
            )
            # //////////////////////////////////////////////////////////////////////////////////////
            self.registration_panel.move((self.width() - self.registration_panel.width()) / 2,
                                         (self.height() - self.registration_panel.height()) / 2)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11:
            FunctionsSystem.resizeFrameChart(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
