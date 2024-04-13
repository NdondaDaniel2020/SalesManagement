# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_registro_venda_painel_insercaoaGGZpX.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from src.qt_core import *


class PyInsertRecordList(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__setupUi()
        self.__validator()
        self.chave_completa = ''

        self.checkBox.clicked.connect(self.__selecionarPorChackeBox)
        self.lineEdit_quantidade.textChanged.connect(self.__selecionarPorLineEdit)


    def __selecionarPorLineEdit(self, value):
        if not value:
            self.lineEdit_quantidade.setText("0")
            value = "0"

        if value:
            self.lineEdit_quantidade.setText(f"{int(value)}")

        if int(value) > 0:
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)

    def __selecionarPorChackeBox(self):
        if self.checkBox.isChecked():
            self.lineEdit_quantidade.setText("1")
        else:
            self.lineEdit_quantidade.setText("0")

    def __validator(self):
        regex = QRegularExpressionValidator(QRegularExpression("^[0-9]*$"), self)
        self.lineEdit_quantidade.setValidator(regex)

    def setChave(self, code):
        self.chave.setText(code[:4])
        self.chave_completa = code

    def setName(self, name):
        self.nome_produto.setText(name)

    def setImage(self, path):
        icon = QIcon()
        icon.addFile(path)
        self.icon_img.setIcon(icon)

    def setPrecoDeVenda(self, value=0):
        self.lbl_preco_valor.setText(f'Kz {value:,.2f}'.replace(',', '.'))

    def setImageSize(self, width, heith):
        self.icon_img.setIconSize(QSize(width, heith))

    def __setupUi(self):

        self.setObjectName(u"frame_registro")
        self.setMinimumSize(QSize(0, 50))
        self.setMaximumSize(QSize(16777215, 50))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setStyleSheet("QPushButton{\n"
                           "border: 1px solid rgb(230, 230, 230);\n"
                           "border-radius:5px;}\n"
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
                           "	border: 1px solid rgb(121, 121, 121);}\n"
                           "\n"
                           "QLineEdit:focus{\n"
                           "	background-color: transparent; \n"
                           "	border: 1px solid rgb(161, 161, 161);}\n"
                           "\n"
                           "QFrame{\n"
                           "	background-color: rgb(32, 33, 37);\n"
                           "	border-radius:10px;}\n"
                           "\n"
                           "#lbl_venda, #lbl_quantidade, #lbl_valor_percentual\n"
                           "{color: rgb(121, 121, 121)}\n"
                           "\n"
                           "#lbl_percentual{\n"
                           "background-color: rgb(230, 230, 230);\n"
                           "color: rgb(0, 0, 0);\n"
                           "border-radius:2px;\n"
                           "margin-left:3px}\n"
                           "\n"
                           "QCheckBox{color: rgb(255, 255, 255);}\n"
                           "QCheckBox::indicator {\n"
                           "    border: 3px solid rgb(47, 54, 100);\n"
                           "	width: 15px;\n"
                           "	height: 15px;\n"
                           "	border-radius: 10px;\n"
                           "    background: rgb(255, 255, 255);\n"
                           "}\n"
                           "QCheckBox::indicator:hover {\n"
                           "    border: 3px solid rgb(49, 57, 105);\n"
                           "}\n"
                           "QCheckBox::indicator:checked {\n"
                           "    background: 3px solid rgb(47, 54, 100);\n"
                           "	border: 3px solid rgb(255, 255, 255);\n"
                           "}")
        self.horizontalLayout_9 = QHBoxLayout(self)
        self.horizontalLayout_9.setSpacing(19)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(6, 0, 10, 0)
        self.icon_img = QPushButton(self)
        self.icon_img.setObjectName(u"icon_img")
        self.icon_img.setMinimumSize(QSize(37, 37))
        self.icon_img.setMaximumSize(QSize(37, 37))
        icon = QIcon()
        icon.addFile(u"../../../../../../imagem de modelo/transferir-removebg-preview.png", QSize(),
                     QIcon.Normal, QIcon.Off)
        self.icon_img.setIcon(icon)
        self.icon_img.setIconSize(QSize(60, 60))

        self.horizontalLayout_9.addWidget(self.icon_img)

        self.frame_chave_nome = QFrame(self)
        self.frame_chave_nome.setObjectName(u"frame_chave_nome")
        self.frame_chave_nome.setFrameShape(QFrame.StyledPanel)
        self.frame_chave_nome.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_chave_nome)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, -1, 0, -1)
        self.chave = QLabel(self.frame_chave_nome)
        self.chave.setObjectName(u"chave")
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(10)
        self.chave.setFont(font)

        self.verticalLayout_10.addWidget(self.chave)

        self.nome_produto = QLabel(self.frame_chave_nome)
        self.nome_produto.setObjectName(u"nome_produto")
        font1 = QFont()
        font1.setFamilies([u"Zilla Slab Medium"])
        font1.setPointSize(10)
        self.nome_produto.setFont(font1)

        self.verticalLayout_10.addWidget(self.nome_produto)


        self.horizontalLayout_9.addWidget(self.frame_chave_nome)

        self.frame_venda = QFrame(self)
        self.frame_venda.setObjectName(u"frame_venda")
        self.frame_venda.setMinimumSize(QSize(77, 0))
        self.frame_venda.setMaximumSize(QSize(2345678, 16777215))
        self.frame_venda.setFrameShape(QFrame.StyledPanel)
        self.frame_venda.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_venda)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 5, 10, 5)
        self.lbl_venda = QLabel(self.frame_venda)
        self.lbl_venda.setObjectName(u"lbl_venda")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        self.lbl_venda.setFont(font2)
        self.lbl_venda.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_venda)

        self.lbl_preco_valor = QLabel(self.frame_venda)
        self.lbl_preco_valor.setObjectName(u"lbl_venda_valor")
        self.lbl_preco_valor.setFont(font2)
        self.lbl_preco_valor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_preco_valor)


        self.horizontalLayout_9.addWidget(self.frame_venda)

        self.frame_unidade = QFrame(self)
        self.frame_unidade.setObjectName(u"frame_unidade")
        self.frame_unidade.setMinimumSize(QSize(80, 0))
        self.frame_unidade.setMaximumSize(QSize(1234567, 16777215))
        self.frame_unidade.setFrameShape(QFrame.StyledPanel)
        self.frame_unidade.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_unidade)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.lbl_quantidade = QLabel(self.frame_unidade)
        self.lbl_quantidade.setObjectName(u"lbl_quantidade")
        self.lbl_quantidade.setFont(font2)
        self.lbl_quantidade.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_quantidade)

        self.lineEdit_quantidade = QLineEdit(self.frame_unidade)
        self.lineEdit_quantidade.setObjectName(u"lineEdit_quantidade")
        self.lineEdit_quantidade.setMinimumSize(QSize(0, 16))
        self.lineEdit_quantidade.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineEdit_quantidade)


        self.horizontalLayout_9.addWidget(self.frame_unidade, 0, Qt.AlignRight)

        self.checkBox = QCheckBox(self)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(24, 16777215))

        self.horizontalLayout_9.addWidget(self.checkBox)


        self.__retranslateUi()
    # setupUi

    def __retranslateUi(self):
        self.chave.setText(QCoreApplication.translate("return_busca", u"333", None))
        self.nome_produto.setText(QCoreApplication.translate("return_busca", u"Coca Cola", None))
        self.lbl_venda.setText(QCoreApplication.translate("return_busca", u"Pre\u00e7o", None))
        self.lbl_preco_valor.setText(QCoreApplication.translate("return_busca", u"Kz 250", None))
        self.lbl_quantidade.setText(QCoreApplication.translate("return_busca", u"Quantidade", None))
        self.lineEdit_quantidade.setText(QCoreApplication.translate("return_busca", u"0", None))

    # retranslateUi



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = PyInsertRecordList()
    win.show()
    sys.exit(app.exec())
