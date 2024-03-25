
# PACOTES NATIVOS
# NATIVE PACKAGES
import sys
import os
import pathlib

# INSTALLED PACKAGES
# PACOTES INSTALADOS
from src.qt_core import *

# CUSTOM WIDGETS
# WIDGETS PERSONALIZADOS
from src.gui.widgets.py_grips.py_grips import PyGrips
from src.gui.widgets.py_left_menu.py_left_menu import LeftMenu
from src.gui.widgets.py_push_button.py_push_button import PyPushButton
from src.gui.widgets.py_product_registration.py_product_registration import PyProductRegistration
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
from src.gui.core.absolute_path import AbsolutePath

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

        # ////////////////////////////////////////////////////////////////////////
        self.setWindowIcon(QIcon(AbsolutePath().getPathImage('icon_resimido.png')))
        self.setWindowTitle("Sales Management MX")

        # ////////////////////////////////////////////////////////////////////////
        self.ui.frame_registro.setImage(r'C:\Users\Daniel\Downloads\mist.png')
        self.ui.frame_registro.setImageSize(40, 40)
        self.ui.frame_registro.setCode('123')
        self.ui.frame_registro.setName('Silking Mist')
        self.ui.frame_registro.setUnidade(12)
        self.ui.frame_registro.setValorDeVenda(11_450)

        self.ui.frame_registro_10.setImage(r'C:\Users\Daniel\Downloads\mascara.png')
        self.ui.frame_registro_10.setImageSize(28, 28)
        self.ui.frame_registro_10.setCode('323')
        self.ui.frame_registro_10.setName('Mascara Hidratante')
        self.ui.frame_registro_10.setUnidade(30)
        self.ui.frame_registro_10.setValorDeVenda(8_500)

        self.ui.frame_registro_11.setImage(r'C:\Users\Daniel\Downloads\tint_spray.png')
        self.ui.frame_registro_11.setImageSize(37, 37)
        self.ui.frame_registro_11.setCode('233')
        self.ui.frame_registro_11.setName('Tint Spray')
        self.ui.frame_registro_11.setUnidade(20)
        self.ui.frame_registro_11.setValorDeVenda(16_000)

        self.ui.frame_registro_12.setImage(r'C:\Users\Daniel\Downloads\barra_de_cera.png')
        self.ui.frame_registro_12.setImageSize(43, 43)
        self.ui.frame_registro_12.setCode('234')
        self.ui.frame_registro_12.setName('Barra de Cera')
        self.ui.frame_registro_12.setUnidade(22)
        self.ui.frame_registro_12.setValorDeVenda(7_450)

        self.ui.frame_registro_9.setImage(r'C:\Users\Daniel\Downloads\spray.png')
        self.ui.frame_registro_9.setImageSize(40, 40)
        self.ui.frame_registro_9.setCode('235')
        self.ui.frame_registro_9.setName('Spray')
        self.ui.frame_registro_9.setUnidade(21)
        self.ui.frame_registro_9.setValorDeVenda(11_500)

        self.ui.frame_registro_8.setImage(r'C:\Users\Daniel\Downloads\mousse.png')
        self.ui.frame_registro_8.setImageSize(37, 37)
        self.ui.frame_registro_8.setCode('236')
        self.ui.frame_registro_8.setName('Mousse')
        self.ui.frame_registro_8.setUnidade(26)
        self.ui.frame_registro_8.setValorDeVenda(13_500)

        self.ui.frame_registro_7.setImage(r'C:\Users\Daniel\Downloads\shampoo.png')
        self.ui.frame_registro_7.setImageSize(30, 30)
        self.ui.frame_registro_9.setCode('237')
        self.ui.frame_registro_9.setName('Shampoo')
        self.ui.frame_registro.setUnidade(40)
        self.ui.frame_registro.setValorDeVenda(18_450)

        # ////////////////////////////////////////////////////////////////////////
        self.set_title_bar = False
        self.product_registration = None

        # /////////////////////////////////////////////////////////////
        SetUpMainWindow.configIconPath(self)
        SetUpMainWindow.addControlWindow(self)
        SetUpMainWindow.configSystem(self)
        SetUpMainWindow.configCircularProgress(self)

        # /////////////////////////////////////////////////////////////
        ChartFunctions.addInventoryChart(self)
        ChartFunctions.addBarChartOnHomepage(self)
        ChartFunctions.addDynamicLineChart(self)

        # /////////////////////////////////////////////////////////////
        self._iniLeftMenu_()

        # /////////////////////////////////////////////////////////////                 QSize(724, 622) QSize(724, 616)
        self._connectingPages_()

        # //////////////////////////////// LEFT MENU /////////////////////////////////////
        self.btn_info_base.clicked.connect(lambda: FunctionsSystem.resizeLeftColumn(self))
        self.btn_info_float.clicked.connect(lambda: FunctionsSystem.resizeLeftColumn(self))

        self.btn_info_base.clicked.connect(self.left_menu.activeBtbInfo)
        self.btn_info_float.clicked.connect(self.left_menu.activeBtbInfo)

        self.btn_back_base.clicked.connect(lambda: print(self.size()))
        # ///////////////////////////////////////////// INVENTORY ///////////////////////////////////////////
        self.ui.btn_adicionar_produto.clicked.connect(lambda: self.showProductRegistration())




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

        elif name_btn == 'btn_inventario':
            self.ui.stacked_widget.setCurrentWidget(self.ui.page_inventario)



    @Slot(None)
    def showProductRegistration(self) -> None:
        """
        ESTE MÉTODO É REPONSAVEL POR CENTRALIZAR MOSTRAR E AJUSTAR O PAINEL DE REGISTRO
        :return:
        """
        if not self.product_registration:
            self.product_registration = PyProductRegistration(self.ui.central_widget)

        # ///////////////////////////////////////////////////////////////////////////////////////
        self.product_registration.move((self.width() - self.product_registration.width()) / 2,
                                       (self.height() - self.product_registration.height()) / 2)


        # ///////////////////////////////////////////////////////////////////////////////////////
        if self.product_registration.isHidden():
            self.product_registration.setGeometry(0, 0, self.width(), self.height())

            # //////////////////////////////////////////////////////////////////////////////////
            self.product_registration.show()





    def mousePressEvent(self, event):
        self._dragPos = event.globalPos()

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
        if self.product_registration:
            self.product_registration.setGeometry(
                self.product_registration.x(),
                self.product_registration.y(),
                self.width(), self.height()
            )
            # //////////////////////////////////////////////////////////////////////////////////////
            self.product_registration.move((self.width() - self.product_registration.width()) / 2,
                                           (self.height() - self.product_registration.height()) / 2)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11:
            FunctionsSystem.resizeFrameChart(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
