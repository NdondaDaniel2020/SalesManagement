# -*- coding: utf-8 -*-
from matplotlib.rcsetup import validate_float_or_None

################################################################################
## self generated from reading UI file 'lista_de_regitro_para_vendaCDcIou.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from src.qt_core import *


class PySaleRegistrationList(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

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
                                                      "#lbl_venda, \n"
                                                      "#lbl_quantidade, \n"
                                                      "#lbl_preco,\n"
                                                      "#lbl_subtotal,\n"
                                                      "#lbl_desconto\n"
                                                      "{color: rgb(121, 121, 121)}\n"
                                                      "")
        self.setMaximumHeight(50)
        self.setMinimumHeight(50)
        self.setupUi()
        self.validator()

        self.chave_completa = ''
        self.quantidade_max = 15
        self.preco_contante = 0
        self.let_desconto.textChanged.connect(self.ajustDescont)
        self.let_quantidade.textChanged.connect(self.ajustQuantidade)

    def ajustDescont(self, value: str):

        if not value:
            self.let_desconto.setText('0')

        value = self.definirOComportamentoDoPercentualDeDesconto(value)
        if value:
            if value.isnumeric():
                self.let_desconto.setText(str(int(value)))
            elif value.isdecimal():
                self.let_desconto.setText(str(float(value.replace(',', '.'))))

            try:
                preco = self.preco_contante
                percentual = float(value.replace(',', '.'))
                novo_preco = preco - ((preco*percentual)/100)
            except ImportError:
                pass
            else:
                self.lbl_preco_valor.setText(f'{novo_preco:,.2f}'.replace(',', '.'))
                if self.let_quantidade.text() != '0':
                    preco = int(value) * float(novo_preco)
                    if preco == 0.0:
                        self.lbl_subtotal_valor.setText(f'{int(preco)}'.replace(',', '.'))
                    else:
                        self.lbl_subtotal_valor.setText(f'{preco:,.2f}'.replace(',', '.'))

    @staticmethod
    def definirOComportamentoDoPercentualDeDesconto(value: str) -> str:

        if (value.count(',') > 1 or value.count('.') > 1) and (value[-1] == ',' or value[-1] == '.'):
            value = value[:-2]

        if (value.count(',') == 1 or value.count('.') == 1) and (value[-1] == '.' or value[-1] == ','):
            value = value[:-2]

        if len(value) > 5:
            value = value[:5]

        if value and float(value.replace(',', '.')) > 100:
            value = '100'

        return value

    def ajustQuantidade(self, value):
        if not value:
            self.let_quantidade.setText('0')

        if value:
            self.let_quantidade.setText(str(int(value)))

        if value and int(value) > self.quantidade_max:
            self.let_quantidade.setText(str(self.quantidade_max))
            value = self.quantidade_max

        if value:
            valor_atual = self.tratarPreco(self.lbl_preco_valor.text())

            preco = int(value) * float(valor_atual)
            if preco == 0.0:
                self.lbl_subtotal_valor.setText(f'{int(preco)}'.replace(',', '.'))
            else:
                self.lbl_subtotal_valor.setText(f'{preco:,.2f}'.replace(',', '.'))

    @staticmethod
    def tratarPreco(value: str) -> str:
        value = list(value.replace('.', ''))
        value.insert(-2, '.')
        value.pop(0)
        value.pop(0)
        value.pop(0)
        value = ''.join(value)

        return value

    def validator(self):
        regex_de = QRegularExpressionValidator(QRegularExpression(r"^[0-9.,]*$"), self)
        regex_qu = QRegularExpressionValidator(QRegularExpression(r"^[0-9]*$"), self)
        self.let_desconto.setValidator(regex_de)
        self.let_quantidade.setValidator(regex_qu)

    def setChave(self, code):
        self.chave.setText(code[:4])
        self.chave_completa = code

    def setName(self, name):
        self.nome_produto.setText(name)

    def setQuantidade(self, valor):
        self.quantidade_max = valor
        self.let_desconto.setText('0')
        self.let_quantidade.setText('0')

    def setPrecoDeVenda(self, value=0):
        self.lbl_preco_valor.setText(f'Kz {value:,.2f}'.replace(',', '.'))
        self.preco_contante = float(value)

    def setImage(self, path):
        icon = QIcon()
        icon.addFile(path)
        self.icon_image.setIcon(icon)

    def setImageSize(self, width, heith):
        self.icon_image.setIconSize(QSize(width, heith))

    def setupUi(self):

        self.horizontalLayout_8 = QHBoxLayout(self)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 0, 10, 0)
        self.icon_image = QPushButton(self)
        self.icon_image.setObjectName(u"icon")
        self.icon_image.setMinimumSize(QSize(37, 37))
        self.icon_image.setMaximumSize(QSize(37, 37))
        icon1 = QIcon()
        icon1.addFile(u"", QSize(), QIcon.Normal,QIcon.Off)
        self.icon_image.setIcon(icon1)
        self.icon_image.setIconSize(QSize(60, 60))

        self.horizontalLayout_8.addWidget(self.icon_image)

        self.frame_chave_nome = QFrame(self)
        self.frame_chave_nome.setObjectName(u"frame_chave_nome")
        self.frame_chave_nome.setFrameShape(QFrame.StyledPanel)
        self.frame_chave_nome.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_chave_nome)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, -1, 0, -1)
        self.chave = QLabel(self.frame_chave_nome)
        self.chave.setObjectName(u"chave")
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(10)
        self.chave.setFont(font)

        self.verticalLayout_9.addWidget(self.chave)

        self.nome_produto = QLabel(self.frame_chave_nome)
        self.nome_produto.setObjectName(u"nome_produto")
        font1 = QFont()
        font1.setFamilies([u"Zilla Slab Medium"])
        font1.setPointSize(10)
        self.nome_produto.setFont(font1)

        self.verticalLayout_9.addWidget(self.nome_produto)

        self.horizontalLayout_8.addWidget(self.frame_chave_nome)

        self.frame_quantidade = QFrame(self)
        self.frame_quantidade.setObjectName(u"frame_quantidade")
        self.frame_quantidade.setMinimumSize(QSize(67, 0))
        self.frame_quantidade.setMaximumSize(QSize(1234567, 16777215))
        self.frame_quantidade.setFrameShape(QFrame.StyledPanel)
        self.frame_quantidade.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_quantidade)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.lbl_quantidade = QLabel(self.frame_quantidade)
        self.lbl_quantidade.setObjectName(u"lbl_quantidade")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        self.lbl_quantidade.setFont(font2)
        self.lbl_quantidade.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_quantidade)

        self.let_quantidade = QLineEdit(self.frame_quantidade)
        self.let_quantidade.setObjectName(u"let_quantidade")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.let_quantidade.sizePolicy().hasHeightForWidth())
        self.let_quantidade.setSizePolicy(sizePolicy)
        self.let_quantidade.setMinimumSize(QSize(0, 17))
        self.let_quantidade.setMaxLength(1000000767)
        self.let_quantidade.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.let_quantidade)

        self.horizontalLayout_8.addWidget(self.frame_quantidade)

        self.frame_desconto = QFrame(self)
        self.frame_desconto.setObjectName(u"frame_desconto")
        self.frame_desconto.setMinimumSize(QSize(60, 0))
        self.frame_desconto.setMaximumSize(QSize(1234567, 16777215))
        self.frame_desconto.setFrameShape(QFrame.StyledPanel)
        self.frame_desconto.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_desconto)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.lbl_desconto = QLabel(self.frame_desconto)
        self.lbl_desconto.setObjectName(u"lbl_desconto")
        self.lbl_desconto.setFont(font2)
        self.lbl_desconto.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_desconto)

        self.let_desconto = QLineEdit(self.frame_desconto)
        self.let_desconto.setObjectName(u"let_desconto")
        sizePolicy.setHeightForWidth(self.let_desconto.sizePolicy().hasHeightForWidth())
        self.let_desconto.setSizePolicy(sizePolicy)
        self.let_desconto.setMinimumSize(QSize(0, 17))
        self.let_desconto.setMaxLength(1000000767)
        self.let_desconto.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.let_desconto)

        self.horizontalLayout_8.addWidget(self.frame_desconto)

        self.frame_venda = QFrame(self)
        self.frame_venda.setObjectName(u"frame_venda")
        self.frame_venda.setMinimumSize(QSize(77, 0))
        self.frame_venda.setMaximumSize(QSize(2345678, 16777215))
        self.frame_venda.setFrameShape(QFrame.StyledPanel)
        self.frame_venda.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_venda)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.lbl_preco = QLabel(self.frame_venda)
        self.lbl_preco.setObjectName(u"lbl_preco")
        self.lbl_preco.setFont(font2)
        self.lbl_preco.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_preco)

        self.lbl_preco_valor = QLabel(self.frame_venda)
        self.lbl_preco_valor.setObjectName(u"lbl_subtotal_valor_2")
        self.lbl_preco_valor.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_preco_valor)

        self.horizontalLayout_8.addWidget(self.frame_venda)

        self.frame_valor_persentual = QFrame(self)
        self.frame_valor_persentual.setObjectName(u"frame_valor_persentual")
        self.frame_valor_persentual.setMinimumSize(QSize(65, 0))
        self.frame_valor_persentual.setFrameShape(QFrame.StyledPanel)
        self.frame_valor_persentual.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_valor_persentual)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 8, 10, 10)
        self.lbl_subtotal = QLabel(self.frame_valor_persentual)
        self.lbl_subtotal.setObjectName(u"lbl_subtotal")
        self.lbl_subtotal.setMaximumSize(QSize(16777215, 15))
        self.lbl_subtotal.setFont(font2)
        self.lbl_subtotal.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lbl_subtotal)

        self.lbl_subtotal_valor = QLabel(self.frame_valor_persentual)
        self.lbl_subtotal_valor.setObjectName(u"lbl_subtotal_valor")
        self.lbl_subtotal_valor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lbl_subtotal_valor)

        self.horizontalLayout_8.addWidget(self.frame_valor_persentual)

        self.retranslateUi()

            # setupUi

    def retranslateUi(self):
            self.chave.setText(QCoreApplication.translate("lista_de_registro_pra_venda", u"333", None))
            self.nome_produto.setText(QCoreApplication.translate("lista_de_registro_pra_venda", u"Coca Cola", None))
            self.lbl_quantidade.setText(QCoreApplication.translate("lista_de_registro_pra_venda", u"Quantidade", None))
            self.let_quantidade.setText(QCoreApplication.translate("lista_de_registro_pra_venda", u"0", None))
            self.lbl_desconto.setText(QCoreApplication.translate("lista_de_registro_pra_venda", u"Desconto", None))
            self.let_desconto.setText(QCoreApplication.translate("lista_de_registro_pra_venda", u"0", None))
            self.lbl_preco.setText(
                    QCoreApplication.translate("lista_de_registro_pra_venda", u"Pre\u00e7o de venda", None))
            self.lbl_preco_valor.setText(QCoreApplication.translate("lista_de_registro_pra_venda", u"16.000.00", None))
            self.lbl_subtotal.setText(QCoreApplication.translate("lista_de_registro_pra_venda", u"Subtotal", None))
            self.lbl_subtotal_valor.setText(QCoreApplication.translate("lista_de_registro_pra_venda", u"0", None))
    # retranslateUi

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = PySaleRegistrationList()
    win.show()
    sys.exit(app.exec())
