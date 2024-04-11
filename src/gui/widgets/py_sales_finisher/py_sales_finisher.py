# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'finalizador_de_vendaRadmXZ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from src.qt_core import *
from src.gui.core.database import DataBase
from src.gui.core.absolute_path import AbsolutePath


class PySalesFinisher(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__setupUi(self)
        self.__autoInsertDados()
        self.__validator()
        self.setStyleSheet(u"QFrame{background-color: rgba(0, 0, 0, 0);}")

        self.can_close: bool = False

        self.btn_show_pagamento.clicked.connect(self.combo_box_pagamento.showPopup)
        self.btn_show_cliente.clicked.connect(self.combo_box_cliente.showPopup)
        self.combo_box_cliente.currentTextChanged.connect(self.__setClienteSelected)
        self.combo_box_pagamento.currentTextChanged.connect(self.__setPagamentoSelected)
        self.lineEdit_cliente.returnPressed.connect(self.__insertCliente)
        self.lineEdit_pagamento.returnPressed.connect(self.__insertPagamento)
        self.lineEdit_pagamento_valor.textChanged.connect(self.__comportamento_pagamento_valor)
        self.btn_deletar.clicked.connect(self.close)
        self.btn_confirmar.clicked.connect(self.confirmar)
        self.lineEdit_pagamento_valor.returnPressed.connect(self.confirmar)

        self.frame_center.enterEvent = self.__enterEventFrameCenter
        self.frame_center.leaveEvent = self.__leaveEventFrameCenter
        self.frame_base.mousePressEvent = self.__closeWhithFrame
        self.frame.mousePressEvent = self.__enterEventFrameCenter

        self.__notification()


    def __enterEventFrameCenter(self, _):
        self.can_close = False

    def __leaveEventFrameCenter(self, _):
        self.can_close = True

    def __closeWhithFrame(self, _):
        if self.can_close:
            self.close()

    def __notification(self):
        self.label_notificacao = QLabel(self.frame_center)
        self.label_notificacao.setObjectName(u"label_notificacao")
        self.label_notificacao.setGeometry(QRect(-300, 40, 261, 24))
        font = QFont()
        font.setPointSize(11)
        self.label_notificacao.setFont(font)
        self.label_notificacao.setAlignment(Qt.AlignCenter)
        self.label_notificacao.setStyleSheet("""QLabel{background-color: rgb(19, 20, 22);color: rgb(255, 255, 255);
        border-radius: 7px;}""")

        self.opacity = QGraphicsOpacityEffect(self.label_notificacao)
        self.opacity.setOpacity(0.0)
        self.label_notificacao.setGraphicsEffect(self.opacity)

        self.__opacityAnimation()

    def __opacityAnimation(self):

        self.group_animation = QParallelAnimationGroup()

        self.opacity_animation_up = QPropertyAnimation(self.opacity, b'opacity')
        self.opacity_animation_up.setStartValue(0.0)
        self.opacity_animation_up.setEndValue(0.9)
        self.opacity_animation_up.setDuration(400)
        self.opacity_animation_up.setEasingCurve(QEasingCurve.Type.InOutExpo)
        self.group_animation.addAnimation(self.opacity_animation_up)

        self.pos_aimation = QPropertyAnimation(self.label_notificacao, b'pos')
        self.pos_aimation.setStartValue(QPoint(83, 25))
        self.pos_aimation.setEndValue(QPoint(83, 10))
        self.pos_aimation.setDuration(400)
        self.pos_aimation.setEasingCurve(QEasingCurve.Type.InOutExpo)
        self.group_animation.addAnimation(self.pos_aimation)

        self.opacity_animation_down = QPropertyAnimation(self.opacity, b'opacity')
        self.opacity_animation_down.setStartValue(0.9)
        self.opacity_animation_down.setEndValue(0.0)
        self.opacity_animation_down.setDuration(400)
        self.opacity_animation_down.setEasingCurve(QEasingCurve.Type.InOutExpo)
        self.opacity_animation_down.finished.connect(lambda: self.label_notificacao.move(-300, 25))

    def __startanimationNotification(self):
        self.group_animation.start()
        QTimer.singleShot(800, lambda: self.opacity_animation_down.start())

    def confirmar(self) -> bool:
        dados = {'cliente': self.lineEdit_cliente.text().lower(), 'metodo_de_pagamento': '', 'troco': '', 'ok': True}

        list_item: list = []
        q = self.combo_box_pagamento.count()
        for i in range(q):
            list_item.append(self.combo_box_pagamento.itemText(i))

        if not self.lineEdit_pagamento.text() in list_item:
            self.label_notificacao.setText("Selecione metodo de pagamento")
            self.__startanimationNotification()
            dados['ok'] = False
        else:
            dados['metodo_de_pagamento'] = self.lineEdit_pagamento.text().lower()

        valor = self.lineEdit_pagamento_valor.text()
        troco = self.lbl_troco.text().split(' ')
        troco = troco[-1]

        if not valor or valor == '.' or valor == ',':
            self.label_notificacao.setText("Falha no valor pago")
            self.__startanimationNotification()
            dados['ok'] = False
        else:
            try:
                float(valor)
            except ImportError as _:
                self.label_notificacao.setText("Falha no valor pago")
                self.__startanimationNotification()
                dados['ok'] = False
            else:
                if troco.count('.') == 1:
                    if float(troco) < 0:
                        self.label_notificacao.setText("Falha no valor pago")
                        self.__startanimationNotification()
                        dados['ok'] = False
                elif troco.count('.') > 1:
                    troco = troco.split('.')
                    troco.insert(-1, '.')
                    troco = float(''.join(troco))
                    if float(troco) < 0:
                        self.label_notificacao.setText("Falha no valor pago")
                        self.__startanimationNotification()
                        dados['ok'] = False

        if dados['ok']:
            dados['troco'] = self.lbl_troco.text()

        return dados

    def __validator(self):
        regex = QRegularExpressionValidator(QRegularExpression(r"^[0-9.,]*$"), self)
        self.lineEdit_pagamento_valor.setValidator(regex)

    def __comportamento_pagamento_valor(self, value: str):
        if not value:
            value = '0'

        if value.count(',') > 1 or value.count('.') > 1:
            value = value[:-2]

        if value and value[-1] == '.' and value.count(',') > 0:
            value = value[:-2]

        if value and value[-1] == ',' and value.count('.') > 0:
            value = value[:-2]

        if value.isnumeric():
            self.lineEdit_pagamento_valor.setText(str(int(value)))
        else:
            self.lineEdit_pagamento_valor.setText(value)

        try:
            total_compra = self.lb_valor_pagamento.text()
            total_compra = total_compra.split('.')
            total_compra.insert(-1, '.')
            total_compra = float(''.join(total_compra))

            valor_cerebido = self.lineEdit_pagamento_valor.text()

            troco = float(valor_cerebido.replace(',', '.')) - total_compra
            self.lbl_troco.setText(f'Troco: {troco:,.2f}'.replace(',', '.'))

        except ImportError:
            pass

    def __insertPagamento(self):
        list_item: list = []
        pagamento: str = self.lineEdit_pagamento.text()
        quantidade = int(self.combo_box_pagamento.count())

        for i in range(quantidade):
            list_item.append(self.combo_box_pagamento.itemText(i))

        if pagamento and not pagamento.isspace() and not pagamento in list_item:
            self.combo_box_pagamento.addItem(pagamento.title())
            self.combo_box_pagamento.showPopup()
            db = DataBase(AbsolutePath().getPathDatabase())
            db.connectDataBase()
            db.executarComand(f"INSERT INTO metodo_de_pagamento(nome) VALUES ('{pagamento.lower()}')")
            db.disconnectDataBase()

    def __insertCliente(self):
        list_item: list = []
        nome: str = self.lineEdit_cliente.text()
        quantidade = int(self.combo_box_cliente.count())

        for i in range(quantidade):
            list_item.append(self.combo_box_cliente.itemText(i))

        if nome and not nome.isspace() and not nome in list_item:
            self.combo_box_cliente.addItem(nome.title())
            self.combo_box_cliente.showPopup()
            db = DataBase(AbsolutePath().getPathDatabase())
            db.connectDataBase()
            db.executarComand(f"INSERT INTO cliente(nome) VALUES ('{nome.lower()}')")
            db.disconnectDataBase()

    def __setClienteSelected(self, nome):
        self.lineEdit_cliente.setText(nome)

    def __setPagamentoSelected(self, pagamento):
        self.lineEdit_pagamento.setText(pagamento)

    def __autoInsertDados(self):
        db = DataBase(AbsolutePath().getPathDatabase())
        db.connectDataBase()
        query1 = db.executarFetchall("SELECT nome FROM cliente ORDER BY nome")
        query2 = db.executarFetchall("SELECT nome FROM metodo_de_pagamento ORDER BY nome")
        db.disconnectDataBase()

        for dados in query1:
            self.combo_box_cliente.addItem(dados[0].title())

        for dados in query2:
            self.combo_box_pagamento.addItem(dados[0].title())

    def __setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(433, 325)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_base = QFrame(Form)
        self.frame_base.setObjectName(u"frame_base")
        self.frame_base.setStyleSheet(u"QFrame{background-color: rgba(0, 0, 0, 65);}")
        self.frame_base.setFrameShape(QFrame.StyledPanel)
        self.frame_base.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_base)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_center = QFrame(self.frame_base)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setMinimumSize(QSize(431, 323))
        self.frame_center.setMaximumSize(QSize(431, 323))
        self.frame_center.setStyleSheet(u"QFrame{\n"
                                        "background-color: rgb(0, 0, 0);\n"
                                        "border-radius: 10px;}\n"
                                        "\n"
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
        self.combo_box_cliente = QComboBox(self.frame)
        self.combo_box_cliente.setObjectName(u"combo_box_cliente")
        self.combo_box_cliente.setGeometry(QRect(5, 10, 394, 37))
        self.combo_box_cliente.setMinimumSize(QSize(0, 37))
        font = QFont()
        font.setPointSize(10)
        self.combo_box_cliente.setFont(font)
        self.combo_box_cliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo_box_cliente.setEditable(False)
        self.combo_box_cliente.setMinimumContentsLength(0)
        self.combo_box_cliente.setDuplicatesEnabled(False)
        self.lineEdit_pagamento_valor = QLineEdit(self.frame)
        self.lineEdit_pagamento_valor.setObjectName(u"lineEdit_nome_produto")
        self.lineEdit_pagamento_valor.setGeometry(QRect(14, 197, 384, 37))
        self.lineEdit_pagamento_valor.setMinimumSize(QSize(0, 30))
        self.lineEdit_pagamento_valor.setFont(font)
        self.combo_box_pagamento = QComboBox(self.frame)
        self.combo_box_pagamento.setObjectName(u"combo_box_pagamento")
        self.combo_box_pagamento.setGeometry(QRect(5, 60, 394, 37))
        self.combo_box_pagamento.setMinimumSize(QSize(0, 37))
        self.combo_box_pagamento.setFont(font)
        self.combo_box_pagamento.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo_box_pagamento.setEditable(False)
        self.combo_box_pagamento.setMinimumContentsLength(0)
        self.combo_box_pagamento.setDuplicatesEnabled(False)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 115, 140, 18))
        font1 = QFont()
        font1.setPointSize(11)
        self.label.setFont(font1)
        self.check_box_recibo_venda = QCheckBox(self.frame)
        self.check_box_recibo_venda.setObjectName(u"check_box_recibo_venda")
        self.check_box_recibo_venda.setGeometry(QRect(17, 145, 135, 20))
        self.lb_valor_pagamento = QLabel(self.frame)
        self.lb_valor_pagamento.setObjectName(u"lb_valor_pagamento")
        self.lb_valor_pagamento.setGeometry(QRect(17, 176, 381, 18))
        self.lb_valor_pagamento.setFont(font1)
        self.lbl_troco = QLabel(self.frame)
        self.lbl_troco.setObjectName(u"lbl_troco")
        self.lbl_troco.setGeometry(QRect(17, 239, 381, 18))
        self.lbl_troco.setFont(font1)
        self.frame_custom_cliente = QFrame(self.frame)
        self.frame_custom_cliente.setObjectName(u"frame_custom_cliente")
        self.frame_custom_cliente.setGeometry(QRect(5, 8, 394, 42))
        self.frame_custom_cliente.setStyleSheet(
            u"QPushButton{border-top-left-radius:0px;border-bottom-left-radius:0px;}\n"
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
        icon.addFile(AbsolutePath().getPathIcon("icon_down_arrow.svg"))
        self.btn_show_cliente.setIcon(icon)
        self.btn_show_cliente.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.btn_show_cliente)

        self.frame_custom_pagamento = QFrame(self.frame)
        self.frame_custom_pagamento.setObjectName(u"frame_custom_pagamento")
        self.frame_custom_pagamento.setGeometry(QRect(5, 58, 394, 41))
        self.frame_custom_pagamento.setStyleSheet(
            u"QPushButton{border-top-left-radius:0px;border-bottom-left-radius:0px;}\n"
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
        self.frame_90.setMinimumSize(QSize(0, 40))
        self.frame_90.setMaximumSize(QSize(16777215, 40))
        self.frame_90.setStyleSheet(u"")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_26.setSpacing(4)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(2, 2, 2, 2)
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
        icon1.addFile(AbsolutePath().getPathIcon("icon_delete.svg"))
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
        icon2.addFile(AbsolutePath().getPathIcon("icon_check_ok.svg"))
        self.btn_confirmar.setIcon(icon2)
        self.btn_confirmar.setIconSize(QSize(25, 25))

        self.horizontalLayout_26.addWidget(self.btn_confirmar)

        self.vertical_layout_inventario_2.addWidget(self.frame_90)

        self.verticalLayout_18.addWidget(self.frame_57)

        self.verticalLayout_2.addWidget(self.frame_30)

        self.verticalLayout_3.addWidget(self.frame_center, 0, Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.frame_base)

        self.__retranslateUi(Form)

        self.combo_box_cliente.setCurrentIndex(-1)
        self.combo_box_pagamento.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def __retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))

        self.combo_box_cliente.setPlaceholderText(QCoreApplication.translate("Form", u"Cliente (opcinal)", None))
        self.lineEdit_pagamento_valor.setPlaceholderText(
            QCoreApplication.translate("Form", u"Pagamento", None))

        self.combo_box_pagamento.setPlaceholderText(
            QCoreApplication.translate("Form", u"Metodo de pagamento", None))
        self.label.setText(QCoreApplication.translate("Form", u"Valor de pagamento", None))
        self.check_box_recibo_venda.setText(QCoreApplication.translate("Form", u"Criar recibo de venda", None))
        self.lb_valor_pagamento.setText(QCoreApplication.translate("Form", u"16.000.00", None))
        self.lbl_troco.setText(QCoreApplication.translate("Form", u"Troco: 0.00", None))
        self.lineEdit_cliente.setPlaceholderText(QCoreApplication.translate("Form", u"Cliente (opcional)", None))
        self.lineEdit_pagamento.setPlaceholderText(QCoreApplication.translate("Form", u"Metodo de pagamento", None))
    # retranslateUi


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = PySalesFinisher()
    win.show()
    sys.exit(app.exec())
