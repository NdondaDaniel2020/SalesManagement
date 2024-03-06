from src.qt_core import *
from src.gui.core.imagepath import ImagePath

class PyEditableComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setEditable(True)

        icon = QIcon()
        icon.addFile(ImagePath().set_svg_icon('icon_down_arrow.svg'))
        self.button = QPushButton(self)
        self.button.setStyleSheet("""QPushButton{
                                        background-color: rgb(32, 33, 36);
                                        border-radius:7px;}
                                    QPushButton:hover{
                                        background-color: rgb(28, 29, 32);}
                                    QPushButton:pressed{
                                        background-color: rgb(19, 20, 22)}""")
        self.button.setIcon(icon)
        self.button.clicked.connect(self.__click_button__)


    def __click_button__(self):
        self.showPopup()


    def resizeEvent(self, event):

        # ///////////////////////////////////////////
        bh = self.height() - 14
        bw = bh + 8
        bx = self.width() - 36
        by = (self.height() - bh) / 2

        # ///////////////////////////////////////////
        self.button.setGeometry(bx, by, bw, bh + 2)
