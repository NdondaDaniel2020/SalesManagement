# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_login_windowZohWrd.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from src.qt_core import *
from src.gui.core.imagepath import ImagePath

class Ui_LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ////////////////////////////////////////////////////
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # ////////////////////////////////////////////////////
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self._dragPos)
                self._dragPos = event.globalPos()
                event.accept()

        # ////////////////////////////////////////////////////
        self.__setupUi__(self)

        # ////////////////////////////////////////////////////
        self.frame_continer_base.mouseMoveEvent = moveWindow
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)



    def mousePressEvent(self, event):
        self._dragPos = event.globalPos()


    def __setupUi__(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(624, 489)
        LoginWindow.setStyleSheet(u"border-radius: 10px;")
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_continer_base = QFrame(self.centralwidget)
        self.frame_continer_base.setObjectName(u"frame_continer_base")
        self.frame_continer_base.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_base.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_continer_base)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_splash_creen = QFrame(self.frame_continer_base)
        self.frame_splash_creen.setObjectName(u"frame_splash_creen")
        self.frame_splash_creen.setMaximumSize(QSize(318, 453))
        self.frame_splash_creen.setStyleSheet(u"background-color: rgb(54, 63, 118)")
        self.frame_splash_creen.setFrameShape(QFrame.StyledPanel)
        self.frame_splash_creen.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_splash_creen)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.painel_image = QPushButton(self.frame_splash_creen)
        self.painel_image.setObjectName(u"painel_image")
        icon = QIcon()
        icon.addFile(u"../../../../../../../DriverTerabox/ajutes/objetos-removebg-preview-ajustu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.painel_image.setIcon(icon)
        self.painel_image.setIconSize(QSize(260, 260))

        self.verticalLayout.addWidget(self.painel_image)


        self.horizontalLayout_2.addWidget(self.frame_splash_creen)

        self.frame_login = QFrame(self.frame_continer_base)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setMaximumSize(QSize(269, 435))
        self.frame_login.setStyleSheet(u"#frame_login{background-color: rgb(23, 24, 26);\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"#btn_chave_qrcode{\n"
"	background-color: rgb(32, 33, 37);\n"
"	border-radius:7px;\n"
"	border: 1px solid rgb(47, 54, 100)}\n"
"\n"
"QPushButton{\n"
"	background-color:  rgb(19, 20, 22);\n"
"	border-radius:7px;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(28, 29, 32)}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(19, 20, 22)}\n"
"\n"
"QLineEdit, QPlainTextEdit{\n"
"border: 1px solid rgb(47, 54, 100);\n"
"border-radius: 5px;\n"
"background-color: rgb(32, 33, 36);\n"
"color: white;padding-left:5px;}\n"
"\n"
"QLineEdit:hover, QPlainTextEdit:hover{background-color: rgb(30, 31, 34);}\n"
"\n"
"QLineEdit:focus, QPlainTextEdit:focus{background-color: rgb(37, 39, 42);}\n"
"")
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.let_nome = QLineEdit(self.frame_login)
        self.let_nome.setObjectName(u"let_nome")
        self.let_nome.setGeometry(QRect(30, 120, 210, 35))
        self.let_nome.setStyleSheet(u"")
        self.let_senha = QLineEdit(self.frame_login)
        self.let_senha.setObjectName(u"let_senha")
        self.let_senha.setGeometry(QRect(30, 200, 210, 35))
        self.let_senha.setStyleSheet(u"")
        self.lbl_nome = QLabel(self.frame_login)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(30, 102, 100, 17))
        self.lbl_nome.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbl_senha = QLabel(self.frame_login)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setGeometry(QRect(30, 180, 49, 16))
        self.lbl_senha.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_entrar = QPushButton(self.frame_login)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(30, 280, 210, 35))
        self.btn_entrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entrar.setStyleSheet(u"border-radius:7px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 33, 37);")
        self.btn_minimize = QPushButton(self.frame_login)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(205, 5, 27, 27))
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minimize.setStyleSheet(u"background-color: rgba(54, 63, 118, 120);\n"
"border-radius: 4px;")
        icon1 = QIcon()
        icon1.addFile(u"../../../images/svg_icons/icon_minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon1)
        self.btn_minimize.setIconSize(QSize(18, 18))
        self.btn_close = QPushButton(self.frame_login)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(237, 5, 27, 27))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setStyleSheet(u"background-color: rgba(54, 63, 118, 120);\n"
"border-radius: 4px;")
        icon2 = QIcon()
        icon2.addFile(u"../../../images/svg_icons/icon_close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setIconSize(QSize(20, 20))
        self.btn_fingerprint = QPushButton(self.frame_login)
        self.btn_fingerprint.setObjectName(u"btn_fingerprint")
        self.btn_fingerprint.setGeometry(QRect(80, 360, 40, 40))
        self.btn_fingerprint.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_fingerprint.setStyleSheet(u"background-color: rgb(54, 63, 118);")
        icon3 = QIcon()
        icon3.addFile(u"../../../images/svg_icons/icon_fingerprint.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fingerprint.setIcon(icon3)
        self.btn_fingerprint.setIconSize(QSize(32, 30))
        self.lbl_ou = QLabel(self.frame_login)
        self.lbl_ou.setObjectName(u"lbl_ou")
        self.lbl_ou.setGeometry(QRect(122, 330, 25, 17))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_ou.setFont(font)
        self.lbl_ou.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbl_ola = QLabel(self.frame_login)
        self.lbl_ola.setObjectName(u"lbl_ola")
        self.lbl_ola.setGeometry(QRect(30, 30, 100, 21))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.lbl_ola.setFont(font1)
        self.lbl_ola.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbl_bemvido = QLabel(self.frame_login)
        self.lbl_bemvido.setObjectName(u"lbl_bemvido")
        self.lbl_bemvido.setGeometry(QRect(30, 60, 151, 19))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.lbl_bemvido.setFont(font2)
        self.lbl_bemvido.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_faceid = QPushButton(self.frame_login)
        self.btn_faceid.setObjectName(u"btn_faceid")
        self.btn_faceid.setGeometry(QRect(150, 360, 40, 40))
        self.btn_faceid.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_faceid.setStyleSheet(u"background-color: rgb(54, 63, 118);")
        icon4 = QIcon()
        icon4.addFile(u"../../../images/svg_icons/icon_user_scan.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_faceid.setIcon(icon4)
        self.btn_faceid.setIconSize(QSize(38, 38))
        self.lbl_entrar = QLabel(self.frame_login)
        self.lbl_entrar.setObjectName(u"lbl_entrar")
        self.lbl_entrar.setGeometry(QRect(30, 260, 81, 16))
        self.lbl_entrar.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.frame_login)


        self.horizontalLayout.addWidget(self.frame_continer_base)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi


    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.painel_image.setText("")
        self.let_nome.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Digite seu nome", None))
        self.let_senha.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Digite sua senha", None))
        self.lbl_nome.setText(QCoreApplication.translate("LoginWindow", u"Nome de usario *", None))
        self.lbl_senha.setText(QCoreApplication.translate("LoginWindow", u"Senha *", None))
        self.btn_entrar.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.btn_minimize.setText("")
        self.btn_close.setText("")
        self.btn_fingerprint.setText("")
        self.lbl_ou.setText(QCoreApplication.translate("LoginWindow", u"OU", None))
        self.lbl_ola.setText(QCoreApplication.translate("LoginWindow", u"Ol\u00c1", None))
        self.lbl_bemvido.setText(QCoreApplication.translate("LoginWindow", u"Bem-vindo de Volta!", None))
        self.btn_faceid.setText("")
        self.lbl_entrar.setText(QCoreApplication.translate("LoginWindow", u"Entrar *", None))
    # retranslateUi

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = Ui_LoginWindow()
    win.show()
    sys.exit(app.exec())
