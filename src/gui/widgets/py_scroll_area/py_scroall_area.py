from src.qt_core import *
from src.gui.core.absolute_path import AbsolutePath

class PyScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.value_horizontal = 0

        self.first_resize = 1

        self.next_btn = PyTransitionButton().next(self)
        self.back_btn = PyTransitionButton().back(self)

        self.next_btn.clicked.connect(self.moveScrollAreaHorizontally)
        self.back_btn.clicked.connect(self.moveScrollAreaHorizontally)

    Slot(str)
    def moveScrollAreaHorizontally(self):
        name_btn = self.sender().objectName()

        value_start = 0
        value_end = 0

        if name_btn == 'next_btn':

            if self.horizontalScrollBar().value() == self.horizontalScrollBar().minimum():
                value_start = self.horizontalScrollBar().minimum()
                value_end = 255

            elif (self.horizontalScrollBar().minimum()
                  < self.horizontalScrollBar().value()
                  < self.horizontalScrollBar().maximum()):

                value_start = self.horizontalScrollBar().value()
                value_end = self.horizontalScrollBar().maximum()

        else:

            if self.horizontalScrollBar().value() == self.horizontalScrollBar().maximum():
                value_start = self.horizontalScrollBar().maximum()
                value_end = 255
            elif (self.horizontalScrollBar().minimum()
                  < self.horizontalScrollBar().value()
                  < self.horizontalScrollBar().maximum()):
                value_start = self.horizontalScrollBar().value()
                value_end = self.horizontalScrollBar().minimum()

        if not ((self.horizontalScrollBar().value() == self.horizontalScrollBar().maximum() and name_btn == 'next_btn') or
                (self.horizontalScrollBar().value() == self.horizontalScrollBar().minimum() and name_btn == 'back_btn')):

            self.scroll_animation = QPropertyAnimation(self.horizontalScrollBar(), b'value')
            self.scroll_animation.setStartValue(value_start)
            self.scroll_animation.setDuration(200)
            self.scroll_animation.setEndValue(value_end)
            self.scroll_animation.setEasingCurve(QEasingCurve.Type.InOutCirc)
            self.scroll_animation.start()


    def enterEvent(self, event):
        if self.width() < 1021:
            self.next_btn.show()
            self.back_btn.show()


    def leaveEvent(self, event):
        self.next_btn.hide()
        self.back_btn.hide()



    def wheelEvent(self, event):

        delta = event.angleDelta().y()

        value_start = 0
        value_end = 0

        if delta > 0:
            if self.horizontalScrollBar().value() == self.horizontalScrollBar().minimum():
                value_start = self.horizontalScrollBar().minimum()
                value_end = 255

            elif(self.horizontalScrollBar().minimum()
                   < self.horizontalScrollBar().value()
                   < self.horizontalScrollBar().maximum()):

                value_start = self.horizontalScrollBar().value()
                value_end = self.horizontalScrollBar().maximum()

        else:
            if self.horizontalScrollBar().value() == self.horizontalScrollBar().maximum():
                value_start = self.horizontalScrollBar().maximum()
                value_end = 255
            elif (self.horizontalScrollBar().minimum()
                  < self.horizontalScrollBar().value()
                  < self.horizontalScrollBar().maximum()):

                value_start = self.horizontalScrollBar().value()
                value_end = self.horizontalScrollBar().minimum()


        if not ((self.horizontalScrollBar().value() == self.horizontalScrollBar().maximum() and delta > 0) or
                (self.horizontalScrollBar().value() == self.horizontalScrollBar().minimum() and delta < 0)):

            self.scroll_animation = QPropertyAnimation(self.horizontalScrollBar(), b'value')
            self.scroll_animation.setStartValue(value_start)
            self.scroll_animation.setDuration(200)
            self.scroll_animation.setEndValue(value_end)
            self.scroll_animation.setEasingCurve(QEasingCurve.Type.InOutCirc)
            self.scroll_animation.start()

    def resizeEvent(self, arg__1):
        QScrollArea.resizeEvent(self, arg__1)

        if self.width() > 1021:
            self.next_btn.hide()
            self.back_btn.hide()
        else:
            self.next_btn.setGeometry(self.width() - 23, 50, 15, 40)


class PyTransitionButton(object):
    def __init__(self):
        super().__init__()
        self.style_next = """
                        QPushButton{
                            background-color: rgba(54, 63, 118, 70);
                            border-radius: 3px;
                            padding-left:0px;
                        }
                        
                        QPushButton:hover{
                            background-color: rgba(54, 63, 118, 90);
                            border-radius: 3px;}
                        
                        QPushButton:pressed{
                            padding-left:1.5px;}
                    """
        self.style_back = """
                            QPushButton{
                                background-color: rgba(54, 63, 118, 70);
                                border-radius: 3px;
                                padding-right:0px;
                            }
                            
                            QPushButton:hover{
                                background-color: rgba(54, 63, 118, 90);
                                border-radius: 3px;}
                            
                            QPushButton:pressed{
                                padding-right:1.5px;}
                            """
        self.size = QSize(14, 40)


    def next(self, form):
        self.next_btn = QPushButton(form)
        self.next_btn.setObjectName(u'next_btn')
        self.next_btn.setGeometry(QRect(490, 50, 15, 40))
        self.next_btn.setMaximumSize(self.size)
        self.next_btn.setMinimumSize(self.size)
        self.next_btn.setStyleSheet(self.style_next)
        self.next_btn.setIconSize(QSize(13, 13))
        self.next_btn.setIcon(QIcon(AbsolutePath().getPathIcon('icon_next_btn')))

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
        self.back_btn.setGeometry(QRect(7, 50, 15, 40))
        self.back_btn.setMaximumSize(self.size)
        self.back_btn.setMinimumSize(self.size)
        self.back_btn.setStyleSheet(self.style_back)
        self.back_btn.setIconSize(QSize(17, 17))
        self.back_btn.setIcon(QIcon(AbsolutePath().getPathIcon('icon_back_btn')))

        self.shadow_back = QGraphicsDropShadowEffect(self.back_btn)
        self.shadow_back.setBlurRadius(30)
        self.shadow_back.setXOffset(0)
        self.shadow_back.setYOffset(0)
        self.shadow_back.setColor(QColor(19, 20, 22, 85))
        self.back_btn.setGraphicsEffect(self.shadow_back)

        self.back_btn.hide()

        return self.back_btn
