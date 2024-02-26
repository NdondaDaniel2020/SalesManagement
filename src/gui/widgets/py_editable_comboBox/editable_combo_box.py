from src.qt_core import *
from src.gui.core.imagepath import ImagePath
class EditableComboBox(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        # self.more_style = """padding: 2px 3px 2px 8px;"""

        # self.line = QFrame(self)
        # self.line.setGeometry(0, 37, 150, 4)
        # self.line.setStyleSheet("background-color: rgb(255, 0, 0); border-radius: 0px;")

    def addbtn(self):
        bh = self.height() - 15
        bw = bh + 4
        bx = self.width() - 31
        by = (self.height() - bh) / 2

        icon = QIcon()
        icon.addFile(ImagePath().set_svg_icon('icon_search.svg'))
        self.button = QPushButton(self)
        self.button.setGeometry(bx, by, bw, bh+2)
        self.button.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 4px;")
        self.button.setCursor(QCursor(Qt.PointingHandCursor))
        self.button.setIcon(icon)

    def __click_line_edit__(self):

        ...

    def resizeEvent(self, event):
        bh = self.height() - 15
        bw = bh + 6
        bx = self.width() - 31
        by = (self.height() - bh) / 2

        self.button.setGeometry(bx, by, bw, bh + 2)