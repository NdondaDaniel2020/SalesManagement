
from src.qt_core import *

from ui_main_window import Ui_MainWindow

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, NavigationWidget, MessageBox,
                            isDarkTheme, setTheme, Theme, qrouter)

from qfluentwidgets import FluentIcon as FIF

from src.gui.core.functions import Functions

from src.gui.widgets.py_grips.py_grips import PyGrips
from src.gui.widgets.py_left_menu.py_left_menu import LeftMenu
from src.gui.widgets.py_push_button.py_push_button import PyPushButton

class SetUpMainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setup = Ui_MainWindow()
        self.setup.setupUi(self)


        # # self.setWindowFlags(Qt.FramelessWindowHint)  # este comando é responsavel por eliminar a barra de titulo
        # # self.setAttribute(Qt.WA_TranslucentBackground)  # este comando é responsavel por tornar o fundo transparente


        self.left_menu = LeftMenu(self.setup.frame_left_menu, self.setup.central_widget, self.geometry().height())

        # self.left_menu.btn_home.connect(lambda: print("test home"))

        self.setup.btn_close.setTooltipText("Fechar", self.setup.central_widget,
                                            pos_tooltip="bottom", adjust_y=-10, adjust_x=-17)
        self.setup.btn_maximize.setTooltipText("Maximizar", self.setup.central_widget,
                                               pos_tooltip="bottom", adjust_y=-10)
        self.setup.btn_minimize.setTooltipText("Minimizar", self.setup.central_widget,
                                               pos_tooltip="bottom", adjust_y=-10)



    def resizeEvent(self, event):
        self.left_menu.setResize(self.setup.frame_left_menu.geometry())





if __name__ == "__main__":

    # sys.argv += ['-platform', 'windows:darkmode=2']
    # app = QApplication(sys.argv)
    # app.setApplicationDisplayName("Should be Dark Theme")
    # app.setStyle("Universal")

    app = QApplication(sys.argv)
    window = SetUpMainWindow()
    window.show()
    sys.exit(app.exec())
