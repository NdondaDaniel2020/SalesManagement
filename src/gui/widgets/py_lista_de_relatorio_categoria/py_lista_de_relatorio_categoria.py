# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lista_de_relatorio_categorianSPdTD.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from src.qt_core import *


class PyListaRelatorioDeCategoria(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__setupUi()
        self.mes_n = 0

    def setMes(self, mes: str) -> None:
        self.lbl_mes.setText(mes)

    def setCategoria(self, categoria: str) -> None:
        self.lbl_categoria.setText(categoria)

    def setQuantidade(self, quantidade: int, quantidade_total: int) -> None:
        self.lbl_quantidade.setText(str(quantidade))
        percentual = (int(quantidade) / int(quantidade_total)) * 100
        self.progress_bar_percentual.setValue(percentual)

    def setColoProgressbar(self, color: tuple) -> None:
        self.setStyleSheet(u'* {color: rgb(233, 234, 236)}\n'
                           'QFrame{background-color: rgb(32, 33, 37);\n'
                           'border-radius:10px;}\n'
                           '\n'
                           'QProgressBar {\n'
                           '	background-color: rgb(49, 50, 55);\n'
                           '	color: #596deb;\n'
                           '	border-style:none;\n'
                           '	border-radius:5px;\n'
                           '	text-align: center;\n'
                           '}\n'
                           '\n'
                           'QProgressBar::chunk {\n'
                           'border-radius:5px;\n'
                           f'background-color: {color}\n'
                           '}')

    def __setupUi(self):
        self.setObjectName(u"frame_lista_de_relatorio_categoria")
        self.setMinimumSize(QSize(0, 50))
        self.setMaximumSize(QSize(16777215, 50))
        self.setStyleSheet(u'* {color: rgb(233, 234, 236)}\n'
                           'QFrame{background-color: rgb(32, 33, 37);\n'
                           'border-radius:10px;}\n'
                           '\n'
                           'QProgressBar {\n'
                           '	background-color: rgb(49, 50, 55);\n'
                           '	color: #596deb;\n'
                           '	border-style:none;\n'
                           '	border-radius:5px;\n'
                           '	text-align: center;\n'
                           '}\n'
                           '\n'
                           'QProgressBar::chunk {\n'
                           'border-radius:5px;\n'
                           'background-color: rgb(64, 80, 170)\n'
                           '}')
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, -1, 12, -1)
        self.frame_mes = QFrame(self)
        self.frame_mes.setObjectName(u"frame_mes")
        self.frame_mes.setFrameShape(QFrame.StyledPanel)
        self.frame_mes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_mes)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.lbl_mes = QLabel(self.frame_mes)
        self.lbl_mes.setObjectName(u"lblmes")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_mes.setFont(font)

        self.horizontalLayout_2.addWidget(self.lbl_mes)


        self.horizontalLayout.addWidget(self.frame_mes)

        self.frame_Categoria = QFrame(self)
        self.frame_Categoria.setObjectName(u"frame_Categoria")
        self.frame_Categoria.setFrameShape(QFrame.StyledPanel)
        self.frame_Categoria.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_Categoria)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_categoria = QLabel(self.frame_Categoria)
        self.lbl_categoria.setObjectName(u"lbl_categoria")
        font1 = QFont()
        font1.setPointSize(10)
        self.lbl_categoria.setFont(font1)

        self.horizontalLayout_3.addWidget(self.lbl_categoria)


        self.horizontalLayout.addWidget(self.frame_Categoria)

        self.frame_percentual = QFrame(self)
        self.frame_percentual.setObjectName(u"frame_percentual")
        self.frame_percentual.setFrameShape(QFrame.StyledPanel)
        self.frame_percentual.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_percentual)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.progress_bar_percentual = QProgressBar(self.frame_percentual)
        self.progress_bar_percentual.setObjectName(u"progress_bar_percentual")
        self.progress_bar_percentual.setStyleSheet(u"")
        self.progress_bar_percentual.setValue(24)

        self.horizontalLayout_5.addWidget(self.progress_bar_percentual)


        self.horizontalLayout.addWidget(self.frame_percentual)

        self.frame_quantidade = QFrame(self)
        self.frame_quantidade.setObjectName(u"frame_quantidade")
        self.frame_quantidade.setFrameShape(QFrame.StyledPanel)
        self.frame_quantidade.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_quantidade)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_quantidade = QLabel(self.frame_quantidade)
        self.lbl_quantidade.setObjectName(u"lbl_quantidade")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semilight"])
        font2.setPointSize(11)
        self.lbl_quantidade.setFont(font2)

        self.horizontalLayout_4.addWidget(self.lbl_quantidade)

        self.horizontalLayout.addWidget(self.frame_quantidade)

        self.__retranslateUi()

    def __retranslateUi(self):
        self.lbl_mes.setText(QCoreApplication.translate("Form", u"Abril", None))
        self.lbl_categoria.setText(QCoreApplication.translate("Form", u"Cosmetico", None))
        self.lbl_quantidade.setText(QCoreApplication.translate("Form", u"16", None))
    # retranslateUi


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = PyListaRelatorioDeCategoria()
    win.show()
    sys.exit(app.exec())
