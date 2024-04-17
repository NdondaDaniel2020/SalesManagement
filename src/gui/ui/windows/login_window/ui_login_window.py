# -*- coding: utf-8 -*-
import cv2

################################################################################
## Form generated from reading UI file 'ui_login_windowZohWrd.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import json
from hashlib import sha256
from src.main import MainWindow
from src.qt_core import *
from src.gui.core.database import DataBase
from src.gui.core.absolute_path import AbsolutePath
from src.gui.widgets.py_circular_progress.py_circular_progress import PyCircularProgress
from src.gui.widgets.py_slide_stacked_widgets.py_slide_stacked_widgets import PySlidingStackedWidget


try:
    from ctypes import windll  # Only exists on Windows.

    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except Exception as _:
    pass



class Ui_LoginWindow(QMainWindow):
    VALUE_PROGRESS_BAR = 0

    def __init__(self):
        super().__init__()

        # ///////////////////////////////////////////////////////////////////////////////
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # ///////////////////////////////////////////////////////////////////////////////
        self.main_window = MainWindow()

        # ///////////////////////////////////////////////////////////////////////////////
        self.__setupUi__(self)
        self.__resizeSplashCreen()
        self.__confiCircularProgressBar()
        self.__moveWindow()
        self.__queryUser()

        self.can_capture: bool = self.__initClassifire()
        # ///////////////////////////////////////////////////////////////////////////////
        self.progress_bar_timer = QTimer()
        self.progress_bar_timer.setInterval(20)
        self.progress_bar_timer.timeout.connect(self.__changeValueProgressBar)

        if self.can_capture:
            self.capture_timer = QTimer()
            self.capture_timer.timeout.connect(self.__capture)
        # ///////////////////////////////////////////////////////////////////////////////

        self.btn_close.clicked.connect(self.close)
        self.btn_minimizar.clicked.connect(self.showMinimized)
        self.let_nome.returnPressed.connect(lambda: self.let_senha.setFocus())
        self.let_nome.textChanged.connect(lambda: self.let_nome.setStyleSheet(""))
        self.let_senha.returnPressed.connect(self.__login)
        self.let_senha.textChanged.connect(lambda: self.let_senha.setStyleSheet(""))
        self.btn_login.clicked.connect(self.__login)

        self.btn_faceid.clicked.connect(self.__starFaceId)


    def __login(self) -> None:
        """
        responsavel por fazer o login
        :return:
        """
        dados_de_acesso = self.__validatorLogin()
        if dados_de_acesso:
            self.main_window.usuario = dados_de_acesso['nome']
            self.main_window.acesso = dados_de_acesso['acesso']
            self.main_window.imageUser = dados_de_acesso['linkImg']
            self.main_window.show()
            self.close()

    def __queryUser(self) -> None:
        db: DataBase = DataBase(AbsolutePath().getPathDatabase())
        db.connectDataBase()
        self.query_usuario = dict(db.executarFetchall(f"SELECT id, nome FROM usuario"))
        db.disconnectDataBase()

        self.query_usuario[0] = 'Desconhecido'

    def __validatorLogin(self) -> dict:
        """
        responsavel por validar os dados de login(nome, senha)
        :return:
        """
        db: DataBase = DataBase(AbsolutePath().getPathDatabase())
        db.connectDataBase()
        query = db.executarFetchall(f"SELECT nome FROM usuario")

        dados_de_acesso = {'nome': '', 'linkImg': '', 'acesso': True, 'validade': False}
        nome = self.let_nome.text()
        senha = self.let_senha.text()

        for user in query:
            if nome == user[0]:
                dados_de_acesso['nome'] = nome
                dados_de_acesso['validade'] = True

        if not dados_de_acesso['validade']:
            self.__animationErrorName()
        else:
            query = db.executarFetchone(f"SELECT senha, acesso, linkImg FROM Usuario WHERE nome='{nome}'")
            if query[0] != sha256(senha.encode()).hexdigest():
                self.__animtionErrorPass()
                dados_de_acesso['validade'] = False
            else:
                dados_de_acesso['validade'] = True
                dados_de_acesso['acesso'] = bool(query[1])
                dados_de_acesso['linkImg'] = query[2]
        db.disconnectDataBase()
        return dados_de_acesso

    def __animationErrorName(self):
        """
        responsavel pela animação de erro de nome
        :return:
        """
        self.let_nome.setStyleSheet("""QLineEdit, QPlainTextEdit{
            border: 1px solid rgb(255, 0, 0);
            border-radius: 5px;
            background-color: rgb(32, 33, 36);
            color: white;padding-left:5px;} 
            QLineEdit:hover, QPlainTextEdit:hover{background-color: rgb(30, 31, 34);}
            QLineEdit:focus, QPlainTextEdit:focus{background-color: rgb(37, 39, 42);}""")
        QTimer.singleShot(0, lambda: self.let_nome.setGeometry(QRect(33, 120, 210, 35)))
        QTimer.singleShot(40, lambda: self.let_nome.setGeometry(QRect(28, 120, 210, 35)))
        QTimer.singleShot(80, lambda: self.let_nome.setGeometry(QRect(33, 120, 210, 35)))
        QTimer.singleShot(120, lambda: self.let_nome.setGeometry(QRect(33, 120, 210, 35)))
        QTimer.singleShot(160, lambda: self.let_nome.setGeometry(QRect(28, 120, 210, 35)))
        QTimer.singleShot(200, lambda: self.let_nome.setGeometry(QRect(33, 120, 210, 35)))

    def __animtionErrorPass(self) -> None:
        """
        responsavel pela animação de erro da senha
        :return:
        """
        self.let_senha.setStyleSheet("""QLineEdit, QPlainTextEdit{
            border: 1px solid rgb(255, 0, 0);
            border-radius: 5px;
            background-color: rgb(32, 33, 36);
            color: white;padding-left:5px;}
            QLineEdit:hover, QPlainTextEdit:hover{background-color: rgb(30, 31, 34);}
            QLineEdit:focus, QPlainTextEdit:focus{background-color: rgb(37, 39, 42);}""")
        QTimer.singleShot(0, lambda: self.let_senha.setGeometry(QRect(33, 200, 210, 35)))
        QTimer.singleShot(40, lambda: self.let_senha.setGeometry(QRect(28, 200, 210, 35)))
        QTimer.singleShot(80, lambda: self.let_senha.setGeometry(QRect(33, 200, 210, 35)))
        QTimer.singleShot(120, lambda: self.let_senha.setGeometry(QRect(33, 200, 210, 35)))
        QTimer.singleShot(160, lambda: self.let_senha.setGeometry(QRect(28, 200, 210, 35)))
        QTimer.singleShot(200, lambda: self.let_senha.setGeometry(QRect(33, 200, 210, 35)))

    def __starFaceId(self):

        if self.cap is None or not self.cap.isOpened():
            json_file = AbsolutePath().getPathIpSelected()
            with open(json_file, 'r') as file:
                ips = json.load(file)

            self.cap = cv2.VideoCapture(ips['ip_selected'])
            self.stacked_widget_splash_screen.slideInIdx(2)
            QTimer().singleShot(400, lambda: self.capture_timer.start())
        else:
            self.stacked_widget_splash_screen.slideInIdx(0)
            self.capture_timer.stop()
            self.cap.release()

    def __initClassifire(self) -> bool:
        """
        responsavel por inicializar iniciar os classificadores para o reconhecimento facial
        :return:
        """
        try:
            self.classificador_haarcascade = cv2.CascadeClassifier(AbsolutePath().getPathHaarcascades())
            self.reconhecidor_facial = cv2.face.LBPHFaceRecognizer_create()
            self.reconhecidor_facial.read(AbsolutePath().getPathClassifire())

            self.cap = None

            self.font_cv2 = cv2.FONT_HERSHEY_COMPLEX_SMALL

            return True
        except Exception as _:
            return False

    def __capture(self) -> None:
        """
        responsavel por fazer a captura com a câmera
        :return:
        """

        status, frame = self.cap.read()
        imagem_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        imagem_colorida = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces_detetadas = self.classificador_haarcascade.detectMultiScale(imagem_cinza,
                                                                          scaleFactor=1.9,
                                                                          minNeighbors=3)
        if status:
            for (x, y, l, a) in faces_detetadas:
                imagem_da_face = cv2.resize(imagem_cinza[y:y + a, x:x + l], (100, 100))
                imagem_colorida = cv2.rectangle(imagem_colorida, (x, y), (x + l, y + a), (22, 22, 22), 1)

                identificador, confinca = self.reconhecidor_facial.predict(imagem_da_face)
                # name = 'NdDaniel'
                font_color = (170, 85, 255)
                cv2.putText(imagem_colorida, self.query_usuario[identificador],
                            (x, y + (a + 30)), self.font_cv2, 1, font_color)

            height, width, channel = imagem_colorida.shape
            step = channel * width
            qimage = QImage(imagem_colorida.data, width, height, step, QImage.Format_RGB888)

            rest = 0
            if width > self.lbl_cam.width():
                rest = (width - self.lbl_cam.width()) / 2
                width = width - rest

            pixmap = QPixmap.fromImage(qimage.copy(rest, 0, width - rest, height))
            self.lbl_cam.setPixmap(pixmap)

    def __changeValueProgressBar(self) -> None:
        """
        responsavel mudar o valor do circular progress bar
        :return:
        """
        if self.VALUE_PROGRESS_BAR == 100:
            self.progress_bar_timer.stop()
            self.stacked_widget_splash_screen.setDirection(Qt.Vertical)
            self.stacked_widget_splash_screen.slideInIdx(0)
            QTimer.singleShot(400, lambda: self.parale_animation.start())
        else:
            self.VALUE_PROGRESS_BAR += 1
            self.widget_cilrcular_progress.value = self.VALUE_PROGRESS_BAR
            self.widget_cilrcular_progress.repaint()

    def __confiCircularProgressBar(self) -> None:
        """
        responsavel por configurar o circular progress bar
        :return:
        """
        self.widget_cilrcular_progress.width = 200
        self.widget_cilrcular_progress.height = 200
        self.widget_cilrcular_progress.value = 0
        self.widget_cilrcular_progress.font_size = 12
        self.widget_cilrcular_progress.progress_width = 6
        self.widget_cilrcular_progress.ad_shadow(True)
        self.widget_cilrcular_progress.progress_color = 0x202124
        self.widget_cilrcular_progress.text_color = 0xE9EAEC
        self.widget_cilrcular_progress.move(200, 100)

    def __resizeSplashCreen(self) -> None:
        """
        responsavel por criar a animação de espanção da tela
        :return:
        """

        self.parale_animation = QParallelAnimationGroup()

        self.animation_min = QPropertyAnimation(self.frame_continer_base, b'minimumWidth')
        self.animation_min.setStartValue(290)
        self.animation_min.setDuration(700)
        self.animation_min.setEndValue(568)
        self.animation_min.setEasingCurve(QEasingCurve.Type.InOutExpo)
        self.parale_animation.addAnimation(self.animation_min)

        self.animation_max = QPropertyAnimation(self.frame_continer_base, b'maximumWidth')
        self.animation_max.setStartValue(290)
        self.animation_max.setDuration(700)
        self.animation_max.setEndValue(568)
        self.animation_max.setEasingCurve(QEasingCurve.Type.InOutExpo)
        self.parale_animation.addAnimation(self.animation_max)

    def __moveWindow(self) -> None:
        """
        responsavel por mover a janela de login
        :return:
        """
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self._dragPos)
                self._dragPos = event.globalPosition().toPoint()
                event.accept()

        self.frame_continer_base.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self._dragPos = event.globalPosition().toPoint()

    def __setupUi__(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(586, 489)
        Form.setStyleSheet(u"border-radius: 10px;")
        self.centralwidget = QWidget(Form)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_continer_base = QFrame(self.centralwidget)
        self.frame_continer_base.setObjectName(u"frame_continer_base")
        self.frame_continer_base.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_base.setFrameShadow(QFrame.Raised)
        self.frame_continer_base.setMaximumWidth(290)
        self.frame_continer_base.setMinimumWidth(290)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_continer_base)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stacked_widget_splash_screen = PySlidingStackedWidget(self.frame_continer_base)
        self.stacked_widget_splash_screen.setObjectName(u"stacked_widget_splash_screen")
        self.stacked_widget_splash_screen.setMinimumSize(QSize(282, 453))
        self.stacked_widget_splash_screen.setMaximumSize(QSize(282, 453))
        self.stacked_widget_splash_screen.setStyleSheet(u"background-color: rgb(54, 63, 118)")
        self.stacked_widget_splash_screen.setFrameShape(QFrame.StyledPanel)
        self.stacked_widget_splash_screen.setFrameShadow(QFrame.Raised)
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.verticalLayout = QVBoxLayout(self.page_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.img = QPushButton(self.page_main)
        self.img.setObjectName(u"img")
        icon = QIcon()
        icon.addFile(u"../../../../../../../DriverTerabox/ajutes/objetos-removebg-preview-ajustu2.png", QSize(),
                     QIcon.Normal, QIcon.Off)
        self.img.setIcon(icon)
        self.img.setIconSize(QSize(260, 260))

        self.verticalLayout.addWidget(self.img)

        self.stacked_widget_splash_screen.addWidget(self.page_main)
        self.page_circular_progress_bar = QWidget()
        self.page_circular_progress_bar.setObjectName(u"page_circular_progress_bar")
        self.verticalLayout_2 = QVBoxLayout(self.page_circular_progress_bar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_conttiner = QWidget(self.page_circular_progress_bar)
        self.widget_conttiner.setObjectName(u"widget_conttiner")
        self.widget_conttiner.setMinimumSize(QSize(264, 260))
        self.widget_conttiner.setMaximumSize(QSize(264, 260))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_conttiner)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_cilrcular_progress = PyCircularProgress(self.widget_conttiner)
        self.widget_cilrcular_progress.setObjectName(u"widget_cilrcular_progress")
        self.widget_cilrcular_progress.setMinimumSize(QSize(200, 200))
        self.widget_cilrcular_progress.setMaximumSize(QSize(200, 200))
        self.widget_cilrcular_progress.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.widget_cilrcular_progress)

        self.verticalLayout_2.addWidget(self.widget_conttiner)

        self.stacked_widget_splash_screen.addWidget(self.page_circular_progress_bar)

        self.page_cam = QWidget()
        self.page_cam.setObjectName(u"page_cam")
        self.verticalLayout_3 = QVBoxLayout(self.page_cam)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.lbl_cam = QLabel(self.page_cam)
        self.lbl_cam.setObjectName(u"lbl_cam")

        self.verticalLayout_3.addWidget(self.lbl_cam)

        self.stacked_widget_splash_screen.addWidget(self.page_cam)

        self.horizontalLayout_2.addWidget(self.stacked_widget_splash_screen)

        self.frame_login = QFrame(self.frame_continer_base)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setMaximumSize(QSize(269, 435))
        self.frame_login.setStyleSheet(u"#frame_login{background-color: rgb(23, 24, 26);\n"
                                       "border-top-left-radius: 0px;\n"
                                       "border-bottom-left-radius: 0px;\n"
                                       "}\n"
                                       "\n"
                                       "#btn_login{\n"
                                       "    border-radius: 7px;\n"
                                       "    background-color: rgb(32, 33, 36);\n"
                                       "    color: white;padding-left:5px;}\n"
                                       "\n"
                                       "\n"
                                       "#btn_fingerprint, #btn_faceid\n"
                                       "{background-color: rgb(54, 63, 118);}\n"
                                       "\n"
                                       "#btn_fingerprint:hover, #btn_faceid:hover\n"
                                       "{background-color: rgb(50, 59, 110)}\n"
                                       "\n"
                                       "#btn_fingerprint:pressed, #btn_faceid:pressed\n"
                                       "{background-color: rgb(56, 65, 121)}\n"
                                       "\n"
                                       "\n"
                                       "#btn_login:hover{background-color: rgb(30, 31, 34);}\n"
                                       "\n"
                                       "#btn_login:pressed{background-color: rgb(32, 33, 36);}\n"
                                       "\n"
                                       "#btn_close,\n"
                                       "#btn_minimizar{\n"
                                       "	background-color: rgba(54, 63, 118, 120);\n"
                                       "	border-radius:4px;}\n"
                                       "\n"
                                       "#btn_close::hover,\n"
                                       "#btn_minimizar::hover{\n"
                                       "	background-color: rgba(54, 63, 118, 150);}\n"
                                       "\n"
                                       "#btn_close:pressed,\n"
                                       "#btn_minimizar:pressed{\n"
                                       "	background-color: rgba(54, 63, 118, 120);}\n"
                                       "\n"
                                       "\n"
                                       "QPushButton{\n"
                                       "	background-c"
                                       "olor:  rgb(19, 20, 22);\n"
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
        self.let_senha.setEchoMode(QLineEdit.Password)
        self.lbl_nome = QLabel(self.frame_login)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setGeometry(QRect(30, 102, 100, 17))
        self.lbl_nome.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbl_senha = QLabel(self.frame_login)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setGeometry(QRect(30, 180, 49, 16))
        self.lbl_senha.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_login = QPushButton(self.frame_login)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(30, 280, 210, 35))
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minimizar = QPushButton(self.frame_login)
        self.btn_minimizar.setObjectName(u"btn_minimizar")
        self.btn_minimizar.setGeometry(QRect(205, 5, 27, 27))
        self.btn_minimizar.setMinimumSize(QSize(27, 27))
        self.btn_minimizar.setMaximumSize(QSize(27, 27))
        self.btn_minimizar.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"../../../images/svg_icons/icon_minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimizar.setIcon(icon1)
        self.btn_minimizar.setIconSize(QSize(18, 18))
        self.btn_close = QPushButton(self.frame_login)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(237, 5, 27, 27))
        self.btn_close.setMinimumSize(QSize(27, 27))
        self.btn_close.setMaximumSize(QSize(27, 27))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"../../../images/svg_icons/icon_close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setIconSize(QSize(20, 20))
        self.btn_fingerprint = QPushButton(self.frame_login)
        self.btn_fingerprint.setObjectName(u"btn_fingerprint")
        self.btn_fingerprint.setGeometry(QRect(80, 360, 40, 40))
        self.btn_fingerprint.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.lbl_ola.setGeometry(QRect(30, 30, 400, 21))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.lbl_ola.setFont(font1)
        self.lbl_ola.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbl_bemvindo = QLabel(self.frame_login)
        self.lbl_bemvindo.setObjectName(u"lbl_bemvindo")
        self.lbl_bemvindo.setGeometry(QRect(30, 60, 150, 19))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.lbl_bemvindo.setFont(font2)
        self.lbl_bemvindo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_faceid = QPushButton(self.frame_login)
        self.btn_faceid.setObjectName(u"btn_faceid")
        self.btn_faceid.setGeometry(QRect(150, 360, 40, 40))
        self.btn_faceid.setCursor(QCursor(Qt.PointingHandCursor))
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

        Form.setCentralWidget(self.centralwidget)

        self.__retranslateUi(Form)

        self.stacked_widget_splash_screen.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(Form)

    def __retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"MainWindow", None))
        self.let_nome.setPlaceholderText(QCoreApplication.translate("Form", u"Digite seu nome", None))
        self.let_senha.setPlaceholderText(QCoreApplication.translate("Form", u"Digite sua senha", None))
        self.lbl_nome.setText(QCoreApplication.translate("Form", u"Nome de usario *", None))
        self.lbl_senha.setText(QCoreApplication.translate("Form", u"Senha *", None))
        self.btn_login.setText(QCoreApplication.translate("Form", u"Login", None))
        self.lbl_ou.setText(QCoreApplication.translate("Form", u"OU", None))
        self.lbl_ola.setText(QCoreApplication.translate("Form", u"Ol\u00c1", None))
        self.lbl_bemvindo.setText(QCoreApplication.translate("Form", u"Bem-vindo de volta!", None))
        self.lbl_entrar.setText(QCoreApplication.translate("Form", u"Entrar *", None))



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = Ui_LoginWindow()
    win.show()
    win.progress_bar_timer.start()
    sys.exit(app.exec())
