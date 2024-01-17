# -*- coding: utf-8 -*-
import sys

from PySide6.QtWidgets import QApplication

################################################################################
## Form generated from reading UI file 'cadastro_produtolrEAUp.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from src.qt_core import *
from qfluentwidgets import SpinBox

from src.gui.core.imagepath import ImagePath

class PyProductRegistration(QFrame):
    def __ini__(self, parent=None):
        super().__init__(parent)

        # self.setGeometry(0, 0, self.parent().width(), self.parent().height())

        # self.__setupUi__()
        self.setStyleSheet(u"background-color: rgba(32, 33, 37, 255); border-radius: 10px;")
        self.setGeometry(0, 0, 105, 0)
        self.__setUp__()

    def autoResize(self):
        ...
        # self.setGeometry(0, 0, self.parent().width(), self.parent().height())

    def __setUp__(self):

         self.setStyleSheet(u"background-color: rgba(32, 33, 37, 255); border-radius: 10px;")
         self.setGeometry(0, 0, 105, 0)

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
         self.verticalLayout_30.setContentsMargins(2, 3, 2, 3)

         self.editar = QPushButton(self.frame_continer)
         self.editar.setObjectName(u"editar")
         self.editar.setMinimumSize(QSize(0, 25))
         self.editar.setSizeIncrement(QSize(0, 0))

         font1 = QFont()
         font1.setFamilies([u"Segoe UI Light"])
         font1.setPointSize(11)

         self.editar.setFont(font1)
         self.editar.setCursor(QCursor(Qt.PointingHandCursor))
         self.editar.setStyleSheet(u"QPushButton{\n"
                                   "background-color: rgb(19, 20, 22);\n"
                                   "border-radius: 5px;\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "text-align: left;\n"
                                   "padding-left: 6px;}\n"
                                   "\n"
                                   "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
                                   "\n"
                                   "QPushButton:pressed{background-color: rgb(33, 38, 70);}")
         self.editar.setIcon(QIcon(ImagePath().set_svg_icon('icon_edit.svg')))
         self.editar.setIconSize(QSize(19, 19))

         self.verticalLayout_30.addWidget(self.editar)

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

         self.deletar.setIcon(QIcon(ImagePath().set_svg_icon('icon_delete.svg')))
         self.deletar.setIconSize(QSize(21, 21))

         self.verticalLayout_30.addWidget(self.deletar)

         self.verticalLayout_29.addWidget(self.frame_continer)

         self.verticalLayout_28.addWidget(self.frame_center)

         self.verticalLayout_27.addWidget(self.frame_line)

         self.editar.setText(QCoreApplication.translate("MainWindow", u"  Editar", None))
         self.deletar.setText(QCoreApplication.translate("MainWindow", u"  Deletar", None))


    def __setupUi__(self):
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_center_style = QFrame(self)
        self.frame_center_style.setObjectName(u"frame_center_style")
        self.frame_center_style.setStyleSheet(u"QFrame{\n"
                                              "	background-color: rgb(19, 20, 22);\n"
                                              "	border-radius:10px;}\n"
                                              "\n"
                                              "\n"
                                              "\n"
                                              "#frame_navigation > QPushButton{\n"
                                              "	background-color: rgb(19, 20, 22);\n"
                                              "	border-radius:7px;}\n"
                                              "\n"
                                              "#frame_navigation>QPushButton:hover{\n"
                                              "	background-color: rgb(28, 29, 32)}\n"
                                              "\n"
                                              "#frame_navigation>QPushButton:pressed{\n"
                                              "	background-color: rgb(19, 20, 22)}\n"
                                              "\n"
                                              "\n"
                                              "\n"
                                              "#frame_btn_edit_image{\n"
                                              "background-color: rgb(24, 25, 27);}\n"
                                              "\n"
                                              "#frame_btn_edit_image>QPushButton{\n"
                                              "	background-color: rgb(24, 25, 27);\n"
                                              "	border-radius:7px;color: rgb(233, 234, 236);}\n"
                                              "\n"
                                              "#frame_btn_edit_image>QPushButton:hover{\n"
                                              "	background-color: rgb(39, 40, 45);}\n"
                                              "\n"
                                              "#frame_btn_edit_image>QPushButton:pressed{\n"
                                              "	background-color: rgb(35, 36, 41);}\n"
                                              "\n"
                                              "\n"
                                              "#image{background-color: rgb(24, 25, 27);border-radius: 12px;}\n"
                                              "\n"
                                              "\n"
                                              "#frame_nave_bar{background-color: rgb(24, 25, 27);border-radiu: 12px;}\n"
                                              "\n"
                                              "#frame_nave_bar>QPushButton{\n"
                                              "background-color: rgb(32, 33, 37);\n"
                                              "border-radius:7p"
                                              "x;\n"
                                              "color: rgb(233, 234, 236);}\n"
                                              "\n"
                                              "#frame_nave_bar>QPushButton:hover{\n"
                                              "background-color: rgb(39, 40, 45);}\n"
                                              "\n"
                                              "#frame_nave_bar>QPushButton:pressed{\n"
                                              "background-color: rgb(35, 36, 41);}\n"
                                              "\n"
                                              "\n"
                                              "#frame_qr_code,\n"
                                              "#frame_quantidade,\n"
                                              "#frame_continer_info\n"
                                              "{\n"
                                              "	background-color: rgb(23, 24, 26);\n"
                                              "}\n"
                                              "\n"
                                              "#lineEdit_chave,\n"
                                              "\n"
                                              "")
        self.frame_center_style.setFrameShape(QFrame.StyledPanel)
        self.frame_center_style.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_center_style)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.frame_navigation = QFrame(self.frame_center_style)
        self.frame_navigation.setObjectName(u"frame_navigation")
        self.frame_navigation.setMaximumSize(QSize(50, 16777215))
        self.frame_navigation.setFrameShape(QFrame.StyledPanel)
        self.frame_navigation.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_navigation)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.btn_nav_camera = QPushButton(self.frame_navigation)
        self.btn_nav_camera.setObjectName(u"btn_nav_camera")
        self.btn_nav_camera.setMinimumSize(QSize(40, 40))
        self.btn_nav_camera.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"../../../images/svg_icons/icon_camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_nav_camera.setIcon(icon)
        self.btn_nav_camera.setIconSize(QSize(27, 27))

        self.verticalLayout_2.addWidget(self.btn_nav_camera)

        self.btn_nav_edit = QPushButton(self.frame_navigation)
        self.btn_nav_edit.setObjectName(u"btn_nav_edit")
        self.btn_nav_edit.setMinimumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u"../../../images/svg_icons/icon_edit_text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_nav_edit.setIcon(icon1)
        self.btn_nav_edit.setIconSize(QSize(27, 27))

        self.verticalLayout_2.addWidget(self.btn_nav_edit)

        self.btn_nav_key = QPushButton(self.frame_navigation)
        self.btn_nav_key.setObjectName(u"btn_nav_key")
        self.btn_nav_key.setMinimumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u"../../../images/svg_icons/icon_key.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_nav_key.setIcon(icon2)
        self.btn_nav_key.setIconSize(QSize(27, 27))

        self.verticalLayout_2.addWidget(self.btn_nav_key)

        self.btn_nav_info = QPushButton(self.frame_navigation)
        self.btn_nav_info.setObjectName(u"btn_nav_info")
        self.btn_nav_info.setMinimumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(u"../../../images/svg_icons/icon_info_2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_nav_info.setIcon(icon3)
        self.btn_nav_info.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.btn_nav_info)

        self.verticalSpacer = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout.addWidget(self.frame_navigation)

        self.frame_2 = QFrame(self.frame_center_style)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.image = QPushButton(self.frame_2)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(10, 10, 181, 171))
        self.image.setStyleSheet(u"background-color: rgb(24, 25, 27);\n"
                                 "border-radius: 12px;\n"
                                 "border: 1px solid rgb(255, 255, 255)")
        icon4 = QIcon()
        icon4.addFile(u"../../../../../../imagem de modelo/transferir-removebg-preview.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.image.setIcon(icon4)
        self.image.setIconSize(QSize(250, 250))
        self.frame_nave_bar = QFrame(self.frame_2)
        self.frame_nave_bar.setObjectName(u"frame_nave_bar")
        self.frame_nave_bar.setGeometry(QRect(200, 10, 330, 45))
        self.frame_nave_bar.setMinimumSize(QSize(310, 45))
        self.frame_nave_bar.setMaximumSize(QSize(1234578, 16777215))
        self.frame_nave_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_nave_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_nave_bar)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(7, 0, 7, 0)
        self.btn_add = QPushButton(self.frame_nave_bar)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMinimumSize(QSize(70, 34))
        font = QFont()
        font.setPointSize(10)
        self.btn_add.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u"../../../images/svg_icons/icon_add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add.setIcon(icon5)
        self.btn_add.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btn_add)

        self.btn_rotate = QPushButton(self.frame_nave_bar)
        self.btn_rotate.setObjectName(u"btn_rotate")
        self.btn_rotate.setMinimumSize(QSize(70, 34))
        self.btn_rotate.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u"../../../images/svg_icons/icon_rotate.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rotate.setIcon(icon6)
        self.btn_rotate.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_rotate)

        self.btn_camera_2 = QPushButton(self.frame_nave_bar)
        self.btn_camera_2.setObjectName(u"btn_camera_2")
        self.btn_camera_2.setMinimumSize(QSize(70, 34))
        self.btn_camera_2.setFont(font)
        self.btn_camera_2.setIcon(icon)
        self.btn_camera_2.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.btn_camera_2)

        self.btn_scan = QPushButton(self.frame_nave_bar)
        self.btn_scan.setObjectName(u"btn_scan")
        self.btn_scan.setMinimumSize(QSize(70, 34))
        self.btn_scan.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u"../../../images/svg_icons/icon_qr_code.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_scan.setIcon(icon7)
        self.btn_scan.setIconSize(QSize(19, 19))

        self.horizontalLayout_2.addWidget(self.btn_scan)

        self.frame_btn_edit_image = QFrame(self.frame_2)
        self.frame_btn_edit_image.setObjectName(u"frame_btn_edit_image")
        self.frame_btn_edit_image.setGeometry(QRect(10, 190, 181, 50))
        self.frame_btn_edit_image.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_edit_image.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btn_edit_image)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.btn_camera = QPushButton(self.frame_btn_edit_image)
        self.btn_camera.setObjectName(u"btn_camera")
        self.btn_camera.setMinimumSize(QSize(37, 37))
        self.btn_camera.setMaximumSize(QSize(37, 37))
        self.btn_camera.setIcon(icon)
        self.btn_camera.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btn_camera)

        self.btn_galeria = QPushButton(self.frame_btn_edit_image)
        self.btn_galeria.setObjectName(u"btn_galeria")
        self.btn_galeria.setMinimumSize(QSize(37, 37))
        self.btn_galeria.setMaximumSize(QSize(37, 37))
        icon8 = QIcon()
        icon8.addFile(u"../../../images/svg_icons/icon_gallery.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_galeria.setIcon(icon8)
        self.btn_galeria.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btn_galeria)

        self.btn_remove_bg = QPushButton(self.frame_btn_edit_image)
        self.btn_remove_bg.setObjectName(u"btn_remove_bg")
        self.btn_remove_bg.setMinimumSize(QSize(37, 37))
        self.btn_remove_bg.setMaximumSize(QSize(37, 37))
        icon9 = QIcon()
        icon9.addFile(u"../../../images/svg_icons/icon_gallery_remove.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove_bg.setIcon(icon9)
        self.btn_remove_bg.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btn_remove_bg)

        self.btn_deletar = QPushButton(self.frame_btn_edit_image)
        self.btn_deletar.setObjectName(u"btn_deletar")
        self.btn_deletar.setMinimumSize(QSize(37, 37))
        self.btn_deletar.setMaximumSize(QSize(37, 37))
        icon10 = QIcon()
        icon10.addFile(u"../../../images/svg_icons/icon_close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_deletar.setIcon(icon10)
        self.btn_deletar.setIconSize(QSize(17, 17))

        self.horizontalLayout_3.addWidget(self.btn_deletar)

        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(200, 60, 330, 363))
        self.stackedWidget.setMinimumSize(QSize(330, 363))
        self.stackedWidget.setStyleSheet(u"")
        self.page_edit_image = QWidget()
        self.page_edit_image.setObjectName(u"page_edit_image")
        self.page_edit_image.setStyleSheet(u"background-color: rgb(19, 20, 22);")
        self.frame_43 = QFrame(self.page_edit_image)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setGeometry(QRect(9, 277, 309, 50))
        self.frame_43.setMinimumSize(QSize(309, 50))
        self.frame_43.setMaximumSize(QSize(309, 50))
        self.frame_43.setStyleSheet(u"background-color: rgb(23, 24, 26);")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, 0)
        self.pushButton_22 = QPushButton(self.frame_43)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(37, 39))
        self.pushButton_22.setMaximumSize(QSize(37, 37))
        self.pushButton_22.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
                                         "border-radius:7px;\n"
                                         "color: #ffffff;\n"
                                         "border: 1px solid rgb(255, 255, 255)")
        self.pushButton_22.setIcon(icon4)
        self.pushButton_22.setIconSize(QSize(60, 60))

        self.horizontalLayout_6.addWidget(self.pushButton_22)

        self.SpinBox_6 = SpinBox(self.frame_43)
        self.SpinBox_6.setObjectName(u"SpinBox_6")
        self.SpinBox_6.setMinimumSize(QSize(0, 37))
        self.SpinBox_6.setStyleSheet(u"SpinBox {\n"
                                     "    color: white;\n"
                                     "	background-color: rgb(34, 35, 38);\n"
                                     "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                     "    border-radius: 5px;\n"
                                     "    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
                                     "    padding: 0px 80px 0 10px;\n"
                                     "    selection-background-color: #2f3664;\n"
                                     "    border-bottom: none;\n"
                                     "}\n"
                                     "\n"
                                     "SpinBox:hover{\n"
                                     "    background-color: rgba(34, 35, 38, 0.5);\n"
                                     "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                     "    border-bottom: none;\n"
                                     "}\n"
                                     "\n"
                                     "SpinBox:focus {\n"
                                     "    background-color: rgba(34, 35, 38, 13);\n"
                                     "    border-bottom: 1px solid #2f3664;\n"
                                     "}\n"
                                     "\n"
                                     "SpinBox:disabled {\n"
                                     "    color: rgba(0, 0, 0, 150);\n"
                                     "    background-color: rgba(34, 35, 38, 0.5);\n"
                                     "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                     "    border-bottom: 1px solid #2f3664;\n"
                                     "}\n"
                                     "\n"
                                     "SpinButton {\n"
                                     "    background-color: transparent;\n"
                                     "    border-radius: 4px;\n"
                                     "    margin: 0;\n"
                                     "    border-bottom: none;\n"
                                     "}\n"
                                     "\n"
                                     "SpinButton:hover {\n"
                                     "    background-color: rgba(0, 0, 0, 9);\n"
                                     "    bord"
                                     "er-bottom: none;\n"
                                     "}\n"
                                     "\n"
                                     "SpinButton:pressed {\n"
                                     "    background-color: rgb(85, 170, 255);\n"
                                     "    border-bottom: 1px solid #2f3664;\n"
                                     "}")

        self.horizontalLayout_6.addWidget(self.SpinBox_6)

        self.frame_45 = QFrame(self.page_edit_image)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setGeometry(QRect(10, 18, 309, 50))
        self.frame_45.setMinimumSize(QSize(309, 50))
        self.frame_45.setMaximumSize(QSize(309, 50))
        self.frame_45.setStyleSheet(u"background-color: rgb(23, 24, 26);")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_remove_bg_3 = QPushButton(self.frame_45)
        self.btn_remove_bg_3.setObjectName(u"btn_remove_bg_3")
        self.btn_remove_bg_3.setMinimumSize(QSize(80, 37))
        self.btn_remove_bg_3.setMaximumSize(QSize(80, 37))
        self.btn_remove_bg_3.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
                                           "border-radius:7px;\n"
                                           "color: #ffffff")
        icon11 = QIcon()
        icon11.addFile(u"../../../images/svg_icons/icon_minimize_size.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove_bg_3.setIcon(icon11)
        self.btn_remove_bg_3.setIconSize(QSize(23, 23))

        self.horizontalLayout_7.addWidget(self.btn_remove_bg_3)

        self.SpinBox_7 = SpinBox(self.frame_45)
        self.SpinBox_7.setObjectName(u"SpinBox_7")
        self.SpinBox_7.setMinimumSize(QSize(0, 37))
        self.SpinBox_7.setStyleSheet(u"SpinBox {\n"
                                     "    color: white;\n"
                                     "	background-color: rgb(34, 35, 38);\n"
                                     "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                     "    border-radius: 5px;\n"
                                     "    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
                                     "    padding: 0px 80px 0 10px;\n"
                                     "    selection-background-color: #2f3664;\n"
                                     "    border-bottom: none;\n"
                                     "}\n"
                                     "\n"
                                     "SpinBox:hover{\n"
                                     "    background-color: rgba(34, 35, 38, 0.5);\n"
                                     "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                     "    border-bottom: none;\n"
                                     "}\n"
                                     "\n"
                                     "SpinBox:focus {\n"
                                     "    background-color: rgba(34, 35, 38, 13);\n"
                                     "    border-bottom: 1px solid #2f3664;\n"
                                     "}\n"
                                     "\n"
                                     "SpinBox:disabled {\n"
                                     "    color: rgba(0, 0, 0, 150);\n"
                                     "    background-color: rgba(34, 35, 38, 0.5);\n"
                                     "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                     "    border-bottom: 1px solid #2f3664;\n"
                                     "}\n"
                                     "\n"
                                     "SpinButton {\n"
                                     "    background-color: transparent;\n"
                                     "    border-radius: 4px;\n"
                                     "    margin: 0;\n"
                                     "    border-bottom: none;\n"
                                     "}\n"
                                     "\n"
                                     "SpinButton:hover {\n"
                                     "    background-color: rgba(0, 0, 0, 9);\n"
                                     "    bord"
                                     "er-bottom: none;\n"
                                     "}\n"
                                     "\n"
                                     "SpinButton:pressed {\n"
                                     "    background-color: rgb(85, 170, 255);\n"
                                     "    border-bottom: 1px solid #2f3664;\n"
                                     "}")

        self.horizontalLayout_7.addWidget(self.SpinBox_7)

        self.frame_46 = QFrame(self.page_edit_image)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setGeometry(QRect(9, 100, 309, 50))
        self.frame_46.setMinimumSize(QSize(309, 50))
        self.frame_46.setMaximumSize(QSize(309, 50))
        self.frame_46.setStyleSheet(u"background-color: rgb(23, 24, 26);")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_remove_bg_4 = QPushButton(self.frame_46)
        self.btn_remove_bg_4.setObjectName(u"btn_remove_bg_4")
        self.btn_remove_bg_4.setMinimumSize(QSize(80, 37))
        self.btn_remove_bg_4.setMaximumSize(QSize(80, 37))
        self.btn_remove_bg_4.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
                                           "border-radius:7px;\n"
                                           "color: #ffffff")
        icon12 = QIcon()
        icon12.addFile(u"../../../images/svg_icons/icon_maximize_size.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove_bg_4.setIcon(icon12)
        self.btn_remove_bg_4.setIconSize(QSize(23, 23))

        self.horizontalLayout_8.addWidget(self.btn_remove_bg_4)

        self.SpinBox_8 = SpinBox(self.frame_46)
        self.SpinBox_8.setObjectName(u"SpinBox_8")
        self.SpinBox_8.setMinimumSize(QSize(0, 37))
        self.SpinBox_8.setStyleSheet(u"SpinBox {\n"
                                     "    color: white;\n"
                                     "	background-color: rgb(34, 35, 38);\n"
                                     "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                     "    border-radius: 5px;\n"
                                     "    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
                                     "    padding: 0px 80px 0 10px;\n"
                                     "    selection-background-color: #2f3664;\n"
                                     "    border-bottom: none;\n"
                                     "}\n"
                                     "\n"
                                     "SpinBox:hover{\n"
                                     "    background-color: rgba(34, 35, 38, 0.5);\n"
                                     "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                     "    border-bottom: none;\n"
                                     "}\n"
                                     "\n"
                                     "SpinBox:focus {\n"
                                     "    background-color: rgba(34, 35, 38, 13);\n"
                                     "    border-bottom: 1px solid #2f3664;\n"
                                     "}\n"
                                     "\n"
                                     "SpinBox:disabled {\n"
                                     "    color: rgba(0, 0, 0, 150);\n"
                                     "    background-color: rgba(34, 35, 38, 0.5);\n"
                                     "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                     "    border-bottom: 1px solid #2f3664;\n"
                                     "}\n"
                                     "\n"
                                     "SpinButton {\n"
                                     "    background-color: transparent;\n"
                                     "    border-radius: 4px;\n"
                                     "    margin: 0;\n"
                                     "    border-bottom: none;\n"
                                     "}\n"
                                     "\n"
                                     "SpinButton:hover {\n"
                                     "    background-color: rgba(0, 0, 0, 9);\n"
                                     "    bord"
                                     "er-bottom: none;\n"
                                     "}\n"
                                     "\n"
                                     "SpinButton:pressed {\n"
                                     "    background-color: rgb(85, 170, 255);\n"
                                     "    border-bottom: 1px solid #2f3664;\n"
                                     "}")

        self.horizontalLayout_8.addWidget(self.SpinBox_8)

        self.frame_48 = QFrame(self.page_edit_image)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setGeometry(QRect(9, 190, 309, 50))
        self.frame_48.setMinimumSize(QSize(309, 50))
        self.frame_48.setMaximumSize(QSize(309, 50))
        self.frame_48.setStyleSheet(u"background-color: rgb(23, 24, 26);")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_remove_bg_2 = QPushButton(self.frame_48)
        self.btn_remove_bg_2.setObjectName(u"btn_remove_bg_2")
        self.btn_remove_bg_2.setMinimumSize(QSize(80, 37))
        self.btn_remove_bg_2.setMaximumSize(QSize(80, 37))
        self.btn_remove_bg_2.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
                                           "border-radius:7px;\n"
                                           "color: #ffffff")
        icon13 = QIcon()
        icon13.addFile(u"../../../images/svg_icons/icon_border_radius.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove_bg_2.setIcon(icon13)
        self.btn_remove_bg_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_10.addWidget(self.btn_remove_bg_2)

        self.SpinBox_9 = SpinBox(self.frame_48)
        self.SpinBox_9.setObjectName(u"SpinBox_9")
        self.SpinBox_9.setMinimumSize(QSize(0, 37))
        self.SpinBox_9.setStyleSheet(u"SpinBox {\n"
                                     "    color: white;\n"
                                     "	background-color: rgb(34, 35, 38);\n"
                                     "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                     "    border-radius: 5px;\n"
                                     "    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
                                     "    padding: 0px 80px 0 10px;\n"
                                     "    selection-background-color: #2f3664;\n"
                                     "    border-bottom: none;\n"
                                     "}\n"
                                     "\n"
                                     "SpinBox:hover{\n"
                                     "    background-color: rgba(34, 35, 38, 0.5);\n"
                                     "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                     "    border-bottom: none;\n"
                                     "}\n"
                                     "\n"
                                     "SpinBox:focus {\n"
                                     "    background-color: rgba(34, 35, 38, 13);\n"
                                     "    border-bottom: 1px solid #2f3664;\n"
                                     "}\n"
                                     "\n"
                                     "SpinBox:disabled {\n"
                                     "    color: rgba(0, 0, 0, 150);\n"
                                     "    background-color: rgba(34, 35, 38, 0.5);\n"
                                     "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                     "    border-bottom: 1px solid #2f3664;\n"
                                     "}\n"
                                     "\n"
                                     "SpinButton {\n"
                                     "    background-color: transparent;\n"
                                     "    border-radius: 4px;\n"
                                     "    margin: 0;\n"
                                     "    border-bottom: none;\n"
                                     "}\n"
                                     "\n"
                                     "SpinButton:hover {\n"
                                     "    background-color: rgba(0, 0, 0, 9);\n"
                                     "    bord"
                                     "er-bottom: none;\n"
                                     "}\n"
                                     "\n"
                                     "SpinButton:pressed {\n"
                                     "    background-color: rgb(85, 170, 255);\n"
                                     "    border-bottom: 1px solid #2f3664;\n"
                                     "}")

        self.horizontalLayout_10.addWidget(self.SpinBox_9)

        self.stackedWidget.addWidget(self.page_edit_image)
        self.page_camera = QWidget()
        self.page_camera.setObjectName(u"page_camera")
        self.page_camera.setStyleSheet(u"background-color: rgb(19, 20, 22);")
        self.verticalLayout_5 = QVBoxLayout(self.page_camera)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_camera = QLabel(self.page_camera)
        self.lbl_camera.setObjectName(u"lbl_camera")

        self.verticalLayout_5.addWidget(self.lbl_camera)

        self.stackedWidget.addWidget(self.page_camera)
        self.page_information_chave = QWidget()
        self.page_information_chave.setObjectName(u"page_information_chave")
        self.page_information_chave.setStyleSheet(u"background-color: rgb(19, 20, 22);")
        self.frame_qr_code = QFrame(self.page_information_chave)
        self.frame_qr_code.setObjectName(u"frame_qr_code")
        self.frame_qr_code.setGeometry(QRect(10, 18, 313, 55))
        self.frame_qr_code.setStyleSheet(u"background-color: rgb(23, 24, 26);")
        self.frame_qr_code.setFrameShape(QFrame.StyledPanel)
        self.frame_qr_code.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_qr_code)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_chave = QLineEdit(self.frame_qr_code)
        self.lineEdit_chave.setObjectName(u"lineEdit_chave")
        self.lineEdit_chave.setMinimumSize(QSize(0, 37))
        self.lineEdit_chave.setFont(font)
        self.lineEdit_chave.setStyleSheet(u"QLineEdit{\n"
                                          "border:none;border-radius: 5px;\n"
                                          "background-color: rgb(32, 33, 36);\n"
                                          "color: rgb(233, 234, 236);padding-left:5px;}\n"
                                          "\n"
                                          "QLineEdit:hover{background-color: rgb(30, 31, 34);}\n"
                                          "\n"
                                          "QLineEdit:focus{background-color: rgb(34, 35, 38);}")

        self.horizontalLayout_5.addWidget(self.lineEdit_chave)

        self.btn_chave_qr_code = QPushButton(self.frame_qr_code)
        self.btn_chave_qr_code.setObjectName(u"btn_chave_qr_code")
        self.btn_chave_qr_code.setMinimumSize(QSize(37, 37))
        self.btn_chave_qr_code.setMaximumSize(QSize(37, 37))
        self.btn_chave_qr_code.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
                                             "border-radius:7px;\n"
                                             "color: #ffffff")
        self.btn_chave_qr_code.setIcon(icon7)
        self.btn_chave_qr_code.setIconSize(QSize(22, 22))

        self.horizontalLayout_5.addWidget(self.btn_chave_qr_code)

        self.frame_continer_info = QFrame(self.page_information_chave)
        self.frame_continer_info.setObjectName(u"frame_continer_info")
        self.frame_continer_info.setGeometry(QRect(10, 80, 311, 160))
        self.frame_continer_info.setStyleSheet(u"background-color: rgb(23, 24, 26);")
        self.frame_continer_info.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_continer_info)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lineEdit_unidade = QLineEdit(self.frame_continer_info)
        self.lineEdit_unidade.setObjectName(u"lineEdit_unidade")
        self.lineEdit_unidade.setMinimumSize(QSize(0, 37))
        self.lineEdit_unidade.setFont(font)
        self.lineEdit_unidade.setStyleSheet(u"QLineEdit{\n"
                                            "border:none;border-radius: 5px;\n"
                                            "background-color: rgb(32, 33, 36);\n"
                                            "color: rgb(233, 234, 236);padding-left:5px;}\n"
                                            "\n"
                                            "QLineEdit:hover{background-color: rgb(30, 31, 34);}\n"
                                            "\n"
                                            "QLineEdit:focus{background-color: rgb(34, 35, 38);}")
        self.lineEdit_unidade.setClearButtonEnabled(False)

        self.verticalLayout_3.addWidget(self.lineEdit_unidade)

        self.lineEdit_categoria = QLineEdit(self.frame_continer_info)
        self.lineEdit_categoria.setObjectName(u"lineEdit_categoria")
        self.lineEdit_categoria.setMinimumSize(QSize(0, 37))
        self.lineEdit_categoria.setFont(font)
        self.lineEdit_categoria.setStyleSheet(u"QLineEdit{\n"
                                              "border:none;border-radius: 5px;\n"
                                              "background-color: rgb(32, 33, 36);\n"
                                              "color: rgb(233, 234, 236);padding-left:5px;}\n"
                                              "\n"
                                              "QLineEdit:hover{background-color: rgb(30, 31, 34);}\n"
                                              "\n"
                                              "QLineEdit:focus{background-color: rgb(34, 35, 38);}")

        self.verticalLayout_3.addWidget(self.lineEdit_categoria)

        self.lineEdit_nome_produto = QLineEdit(self.frame_continer_info)
        self.lineEdit_nome_produto.setObjectName(u"lineEdit_nome_produto")
        self.lineEdit_nome_produto.setMinimumSize(QSize(0, 37))
        self.lineEdit_nome_produto.setFont(font)
        self.lineEdit_nome_produto.setStyleSheet(u"QLineEdit{\n"
                                                 "border:none;border-radius: 5px;\n"
                                                 "background-color: rgb(32, 33, 36);\n"
                                                 "color: rgb(233, 234, 236);padding-left:5px;}\n"
                                                 "\n"
                                                 "QLineEdit:hover{background-color: rgb(30, 31, 34);}\n"
                                                 "\n"
                                                 "QLineEdit:focus{background-color: rgb(34, 35, 38);}")

        self.verticalLayout_3.addWidget(self.lineEdit_nome_produto)

        self.frame_quantidade = QFrame(self.page_information_chave)
        self.frame_quantidade.setObjectName(u"frame_quantidade")
        self.frame_quantidade.setGeometry(QRect(10, 250, 312, 55))
        self.frame_quantidade.setStyleSheet(u"background-color: rgb(23, 24, 26);")
        self.frame_quantidade.setFrameShape(QFrame.StyledPanel)
        self.frame_quantidade.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_quantidade)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lineEdit_quantidade = QLineEdit(self.frame_quantidade)
        self.lineEdit_quantidade.setObjectName(u"lineEdit_quantidade")
        self.lineEdit_quantidade.setMinimumSize(QSize(0, 37))
        self.lineEdit_quantidade.setFont(font)
        self.lineEdit_quantidade.setStyleSheet(u"QLineEdit{\n"
                                               "border:none;border-radius: 5px;\n"
                                               "background-color: rgb(32, 33, 36);\n"
                                               "color: rgb(233, 234, 236);}\n"
                                               "\n"
                                               "QLineEdit:hover{background-color: rgb(30, 31, 34);}\n"
                                               "\n"
                                               "QLineEdit:focus{background-color: rgb(34, 35, 38);}")
        self.lineEdit_quantidade.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.lineEdit_quantidade)

        self.lineEdit_quantidade_reserva = QLineEdit(self.frame_quantidade)
        self.lineEdit_quantidade_reserva.setObjectName(u"lineEdit_quantidade_reserva")
        self.lineEdit_quantidade_reserva.setMinimumSize(QSize(0, 37))
        self.lineEdit_quantidade_reserva.setFont(font)
        self.lineEdit_quantidade_reserva.setStyleSheet(u"QLineEdit{\n"
                                                       "border:none;border-radius: 5px;\n"
                                                       "background-color: rgb(32, 33, 36);\n"
                                                       "color: rgb(233, 234, 236);}\n"
                                                       "\n"
                                                       "QLineEdit:hover{background-color: rgb(30, 31, 34);}\n"
                                                       "\n"
                                                       "QLineEdit:focus{background-color: rgb(34, 35, 38);}")
        self.lineEdit_quantidade_reserva.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.lineEdit_quantidade_reserva)

        self.stackedWidget.addWidget(self.page_information_chave)
        self.page_information_adicional = QWidget()
        self.page_information_adicional.setObjectName(u"page_information_adicional")
        self.page_information_adicional.setStyleSheet(u"background-color: rgb(19, 20, 22);")
        self.frame_continer_preco = QFrame(self.page_information_adicional)
        self.frame_continer_preco.setObjectName(u"frame_continer_preco")
        self.frame_continer_preco.setGeometry(QRect(9, 18, 312, 55))
        self.frame_continer_preco.setStyleSheet(u"background-color: rgb(23, 24, 26);")
        self.frame_continer_preco.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_preco.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_continer_preco)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEdit_preco_compra = QLineEdit(self.frame_continer_preco)
        self.lineEdit_preco_compra.setObjectName(u"lineEdit_preco_compra")
        self.lineEdit_preco_compra.setMinimumSize(QSize(0, 37))
        self.lineEdit_preco_compra.setFont(font)
        self.lineEdit_preco_compra.setStyleSheet(u"QLineEdit{\n"
                                                 "border:none;border-radius: 5px;\n"
                                                 "background-color: rgb(32, 33, 36);\n"
                                                 "color: rgb(233, 234, 236);}\n"
                                                 "\n"
                                                 "QLineEdit:hover{background-color: rgb(30, 31, 34);}\n"
                                                 "\n"
                                                 "QLineEdit:focus{background-color: rgb(34, 35, 38);}")
        self.lineEdit_preco_compra.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.lineEdit_preco_compra)

        self.lineEdit_preco_venda = QLineEdit(self.frame_continer_preco)
        self.lineEdit_preco_venda.setObjectName(u"lineEdit_preco_venda")
        self.lineEdit_preco_venda.setMinimumSize(QSize(0, 37))
        self.lineEdit_preco_venda.setFont(font)
        self.lineEdit_preco_venda.setStyleSheet(u"QLineEdit{\n"
                                                "border:none;border-radius: 5px;\n"
                                                "background-color: rgb(32, 33, 36);\n"
                                                "color: rgb(233, 234, 236);}\n"
                                                "\n"
                                                "QLineEdit:hover{background-color: rgb(30, 31, 34);}\n"
                                                "\n"
                                                "QLineEdit:focus{background-color: rgb(34, 35, 38);}")
        self.lineEdit_preco_venda.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.lineEdit_preco_venda)

        self.frame_continer_information_adicionais = QFrame(self.page_information_adicional)
        self.frame_continer_information_adicionais.setObjectName(u"frame_continer_information_adicionais")
        self.frame_continer_information_adicionais.setGeometry(QRect(10, 80, 311, 271))
        self.frame_continer_information_adicionais.setStyleSheet(u"background-color: rgb(23, 24, 26);")
        self.frame_continer_information_adicionais.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_information_adicionais.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_continer_information_adicionais)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_preco_adicional = QFrame(self.frame_continer_information_adicionais)
        self.frame_preco_adicional.setObjectName(u"frame_preco_adicional")
        self.frame_preco_adicional.setStyleSheet(u"border:none;\n"
                                                 "background-color: rgb(34, 35, 38);\n"
                                                 "border-radius: 5px;\n"
                                                 "color: rgb(233, 234, 236);\n"
                                                 "padding-left:5px;")
        self.frame_preco_adicional.setFrameShape(QFrame.StyledPanel)
        self.frame_preco_adicional.setFrameShadow(QFrame.Raised)
        self.lbl_tag = QLabel(self.frame_preco_adicional)
        self.lbl_tag.setObjectName(u"lbl_tag")
        self.lbl_tag.setGeometry(QRect(20, 7, 250, 20))
        self.lbl_tag.setFont(font)
        self.lbl_tag.setStyleSheet(u"color: rgb(134, 134, 137)")
        self.btn_add_preco = QPushButton(self.frame_preco_adicional)
        self.btn_add_preco.setObjectName(u"btn_add_preco")
        self.btn_add_preco.setGeometry(QRect(248, 45, 39, 39))
        self.btn_add_preco.setLayoutDirection(Qt.RightToLeft)
        self.btn_add_preco.setStyleSheet(u"QPushButton{\n"
                                         "background-color: rgb(24, 25, 27);\n"
                                         "border-radius:19px;\n"
                                         "color: rgb(233, 234, 236);\n"
                                         "padding-right: 6px}\n"
                                         "\n"
                                         "QPushButton:hover{background-color: rgb(39, 40, 45);}\n"
                                         "\n"
                                         "QPushButton:pressed{background-color: rgb(35, 36, 41);}")
        self.btn_add_preco.setIcon(icon5)
        self.btn_add_preco.setIconSize(QSize(34, 34))
        self.icon_tag = QPushButton(self.frame_preco_adicional)
        self.icon_tag.setObjectName(u"icon_tag")
        self.icon_tag.setGeometry(QRect(3, 6, 20, 24))
        icon14 = QIcon()
        icon14.addFile(u"../../../images/svg_icons/icon_tag.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_tag.setIcon(icon14)
        self.icon_tag.setIconSize(QSize(17, 17))

        self.verticalLayout_4.addWidget(self.frame_preco_adicional)

        self.frame_calendario = QFrame(self.frame_continer_information_adicionais)
        self.frame_calendario.setObjectName(u"frame_calendario")
        self.frame_calendario.setStyleSheet(u"border:none;\n"
                                            "background-color: rgb(34, 35, 38);\n"
                                            "border-radius: 5px;\n"
                                            "color: rgb(233, 234, 236);\n"
                                            "padding-left:5px;")
        self.frame_calendario.setFrameShape(QFrame.StyledPanel)
        self.frame_calendario.setFrameShadow(QFrame.Raised)
        self.lbl_calendario = QLabel(self.frame_calendario)
        self.lbl_calendario.setObjectName(u"lbl_calendario")
        self.lbl_calendario.setGeometry(QRect(20, 7, 260, 20))
        self.lbl_calendario.setFont(font)
        self.lbl_calendario.setStyleSheet(u"color: rgb(134, 134, 137)")
        self.btn_add_data = QPushButton(self.frame_calendario)
        self.btn_add_data.setObjectName(u"btn_add_data")
        self.btn_add_data.setGeometry(QRect(248, 45, 39, 39))
        self.btn_add_data.setLayoutDirection(Qt.RightToLeft)
        self.btn_add_data.setStyleSheet(u"QPushButton{\n"
                                        "background-color: rgb(24, 25, 27);\n"
                                        "border-radius:19px;\n"
                                        "color: rgb(233, 234, 236);\n"
                                        "padding-right: 6px}\n"
                                        "\n"
                                        "QPushButton:hover{background-color: rgb(39, 40, 45);}\n"
                                        "\n"
                                        "QPushButton:pressed{background-color: rgb(35, 36, 41);}")
        self.btn_add_data.setIcon(icon5)
        self.btn_add_data.setIconSize(QSize(37, 37))
        self.btn_calendario = QPushButton(self.frame_calendario)
        self.btn_calendario.setObjectName(u"btn_calendario")
        self.btn_calendario.setGeometry(QRect(3, 6, 20, 20))
        icon15 = QIcon()
        icon15.addFile(u"../../../images/svg_icons/icon_service.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_calendario.setIcon(icon15)
        self.btn_calendario.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.frame_calendario)

        self.informacoes_adicionais = QPlainTextEdit(self.frame_continer_information_adicionais)
        self.informacoes_adicionais.setObjectName(u"informacoes_adicionais")
        self.informacoes_adicionais.setMaximumSize(QSize(16777215, 60))
        self.informacoes_adicionais.setFont(font)
        self.informacoes_adicionais.setStyleSheet(u"QPlainTextEdit{\n"
                                                  "border:none;border-radius: 5px;\n"
                                                  "background-color: rgb(32, 33, 36);\n"
                                                  "color: rgb(233, 234, 236);}\n"
                                                  "\n"
                                                  "QPlainTextEdit:hover{background-color: rgb(30, 31, 34);}\n"
                                                  "\n"
                                                  "QPlainTextEdit:focus{background-color: rgb(34, 35, 38);}")

        self.verticalLayout_4.addWidget(self.informacoes_adicionais)

        self.stackedWidget.addWidget(self.page_information_adicional)
        self.pushButton_16 = QPushButton(self.frame_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(40, 330, 120, 37))
        self.pushButton_16.setMinimumSize(QSize(0, 37))
        self.pushButton_16.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
                                         "border-radius:7px;\n"
                                         "color: #ffffff")

        self.horizontalLayout.addWidget(self.frame_2)

        self.verticalLayout.addWidget(self.frame_center_style)

        self.__retranslateUi__(self)

        self.stackedWidget.setCurrentIndex(0)


        # setupUi

    def __retranslateUi__(self):
        self.btn_add.setText(QCoreApplication.translate("Form", u"Add", None))
        self.btn_rotate.setText(QCoreApplication.translate("Form", u" Rotate", None))
        self.btn_camera_2.setText(QCoreApplication.translate("Form", u" C\u00e2mera", None))
        self.btn_scan.setText(QCoreApplication.translate("Form", u" Scan", None))
        self.btn_remove_bg_3.setText(QCoreApplication.translate("Form", u"Size in", None))
        self.btn_remove_bg_4.setText(QCoreApplication.translate("Form", u"Size out", None))
        self.btn_remove_bg_2.setText(QCoreApplication.translate("Form", u"Border", None))
        self.lineEdit_chave.setPlaceholderText(QCoreApplication.translate("Form", u"Chave", None))
        self.lineEdit_unidade.setPlaceholderText(QCoreApplication.translate("Form", u"Unidade", None))
        self.lineEdit_categoria.setPlaceholderText(QCoreApplication.translate("Form", u"Categoria", None))
        self.lineEdit_nome_produto.setPlaceholderText(QCoreApplication.translate("Form", u"Nome do produto", None))
        self.lineEdit_quantidade.setPlaceholderText(QCoreApplication.translate("Form", u"Quantidade", None))
        self.lineEdit_quantidade_reserva.setPlaceholderText(
            QCoreApplication.translate("Form", u"Quantidade Reserva", None))
        self.lineEdit_preco_compra.setPlaceholderText(QCoreApplication.translate("Form", u"Pre\u00e7o de compra", None))
        self.lineEdit_preco_venda.setPlaceholderText(QCoreApplication.translate("Form", u"Pre\u00e7o de venda", None))
        self.lbl_tag.setText(QCoreApplication.translate("Form", u"Pre\u00e7os adicional de venda (opcional)", None))
        self.lbl_calendario.setText(
            QCoreApplication.translate("Form", u"Data de expira\u00e7\u00e3o do produto (opcional)", None))
        self.informacoes_adicionais.setPlaceholderText(
            QCoreApplication.translate("Form", u"Informa\u00e7\u00f5es adicionais sobre o produto (opcional)", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"Next", None))


if __name__ == '__main__':
    app = QApplication([])
    window = PyProductRegistration()
    window.show()
    sys.exit(app.exec())
