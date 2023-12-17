from src.qt_core import *
from src.gui.uis.windows.main_window.ui_main_window import Ui_MainWindow

class FunctionResize:

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def resizeLeftColumn(self) -> None:

        width = self.sender().width()

        width_init = 0
        width_end = 200

        if width != 0:
            width_init = 200
            width_end = 0






