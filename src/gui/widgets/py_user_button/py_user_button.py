# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerjgVhdq.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from src.qt_core import *
from src.gui.core.functions import Functions

class PyUserButton(QWidget):

    btn_style = {False:
    """
    QWidget{
        background-color: rgb(32, 33, 37);
        border: 1px solid rgb(44, 45, 50);
        border-radius: 8px;
    }
    QWidget:hover{
        background-color: rgb(65, 80, 173);
        border-radius: 8px;
    }
    QWidget:focus {
        background-color: rgb(88, 106, 233);
    }
    """,
    True:
    """
    QWidget{
        background-color: rgb(38, 39, 43);
        border: 1px solid rgb(47, 54, 100);
        border-radius: 8px;
    }
    QWidget:hover{
        background-color: rgb(65, 80, 173);
        border-radius: 8px;
    }
    QWidget:focus {
        background-color: rgb(88, 106, 233);
    }
    """}

    def __init__(self, parent=None):
        super().__init__(parent)

        # PROPERTY
        self._image_user = ''
        self._color = (255, 255, 255)
        self._name = 'Daniel'
        self._access = 'Admin'

        self.sinal = CustomSignals()

        self.active = True

        self.current_style = self.btn_style[False]

        self.__ini_ui__(parent)

        self.perfil_user.clicked.connect(self.__click__)

    def enterEvent(self, event):
        pass

    def leaveEvent(self, event):
        pass

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            return self.sinal.clicked.emit()

    def setActive(self, active):
        self.actie = active

    def isActive(self):
        return self.active

    def checkActive(self):
        if self.isActive():
            self.current_style = self.btn_style[True]

    def pathImage(self):
        return self._image_user

    def setPathImage(self, path):
        self._image_user = path
        icon = QIcon(path)
        self.perfil_user.setIcon(icon)

    def color(self):
        return self._color

    def setColor(self, color):
        self._color = color

    def textName(self):
        return self._name

    def setTextName(self, name):
        self._name = name

    def textAccess(self):
        return self._access

    def setTextAccess(self, access):
        self._access = access

    def __ini_ui__(self, parent):

        self.vertical_layout = QVBoxLayout(parent)
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setSpacing(0)


        self.frame = QFrame(parent)
        self.frame.setObjectName(u"frame")


        self.horizontal_layout = QHBoxLayout(self.frame)
        self.horizontal_layout.setSpacing(0)
        self.horizontal_layout.setObjectName(u"horizontalLayout")
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)


        self.perfil_user = QPushButton(self.frame)
        self.perfil_user.setObjectName(u"perfil_user")
        self.perfil_user.setMinimumSize(QSize(37, 37))
        self.perfil_user.setMaximumSize(QSize(36, 37))

        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(10)

        self.perfil_user.setFont(font)
        self.perfil_user.setStyleSheet("""QPushButton {
                                            color: rgb(233, 234, 236);
                                            background-color: transparent;
                                            padding-left: 7px;
                                            text-align: left;
                                            border: none;
                                            border-radius: 8px;}""")
        self.perfil_user.setIconSize(QSize(26, 26))


        self.horizontal_layout.addWidget(self.perfil_user, 0, Qt.AlignLeft)


        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border:none;background-color: transparent;")


        self.vertical_layout_center = QVBoxLayout(self.frame_2)
        self.vertical_layout_center.setSpacing(0)
        self.vertical_layout_center.setObjectName(u"vertical_layout_center")
        self.vertical_layout_center.setContentsMargins(0, 0, 0, 0)


        self.nome = QLabel(self.frame_2)
        self.nome.setObjectName(u"nome")
        self.nome.setMinimumSize(QSize(0, 10))
        self.nome.setMaximumSize(QSize(16777215, 13))
        self.nome.setFont(font)
        self.nome.setStyleSheet("""color: rgb(255, 255, 255);
                                background-color: transparent;border:none""")


        self.vertical_layout_center.addWidget(self.nome, 0, Qt.AlignLeft)


        self.acesso = QLabel(self.frame_2)
        self.acesso.setObjectName(u"acesso")
        self.acesso.setMinimumSize(QSize(0, 10))
        self.acesso.setMaximumSize(QSize(16777215, 10))

        font1 = QFont()
        font1.setFamilies([u"Segoe UI Light"])
        font1.setPointSize(7)

        self.acesso.setFont(font1)
        self.acesso.setStyleSheet("""color: rgb(255, 255, 255);
                                  background-color: transparent;
                                  border:none;padding-left: 0.4px;""")


        self.vertical_layout_center.addWidget(self.acesso, 0, Qt.AlignLeft)


        self.horizontal_layout.addWidget(self.frame_2)


        self.more = QPushButton(self.frame)
        self.more.setObjectName(u"more")
        self.more.setMinimumSize(QSize(36, 37))
        self.more.setMaximumSize(QSize(36, 37))
        self.more.setStyleSheet(u"QPushButton {\n"
                                "            color: rgb(233, 234, 236);\n"
                                "            background-color: transparent;;\n"
                                "            border: none;\n"
                                "            border-radius: 8px;\n"
                                "}")

        icon1 = QIcon()
        icon1.addFile(Functions().set_svg_icon("icon_more.svg"))

        self.more.setIcon(icon1)
        self.more.setIconSize(QSize(21, 21))

        self.horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontal_layout.addItem(self.horizontal_spacer)

        self.horizontal_layout.addWidget(self.more, 0, Qt.AlignRight)


        self.vertical_layout.addWidget(self.frame)


        self.nome.setText(QCoreApplication.translate("Form", u" Daniel", None))
        self.acesso.setText(QCoreApplication.translate("Form", u"  Admin", None))


        self.setLayout(self.vertical_layout)

    def __click__(self):
        return self.sinal.clicked.emit()

class CustomSignals(QObject):
    clicked = Signal()
