# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro_produtoyMjAHS.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
import locale
import platform
from src.qt_core import *
from qfluentwidgets import SpinBox
from src.gui.core.imagepath import ImagePath
from src.gui.widgets.py_editable_comboBox.editable_combo_box import PyEditableComboBox
from src.gui.widgets.py_slide_stacked_widgets.py_slide_stacked_widgets import PySlidingStackedWidget

class PyProductRegistration(QWidget):
    def __init__(self, widget=None) -> None:
        super().__init__(widget)

        self.setupUi(self)
        self.validator()

        # self.frame_style.mousePressEvent = lambda e: self.close()
        # clia um algoritmo que resolve o probema so cera deletado se estiver fora do quadrado

        self.btn_activate.setGeometry(
            self.btn_nav_camera.x() + self.frame_segmented_nave.x() + 3,
            self.btn_nav_camera.y() + self.frame_segmented_nave.y() + 3,
            40, 40
        )

        self.image.clicked.connect(self.openfile)

        self.btn_nav_key.clicked.connect(self.changePosition)
        self.btn_nav_info.clicked.connect(self.changePosition)
        self.btn_nav_camera.clicked.connect(self.changePosition)
        self.btn_nav_edit.clicked.connect(self.changePosition)

    def openfile(self):

        languege = str(locale.getlocale()[0].lower())
        path = '~\Imagens'

        if 'en' in languege:
            path = '~\Pictures'

        path = os.path.expanduser(path)
        path = os.path.normpath(path)

        file = QFileDialog.getOpenFileName(
            parent=self,
            dir=path,
            filter=self.tr('img file (*.png *.jpeg *.jpg *.PNG *.JPG) ')
        )

        if file[0]:
            icon = QIcon()
            icon.addFile(file[0])

            self.image.setIconSize(QSize(250, 250))
            self.icon_img.setIconSize(QSize(30, 30))

            self.image.setIcon(icon)
            self.icon_img.setIcon(icon)

    def validator(self) -> None:
        """
        método de validação usando Expressões regulares
        :return:
        """
        regex_nu = QRegularExpressionValidator(QRegularExpression("^[0-9]*$"), self)
        self.lineEdit_chave.setValidator(regex_nu)
        self.lineEdit_unidade.setValidator(regex_nu)
        self.lineEdit_quantidade.setValidator(regex_nu)
        self.lineEdit_preco_venda.setValidator(regex_nu)
        self.lineEdit_preco_compra.setValidator(regex_nu)
        self.lineEdit_quantidade_reserva.setValidator(regex_nu)

    def changePosition(self):
        btn = self.sender()

        btn.repaint()
        self.posAnimation = QPropertyAnimation(self.btn_activate, b'pos')
        self.posAnimation.setStartValue(QPoint(self.btn_activate.x(), self.btn_activate.y()))
        self.posAnimation.setDuration(400)
        self.posAnimation.setEndValue(QPoint(btn.x() + self.frame_segmented_nave.x(), btn.y() + self.frame_segmented_nave.y()))
        self.posAnimation.setEasingCurve(QEasingCurve.Type.InOutExpo)
        self.posAnimation.finished.connect(self.btn_activate.setIcon(btn.icon()))
        self.posAnimation.start()

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(298, 455)
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_style = QFrame(Form)
        self.frame_style.setObjectName(u"frame_style")
        self.frame_style.setStyleSheet(u"#frame_style{\n"
                                        "   border-radius: 10px;\n"
                                        "   background-color: rgba(19, 20, 22, 50);}\n"
                                       "QStackedWidget, #btn_calendario, #icon_tag{\n"
                                       "	background-color: transparent;}\n"
                                       "\n"
                                       "#frame_chave_qrcode, #btn_chave_qrcode,\n"
                                       "#frame_continer_prima_info, #frame_quantidade,\n"
                                       "#frame_continer_preco, #frame_continer_information_adicionais{\n"
                                       "	background-color: rgb(23, 24, 26);\n"
                                       "	border-radius: 7px;}\n"
                                       "\n"
                                       "#frame_central{\n"
                                       "	background-color: rgb(19, 20, 22);\n"
                                       "	border-radius: 7px;}\n"
                                       "\n"
                                       "#btn_chave_qrcode{\n"
                                       "	background-color: rgb(32, 33, 37);\n"
                                       "	border-radius:7px;\n"
                                       "	border: 1px solid rgb(47, 54, 100)}\n"
                                       "\n"
                                       "#btn_chave_qrcode:hover{background-color: rgb(39, 40, 45);}\n"
                                       "\n"
                                       "#btn_chave_qrcode:pressed{background-color: rgb(35, 36, 41);}\n"
                                       "\n"
                                       "#informacoes_adicionais, #frame_preco_adicional,\n"
                                       "#frame_calendario, #frame_preco_adicional {\n"
                                       "	border: 1px solid rgb(47, 54, 100);\n"
                                       "	background-color: rgb(34, 35, 38);\n"
                                       "	border-radius: 6px;\n"
                                       "	color: rgb(233, 234, 236);\n"
                                       "	padding-left:5px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton{\n"
                                       "	background-color:  rgb(19, 20, 22);\n"
                                       "	border"
                                       "-radius:7px;}\n"
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
                                       "\n"
                                       "\n"
                                       "#btn_add_data, #btn_add_preco{\n"
                                       "background-color: rgb(24, 25, 27);\n"
                                       "border-radius:17px;\n"
                                       "color: rgb(233, 234, 236);}\n"
                                       "\n"
                                       "#btn_add_data:hover, #btn_add_preco:hover{background-color: rgb(39, 40, 45);}\n"
                                       "\n"
                                       "#btn_add_data:pressed, #btn_add_preco:pressed{background-color: rgb(35, 36, 41);}")
        self.frame_style.setFrameShape(QFrame.StyledPanel)
        self.frame_style.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_style)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_central = QFrame(self.frame_style)
        self.frame_central.setObjectName(u"frame_central")
        self.frame_central.setMinimumSize(QSize(296, 452))
        self.frame_central.setMaximumSize(QSize(296, 452))
        self.frame_central.setFrameShape(QFrame.StyledPanel)
        self.frame_central.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_central)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = PySlidingStackedWidget(self.frame_central)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_foto = QWidget()
        self.page_foto.setObjectName(u"page_foto")
        self.image = QPushButton(self.page_foto)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(40, 30, 220, 390))
        self.image.setStyleSheet(u"background-color: transparent;\n"
                                 "border-radius: 12px;")
        icon = QIcon()
        icon.addFile(ImagePath().set_svg_icon("icon_gallery.svg"))
        self.image.setIcon(icon)
        self.image.setIconSize(QSize(25, 25))
        self.icon_img = QPushButton(self.page_foto)
        self.icon_img.setObjectName(u"icon_img")
        self.icon_img.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img.setMinimumSize(QSize(37, 37))
        self.icon_img.setMaximumSize(QSize(37, 37))
        self.icon_img.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
                                    "border-radius:7px;\n"
                                    "color: #ffffff;\n"
                                    "border: 1px solid rgb(255, 255, 255)")
        self.icon_img.setIcon(icon)
        self.icon_img.setIconSize(QSize(18, 18))
        self.frame_segmented_nave = QFrame(self.page_foto)
        self.frame_segmented_nave.setObjectName(u"frame_nave_bar_2")
        self.frame_segmented_nave.setGeometry(QRect(60, 390, 182, 47))
        self.frame_segmented_nave.setMinimumSize(QSize(100, 30))
        self.frame_segmented_nave.setMaximumSize(QSize(1234578, 16777215))
        self.frame_segmented_nave.setStyleSheet(u"QFrame{background-color: rgb(19, 20, 22);}\n"
                                            "QPushButton{\n"
                                            "background-color: rgb(19, 20, 22);\n"
                                            "color: rgb(233, 234, 236);}\n"
                                            "\n"
                                            "QPushButton:hover{background-color: rgb(39, 40, 45);}\n"
                                            "\n"
                                            "QPushButton:pressed{background-color: rgb(35, 36, 41);}")
        self.frame_segmented_nave.setFrameShape(QFrame.StyledPanel)
        self.frame_segmented_nave.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_segmented_nave)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 0, 5, 0)
        self.btn_nav_camera = QPushButton(self.frame_segmented_nave)
        self.btn_nav_camera.setObjectName(u"btn_nav_camera")
        self.btn_nav_camera.setMinimumSize(QSize(40, 40))
        self.btn_nav_camera.setMaximumSize(QSize(40, 40))
        self.btn_nav_camera.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(ImagePath().set_svg_icon("icon_camera.svg"))
        self.btn_nav_camera.setIcon(icon1)
        self.btn_nav_camera.setIconSize(QSize(27, 27))

        self.horizontalLayout_3.addWidget(self.btn_nav_camera)

        self.btn_nav_key = QPushButton(self.frame_segmented_nave)
        self.btn_nav_key.setObjectName(u"btn_nav_key")
        self.btn_nav_key.setMinimumSize(QSize(40, 40))
        self.btn_nav_key.setMaximumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(ImagePath().set_svg_icon("icon_key.svg"))
        self.btn_nav_key.setIcon(icon2)
        self.btn_nav_key.setIconSize(QSize(27, 27))

        self.horizontalLayout_3.addWidget(self.btn_nav_key)

        self.btn_nav_edit = QPushButton(self.frame_segmented_nave)
        self.btn_nav_edit.setObjectName(u"btn_nav_edit")
        self.btn_nav_edit.setMinimumSize(QSize(40, 40))
        self.btn_nav_edit.setMaximumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(ImagePath().set_svg_icon("icon_edit_text.svg"))
        self.btn_nav_edit.setIcon(icon3)
        self.btn_nav_edit.setIconSize(QSize(27, 27))

        self.horizontalLayout_3.addWidget(self.btn_nav_edit)

        self.btn_nav_info = QPushButton(self.frame_segmented_nave)
        self.btn_nav_info.setObjectName(u"btn_nav_info")
        self.btn_nav_info.setMinimumSize(QSize(40, 40))
        self.btn_nav_info.setMaximumSize(QSize(40, 40))
        icon4 = QIcon()
        icon4.addFile(ImagePath().set_svg_icon("icon_info_2.svg"))
        self.btn_nav_info.setIcon(icon4)
        self.btn_nav_info.setIconSize(QSize(28, 28))

        self.horizontalLayout_3.addWidget(self.btn_nav_info)

        self.btn_activate = QPushButton(self.page_foto)
        self.btn_activate.setObjectName(u"btn_activate")
        self.btn_activate.setGeometry(QRect(60, 340, 40, 40))
        self.btn_activate.setMinimumSize(QSize(40, 40))
        self.btn_activate.setMaximumSize(QSize(40, 40))
        self.btn_activate.setStyleSheet(u"QPushButton{\n"
                                        "background-color: rgb(47, 54, 100);\n"
                                        "color: rgb(233, 234, 236);}\n"
                                        "\n"
                                        "QPushButton:hover{background-color: rgb(50, 57, 106);}\n"
                                        "\n"
                                        "QPushButton:pressed{background-color: rgb(48, 55, 102);}\n"
                                        "")
        self.btn_activate.setIcon(icon1)
        self.btn_activate.setIconSize(QSize(27, 27))
        self.stackedWidget.addWidget(self.page_foto)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.frame_nave_bar = QFrame(self.page_3)
        self.frame_nave_bar.setObjectName(u"frame_nave_bar")
        self.frame_nave_bar.setGeometry(QRect(10, 10, 278, 45))
        self.frame_nave_bar.setMinimumSize(QSize(0, 33))
        self.frame_nave_bar.setMaximumSize(QSize(1234578, 16777215))
        self.frame_nave_bar.setStyleSheet(u"QFrame{background-color: rgb(47, 54, 100); border-radius: 7px}\n"
                                          "\n"
                                          "QPushButton{\n"
                                          "background-color: rgb(19, 20, 22);\n"
                                          "color: rgb(233, 234, 236);}\n"
                                          "\n"
                                          "QPushButton:hover{background-color: rgb(39, 40, 45);}\n"
                                          "\n"
                                          "QPushButton:pressed{background-color: rgb(35, 36, 41);}")
        self.frame_nave_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_nave_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_nave_bar)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.btn_ok = QPushButton(self.frame_nave_bar)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setMinimumSize(QSize(10, 33))
        font = QFont()
        font.setPointSize(10)
        self.btn_ok.setFont(font)
        icon5 = QIcon()
        icon5.addFile(ImagePath().set_svg_icon("icon_check_ok.svg"))
        self.btn_ok.setIcon(icon5)
        self.btn_ok.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.btn_ok)

        self.btn_scan = QPushButton(self.frame_nave_bar)
        self.btn_scan.setObjectName(u"btn_scan")
        self.btn_scan.setMinimumSize(QSize(10, 33))
        self.btn_scan.setFont(font)
        icon6 = QIcon()
        icon6.addFile(ImagePath().set_svg_icon("icon_qr_code.svg"))
        self.btn_scan.setIcon(icon6)
        self.btn_scan.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.btn_scan)

        self.btn_add = QPushButton(self.frame_nave_bar)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMinimumSize(QSize(10, 33))
        self.btn_add.setFont(font)
        icon7 = QIcon()
        icon7.addFile(ImagePath().set_svg_icon("icon_add.svg"))
        self.btn_add.setIcon(icon7)
        self.btn_add.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.btn_add)

        self.btn_camera = QPushButton(self.frame_nave_bar)
        self.btn_camera.setObjectName(u"btn_camera")
        self.btn_camera.setMinimumSize(QSize(10, 33))
        self.btn_camera.setFont(font)
        self.btn_camera.setIcon(icon1)
        self.btn_camera.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.btn_camera)

        self.btn_setting = QPushButton(self.frame_nave_bar)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setMinimumSize(QSize(10, 33))
        self.btn_setting.setFont(font)
        icon8 = QIcon()
        icon8.addFile(ImagePath().set_svg_icon("icon_setting.svg"))
        self.btn_setting.setIcon(icon8)
        self.btn_setting.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.btn_setting)

        self.btn_del = QPushButton(self.frame_nave_bar)
        self.btn_del.setObjectName(u"btn_del")
        self.btn_del.setMinimumSize(QSize(10, 33))
        self.btn_del.setFont(font)
        icon9 = QIcon()
        icon9.addFile(ImagePath().set_svg_icon("icon_delete.svg"))
        self.btn_del.setIcon(icon9)
        self.btn_del.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.btn_del)

        self.stackedWidget_2 = PySlidingStackedWidget(self.page_3)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(0, 70, 300, 371))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame_quantidade = QFrame(self.page)
        self.frame_quantidade.setObjectName(u"frame_quantidade")
        self.frame_quantidade.setGeometry(QRect(10, 270, 272, 55))
        self.frame_quantidade.setFrameShape(QFrame.StyledPanel)
        self.frame_quantidade.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_quantidade)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lineEdit_quantidade = QLineEdit(self.frame_quantidade)
        self.lineEdit_quantidade.setObjectName(u"lineEdit_quantidade")
        self.lineEdit_quantidade.setMinimumSize(QSize(0, 37))
        self.lineEdit_quantidade.setFont(font)
        self.lineEdit_quantidade.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lineEdit_quantidade)

        self.lineEdit_quantidade_reserva = QLineEdit(self.frame_quantidade)
        self.lineEdit_quantidade_reserva.setObjectName(u"lineEdit_quantidade_reserva")
        self.lineEdit_quantidade_reserva.setMinimumSize(QSize(0, 37))
        self.lineEdit_quantidade_reserva.setFont(font)
        self.lineEdit_quantidade_reserva.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lineEdit_quantidade_reserva)

        self.frame_chave_qrcode = QFrame(self.page)
        self.frame_chave_qrcode.setObjectName(u"frame_chave_qrcode")
        self.frame_chave_qrcode.setGeometry(QRect(10, 10, 272, 55))
        self.frame_chave_qrcode.setFrameShape(QFrame.StyledPanel)
        self.frame_chave_qrcode.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_chave_qrcode)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit_chave = QLineEdit(self.frame_chave_qrcode)
        self.lineEdit_chave.setObjectName(u"lineEdit_chave")
        self.lineEdit_chave.setMinimumSize(QSize(0, 37))
        self.lineEdit_chave.setFont(font)

        self.horizontalLayout_11.addWidget(self.lineEdit_chave)

        self.btn_chave_qrcode = QPushButton(self.frame_chave_qrcode)
        self.btn_chave_qrcode.setObjectName(u"btn_chave_qrcode")
        self.btn_chave_qrcode.setMinimumSize(QSize(37, 37))
        self.btn_chave_qrcode.setMaximumSize(QSize(37, 37))
        self.btn_chave_qrcode.setIcon(icon6)
        self.btn_chave_qrcode.setIconSize(QSize(22, 22))

        self.horizontalLayout_11.addWidget(self.btn_chave_qrcode)

        self.frame_continer_prima_info = QFrame(self.page)
        self.frame_continer_prima_info.setObjectName(u"frame_continer_prima_info")
        self.frame_continer_prima_info.setGeometry(QRect(10, 90, 272, 160))
        self.frame_continer_prima_info.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_prima_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_continer_prima_info)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lineEdit_unidade = QLineEdit(self.frame_continer_prima_info)
        self.lineEdit_unidade.setObjectName(u"lineEdit_unidade")
        self.lineEdit_unidade.setMinimumSize(QSize(0, 37))
        self.lineEdit_unidade.setFont(font)
        self.lineEdit_unidade.setClearButtonEnabled(False)

        self.verticalLayout_7.addWidget(self.lineEdit_unidade)

        self.combo_box_categoria = PyEditableComboBox(self.frame_continer_prima_info)
        self.combo_box_categoria.addItem("")
        self.combo_box_categoria.addItem("")
        self.combo_box_categoria.addItem("")
        self.combo_box_categoria.setObjectName(u"combo_box_categoria")
        self.combo_box_categoria.setMinimumSize(QSize(0, 37))
        self.combo_box_categoria.setFont(font)
        self.combo_box_categoria.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo_box_categoria.setStyleSheet(u"QComboBox , QLineEdit{\n"
                                               "    border: 1px solid rgb(47, 54, 100);\n"
                                               "    border-radius: 5px;\n"
                                               "    padding-left: 5px;\n"
                                               "    padding-right: -187px;\n"
                                               "	color: rgb(133, 133, 136);\n"
                                               "    background-color: rgb(32, 33, 36);\n"
                                               "    text-align: left;\n"
                                               "}\n"
                                               "\n"
                                               "QComboBox:hover {\n"
                                               "	background-color: rgb(30, 31, 34);\n"
                                               "}\n"
                                               "\n"
                                               "QComboBox:pressed , QComboBox:focus{\n"
                                               "    background-color: rgb(37, 39, 42);\n"
                                               "    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
                                               "	color: rgb(133, 133, 136);\n"
                                               "}\n"
                                               "\n"
                                               "QComboBox:disabled {\n"
                                               "	color: rgb(133, 133, 136);\n"
                                               "    background: rgba(249, 249, 249, 0.3);\n"
                                               "    border: 1px solid rgba(0, 0, 0, 0.06);\n"
                                               "    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
                                               "}\n"
                                               "                        \n"
                                               "QComboBox::drop-down {\n"
                                               "	border-top-right-radius: 5px;\n"
                                               "	border-bottom-right-radius: 5px;\n"
                                               "	width: 34px; }\n"
                                               "\n"
                                               "QComboBox QAbstractItemView {\n"
                                               "	color: rgb(133, 133, 136);\n"
                                               "	background-color: rgb(23, 24, 26);\n"
                                               "	padding: 10px;\n"
                                               "	selection-"
                                               "background-color: rgb(195, 155, 255);\n"
                                               "	border: 2px solid  rgb(47, 54, 100);\n"
                                               "	border-radius:5px;}")
        self.combo_box_categoria.setEditable(False)
        self.combo_box_categoria.setMinimumContentsLength(0)
        self.combo_box_categoria.setDuplicatesEnabled(False)

        self.verticalLayout_7.addWidget(self.combo_box_categoria)

        self.lineEdit_nome_produto = QLineEdit(self.frame_continer_prima_info)
        self.lineEdit_nome_produto.setObjectName(u"lineEdit_nome_produto")
        self.lineEdit_nome_produto.setMinimumSize(QSize(0, 37))
        self.lineEdit_nome_produto.setFont(font)

        self.verticalLayout_7.addWidget(self.lineEdit_nome_produto)

        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame_continer_preco = QFrame(self.page_2)
        self.frame_continer_preco.setObjectName(u"frame_continer_preco")
        self.frame_continer_preco.setGeometry(QRect(10, 10, 272, 55))
        self.frame_continer_preco.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_preco.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_continer_preco)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lineEdit_preco_compra = QLineEdit(self.frame_continer_preco)
        self.lineEdit_preco_compra.setObjectName(u"lineEdit_preco_compra")
        self.lineEdit_preco_compra.setMinimumSize(QSize(0, 37))
        self.lineEdit_preco_compra.setFont(font)
        self.lineEdit_preco_compra.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.lineEdit_preco_compra)

        self.lineEdit_preco_venda = QLineEdit(self.frame_continer_preco)
        self.lineEdit_preco_venda.setObjectName(u"lineEdit_preco_venda")
        self.lineEdit_preco_venda.setMinimumSize(QSize(0, 37))
        self.lineEdit_preco_venda.setFont(font)
        self.lineEdit_preco_venda.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.lineEdit_preco_venda)

        self.frame_continer_information_adicionais = QFrame(self.page_2)
        self.frame_continer_information_adicionais.setObjectName(u"frame_continer_information_adicionais")
        self.frame_continer_information_adicionais.setGeometry(QRect(10, 90, 273, 241))
        self.frame_continer_information_adicionais.setMaximumSize(QSize(286, 262))
        self.frame_continer_information_adicionais.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_information_adicionais.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_continer_information_adicionais)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_preco_adicional = QFrame(self.frame_continer_information_adicionais)
        self.frame_preco_adicional.setObjectName(u"frame_preco_adicional")
        self.frame_preco_adicional.setMaximumSize(QSize(16777215, 80))
        self.frame_preco_adicional.setStyleSheet(u"")
        self.frame_preco_adicional.setFrameShape(QFrame.StyledPanel)
        self.frame_preco_adicional.setFrameShadow(QFrame.Raised)
        self.lbl_tag = QLabel(self.frame_preco_adicional)
        self.lbl_tag.setObjectName(u"lbl_tag")
        self.lbl_tag.setGeometry(QRect(22, 7, 220, 20))
        self.lbl_tag.setFont(font)
        self.lbl_tag.setStyleSheet(u"color: rgb(134, 134, 137)")
        self.btn_add_preco = QPushButton(self.frame_preco_adicional)
        self.btn_add_preco.setObjectName(u"btn_add_preco")
        self.btn_add_preco.setGeometry(QRect(215, 40, 35, 35))
        self.btn_add_preco.setLayoutDirection(Qt.RightToLeft)
        self.btn_add_preco.setIcon(icon7)
        self.btn_add_preco.setIconSize(QSize(33, 33))
        self.icon_tag = QPushButton(self.frame_preco_adicional)
        self.icon_tag.setObjectName(u"icon_tag")
        self.icon_tag.setGeometry(QRect(3, 6, 20, 24))
        icon10 = QIcon()
        icon10.addFile(ImagePath().set_svg_icon("icon_tag.svg"))
        self.icon_tag.setIcon(icon10)
        self.icon_tag.setIconSize(QSize(17, 17))

        self.verticalLayout_9.addWidget(self.frame_preco_adicional)

        self.frame_calendario = QFrame(self.frame_continer_information_adicionais)
        self.frame_calendario.setObjectName(u"frame_calendario")
        self.frame_calendario.setMaximumSize(QSize(16777215, 80))
        self.frame_calendario.setFrameShape(QFrame.StyledPanel)
        self.frame_calendario.setFrameShadow(QFrame.Raised)
        self.lbl_calendario = QLabel(self.frame_calendario)
        self.lbl_calendario.setObjectName(u"lbl_calendario")
        self.lbl_calendario.setGeometry(QRect(22, 7, 230, 16))
        self.lbl_calendario.setFont(font)
        self.lbl_calendario.setStyleSheet(u"color: rgb(134, 134, 137)")
        self.btn_add_data = QPushButton(self.frame_calendario)
        self.btn_add_data.setObjectName(u"btn_add_data")
        self.btn_add_data.setGeometry(QRect(215, 40, 35, 35))
        self.btn_add_data.setLayoutDirection(Qt.RightToLeft)
        self.btn_add_data.setIcon(icon7)
        self.btn_add_data.setIconSize(QSize(31, 31))
        self.btn_calendario = QPushButton(self.frame_calendario)
        self.btn_calendario.setObjectName(u"btn_calendario")
        self.btn_calendario.setGeometry(QRect(2, 4, 20, 20))
        icon11 = QIcon()
        icon11.addFile(ImagePath().set_svg_icon("icon_service.svg"))
        self.btn_calendario.setIcon(icon11)
        self.btn_calendario.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.frame_calendario)

        self.informacoes_adicionais = QPlainTextEdit(self.frame_continer_information_adicionais)
        self.informacoes_adicionais.setObjectName(u"informacoes_adicionais")
        self.informacoes_adicionais.setMaximumSize(QSize(16777215, 55))
        self.informacoes_adicionais.setFont(font)

        self.verticalLayout_9.addWidget(self.informacoes_adicionais)

        self.stackedWidget_2.addWidget(self.page_2)
        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_6.addWidget(self.stackedWidget)

        self.verticalLayout_2.addWidget(self.frame_central, 0, Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.frame_style)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.combo_box_categoria.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(Form)
        # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.image.setText("")
        self.icon_img.setText("")
        self.btn_nav_camera.setText("")
        self.btn_nav_key.setText("")
        self.btn_nav_edit.setText("")
        self.btn_nav_info.setText("")
        self.btn_activate.setText("")
        self.btn_ok.setText("")
        self.btn_scan.setText("")
        self.btn_add.setText("")
        self.btn_camera.setText("")
        self.btn_setting.setText("")
        self.btn_del.setText("")
        self.lineEdit_quantidade.setPlaceholderText(QCoreApplication.translate("Form", u"Quantidade", None))
        self.lineEdit_quantidade_reserva.setPlaceholderText(
            QCoreApplication.translate("Form", u"Quantidade Reserva", None))
        self.lineEdit_chave.setPlaceholderText(QCoreApplication.translate("Form", u"Chave", None))
        self.btn_chave_qrcode.setText("")
        self.lineEdit_unidade.setPlaceholderText(QCoreApplication.translate("Form", u"Unidade", None))
        self.combo_box_categoria.setItemText(0, QCoreApplication.translate("Form", u"New Item", None))
        self.combo_box_categoria.setItemText(1, QCoreApplication.translate("Form", u"New Item", None))
        self.combo_box_categoria.setItemText(2, QCoreApplication.translate("Form", u"New Item", None))

        self.combo_box_categoria.setCurrentText("")
        self.combo_box_categoria.setPlaceholderText(QCoreApplication.translate("Form", u"Categoria", None))
        self.lineEdit_nome_produto.setPlaceholderText(QCoreApplication.translate("Form", u"Nome do produto", None))
        self.lineEdit_preco_compra.setPlaceholderText(QCoreApplication.translate("Form", u"Pre\u00e7o de compra", None))
        self.lineEdit_preco_venda.setPlaceholderText(QCoreApplication.translate("Form", u"Pre\u00e7o de venda", None))
        self.lbl_tag.setText(QCoreApplication.translate("Form", u"Pre\u00e7os adicional de venda(opcional)", None))
        self.btn_add_preco.setText("")
        self.icon_tag.setText("")
        self.lbl_calendario.setText(
            QCoreApplication.translate("Form", u"Data de expira\u00e7\u00e3o do produto(opcional)", None))
        self.btn_add_data.setText("")
        self.btn_calendario.setText("")
        self.informacoes_adicionais.setPlaceholderText(
            QCoreApplication.translate("Form", u"Informa\u00e7\u00f5es adicionais sobre o produto (opcional)", None))
    # retranslateUi



if __name__ == '__main__':
    import sys
    app = QApplication([])
    window = PyProductRegistration()
    window.show()
    sys.exit(app.exec())