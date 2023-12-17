# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerLKbydJ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from src.qt_core import *
from src.gui.core.functions import Functions

class PyCustomPushButton(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.icon = QIcon()

        self.sinal = CustomSignals()

        self._setupUi_(parent)

        self.button.clicked.connect(self.__click__)
        # self.more.clicked.connect(self.__click__)

    def text(self):
        return self.button.text()

    def setText(self, text):
        self.button.setText(text)

    def setIcon(self, icon):
        self.button.setIcon(QIcon(Functions().set_svg_icon(icon)))


    def _setupUi_(self, parent):
        style_button = """QPushButton{
                                        color: rgb(233, 234, 236);
                                        background-color: transparent;
                                        padding-left: 7px;
                                        text-align: left;
                                        border: none}
                                    QPushButton:hover{color: rgb(233, 234, 236);
                                        background-color: transparent;
                                        padding-left: 7px;
                                        text-align: left;
                                        border: none}
                                    QPushButton:pressed{color: rgb(233, 234, 236);
                                        background-color: transparent;
                                        padding-left: 7px;
                                        text-align: left;
                                        border: none}}"""
        self.horizontalLayout = QHBoxLayout(parent)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 0, 2, 0)
        self.button = QPushButton(parent)
        self.button.setObjectName(u"button")
        self.button.setMinimumSize(QSize(37, 37))
        self.button.setMaximumSize(QSize(1234, 37))
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(10)
        self.button.setFont(font)
        self.button.setStyleSheet(style_button)

        self.button.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.button, 0, Qt.AlignLeft)

        self.more = QPushButton(parent)
        self.more.setObjectName(u"more")
        self.more.setMinimumSize(QSize(36, 37))
        self.more.setMaximumSize(QSize(36, 37))
        self.more.setStyleSheet(style_button)
        icon1 = QIcon()
        icon1.addFile(Functions().set_svg_icon('icon_more.svg'), QSize(), QIcon.Normal, QIcon.Off)

        self.more.setIcon(icon1)
        self.more.setIconSize(QSize(21, 21))

        self.horizontalLayout.addWidget(self.more, 50, Qt.AlignRight)

        self.setLayout(self.horizontalLayout)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            return self.sinal.clicked.emit()

    def __click__(self):
        return self.sinal.clicked.emit()

class CustomSignals(QObject):

    clicked = Signal()
