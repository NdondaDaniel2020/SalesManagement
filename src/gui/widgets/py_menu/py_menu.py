from src.qt_core import *
from src.gui.core.database import DataBase
from src.gui.core.absolute_path import AbsolutePath

class PySaleMenu(QFrame):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.__setUp__()
        self.visualisador = True

    def __setUp__(self) -> None:
        self.setStyleSheet(u"background-color: rgba(32, 33, 37, 255); border-radius: 10px;")
        self.setGeometry(0, 0, 197, 120)


        self.verticalLayout_27 = QVBoxLayout(self)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(2, 2, 2, 2)

        self.frame_line = QFrame(self)
        self.frame_line.setObjectName(u"frame_line")
        self.frame_line.setStyleSheet(u"background-color: rgba(64, 80, 170, 255);\n"
                                      "border-radius: 8px")
        self.frame_line.setFrameShape(QFrame.StyledPanel)
        self.frame_line.setFrameShadow(QFrame.Raised)

        self.verticalLayout_28 = QVBoxLayout(self.frame_line)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)

        self.frame_center = QFrame(self.frame_line)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setStyleSheet(u"background-color: rgba(32, 33, 37, 190);")
        self.frame_center.setFrameShape(QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QFrame.Raised)

        self.verticalLayout_29 = QVBoxLayout(self.frame_center)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(1, 1, 1, 1)

        self.frame_continer = QFrame(self.frame_center)
        self.frame_continer.setObjectName(u"frame_continer")
        self.frame_continer.setMinimumSize(QSize(70, 10))
        self.frame_continer.setStyleSheet(u"background-color:  rgb(19, 20, 22);\n"
                                          "border-radius:6px;")
        self.frame_continer.setFrameShape(QFrame.StyledPanel)
        self.frame_continer.setFrameShadow(QFrame.Raised)

        self.verticalLayout_30 = QVBoxLayout(self.frame_continer)
        self.verticalLayout_30.setSpacing(3)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(2, 2, 2, 3)

        self.abrir_painel_de_produto = QPushButton(self.frame_continer)
        self.abrir_painel_de_produto.setObjectName(u"abrir_painel_de_produto")
        self.abrir_painel_de_produto.setMinimumSize(QSize(0, 25))
        self.abrir_painel_de_produto.setSizeIncrement(QSize(0, 0))

        font1 = QFont()
        font1.setFamilies([u"Segoe UI Light"])
        font1.setPointSize(11)

        self.abrir_painel_de_produto.setFont(font1)
        self.abrir_painel_de_produto.setCursor(QCursor(Qt.PointingHandCursor))
        self.abrir_painel_de_produto.setStyleSheet(u"QPushButton{\n"
                               "background-color: rgb(19, 20, 22);\n"
                               "border-radius: 5px;\n"
                               "color: rgb(255, 255, 255);\n"
                               "text-align: left;\n"
                               "padding-left: 1px;}\n"
                               "\n"
                               "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
                               "\n"
                               "QPushButton:pressed{background-color: rgb(33, 38, 70);}")
        self.abrir_painel_de_produto.setIcon(QIcon(AbsolutePath().getPathIcon('icon_action.svg')))
        self.abrir_painel_de_produto.setIconSize(QSize(27, 27))

        self.verticalLayout_30.addWidget(self.abrir_painel_de_produto)

        self.scanner = QPushButton(self.frame_continer)
        self.scanner.setObjectName(u"scaner")
        self.scanner.setMinimumSize(QSize(0, 25))
        self.scanner.setSizeIncrement(QSize(0, 0))
        self.scanner.setFont(font1)
        self.scanner.setCursor(QCursor(Qt.PointingHandCursor))
        self.scanner.setStyleSheet(u"QPushButton{\n"
                                "background-color: rgb(19, 20, 22);\n"
                                "border-radius: 5px;\n"
                                "color: rgb(255, 255, 255);\n"
                                "text-align: left;\n"
                                "padding-left: 5px;}\n"
                                "\n"
                                "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
                                "\n"
                                "QPushButton:pressed{background-color: rgb(33, 38, 70);}")

        self.scanner.setIcon(QIcon(AbsolutePath().getPathIcon('icon_scan.svg')))
        self.scanner.setIconSize(QSize(19, 19))

        self.verticalLayout_30.addWidget(self.scanner)

        # self.rembg = QPushButton(self.frame_continer)
        # self.rembg.setObjectName(u"rembg")
        # self.rembg.setMinimumSize(QSize(0, 25))
        # self.rembg.setSizeIncrement(QSize(0, 0))
        # self.rembg.setFont(font1)
        # self.rembg.setCursor(QCursor(Qt.PointingHandCursor))
        # self.rembg.setStyleSheet(u"QPushButton{\n"
        #                          "background-color: rgb(19, 20, 22);\n"
        #                          "border-radius: 5px;\n"
        #                          "color: rgb(255, 255, 255);\n"
        #                          "text-align: left;\n"
        #                          "padding-left: 6px;}\n"
        #                          "\n"
        #                          "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
        #                          "\n"
        #                          "QPushButton:pressed{background-color: rgb(33, 38, 70);}")
        #
        # self.rembg.setIcon(QIcon(AbsolutePath().getPathIcon('icon_gallery_remove.svg')))
        # self.rembg.setIconSize(QSize(20, 20))
        #
        # self.verticalLayout_30.addWidget(self.rembg)

        self.finalizar = QPushButton(self.frame_continer)
        self.finalizar.setObjectName(u"rotate")
        self.finalizar.setMinimumSize(QSize(0, 25))
        self.finalizar.setSizeIncrement(QSize(0, 0))
        self.finalizar.setFont(font1)
        self.finalizar.setCursor(QCursor(Qt.PointingHandCursor))
        self.finalizar.setStyleSheet(u"QPushButton{\n"
                                  "background-color: rgb(19, 20, 22);\n"
                                  "border-radius: 5px;\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "text-align: left;\n"
                                  "padding-left: 7px;}\n"
                                  "\n"
                                  "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
                                  "\n"
                                  "QPushButton:pressed{background-color: rgb(33, 38, 70);}")

        self.finalizar.setIcon(QIcon(AbsolutePath().getPathIcon('icon_check_ok.svg')))
        self.finalizar.setIconSize(QSize(20, 20))

        self.verticalLayout_30.addWidget(self.finalizar)

        self.limpar = QPushButton(self.frame_continer)
        self.limpar.setObjectName(u"deletar")
        self.limpar.setMinimumSize(QSize(0, 25))
        self.limpar.setSizeIncrement(QSize(0, 0))
        self.limpar.setFont(font1)
        self.limpar.setCursor(QCursor(Qt.PointingHandCursor))
        self.limpar.setStyleSheet(u"QPushButton{\n"
                                   "background-color: rgb(19, 20, 22);\n"
                                   "border-radius: 5px;\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "text-align: left;\n"
                                   "padding-left: 5px;}\n"
                                   "\n"
                                   "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
                                   "\n"
                                   "QPushButton:pressed{background-color: rgb(33, 38, 70);}")

        self.limpar.setIcon(QIcon(AbsolutePath().getPathIcon('icon_delete.svg')))
        self.limpar.setIconSize(QSize(25, 21))

        self.verticalLayout_30.addWidget(self.limpar)

        self.verticalLayout_29.addWidget(self.frame_continer)

        self.verticalLayout_28.addWidget(self.frame_center)

        self.verticalLayout_27.addWidget(self.frame_line)

        self.abrir_painel_de_produto.setText(" Abrir painel de produto")
        self.scanner.setText("  Scanear com câmera")
        # self.rembg.setText("  Rotacionar")
        self.finalizar.setText("  Finalizar venda")
        self.limpar.setText("  Deletar tudo")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    m = PySaleMenu()
    m.move((QApplication.primaryScreen().size().width() - m.width()) / 2,
           (QApplication.primaryScreen().size().height() - m.height()) / 4.8)
    m.show()
    print(m.size())
    sys.exit(app.exec())
