# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_registro_venda_painel_insercaoaGGZpX.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class PyInsertRecordList(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi()
        self.chave_completa = ''


    def setChave(self, code):
        self.chave.setText(code[:4])
        self.chave_completa = code

    def setName(self, name):
        self.nome_produto.setText(name)

    def setQuantidade(self, value=0):
        self.lbl_quantidade_valor.setText(str(value))

    def setImage(self, path):
        icon = QIcon()
        icon.addFile(path)
        self.icon_img.setIcon(icon)

    def setPrecoDeVenda(self, value=0, auto=False):
        self.lbl_preco_valor.setText(f'Kz {value:,.2f}'.replace(',', '.'))

    def setImageSize(self, width, heith):
        self.icon_img.setIconSize(QSize(width, heith))

    def setupUi(self):
        self.verticalLayout = QVBoxLayout(return_busca)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_registro = QFrame(return_busca)
        self.frame_registro.setObjectName(u"frame_registro")
        self.frame_registro.setMinimumSize(QSize(0, 50))
        self.frame_registro.setMaximumSize(QSize(16777215, 50))
        self.frame_registro.setFrameShape(QFrame.StyledPanel)
        self.frame_registro.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_registro)
        self.horizontalLayout_9.setSpacing(19)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(6, 0, 10, 0)
        self.icon_img = QPushButton(self.frame_registro)
        self.icon_img.setObjectName(u"icon_img")
        self.icon_img.setMinimumSize(QSize(37, 37))
        self.icon_img.setMaximumSize(QSize(37, 37))
        icon = QIcon()
        icon.addFile(u"../../../../../../imagem de modelo/transferir-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_img.setIcon(icon)
        self.icon_img.setIconSize(QSize(60, 60))

        self.horizontalLayout_9.addWidget(self.icon_img)

        self.frame_chave_nome = QFrame(self.frame_registro)
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

        self.frame_venda = QFrame(self.frame_registro)
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
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        self.lbl_venda.setFont(font2)
        self.lbl_venda.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_venda)

        self.lbl_venda_valor = QLabel(self.frame_venda)
        self.lbl_venda_valor.setObjectName(u"lbl_venda_valor")
        self.lbl_venda_valor.setFont(font2)
        self.lbl_venda_valor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_venda_valor)


        self.horizontalLayout_9.addWidget(self.frame_venda)

        self.frame_unidade = QFrame(self.frame_registro)
        self.frame_unidade.setObjectName(u"frame_unidade")
        self.frame_unidade.setMinimumSize(QSize(80, 0))
        self.frame_unidade.setMaximumSize(QSize(1234567, 16777215))
        self.frame_unidade.setFrameShape(QFrame.StyledPanel)
        self.frame_unidade.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_unidade)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 8, 10, 9)
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


        self.horizontalLayout_9.addWidget(self.frame_unidade)

        self.checkBox = QCheckBox(self.frame_registro)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(24, 16777215))

        self.horizontalLayout_9.addWidget(self.checkBox)


        self.verticalLayout.addWidget(self.frame_registro)


        self.retranslateUi(return_busca)

        QMetaObject.connectSlotsByName(return_busca)
    # setupUi

    def retranslateUi(self, return_busca):
        return_busca.setWindowTitle(QCoreApplication.translate("return_busca", u"Form", None))
        self.chave.setText(QCoreApplication.translate("return_busca", u"333", None))
        self.nome_produto.setText(QCoreApplication.translate("return_busca", u"Coca Cola", None))
        self.lbl_venda.setText(QCoreApplication.translate("return_busca", u"Pres\u00e7o", None))
        self.lbl_venda_valor.setText(QCoreApplication.translate("return_busca", u"Kz 250", None))
        self.lbl_quantidade.setText(QCoreApplication.translate("return_busca", u"Quantidade", None))
        self.lineEdit_quantidade.setText(QCoreApplication.translate("return_busca", u"0", None))

    # retranslateUi



if __name__ == '__main__':
    import sys

    app =QApplication(sys.argv)
    win =
