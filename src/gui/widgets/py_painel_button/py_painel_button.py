from src.qt_core import *


class PyPanelButton(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setCursor(Qt.PointingHandCursor)

        self._border_color = (89, 109, 235, 255)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(5)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(*self._border_color))
        self.setGraphicsEffect(self.shadow)



    def enterEvent(self, event):
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(89, 109, 235, 130))
        self.setGraphicsEffect(self.shadow)

    def leaveEvent(self, event):
        self.shadow.setBlurRadius(5)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(89, 109, 235, 255))
        self.setGraphicsEffect(self.shadow)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("clicked")
            # return self.clicked.emit()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("released")
            # return self.released.emit()

    @Property(tuple)
    def border_color(self):
        return self._border_color

    @border_color.setter
    def border_color(self, color: tuple) -> None:
        self._border_color = color

