from src.qt_core import *
from src.gui.core.functions import Functions

class PyScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.value_horizontal = 0

        self.setVerticalScrollBarPolicy
        # self.horizontalScrollBar().valueChanged.connect(self.test)

        self.first_resize = 1

        self.next_btn = PyTransitionButton().next(self)
        self.back_btn = PyTransitionButton().back(self)



    def enterEvent(self, event):
        self.next_btn.show()
        self.back_btn.show()
        ...

    def leaveEvent(self, event):
        self.next_btn.hide()
        self.back_btn.hide()
        ...

    def wheelEvent(self, event):

        delta = event.angleDelta().y()

        print("delta", delta)

    def resizeEvent(self, arg__1):
        QScrollArea.resizeEvent(self, arg__1)

        if self.width() > 1021:
            self.next_btn.hide()
            self.back_btn.hide()
        else:
            self.next_btn.setGeometry(self.width() - 25, 50, 17, 56)

class PyTransitionButton(object):
    def __init__(self):
        super().__init__()
        self.style_next = """
                        QPushButton{
                            background-color: rgba(54, 63, 118, 70);
                            border-radius: 5px;
                            padding-left:0px;
                        }
                        
                        QPushButton:hover{
                            background-color: rgba(54, 63, 118, 90);
                            border-radius: 5px;}
                        
                        QPushButton:pressed{
                            padding-left:1.5px;}
                    """
        self.style_back = """
                            QPushButton{
                                background-color: rgba(54, 63, 118, 70);
                                border-radius: 5px;
                                padding-right:0px;
                            }
                            
                            QPushButton:hover{
                                background-color: rgba(54, 63, 118, 90);
                                border-radius: 5px;}
                            
                            QPushButton:pressed{
                                padding-right:1.5px;}
                            """
        self.size = QSize(20, 50)


    def next(self, form):
        self.next_btn = QPushButton(form)
        self.next_btn.setObjectName(u'next_btn')
        self.next_btn.setGeometry(QRect(488, 50, 17, 46))
        self.next_btn.setStyleSheet(self.style_next)
        self.next_btn.setIconSize(QSize(13, 13))
        self.next_btn.setIcon(QIcon(Functions().set_svg_icon('icon_next_btn')))

        self.shadow_next = QGraphicsDropShadowEffect(self.next_btn)
        self.shadow_next.setBlurRadius(30)
        self.shadow_next.setXOffset(0)
        self.shadow_next.setYOffset(0)
        self.shadow_next.setColor(QColor(19, 20, 22, 85))
        self.next_btn.setGraphicsEffect(self.shadow_next)

        self.next_btn.hide()

        return self.next_btn

    def back(self, form):
        self.back_btn = QPushButton(form)
        self.back_btn.setObjectName(u'back_btn')
        self.back_btn.setGeometry(QRect(7, 50, 17, 46))
        self.back_btn.setStyleSheet(self.style_back)
        self.back_btn.setIconSize(QSize(17, 17))
        self.back_btn.setIcon(QIcon(Functions().set_svg_icon('icon_back_btn')))

        self.shadow_back = QGraphicsDropShadowEffect(self.back_btn)
        self.shadow_back.setBlurRadius(30)
        self.shadow_back.setXOffset(0)
        self.shadow_back.setYOffset(0)
        self.shadow_back.setColor(QColor(19, 20, 22, 80))
        self.back_btn.setGraphicsEffect(self.shadow_back)

        self.back_btn.hide()

        return self.back_btn