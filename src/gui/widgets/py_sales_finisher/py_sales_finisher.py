# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'finalizador_de_vendaRadmXZ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(433, 362)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(184, 184, 185);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_center = QFrame(self.frame_2)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setMinimumSize(QSize(431, 360))
        self.frame_center.setMaximumSize(QSize(431, 360))
        self.frame_center.setStyleSheet(u"QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #26272b;\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(64, 80, 170, 150);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgba(64, 80, 170, 190);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #313237;\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #313237;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: m"
                        "argin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"	 border: none;\n"
"     background: #26272b;\n"
"     width: 8px;\n"
"     margin: 21px 0 21px 0;\n"
"	 border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgba(64, 80, 170, 150);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgba(64, 80, 170, 190);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"     background: #313237;\n"
"     height: 20px;\n"
"	 border-bottom-left-radius: 4px;\n"
"     border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	 border: none;\n"
"     background: #3"
                        "13237;\n"
"     height: 20px;\n"
"	 border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
"}\n"
"")
        self.frame_center.setFrameShape(QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_center)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame_30 = QFrame(self.frame_center)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_30)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(4, 4, 4, 4)
        self.frame_57 = QFrame(self.frame_30)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setStyleSheet(u"background-color: rgb(19, 20, 22);\n"
"border-radius:10px;")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.vertical_layout_inventario_2 = QVBoxLayout(self.frame_57)
        self.vertical_layout_inventario_2.setSpacing(0)
        self.vertical_layout_inventario_2.setObjectName(u"vertical_layout_inventario_2")
        self.vertical_layout_inventario_2.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.frame_57)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QPushButton{\n"
"	background-color:  rgb(32, 33, 36);\n"
"	border-radius:7px;\n"
"	border: 1px solid rgb(47, 54, 100);\n"
"	color: #ffffff}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(28, 29, 32)}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(19, 20, 22)}\n"
"\n"
"\n"
"QLineEdit{\n"
"border: 1px solid rgb(47, 54, 100);\n"
"border-radius: 5px;\n"
"background-color: rgb(32, 33, 36);\n"
"color: white;padding-left:5px;}\n"
"\n"
"QLineEdit:hover{background-color: rgb(30, 31, 34);}\n"
"\n"
"QLineEdit:focus{background-color: rgb(37, 39, 42);}\n"
"\n"
"\n"
"QComboBox{\n"
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
"    border-bottom: 1px solid rgba"
                        "(0, 0, 0, 0.073);\n"
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
"	selection-background-color: rgb(195, 155, 255);\n"
"	border: 2px solid  rgb(47, 54, 100);\n"
"	border-radius:5px;}\n"
"\n"
"QLabel{color:#ffffff}\n"
"\n"
"QCheckBox{color: rgb(255, 255, 255);}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.combo_box_unidade = QComboBox(self.frame)
        self.combo_box_unidade.addItem("")
        self.combo_box_unidade.addItem("")
        self.combo_box_unidade.addItem("")
        self.combo_box_unidade.setObjectName(u"combo_box_unidade")
        self.combo_box_unidade.setGeometry(QRect(5, 10, 394, 37))
        self.combo_box_unidade.setMinimumSize(QSize(0, 37))
        font = QFont()
        font.setPointSize(10)
        self.combo_box_unidade.setFont(font)
        self.combo_box_unidade.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo_box_unidade.setEditable(False)
        self.combo_box_unidade.setMinimumContentsLength(0)
        self.combo_box_unidade.setDuplicatesEnabled(False)
        self.lineEdit_nome_produto = QLineEdit(self.frame)
        self.lineEdit_nome_produto.setObjectName(u"lineEdit_nome_produto")
        self.lineEdit_nome_produto.setGeometry(QRect(5, 210, 394, 37))
        self.lineEdit_nome_produto.setMinimumSize(QSize(0, 30))
        self.lineEdit_nome_produto.setFont(font)
        self.combo_box_categoria = QComboBox(self.frame)
        self.combo_box_categoria.addItem("")
        self.combo_box_categoria.addItem("")
        self.combo_box_categoria.addItem("")
        self.combo_box_categoria.setObjectName(u"combo_box_categoria")
        self.combo_box_categoria.setGeometry(QRect(5, 60, 394, 37))
        self.combo_box_categoria.setMinimumSize(QSize(0, 37))
        self.combo_box_categoria.setFont(font)
        self.combo_box_categoria.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo_box_categoria.setEditable(False)
        self.combo_box_categoria.setMinimumContentsLength(0)
        self.combo_box_categoria.setDuplicatesEnabled(False)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 120, 140, 18))
        font1 = QFont()
        font1.setPointSize(11)
        self.label.setFont(font1)
        self.check_box_recibo_venda = QCheckBox(self.frame)
        self.check_box_recibo_venda.setObjectName(u"check_box_recibo_venda")
        self.check_box_recibo_venda.setGeometry(QRect(17, 150, 135, 20))
        self.lb_valor_pagamento = QLabel(self.frame)
        self.lb_valor_pagamento.setObjectName(u"lb_valor_pagamento")
        self.lb_valor_pagamento.setGeometry(QRect(10, 185, 381, 18))
        self.lb_valor_pagamento.setFont(font1)
        self.lbl_troco = QLabel(self.frame)
        self.lbl_troco.setObjectName(u"lbl_troco")
        self.lbl_troco.setGeometry(QRect(10, 260, 381, 18))
        self.lbl_troco.setFont(font1)
        self.frame_custom_cliente = QFrame(self.frame)
        self.frame_custom_cliente.setObjectName(u"frame_custom_cliente")
        self.frame_custom_cliente.setGeometry(QRect(5, 8, 394, 42))
        self.frame_custom_cliente.setStyleSheet(u"QPushButton{border-top-left-radius:0px;border-bottom-left-radius:0px;}\n"
"QLineEdit{border-top-right-radius:0px;border-bottom-right-radius:0px;}")
        self.frame_custom_cliente.setFrameShape(QFrame.StyledPanel)
        self.frame_custom_cliente.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_custom_cliente)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_cliente = QLineEdit(self.frame_custom_cliente)
        self.lineEdit_cliente.setObjectName(u"lineEdit_cliente")
        self.lineEdit_cliente.setMinimumSize(QSize(0, 37))
        self.lineEdit_cliente.setFont(font)

        self.horizontalLayout_5.addWidget(self.lineEdit_cliente)

        self.btn_show_cliente = QPushButton(self.frame_custom_cliente)
        self.btn_show_cliente.setObjectName(u"btn_show_cliente")
        self.btn_show_cliente.setMinimumSize(QSize(37, 37))
        self.btn_show_cliente.setMaximumSize(QSize(37, 37))
        icon = QIcon()
        icon.addFile(u"../../../images/svg_icons/icon_down_arrow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_show_cliente.setIcon(icon)
        self.btn_show_cliente.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.btn_show_cliente)

        self.frame_custom_pagamento = QFrame(self.frame)
        self.frame_custom_pagamento.setObjectName(u"frame_custom_pagamento")
        self.frame_custom_pagamento.setGeometry(QRect(5, 58, 394, 41))
        self.frame_custom_pagamento.setStyleSheet(u"QPushButton{border-top-left-radius:0px;border-bottom-left-radius:0px;}\n"
"QLineEdit{border-top-right-radius:0px;border-bottom-right-radius:0px;}")
        self.frame_custom_pagamento.setFrameShape(QFrame.StyledPanel)
        self.frame_custom_pagamento.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_custom_pagamento)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_pagamento = QLineEdit(self.frame_custom_pagamento)
        self.lineEdit_pagamento.setObjectName(u"lineEdit_pagamento")
        self.lineEdit_pagamento.setMinimumSize(QSize(0, 37))
        self.lineEdit_pagamento.setFont(font)
        self.lineEdit_pagamento.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.lineEdit_pagamento)

        self.btn_show_pagamento = QPushButton(self.frame_custom_pagamento)
        self.btn_show_pagamento.setObjectName(u"btn_show_pagamento")
        self.btn_show_pagamento.setMinimumSize(QSize(37, 37))
        self.btn_show_pagamento.setMaximumSize(QSize(37, 37))
        self.btn_show_pagamento.setStyleSheet(u"")
        self.btn_show_pagamento.setIcon(icon)
        self.btn_show_pagamento.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_show_pagamento)


        self.vertical_layout_inventario_2.addWidget(self.frame)

        self.frame_90 = QFrame(self.frame_57)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(0, 44))
        self.frame_90.setMaximumSize(QSize(16777215, 44))
        self.frame_90.setStyleSheet(u"")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_26.setSpacing(4)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(4, 4, 4, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer)

        self.btn_deletar = QPushButton(self.frame_90)
        self.btn_deletar.setObjectName(u"btn_deletar")
        self.btn_deletar.setMinimumSize(QSize(37, 37))
        self.btn_deletar.setMaximumSize(QSize(37, 37))
        self.btn_deletar.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: rgb(38, 39, 43);\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}\n"
" QPushButton:hover {\n"
" 	background-color: rgb(49, 50, 55)\n"
" }\n"
"QPushButton:pressed {\n"
" 	background-color: rgb(38, 39, 43);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../../images/svg_icons/icon_delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_deletar.setIcon(icon1)
        self.btn_deletar.setIconSize(QSize(25, 25))

        self.horizontalLayout_26.addWidget(self.btn_deletar)

        self.btn_confirmar = QPushButton(self.frame_90)
        self.btn_confirmar.setObjectName(u"btn_confirmar")
        self.btn_confirmar.setMinimumSize(QSize(37, 37))
        self.btn_confirmar.setMaximumSize(QSize(37, 37))
        self.btn_confirmar.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: rgb(38, 39, 43);\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}\n"
" QPushButton:hover {\n"
" 	background-color: rgb(49, 50, 55)\n"
" }\n"
"QPushButton:pressed {\n"
" 	background-color: rgb(38, 39, 43);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../../../images/svg_icons/icon_check_ok.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_confirmar.setIcon(icon2)
        self.btn_confirmar.setIconSize(QSize(25, 25))

        self.horizontalLayout_26.addWidget(self.btn_confirmar)


        self.vertical_layout_inventario_2.addWidget(self.frame_90)


        self.verticalLayout_18.addWidget(self.frame_57)


        self.verticalLayout_2.addWidget(self.frame_30)


        self.verticalLayout_3.addWidget(self.frame_center, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form)

        self.combo_box_unidade.setCurrentIndex(-1)
        self.combo_box_categoria.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.combo_box_unidade.setItemText(0, QCoreApplication.translate("Form", u"New Item", None))
        self.combo_box_unidade.setItemText(1, QCoreApplication.translate("Form", u"New Item", None))
        self.combo_box_unidade.setItemText(2, QCoreApplication.translate("Form", u"New Item", None))

        self.combo_box_unidade.setCurrentText("")
        self.combo_box_unidade.setPlaceholderText(QCoreApplication.translate("Form", u"Cliente (opcinal)", None))
        self.lineEdit_nome_produto.setPlaceholderText(QCoreApplication.translate("Form", u"Pagamento (opcional)", None))
        self.combo_box_categoria.setItemText(0, QCoreApplication.translate("Form", u"New Item", None))
        self.combo_box_categoria.setItemText(1, QCoreApplication.translate("Form", u"New Item", None))
        self.combo_box_categoria.setItemText(2, QCoreApplication.translate("Form", u"New Item", None))

        self.combo_box_categoria.setCurrentText("")
        self.combo_box_categoria.setPlaceholderText(QCoreApplication.translate("Form", u"Metodo de pagamento", None))
        self.label.setText(QCoreApplication.translate("Form", u"Valor de pagamento", None))
        self.check_box_recibo_venda.setText(QCoreApplication.translate("Form", u"Criar recibo de venda", None))
        self.lb_valor_pagamento.setText(QCoreApplication.translate("Form", u"16.000.00", None))
        self.lbl_troco.setText(QCoreApplication.translate("Form", u"Troco:  3.000", None))
        self.lineEdit_cliente.setPlaceholderText(QCoreApplication.translate("Form", u"Cliente (opcional)", None))
        self.btn_show_cliente.setText("")
        self.lineEdit_pagamento.setPlaceholderText(QCoreApplication.translate("Form", u"Metodo de pagamento", None))
        self.btn_show_pagamento.setText("")
        self.btn_deletar.setText("")
        self.btn_confirmar.setText("")
    # retranslateUi

