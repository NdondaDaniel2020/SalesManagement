
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
from src.gui.uis.windows.main_window.ui_main_window import Ui_MainWindow
from src.gui.function.functions_main_window.functions_system import FunctionsSystem

# INTERFACE AUXILIARY CODE
# CÓDIGO AUXILIAR DA INTERFACE
from src.gui.uis.windows.main_window.setup_main_window import *
from src.gui.function.functions_main_window.functions_chart import ChartFunctions

# AUXILIARY CODE
# CÓDIGO AUXILIAR
from src.gui.core.imagepath import ImagePath
from src.gui.core.qss_themes import QssThemes


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # /////////////////////////////////////////////////////////////
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

        # /////////////////////////////////////////////////////////////
        self._connectingPages_()

        # //////////////////////////////// LEFT MENU /////////////////////////////////////
        self.btn_info_base.clicked.connect(lambda: FunctionsSystem.resizeLeftColumn(self))
        self.btn_info_float.clicked.connect(lambda: FunctionsSystem.resizeLeftColumn(self))

        self.btn_info_base.clicked.connect(self.left_menu.activeBtbInfo)
        self.btn_info_float.clicked.connect(self.left_menu.activeBtbInfo)

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
