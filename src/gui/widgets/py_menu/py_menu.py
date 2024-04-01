from src.qt_core import *
from src.gui.core.database import DataBase
from src.gui.core.absolute_path import AbsolutePath

class SaleMenu(QFrame):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.__setUp__()
        self.visualisador = True

    def __setUp__(self) -> None:
        self.setStyleSheet(u"background-color: rgba(32, 33, 37, 255); border-radius: 10px;")
        self.setGeometry(0, 0, 193, 176)


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
                               "padding-left: 0px;}\n"
                               "\n"
                               "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
                               "\n"
                               "QPushButton:pressed{background-color: rgb(33, 38, 70);}")
        self.abrir_painel_de_produto.setIcon(QIcon(AbsolutePath().getPathIcon('icon_action.svg')))
        self.abrir_painel_de_produto.setIconSize(QSize(24, 24))

        self.verticalLayout_30.addWidget(self.abrir_painel_de_produto)

        self.foto = QPushButton(self.frame_continer)
        self.foto.setObjectName(u"foto")
        self.foto.setMinimumSize(QSize(0, 25))
        self.foto.setSizeIncrement(QSize(0, 0))
        self.foto.setFont(font1)
        self.foto.setCursor(QCursor(Qt.PointingHandCursor))
        self.foto.setStyleSheet(u"QPushButton{\n"
                                "background-color: rgb(19, 20, 22);\n"
                                "border-radius: 5px;\n"
                                "color: rgb(255, 255, 255);\n"
                                "text-align: left;\n"
                                "padding-left: 6px;}\n"
                                "\n"
                                "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
                                "\n"
                                "QPushButton:pressed{background-color: rgb(33, 38, 70);}")

        self.foto.setIcon(QIcon(AbsolutePath().getPathIcon('icon_camera.svg')))
        self.foto.setIconSize(QSize(21, 21))

        self.verticalLayout_30.addWidget(self.foto)

        self.rembg = QPushButton(self.frame_continer)
        self.rembg.setObjectName(u"rembg")
        self.rembg.setMinimumSize(QSize(0, 25))
        self.rembg.setSizeIncrement(QSize(0, 0))
        self.rembg.setFont(font1)
        self.rembg.setCursor(QCursor(Qt.PointingHandCursor))
        self.rembg.setStyleSheet(u"QPushButton{\n"
                                 "background-color: rgb(19, 20, 22);\n"
                                 "border-radius: 5px;\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "text-align: left;\n"
                                 "padding-left: 6px;}\n"
                                 "\n"
                                 "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
                                 "\n"
                                 "QPushButton:pressed{background-color: rgb(33, 38, 70);}")

        self.rembg.setIcon(QIcon(AbsolutePath().getPathIcon('icon_gallery_remove.svg')))
        self.rembg.setIconSize(QSize(20, 20))

        self.verticalLayout_30.addWidget(self.rembg)

        self.rotate = QPushButton(self.frame_continer)
        self.rotate.setObjectName(u"rotate")
        self.rotate.setMinimumSize(QSize(0, 25))
        self.rotate.setSizeIncrement(QSize(0, 0))
        self.rotate.setFont(font1)
        self.rotate.setCursor(QCursor(Qt.PointingHandCursor))
        self.rotate.setStyleSheet(u"QPushButton{\n"
                                  "background-color: rgb(19, 20, 22);\n"
                                  "border-radius: 5px;\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "text-align: left;\n"
                                  "padding-left: 7px;}\n"
                                  "\n"
                                  "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
                                  "\n"
                                  "QPushButton:pressed{background-color: rgb(33, 38, 70);}")

        self.rotate.setIcon(QIcon(AbsolutePath().getPathIcon('icon_rotate.svg')))
        self.rotate.setIconSize(QSize(18, 18))

        self.verticalLayout_30.addWidget(self.rotate)

        self.resize_img = QPushButton(self.frame_continer)
        self.resize_img.setObjectName(u"resize_img")
        self.resize_img.setMinimumSize(QSize(0, 25))
        self.resize_img.setSizeIncrement(QSize(0, 0))
        self.resize_img.setFont(font1)
        self.resize_img.setCursor(QCursor(Qt.PointingHandCursor))
        self.resize_img.setStyleSheet(u"QPushButton{\n"
                                      "background-color: rgb(19, 20, 22);\n"
                                      "border-radius: 5px;\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "text-align: left;\n"
                                      "padding-left: 5px;}\n"
                                      "\n"
                                      "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
                                      "\n"
                                      "QPushButton:pressed{background-color: rgb(33, 38, 70);}")

        self.resize_img.setIcon(QIcon(AbsolutePath().getPathIcon('icon_size_svgrepo.svg')))
        self.resize_img.setIconSize(QSize(23, 23))

        self.verticalLayout_30.addWidget(self.resize_img)

        self.deletar = QPushButton(self.frame_continer)
        self.deletar.setObjectName(u"deletar")
        self.deletar.setMinimumSize(QSize(0, 25))
        self.deletar.setSizeIncrement(QSize(0, 0))
        self.deletar.setFont(font1)
        self.deletar.setCursor(QCursor(Qt.PointingHandCursor))
        self.deletar.setStyleSheet(u"QPushButton{\n"
                                   "background-color: rgb(19, 20, 22);\n"
                                   "border-radius: 5px;\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "text-align: left;\n"
                                   "padding-left: 5px;}\n"
                                   "\n"
                                   "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
                                   "\n"
                                   "QPushButton:pressed{background-color: rgb(33, 38, 70);}")

        self.deletar.setIcon(QIcon(AbsolutePath().getPathIcon('icon_delete.svg')))
        self.deletar.setIconSize(QSize(25, 21))

        self.verticalLayout_30.addWidget(self.deletar)

        self.verticalLayout_29.addWidget(self.frame_continer)

        self.verticalLayout_28.addWidget(self.frame_center)

        self.verticalLayout_27.addWidget(self.frame_line)

        self.abrir_painel_de_produto.setText(" Abrir painel de produto")
        self.foto.setText("  Fotografia")
        self.rembg.setText("  Remover bg")
        self.rotate.setText("  Rotacionar")
        self.resize_img.setText(" Tamanho")
        self.deletar.setText("  Deletar")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    m = SaleMenu()
    m.move((QApplication.primaryScreen().size().width() - m.width()) / 2,
                  (QApplication.primaryScreen().size().height() - m.height()) / 4.8)
    m.show()
    print(m.size())
    sys.exit(app.exec())
