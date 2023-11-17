

from src.qt_core import *

from ui_main_window import Ui_MainWindow

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, NavigationWidget, MessageBox,
                            isDarkTheme, setTheme, Theme, qrouter)

from qfluentwidgets import FluentIcon as FIF

from src.gui.core.functions import Functions

from src.gui.widgets.py_grips.py_grips import PyGrips
# from src.gui.widgets.py_left_menu.py_left_menu import Ui_LeftMenu
from src.gui.widgets.py_push_button.py_push_button import PyPushButton

class LoginWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        super(LoginWindow).__init__()


        # self.left_menu = Ui_LeftMenu(self.ui.left_menu)




        # # self.setWindowFlags(Qt.FramelessWindowHint)  # este comando é responsavel por eliminar a barra de titulo
        # # self.setAttribute(Qt.WA_TranslucentBackground)  # este comando é responsavel por tornar o fundo transparente
        #
        #
        #
        # # ADD TEX DO TOOL AND ICON
        # #///////////////////////////////////////
        self.ui.btn_close.setTooltipText("Fechar", self.ui.central_widget, pos_tooltip="bottom")
        icon_close = QIcon()
        icon_close.addFile(Functions().set_svg_icon("icon_close"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_close.setIcon(icon_close)
        self.ui.btn_close.setIconSize(QSize(19, 19))

        self.ui.btn_maximize.setTooltipText("Maximizar", self.ui.central_widget, pos_tooltip="bottom")
        icon_max = QIcon()
        icon_max.addFile(Functions().set_svg_icon("icon_maximize.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_maximize.setIcon(icon_max)
        self.ui.btn_maximize.setIconSize(QSize(19, 19))

        self.ui.btn_minimize.setTooltipText("Minimizar", self.ui.central_widget, pos_tooltip="bottom")
        icon_min = QIcon()
        icon_min.addFile(Functions().set_svg_icon("icon_minimize.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_minimize.setIcon(icon_min)
        self.ui.btn_minimize.setIconSize(QSize(18, 18))



        self.ui.btn_home.setTooltipText("Home", self.ui.central_widget)
        icon_home = QIcon()
        icon_home.addFile(Functions().set_svg_icon("icon_home.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_home.setIcon(icon_home)
        self.ui.btn_home.setIconSize(QSize(28, 28))

        self.ui.btn_menu.setTooltipText("Menu", self.ui.central_widget, adjust_x=67, adjust_y=18)
        icon_home = QIcon()
        icon_home.addFile(Functions().set_svg_icon("icon_menu.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_menu.setIcon(icon_home)
        self.ui.btn_menu.setIconSize(QSize(40, 40))

        self.ui.btn_compra.setTooltipText("Compra", self.ui.central_widget, pos_tooltip="right")
        icon_compra = QIcon()
        icon_compra.addFile(Functions().set_svg_icon("icon_compra.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_compra.setIcon(icon_compra)
        self.ui.btn_compra.setIconSize(QSize(36, 36))

        self.ui.btn_venda.setTooltipText("Venda", self.ui.central_widget, pos_tooltip="right")
        icon_venda = QIcon()
        icon_venda.addFile(Functions().set_svg_icon("icon_venda.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_venda.setIcon(icon_venda)
        self.ui.btn_venda.setIconSize(QSize(36, 36))

        self.ui.btn_relatorio.setTooltipText("Relatorio", self.ui.central_widget,
                                             adjust_y=self.ui.btn_relatorio.pos().y())


        icon_relatorio = QIcon()
        icon_relatorio.addFile(Functions().set_svg_icon("icon_inventory.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_relatorio.setIcon(icon_relatorio)
        self.ui.btn_relatorio.setIconSize(QSize(40, 40))

        self.ui.pushButton_test_5.setTooltipText("Test naversario",  self.ui.central_widget, pos_tooltip="right")
        self.ui.btn_agenda.setTooltipText("Test localisation",  self.ui.central_widget)
        self.ui.btn_cliente.setTooltipText("Test localisation", self.ui.central_widget)
        self.ui.btn_copia_seguranca.setTooltipText("Test localisation", self.ui.central_widget)
        self.ui.btn_fornecedor.setTooltipText("Test localisation", self.ui.central_widget)
        self.ui.btn_recibo.setTooltipText("Test localisation", self.ui.central_widget)
        self.ui.btn_relatorio.setTooltipText("Test localisation", self.ui.central_widget)
        self.ui.btn_service.setTooltipText("Test localisation", self.ui.central_widget)




        self.ui.btn_setting.setTooltipText("Configuração", self.ui.central_widget, pos_tooltip="right")
        self.ui.btn_info.setTooltipText("Informação", self.ui.central_widget, pos_tooltip="right")
        self.ui.btn_user.setTooltipText("Usuario", self.ui.central_widget, pos_tooltip="right")

        # self.ui.pushButton_test.setIconSvg("icon_close_.svg", "#e9eaec")



if __name__ == "__main__":

    # sys.argv += ['-platform', 'windows:darkmode=2']
    # app = QApplication(sys.argv)
    # app.setApplicationDisplayName("Should be Dark Theme")
    # app.setStyle("Universal")

    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())




