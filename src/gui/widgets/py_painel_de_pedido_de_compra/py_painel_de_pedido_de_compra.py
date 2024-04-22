# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'painel_de_produtos_a_vendadcAwgk.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import json
from src.qt_core import *
from src.gui.widgets.py_list_registro_venda_painel_insercao.py_list_registro_venda_painel_insercao import (
                                                                                                    PyInsertRecordList)
from src.gui.core.database import DataBase
from src.gui.core.absolute_path import AbsolutePath


class PyPainelDePerda(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__setupUi(self)
        self.setGeometry(0, 0, 641, 429)
        self.automaticProductInsertion()

        self.can_close = False

        self.line_edit_pesquisa_produto.returnPressed.connect(self.searchProduct)
        self.btn_pesquisa_produto.clicked.connect(self.searchProduct)
        self.btn_deletar.clicked.connect(self.close)
        self.btn_confirmar.clicked.connect(self.getChaves)

        self.frame_center.enterEvent = self.enterEventFrameCenter
        self.frame_center.leaveEvent = self.leaveEventFrameCenter
        self.frame_base.mousePressEvent = self.closeClickedFrame

    def closeClickedFrame(self, _):
        if self.can_close:
            self.close()

    def enterEventFrameCenter(self, _):
        self.can_close = False

    def leaveEventFrameCenter(self, _):
        self.can_close = True

    def getChaves(self):

        objs = self.scrollAreaWidgetContents_3.findChildren(PyInsertRecordList)

        ls = list()
        for obj in objs:
            if obj.checkBox.isChecked():
                ls.append((obj.chave_completa, obj.lineEdit_quantidade.text()))
        return ls

    def automaticProductInsertion(self):

        json_file = AbsolutePath().getPathSettingSize()
        db = DataBase(AbsolutePath().getPathDatabase())
        db.connectDataBase()
        query = db.executarFetchall("SELECT chave, nome, quantidade, preco_venda, linkImg from produto")
        db.disconnectDataBase()

        for dados in query:
            if dados[2] > 0:
                list_produto = PyInsertRecordList()
                list_produto.setImage(dados[4])
                list_produto.setChave(dados[0])
                list_produto.setPrecoDeVenda(dados[3])
                list_produto.setName(dados[1].capitalize())

                with open(json_file, 'r') as file:
                    dado = json.load(file)
                    list_produto.setImageSize(*dado[dados[1]]["icon_image"])

                self.vertical_layout.insertWidget(0, list_produto)

    def searchProduct(self):
        nome = self.line_edit_pesquisa_produto.text()

        objs = self.scrollAreaWidgetContents_3.findChildren(PyInsertRecordList)

        if not nome:
            for obj in objs:
                obj.show()
        else:
            for obj in objs:
                obj.hide()
                if nome.lower() in obj.nome_produto.text().lower():
                    obj.show()

    def resizeEvent(self, event):

        if self.width() >= 724 or self.height() >= 568:
            width = self.width() - 234
            if width < 490:
                width = 490
            self.frame_center.setMinimumWidth(width)

            height = self.height() - 218
            if height < 350:
                height = 350

            self.frame_center.setMinimumHeight(height)
            self.frame_center.setMaximumHeight(height)

    def __setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(583, 509)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_base = QFrame(Form)
        self.frame_base.setObjectName(u"frame_2")
        self.frame_base.setStyleSheet(u"background-color: rgba(0, 0, 0, 65);")
        self.frame_base.setFrameShape(QFrame.StyledPanel)
        self.frame_base.setFrameShadow(QFrame.Raised)
        self.HorizontalLayout = QHBoxLayout(self.frame_base)
        self.HorizontalLayout.setObjectName(u"verticalLayout")
        self.frame_center = QFrame(self.frame_base)
        self.frame_center.setObjectName(u"frame")
        self.frame_center.setMinimumSize(QSize(490, 350))
        self.frame_center.setMaximumSize(QSize(490, 350))
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
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_89 = QFrame(self.frame_center)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(0, 44))
        self.frame_89.setMaximumSize(QSize(16777215, 44))
        self.frame_89.setStyleSheet(u"background-color: rgb(32, 33, 37)")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_25.setSpacing(4)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(4, 0, 4, 0)
        self.btn_pesquisa_produto = QPushButton(self.frame_89)
        self.btn_pesquisa_produto.setObjectName(u"btn_pesquisa_produto_3")
        self.btn_pesquisa_produto.setMinimumSize(QSize(37, 37))
        self.btn_pesquisa_produto.setMaximumSize(QSize(37, 37))
        self.btn_pesquisa_produto.setStyleSheet(u"QPushButton {\n"
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
        icon = QIcon()
        icon.addFile(AbsolutePath().getPathIcon("icon_search.svg"))
        self.btn_pesquisa_produto.setIcon(icon)
        self.btn_pesquisa_produto.setIconSize(QSize(25, 25))

        self.horizontalLayout_25.addWidget(self.btn_pesquisa_produto)

        self.line_edit_pesquisa_produto = QLineEdit(self.frame_89)
        self.line_edit_pesquisa_produto.setObjectName(u"line_edit_pesquisa_produto_2")
        self.line_edit_pesquisa_produto.setMinimumSize(QSize(0, 35))
        self.line_edit_pesquisa_produto.setStyleSheet(u"QLineEdit{\n"
                                                      "color: rgb(233, 234, 236);\n"
                                                      "border: 1px solid rgb(47, 54, 100);\n"
                                                      "border-radius: 5px;\n"
                                                      "padding-left: 5px;\n"
                                                      "}\n"
                                                      "QLineEdit:hover{\n"
                                                      "border: 1px solid rgb(64, 80, 170);\n"
                                                      "}\n"
                                                      "QLineEdit:focus{\n"
                                                      "border: 1px solid rgb(89, 109, 235);\n"
                                                      "}")
        self.line_edit_pesquisa_produto.setClearButtonEnabled(False)

        self.horizontalLayout_25.addWidget(self.line_edit_pesquisa_produto)

        self.verticalLayout_2.addWidget(self.frame_89)

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
        self.vertical_layout_inventario_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.frame_57)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setStyleSheet(u"background-color: rgb(19, 20, 22);\n"
                                        "border-radius: 10px;")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 527, 359))
        self.vertical_layout = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.vertical_layout.setObjectName(u"verticalLayout_268")
        self.verticalSpacer = QSpacerItem(20, 387, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vertical_layout.addItem(self.verticalSpacer)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.vertical_layout_inventario_2.addWidget(self.scrollArea_3)

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
        self.btn_deletar.setObjectName(u"btn_mais_opcoes_3")
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
        self.btn_confirmar.setObjectName(u"btn_adicionar_produto_4")
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

        self.HorizontalLayout.addWidget(self.frame_center)

        self.verticalLayout_3.addWidget(self.frame_base)

        QMetaObject.connectSlotsByName(Form)



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = PyPainelDePerda()
    win.show()
    sys.exit(app.exec())
