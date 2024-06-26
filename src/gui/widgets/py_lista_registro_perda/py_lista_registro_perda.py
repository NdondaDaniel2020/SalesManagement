from src.qt_core import *
from src.gui.core.database import DataBase
from src.gui.core.absolute_path import AbsolutePath


class PyListaDePerda(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(0, 0, 618, 50)
        self.setStyleSheet("QFrame{background-color: rgb(32, 33, 37);border-radius:10px;}")
        self.setFixedHeight(50)
        self.__setUp__()

        self.btn_close.clicked.connect(self.deleteLater)

        self.chave_completa = ''


    def setChave(self, code):
        self.chave.setText(code[:4])
        self.chave_completa = code

    def setName(self, name):
        self.nome_produto.setText(name)

    def setQuantidade(self, value=0):
        self.lbl_quantidade.setText(str(value))

    def setValorDeVenda(self, value=0):
        self.lbl_venda_valor.setText(f'Kz {value:,.2f}'.replace(',', '.'))
        quantidade = int(self.lbl_quantidade.text())
        self.lbl_valor_total.setText(f'Kz {(value * quantidade):,.2f}'.replace(',', '.'))

    def setImage(self, path):
        icon = QIcon()
        icon.addFile(path)
        self.icon_img.setIcon(icon)

    def setImageSize(self, width, heith):
        self.icon_img.setIconSize(QSize(width, heith))

    def __setUp__(self):
        self.horizontalLayout_3 = QHBoxLayout(self)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.frame_registro = QFrame(self)
        self.frame_registro.setObjectName(u"frame_registro")
        self.frame_registro.setMinimumSize(QSize(0, 50))
        self.frame_registro.setMaximumSize(QSize(16777215, 50))
        self.frame_registro.setFrameShape(QFrame.StyledPanel)
        self.frame_registro.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_registro)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 0, 10, 0)
        self.icon_img = QPushButton(self.frame_registro)
        self.icon_img.setObjectName(u"icon")
        self.icon_img.setMinimumSize(QSize(37, 37))
        self.icon_img.setMaximumSize(QSize(37, 37))
        self.icon_img.setStyleSheet(u"QPushButton{border: 1px solid rgb(230, 230, 230);border-radius:5px;}")
        icon = QIcon()

        self.icon_img.setIcon(icon)
        self.icon_img.setIconSize(QSize(60, 60))

        self.horizontalLayout_8.addWidget(self.icon_img)

        self.frame_chave_nome = QFrame(self.frame_registro)
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
        self.chave.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.verticalLayout_9.addWidget(self.chave)

        self.nome_produto = QLabel(self.frame_chave_nome)
        self.nome_produto.setObjectName(u"nome_produto")
        font1 = QFont()
        font1.setFamilies([u"Zilla Slab Medium"])
        font1.setPointSize(10)
        self.nome_produto.setFont(font1)
        self.nome_produto.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.verticalLayout_9.addWidget(self.nome_produto)

        self.horizontalLayout_8.addWidget(self.frame_chave_nome)

        self.frame_valor_persentual = QFrame(self.frame_registro)
        self.frame_valor_persentual.setObjectName(u"frame_valor_persentual")
        self.frame_valor_persentual.setMinimumSize(QSize(92, 0))
        self.frame_valor_persentual.setFrameShape(QFrame.StyledPanel)
        self.frame_valor_persentual.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_valor_persentual)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 8, 10, 10)
        self.lbl_valor_percentual = QLabel(self.frame_valor_persentual)
        self.lbl_valor_percentual.setObjectName(u"lbl_valor_percentual")
        self.lbl_valor_percentual.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        self.lbl_valor_percentual.setFont(font2)
        self.lbl_valor_percentual.setStyleSheet(u"color: rgb(121, 121, 121)")
        self.lbl_valor_percentual.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lbl_valor_percentual)

        self.lbl_valor_total = QLabel(self.frame_valor_persentual)
        self.lbl_valor_total.setObjectName(u"lbl_valor_total")
        self.lbl_valor_total.setMaximumSize(QSize(16777215, 15))
        self.lbl_valor_total.setFont(font2)
        self.lbl_valor_total.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.lbl_valor_total.setAlignment(Qt.AlignCenter)

        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semibold"])
        font3.setPointSize(8)

        self.verticalLayout_6.addWidget(self.lbl_valor_total)

        self.horizontalLayout_8.addWidget(self.frame_valor_persentual)

        self.frame_unidade = QFrame(self.frame_registro)
        self.frame_unidade.setObjectName(u"frame_unidade")
        self.frame_unidade.setMinimumSize(QSize(80, 0))
        self.frame_unidade.setMaximumSize(QSize(1234567, 16777215))
        self.frame_unidade.setFrameShape(QFrame.StyledPanel)
        self.frame_unidade.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_unidade)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.lbl_quantidade_inf = QLabel(self.frame_unidade)
        self.lbl_quantidade_inf.setObjectName(u"lbl_unidade")
        self.lbl_quantidade_inf.setFont(font2)
        self.lbl_quantidade_inf.setStyleSheet(u"color: rgb(121, 121, 121)")
        self.lbl_quantidade_inf.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_quantidade_inf)

        self.lbl_quantidade = QLabel(self.frame_unidade)
        self.lbl_quantidade.setObjectName(u"lbl_unidade_valor")
        self.lbl_quantidade.setFont(font2)
        self.lbl_quantidade.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.lbl_quantidade.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_quantidade)

        self.horizontalLayout_8.addWidget(self.frame_unidade)

        self.frame_venda = QFrame(self.frame_registro)
        self.frame_venda.setObjectName(u"frame_venda")
        self.frame_venda.setMinimumSize(QSize(77, 0))
        self.frame_venda.setMaximumSize(QSize(2345678, 16777215))
        self.frame_venda.setFrameShape(QFrame.StyledPanel)
        self.frame_venda.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_venda)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.lbl_venda = QLabel(self.frame_venda)
        self.lbl_venda.setObjectName(u"lbl_venda")
        self.lbl_venda.setFont(font2)
        self.lbl_venda.setStyleSheet(u"color: rgb(121, 121, 121)")
        self.lbl_venda.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_venda)

        self.lbl_venda_valor = QLabel(self.frame_venda)
        self.lbl_venda_valor.setObjectName(u"lbl_venda_valor")
        self.lbl_venda_valor.setFont(font2)
        self.lbl_venda_valor.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.lbl_venda_valor.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_venda_valor)

        self.horizontalLayout_8.addWidget(self.frame_venda)

        self.btn_close = QPushButton(self.frame_registro)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(30, 25))
        self.btn_close.setMaximumSize(QSize(30, 25))
        self.btn_close.setSizeIncrement(QSize(0, 0))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        self.btn_close.setFont(font4)
        self.btn_close.setStyleSheet(u"QPushButton {\n"
                                     "            color: rgb(233, 234, 236);\n"
                                     "            background-color: rgb(38, 39, 43);\n"
                                     "            border: none;\n"
                                     "            border-radius: 6px;\n"
                                     "}\n"
                                     " QPushButton:hover {\n"
                                     " 	background-color: rgb(49, 50, 55)\n"
                                     " }\n"
                                     "QPushButton:pressed {\n"
                                     " 	background-color: rgb(38, 39, 43);\n"
                                     "}")

        self.btn_close.setIcon(QIcon(AbsolutePath().getPathIcon('icon_close.svg')))
        self.btn_close.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.btn_close)

        self.horizontalLayout_3.addWidget(self.frame_registro)

        self.__retranslateUi__()

    def __retranslateUi__(self):
        self.chave.setText(QCoreApplication.translate("return_busca", u"333", None))
        self.nome_produto.setText(QCoreApplication.translate("return_busca", u"Coca Cola", None))
        self.lbl_valor_percentual.setText(QCoreApplication.translate("return_busca", u"Valor total", None))
        self.lbl_valor_total.setText(QCoreApplication.translate("return_busca", u"Kz 5000", None))
        self.lbl_quantidade_inf.setText(QCoreApplication.translate("return_busca", u"Quantidade", None))
        self.lbl_quantidade.setText(QCoreApplication.translate("return_busca", u"20", None))
        self.lbl_venda.setText(QCoreApplication.translate("return_busca", u"Preço de venda", None))
        self.lbl_venda_valor.setText(QCoreApplication.translate("return_busca", u"Kz 250", None))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = PyListaDePerda()
    win.show()
    sys.exit(app.exec())
