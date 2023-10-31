from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

import sys


class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())
