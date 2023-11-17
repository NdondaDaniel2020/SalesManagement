from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

from gui.uis.windows.main_window.ui_main_window import Ui_MainWindow

import sys

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, NavigationWidget, MessageBox,
                            isDarkTheme, setTheme, Theme, qrouter)
from qfluentwidgets import FluentIcon as FIF


class LoginWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.left_menu.setGeometry(self.ui.continer_left_menu.geometry())


        self.ui.left_menu.addItem(
            routeKey="music",
            icon=FIF.MUSIC,
            text="Music",
            onClick=lambda: print("test music"),
            position=NavigationItemPosition.TOP
        )

        self.ui.left_menu.addItem(
            routeKey="dfsgic",
            icon=FIF.FILTER,
            text="Filter",
            onClick=lambda: print("test filter"),
            position=NavigationItemPosition.BOTTOM
        )

        self.ui.left_menu.addItem(
            routeKey="TASf",
            icon=FIF.ALBUM,
            text="Album",
            onClick=lambda: print("test filter"),
            tooltip="Tasf",
            position=NavigationItemPosition.SCROLL
        )

        self.ui.left_menu.setExpandWidth(190)

        self.ui.left_menu.panel.setStyleSheet("""background-color: rgb(255, 255, 255);border-radius: 7px;""")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
