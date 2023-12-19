
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

# MAIN INTERFACE CODE
# CÓDIGO PRINCIPAL DA INTERFACE
from src.gui.uis.windows.main_window.ui_main_window import Ui_MainWindow
from src.gui.function.functions_main_window.function_resize import FunctionResize

# INTERFACE AUXILIARY CODE
# CÓDIGO AUXILIAR DA INTERFACE
from src.gui.uis.windows.main_window.setup_main_window import *

# AUXILIARY CODE
# CÓDIGO AUXILIAR
from src.gui.core.functions import Functions
from src.gui.core.qss_themes import QssThemes


class MainWindow(QMainWindow):

    def __init__(self):
        # QMainWindow.__init__(self)
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.set_title_bar = False

        SetUpMainWindow.configIconPath(self)
        SetUpMainWindow.addControlWindow(self)

        self._configSystem_()

        # /////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////

        self._iniLeftMenu_()



        self.btn_info_base.clicked.connect(lambda: FunctionResize.resizeLeftColumn(self))
        self.btn_info_float.clicked.connect(lambda: FunctionResize.resizeLeftColumn(self))

        self.btn_info_base.clicked.connect(self.left_menu.activeBtbInfo)
        self.btn_info_float.clicked.connect(self.left_menu.activeBtbInfo)



    def _activeBtbInfo_(self):

        if not self.btn_info_base.is_active:
            self.btn_info_base.set_style(is_active=True, btn_radius=8, text_padding=6)
            self.btn_info_float.set_style(is_active=True, btn_radius=8, text_padding=6)

        else:
            self.btn_info_base.set_style(is_active=False, btn_radius=8, text_padding=6)
            self.btn_info_float.set_style(is_active=False, btn_radius=8, text_padding=6)

    def _configSystem_(self):

        if platform.system() == 'Windows':
            # ////////////////////////////////////////////////////////////////////////////////
            self.set_title_bar = True

            # ////////////////////////////////////////////////////////////////////////////////
            self.windowsConfiguration()

            # ////////////////////////////////////////////////////////////////////////////////
            self.move((QApplication.primaryScreen().size().width() - self.width()) / 2,
                      (QApplication.primaryScreen().size().height() - self.height()) / 4.8)

        else:
            # ////////////////////////////////////////////////////////////////////////////////
            self.nonWindowConfiguration()

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

    def addControlWindow(self):

        # CREATE AND CONFIG BTN MINIMIZE
        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_minimize = PyPushButton(self.ui.frame_control_window, btn_hover="#313237",
                                         btn_pressed="#26272b", btn_radius=4, text_padding=4.5)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(26, 26))
        self.btn_minimize.setMaximumSize(QSize(26, 26))

        # ADD ICON
        # ////////////////////////////////////////////////////////////////////////////////
        icon = QIcon()
        icon.addFile(Functions().set_svg_icon("icon_minimize.svg"), QSize(), QIcon.Normal, QIcon.Off)

        # CONFIG ICON SIZE
        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setIconSize(QSize(17, 17))

        # ADD BTN ON LAYOUT
        # ////////////////////////////////////////////////////////////////////////////////
        self.ui.horizontal_layout_frame_control_window.addWidget(self.btn_minimize)

        # CREATE AND CONFIG BTN MINIMIZE
        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_maximize = PyPushButton(self.ui.frame_control_window, btn_hover="#313237",
                                         btn_pressed="#26272b", btn_radius=4, text_padding=4)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(26, 26))
        self.btn_maximize.setMaximumSize(QSize(26, 26))

        # ADD ICON
        # ////////////////////////////////////////////////////////////////////////////////
        icon1 = QIcon()
        icon1.addFile(Functions().set_svg_icon("icon_maximize.svg"), QSize(), QIcon.Normal, QIcon.Off)

        # CONFIG ICON SIZE
        # //////////////////////////////
        self.btn_maximize.setIcon(icon1)
        self.btn_maximize.setIconSize(QSize(17, 17))

        # ADD BTN ON LAYOUT
        # /////////////////////////////////////////////////////////////////////////
        self.ui.horizontal_layout_frame_control_window.addWidget(self.btn_maximize)

        # CREATE AND CONFIG BTN CLOSE
        # //////////////////////////////////////////////////////////////////////////////
        self.btn_close = PyPushButton(self.ui.frame_control_window, btn_hover="#313237",
                                      btn_pressed="#e10000", btn_radius=4, text_padding=5)

        # //////////////////////////////////////////////////////////////////////////////
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(26, 26))
        self.btn_close.setMaximumSize(QSize(26, 26))

        # ADD ICON
        # //////////////////////////////////////////////////////////////////////////////
        icon2 = QIcon()
        icon2.addFile(Functions().set_svg_icon("icon_close.svg"), QSize(), QIcon.Normal, QIcon.Off)

        # ICON SIZE
        # //////////////////////////////////////////////////////////////////////////////
        self.btn_close.setIcon(icon2)
        self.btn_close.setIconSize(QSize(16, 16))

        # ADD BTN ON LAYOUT
        # //////////////////////////////////////////////////////////////////////////////
        self.ui.horizontal_layout_frame_control_window.addWidget(self.btn_close)

        # CONFIGURATION TOOLTIP
        # //////////////////////////////////////////////////////////////////////////////
        self.btn_close.setTooltipText("Fechar", self.ui.central_widget,
                                      pos_tooltip="bottom", adjust_y=-10, adjust_x=-17)

        # //////////////////////////////////////////////////////////////////////////////
        self.btn_maximize.setTooltipText("Maximizar", self.ui.central_widget,
                                         pos_tooltip="bottom", adjust_y=-10)

        # //////////////////////////////////////////////////////////////////////////////
        self.btn_minimize.setTooltipText("Minimizar", self.ui.central_widget,
                                         pos_tooltip="bottom", adjust_y=-10)

    def windowsConfiguration(self):

        # falta ajustar a posição dos btn e # estilo da janela removendo as bordas
        # ////////////////////////////////////////////////////////////////////////////////
        self.set_title_bar = True

        # ADD STYLE WINDOW
        # ////////////////////////////////////////////////////////////////////////////////
        self.ui.widget_style_sheet.setStyleSheet(QssThemes().set_qss(file_name='window_normal.qss', theme='dark'))


        # ////////////////////////////////////////////////////////////////////////////////
        self.setWindowFlags(Qt.FramelessWindowHint)  # este comando é responsavel por eliminar a barra de titulo
        self.setAttribute(Qt.WA_TranslucentBackground)  # este comando é responsavel por tornar o fundo transself.uie


        # CONENCTION
        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_close.clicked.connect(lambda: self.close())
        self.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.btn_maximize.clicked.connect(lambda:  SetUpMainWindow.restoreWindow(self))


        # ADD LOGO AND SVG WIDGET
        # ////////////////////////////////////////////////////////////////////////////////


        # EVENTO PARA MOVER A JANELA
        # ////////////////////////////////////////////////////////////////////////////////
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self._dragPos)
                self._dragPos = event.globalPos()  ## event.globalPos() deprecated
                event.accept()


        # EVENTO PARA MAXIMIZAR E NORMALIZAR A JANELA
        # ////////////////////////////////////////////////////////////////////////////////
        def mouseDoubleClickEvent(event):
            if event.type() == QEvent.MouseButtonDblClick:
                SetUpMainWindow.restoreWindow(self)

        self.ui.title_bar.mouseMoveEvent = moveWindow
        self.ui.title_bar.mouseDoubleClickEvent = mouseDoubleClickEvent


        # ADICIONAR SOMBRA NA JANELA PRINCIPAL
        # ////////////////////////////////////////////////////////////////////////////////
        self.shadow_window = QGraphicsDropShadowEffect(self)
        self.shadow_window.setBlurRadius(30)
        self.shadow_window.setXOffset(0)
        self.shadow_window.setYOffset(0)
        self.shadow_window.setColor(QColor(0, 0, 0, 60))
        self.ui.central_widget.setGraphicsEffect(self.shadow_window)


        # PONTOS DE MOVIMENTAÇÃO INSTANCIADOS
        # INSTANCED MOVEMENT POINTS
        # ////////////////////////////////////////////////////////////////////////////////
        self.left_grip = PyGrips(self, "left", True)
        self.right_grip = PyGrips(self, "right", True)
        self.top_grip = PyGrips(self, "top", True)
        self.bottom_grip = PyGrips(self, "bottom", True)
        self.top_left_grip = PyGrips(self, "top_left", True)
        self.top_right_grip = PyGrips(self, "top_right", True)
        self.bottom_left_grip = PyGrips(self, "bottom_left", True)
        self.bottom_right_grip = PyGrips(self, "bottom_right", True)

    def nonWindowConfiguration(self):

        self.set_title_bar = False

        # REMOVE WIDGETS
        # ///////////////////////////////////////////////////////////////////////////////
        self.ui.frame_logo.hide()
        self.ui.frame_control_window.hide()
        self.ui.title_bar.hide()

        # CONFIG INTERFACE NO WINDOW
        #///////////////////////////////////////////////////////////////////////////////
        self.ui.widget_style_sheet.setStyleSheet(
            QssThemes().set_qss(file_name='non_window_configuration.qss', theme='dark'))

        # REMOVE MARGIN ON WINDOW
        # //////////////////////////////////////////////////////////////////////////////
        self.ui.horizontal_layout_widget_style_sheet.setContentsMargins(0, 0, 0, 0)
        self.ui.vertical_layout_frame_line.setContentsMargins(0, 0, 0, 0)

        # ajustar o left menu float

    def mousePressEvent(self, event):
        self._dragPos = event.globalPos()

    def resizeEvent(self, event):
        """
        WINDOW RESIZE EVENT
        EVENTO DE REDIMENSIONAMENTO DA JANELA
        :param event:
        :return:
        """
        SetUpMainWindow.resizeLeftMenu(self, event)
        SetUpMainWindow.resizeGrips(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
