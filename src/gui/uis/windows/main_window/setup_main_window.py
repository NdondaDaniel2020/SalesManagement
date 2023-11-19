
from src.qt_core import *

from ui_main_window import Ui_MainWindow

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, NavigationWidget, MessageBox,
                            isDarkTheme, setTheme, Theme, qrouter)

from qfluentwidgets import FluentIcon as FIF

from src.gui.core.functions import Functions

from src.gui.widgets.py_grips.py_grips import PyGrips
from src.gui.widgets.py_left_menu.py_left_menu import LeftMenu
from src.gui.widgets.py_push_button.py_push_button import PyPushButton

class LoginWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        super(LoginWindow).__init__()

        # # self.setWindowFlags(Qt.FramelessWindowHint)  # este comando é responsavel por eliminar a barra de titulo
        # # self.setAttribute(Qt.WA_TranslucentBackground)  # este comando é responsavel por tornar o fundo transparente


        self.left_menu = LeftMenu(self.ui.frame_left_menu, self.ui.central_widget, self.geometry().height())


        self.ui.btn_close.setTooltipText("Fechar", self.ui.central_widget, pos_tooltip="bottom", adjust_y=-10)
        self.ui.btn_maximize.setTooltipText("Maximizar", self.ui.central_widget, pos_tooltip="bottom", adjust_y=-10)
        self.ui.btn_minimize.setTooltipText("Minimizar", self.ui.central_widget, pos_tooltip="bottom", adjust_y=-10)



    def resizeEvent(self, event):
        self.left_menu.setResize(self.ui.frame_left_menu.geometry())





if __name__ == "__main__":

    # sys.argv += ['-platform', 'windows:darkmode=2']
    # app = QApplication(sys.argv)
    # app.setApplicationDisplayName("Should be Dark Theme")
    # app.setStyle("Universal")

    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
