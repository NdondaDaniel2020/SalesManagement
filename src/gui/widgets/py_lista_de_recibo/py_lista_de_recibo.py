# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lista_de_reciboltADBq.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from src.qt_core import *


class PyLisaRecibo(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__setupUi()


    def __setupUi(self):
        self.setObjectName(u"frame_recibo")
        self.setMinimumSize(QSize(0, 50))
        self.setMaximumSize(QSize(400, 50))
        self.setStyleSheet(u"QPushButton{\n"
                                        "border: 1px solid rgb(230, 230, 230);\n"
                                        "border-radius:8px;\n"
                                        "color: rgb(255, 255, 255)}\n"
                                        "\n"
                                        "QLabel{color: rgb(233, 234, 236);}\n"
                                        "\n"
                                        "QLineEdit{\n"
                                        "	background-color: transparent; \n"
                                        "	border-radius: 6px;\n"
                                        "	border: transparent;\n"
                                        "	color: rgb(233, 234, 236);}\n"
                                        "\n"
                                        "QLineEdit:hover{\n"
                                        "	background-color: transparent; \n"
                                        "	border: 1px solid rgb(121, 121, 121); \n"
                                        "	color: rgb(233, 234, 236);}\n"
                                        "\n"
                                        "QLineEdit:focus{\n"
                                        "	background-color: transparent; \n"
                                        "	border: 1px solid rgb(161, 161, 161); \n"
                                        "	color: rgb(233, 234, 236);}\n"
                                        "\n"
                                        "#frame_recibo{\n"
                                        "	background-color: rgb(32, 33, 37);\n"
                                        "	border-radius:14px;\n"
                                        "	border: 1px solid rgba(233, 234, 236, 30)}\n"
                                        "\n"
                                        "#frame_recibo:hover{background-color: rgb(35, 36, 40)}\n"
                                        "\n"
                                        "#frame_recibo > QLabel, QFrame\n"
                                        "{background-color: transparent;border-radius:14px;}\n"
                                        "\n"
                                        "#lbl_cliente, #lbl_vendedor, #lbl_pagamento\n"
                                        "{color: rgb(121, 121, 121)}\n"
                                        "")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self)
        self.horizontalLayout_9.setSpacing(8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(6, 0, 2, 0)
        self.id = QPushButton(self)
        self.id.setObjectName(u"id")
        self.id.setMinimumSize(QSize(37, 37))
        self.id.setMaximumSize(QSize(37, 37))
        font = QFont()
        font.setFamilies([u"Segoe Fluent Icons"])
        font.setPointSize(20)
        self.id.setFont(font)
        self.id.setIconSize(QSize(60, 60))

        self.horizontalLayout_9.addWidget(self.id)

        self.frame_chave_nome = QFrame(self)
        self.frame_chave_nome.setObjectName(u"frame_chave_nome")
        self.frame_chave_nome.setFrameShape(QFrame.StyledPanel)
        self.frame_chave_nome.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_chave_nome)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, -1, 0, -1)
        self.id_venda = QLabel(self.frame_chave_nome)
        self.id_venda.setObjectName(u"id_venda")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(10)
        self.id_venda.setFont(font1)

        self.verticalLayout_10.addWidget(self.id_venda)

        self.data = QLabel(self.frame_chave_nome)
        self.data.setObjectName(u"data")
        font2 = QFont()
        font2.setFamilies([u"Zilla Slab Medium"])
        font2.setPointSize(10)
        self.data.setFont(font2)

        self.verticalLayout_10.addWidget(self.data)

        self.horizontalLayout_9.addWidget(self.frame_chave_nome)

        self.frame_unidade = QFrame(self)
        self.frame_unidade.setObjectName(u"frame_unidade")
        self.frame_unidade.setMinimumSize(QSize(80, 0))
        self.frame_unidade.setMaximumSize(QSize(1234567, 16777215))
        self.frame_unidade.setFrameShape(QFrame.StyledPanel)
        self.frame_unidade.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_unidade)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.lbl_cliente = QLabel(self.frame_unidade)
        self.lbl_cliente.setObjectName(u"lbl_cliente")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semibold"])
        self.lbl_cliente.setFont(font3)
        self.lbl_cliente.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_cliente)

        self.lineEdit_cliente = QLineEdit(self.frame_unidade)
        self.lineEdit_cliente.setObjectName(u"lineEdit_cliente")
        self.lineEdit_cliente.setMinimumSize(QSize(0, 16))
        self.lineEdit_cliente.setAlignment(Qt.AlignCenter)
        self.lineEdit_cliente.setDragEnabled(False)
        self.lineEdit_cliente.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.lineEdit_cliente)

        self.horizontalLayout_9.addWidget(self.frame_unidade, 0, Qt.AlignRight)

        self.frame_venda = QFrame(self)
        self.frame_venda.setObjectName(u"frame_venda")
        self.frame_venda.setMinimumSize(QSize(77, 0))
        self.frame_venda.setMaximumSize(QSize(2345678, 16777215))
        self.frame_venda.setFrameShape(QFrame.StyledPanel)
        self.frame_venda.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_venda)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 5, 0, 5)
        self.lbl_pagamento = QLabel(self.frame_venda)
        self.lbl_pagamento.setObjectName(u"lbl_pagamento")
        self.lbl_pagamento.setFont(font3)
        self.lbl_pagamento.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.lbl_pagamento)

        self.lbl_pagamento_txt = QLabel(self.frame_venda)
        self.lbl_pagamento_txt.setObjectName(u"lbl_pagamento_txt")
        self.lbl_pagamento_txt.setFont(font3)
        self.lbl_pagamento_txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.lbl_pagamento_txt)

        self.horizontalLayout_9.addWidget(self.frame_venda)

        self.__retranslateUi()
    # setupUi

    def __retranslateUi(self):
        self.id.setText(QCoreApplication.translate("Form", u"1", None))
        self.id_venda.setText(QCoreApplication.translate("Form", u"1", None))
        self.data.setText(QCoreApplication.translate("Form", u"21/01/2024 12:20:09", None))
        self.lbl_cliente.setText(QCoreApplication.translate("Form", u"Cliente", None))
        self.lineEdit_cliente.setText(QCoreApplication.translate("Form", u"Alberto", None))
        self.lbl_pagamento.setText(QCoreApplication.translate("Form", u"Pagamento", None))
        self.lbl_pagamento_txt.setText(QCoreApplication.translate("Form", u"Em dinheiro", None))
    # retranslateUi

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = PyLisaRecibo()
    win.show()
    sys.exit(app.exec())
