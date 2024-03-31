# -*- coding: utf-8 -*-
from src.gui.widgets.py_slide_stacked_widgets.py_slide_stacked_widgets import PySlidingStackedWidget
################################################################################
## Form generated from reading UI file 'list_registro_venda_painel_selecaohQmcxp.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from src.qt_core import *
from src.gui.core.database import DataBase
from src.gui.core.absolute_path import AbsolutePath


class PySelectionRecordList(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi()


    def setChave(self, code):
        self.chave.setText(code)


    def setName(self, name):
        self.nome_produto.setText(name)


    def setQuantidade(self, value=0):
        self.lbl_quantidade.setText(str(value))

    def setValorDeVenda(self, value=0, auto=False):

        self.lbl_venda_valor.setText(f'Kz {value:,}'.replace(',', '.'))
        quantidade = int(self.lbl_quantidade.text())
        self.lbl_valor_total.setText(f'Kz {(value * quantidade):,}'.replace(',', '.'))

        db = DataBase(AbsolutePath().getPathDatabase())
        db.connectDataBase()
        quantidade_total = db.executarFetchone("SELECT sum(quantidade) from produto")
        db.disconnectDataBase()

        quantidade_total = quantidade_total[0]

        if not auto:
            quantidade_total += quantidade
        self.lbl_percentual.setText(f'{(quantidade / quantidade_total) * 100:.1f}')


    def setImage(self, path):
        icon = QIcon()
        icon.addFile(path)
        self.icon_img.setIcon(icon)


    def setImageSize(self, width, heith):
        self.icon_img.setIconSize(QSize(width, heith))


    def setupUi(self):

        self.setObjectName(u"PySelectionRecordList")
        self.setMinimumSize(QSize(0, 50))
        self.setMaximumSize(QSize(16777215, 50))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setStyleSheet(u"QPushButton{\n"
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
"	border: 1px solid rgb(121, 121, 121); \n"
"	color: rgb(233, 234, 236);}\n"
"\n"
"QLineEdit:focus{\n"
"	background-color: transparent; \n"
"	border: 1px solid rgb(161, 161, 161); \n"
"	color: rgb(233, 234, 236);}\n"
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
"	border-ra"
                        "dius: 10px;\n"
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
        self.icon_img.setObjectName(u"icon")
        self.icon_img.setMinimumSize(QSize(37, 37))
        self.icon_img.setMaximumSize(QSize(37, 37))
        icon1 = QIcon()
        icon1.addFile(u"../../../../../../imagem de modelo/transferir-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_img.setIcon(icon1)
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

        self.frame_valor_persentual = QFrame(self)
        self.frame_valor_persentual.setObjectName(u"frame_valor_persentual")
        self.frame_valor_persentual.setMinimumSize(QSize(92, 0))
        self.frame_valor_persentual.setFrameShape(QFrame.StyledPanel)
        self.frame_valor_persentual.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_valor_persentual)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 8, 10, 10)
        self.lbl_valor_percentual = QLabel(self.frame_valor_persentual)
        self.lbl_valor_percentual.setObjectName(u"lbl_valor_percentual")
        self.lbl_valor_percentual.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        self.lbl_valor_percentual.setFont(font2)
        self.lbl_valor_percentual.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lbl_valor_percentual)

        self.frame_continer = QFrame(self.frame_valor_persentual)
        self.frame_continer.setObjectName(u"frame_continer")
        self.frame_continer.setMaximumSize(QSize(16777215, 16))
        self.frame_continer.setFrameShape(QFrame.StyledPanel)
        self.frame_continer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_continer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_valor_total = QLabel(self.frame_continer)
        self.lbl_valor_total.setObjectName(u"lbl_valor_total")
        self.lbl_valor_total.setMaximumSize(QSize(16777215, 15))
        self.lbl_valor_total.setFont(font2)
        self.lbl_valor_total.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lbl_valor_total, 0, Qt.AlignRight)

        self.lbl_percentual = QLabel(self.frame_continer)
        self.lbl_percentual.setObjectName(u"lbl_percentual")
        self.lbl_percentual.setMinimumSize(QSize(44, 0))
        self.lbl_percentual.setMaximumSize(QSize(123456, 16))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semibold"])
        font3.setPointSize(8)
        self.lbl_percentual.setFont(font3)
        self.lbl_percentual.setAlignment(Qt.AlignCenter)
        self.lbl_percentual.setWordWrap(False)
        self.lbl_percentual.setMargin(0)

        self.horizontalLayout_4.addWidget(self.lbl_percentual, 0, Qt.AlignLeft)


        self.verticalLayout_7.addWidget(self.frame_continer)


        self.horizontalLayout_9.addWidget(self.frame_valor_persentual)

        self.frame_unidade = QFrame(self)
        self.frame_unidade.setObjectName(u"frame_unidade")
        self.frame_unidade.setMinimumSize(QSize(80, 0))
        self.frame_unidade.setMaximumSize(QSize(1234567, 16777215))
        self.frame_unidade.setFrameShape(QFrame.StyledPanel)
        self.frame_unidade.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_unidade)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.lbl_quantidade = QLabel(self.frame_unidade)
        self.lbl_quantidade.setObjectName(u"lbl_quantidade")
        self.lbl_quantidade.setFont(font2)
        self.lbl_quantidade.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_quantidade)

        self.lbl_unidade_valor = QLabel(self.frame_unidade)
        self.lbl_unidade_valor.setObjectName(u"lbl_unidade_valor")
        self.lbl_unidade_valor.setFont(font2)
        self.lbl_unidade_valor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_unidade_valor)


        self.horizontalLayout_9.addWidget(self.frame_unidade)

        self.frame_venda = QFrame(self)
        self.frame_venda.setObjectName(u"frame_venda")
        self.frame_venda.setMinimumSize(QSize(77, 0))
        self.frame_venda.setMaximumSize(QSize(2345678, 16777215))
        self.frame_venda.setFrameShape(QFrame.StyledPanel)
        self.frame_venda.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_venda)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.lbl_venda = QLabel(self.frame_venda)
        self.lbl_venda.setObjectName(u"lbl_venda")
        self.lbl_venda.setFont(font2)
        self.lbl_venda.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_venda)

        self.lbl_venda_valor = QLabel(self.frame_venda)
        self.lbl_venda_valor.setObjectName(u"lbl_venda_valor")
        self.lbl_venda_valor.setFont(font2)
        self.lbl_venda_valor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_venda_valor)


        self.horizontalLayout_9.addWidget(self.frame_venda)

        self.checkBox = QCheckBox(self)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(22, 16777215))

        self.horizontalLayout_9.addWidget(self.checkBox)



        self.retranslateUi()
    # setupUi

    def retranslateUi(self):
        self.chave.setText(QCoreApplication.translate("return_busca", u"333", None))
        self.nome_produto.setText(QCoreApplication.translate("return_busca", u"Coca Cola", None))
        self.lbl_valor_percentual.setText(QCoreApplication.translate("return_busca", u"Valor/percent", None))
        self.lbl_valor_total.setText(QCoreApplication.translate("return_busca", u"Kz 5000", None))
        self.lbl_percentual.setText(QCoreApplication.translate("return_busca", u"60%", None))
        self.lbl_quantidade.setText(QCoreApplication.translate("return_busca", u"Quantidade", None))
        self.lbl_unidade_valor.setText(QCoreApplication.translate("return_busca", u"20", None))
        self.lbl_venda.setText(QCoreApplication.translate("return_busca", u"valor de venda", None))
        self.lbl_venda_valor.setText(QCoreApplication.translate("return_busca", u"Kz 250", None))
        self.checkBox.setText("")
    # retranslateUi

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ls = PySelectionRecordList()
    ls.show()
    sys.exit(app.exec())

