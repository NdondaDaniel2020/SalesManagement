# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowzYJTSB.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from src.gui.widgets.py_push_button.py_push_button import PyPushButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(910, 584)
        self.widget_style_sheet = QWidget(MainWindow)
        self.widget_style_sheet.setObjectName(u"widget_style_sheet")
        self.widget_style_sheet.setStyleSheet(u"#central_widget, #line_left_menu, #line_title_bar{\n"
"	background-color: rgb(32, 33, 37);	\n"
"    border-radius: 8px}\n"
"\n"
"#container_central_frame{\n"
"	background-color: rgb(19, 20, 22);	\n"
"	border-top-left-radius: 7px;}\n"
"\n"
"#scroll_area_widget_contents_left_menu, #scroll_area_left_menu{\n"
"	background-color: rgb(32, 33, 37);\n"
"	border:none}\n"
"\n"
"#line_left_menu, #line_title_bar{	border:none}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.widget_style_sheet)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.central_widget = QWidget(self.widget_style_sheet)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.frame_left_menu = QFrame(self.central_widget)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(46, 0))
        self.frame_left_menu.setMaximumSize(QSize(46, 16777215))
        self.frame_left_menu.setStyleSheet(u"")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu_top = QFrame(self.frame_left_menu)
        self.frame_left_menu_top.setObjectName(u"frame_left_menu_top")
        self.frame_left_menu_top.setStyleSheet(u"")
        self.frame_left_menu_top.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu_top)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 0, 6, 0)
        self.btn_back = PyPushButton(self.frame_left_menu_top)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setMinimumSize(QSize(37, 37))
        self.btn_back.setMaximumSize(QSize(1234, 37))
        icon = QIcon()
        icon.addFile(u"../../../images/svg_icons/icon_back.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.btn_back)

        self.btn_menu = PyPushButton(self.frame_left_menu_top)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(37, 37))
        self.btn_menu.setMaximumSize(QSize(1234, 37))
        icon1 = QIcon()
        icon1.addFile(u"../../../images/svg_icons/icon_menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon1)
        self.btn_menu.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.btn_menu)

        self.btn_home = PyPushButton(self.frame_left_menu_top)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(37, 37))
        self.btn_home.setMaximumSize(QSize(1234, 37))
        icon2 = QIcon()
        icon2.addFile(u"../../../images/svg_icons/icon_home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon2)
        self.btn_home.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_compra = PyPushButton(self.frame_left_menu_top)
        self.btn_compra.setObjectName(u"btn_compra")
        self.btn_compra.setMinimumSize(QSize(37, 37))
        self.btn_compra.setMaximumSize(QSize(1234, 37))
        icon3 = QIcon()
        icon3.addFile(u"../../../images/svg_icons/icon_compra.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_compra.setIcon(icon3)
        self.btn_compra.setIconSize(QSize(36, 36))

        self.verticalLayout_3.addWidget(self.btn_compra)

        self.btn_venda = PyPushButton(self.frame_left_menu_top)
        self.btn_venda.setObjectName(u"btn_venda")
        self.btn_venda.setMinimumSize(QSize(37, 37))
        self.btn_venda.setMaximumSize(QSize(1234, 37))
        icon4 = QIcon()
        icon4.addFile(u"../../../images/svg_icons/icon_venda.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_venda.setIcon(icon4)
        self.btn_venda.setIconSize(QSize(36, 36))

        self.verticalLayout_3.addWidget(self.btn_venda)


        self.verticalLayout_6.addWidget(self.frame_left_menu_top)

        self.line_left_menu = QFrame(self.frame_left_menu)
        self.line_left_menu.setObjectName(u"line_left_menu")
        self.line_left_menu.setMaximumSize(QSize(42, 2))
        self.line_left_menu.setStyleSheet(u"background-color: rgb(63, 78, 169);")
        self.line_left_menu.setFrameShape(QFrame.HLine)
        self.line_left_menu.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_left_menu)

        self.frame_continer_scroll_area_widget = QFrame(self.frame_left_menu)
        self.frame_continer_scroll_area_widget.setObjectName(u"frame_continer_scroll_area_widget")
        self.frame_continer_scroll_area_widget.setMinimumSize(QSize(0, 123))
        self.frame_continer_scroll_area_widget.setMaximumSize(QSize(16777215, 123))
        self.frame_continer_scroll_area_widget.setStyleSheet(u"")
        self.frame_continer_scroll_area_widget.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_scroll_area_widget.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_continer_scroll_area_widget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scroll_area_left_menu = QScrollArea(self.frame_continer_scroll_area_widget)
        self.scroll_area_left_menu.setObjectName(u"scroll_area_left_menu")
        self.scroll_area_left_menu.setMinimumSize(QSize(0, 120))
        self.scroll_area_left_menu.setLineWidth(0)
        self.scroll_area_left_menu.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_left_menu.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_left_menu.setWidgetResizable(True)
        self.scroll_area_widget_contents_left_menu = QWidget()
        self.scroll_area_widget_contents_left_menu.setObjectName(u"scroll_area_widget_contents_left_menu")
        self.scroll_area_widget_contents_left_menu.setGeometry(QRect(0, 0, 46, 291))
        self.verticalLayout_4 = QVBoxLayout(self.scroll_area_widget_contents_left_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 7, 0)
        self.frame_continer_scroll_area_widget_contents_left_menu = QFrame(self.scroll_area_widget_contents_left_menu)
        self.frame_continer_scroll_area_widget_contents_left_menu.setObjectName(u"frame_continer_scroll_area_widget_contents_left_menu")
        self.frame_continer_scroll_area_widget_contents_left_menu.setStyleSheet(u"")
        self.frame_continer_scroll_area_widget_contents_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_scroll_area_widget_contents_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_continer_scroll_area_widget_contents_left_menu)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_relatorio = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu)
        self.btn_relatorio.setObjectName(u"btn_relatorio")
        self.btn_relatorio.setMinimumSize(QSize(37, 37))
        self.btn_relatorio.setMaximumSize(QSize(1234, 37))
        icon5 = QIcon()
        icon5.addFile(u"../../../images/svg_icons/icon_inventory.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_relatorio.setIcon(icon5)
        self.btn_relatorio.setIconSize(QSize(40, 40))

        self.verticalLayout_7.addWidget(self.btn_relatorio)

        self.btn_service = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu)
        self.btn_service.setObjectName(u"btn_service")
        self.btn_service.setMinimumSize(QSize(37, 37))
        self.btn_service.setMaximumSize(QSize(1234, 37))
        icon6 = QIcon()
        icon6.addFile(u"../../../images/svg_icons/icon_sevice.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_service.setIcon(icon6)
        self.btn_service.setIconSize(QSize(22, 22))

        self.verticalLayout_7.addWidget(self.btn_service)

        self.btn_fornecedor = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu)
        self.btn_fornecedor.setObjectName(u"btn_fornecedor")
        self.btn_fornecedor.setMinimumSize(QSize(37, 37))
        self.btn_fornecedor.setMaximumSize(QSize(1234, 37))
        icon7 = QIcon()
        icon7.addFile(u"../../../images/svg_icons/icon_employee.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fornecedor.setIcon(icon7)
        self.btn_fornecedor.setIconSize(QSize(28, 28))

        self.verticalLayout_7.addWidget(self.btn_fornecedor)

        self.btn_cliente = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu)
        self.btn_cliente.setObjectName(u"btn_cliente")
        self.btn_cliente.setMinimumSize(QSize(37, 37))
        self.btn_cliente.setMaximumSize(QSize(1234, 37))
        icon8 = QIcon()
        icon8.addFile(u"../../../images/svg_icons/icon_cliente.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cliente.setIcon(icon8)
        self.btn_cliente.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.btn_cliente)

        self.btn_agenda = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu)
        self.btn_agenda.setObjectName(u"btn_agenda")
        self.btn_agenda.setMinimumSize(QSize(37, 37))
        self.btn_agenda.setMaximumSize(QSize(1234, 37))
        icon9 = QIcon()
        icon9.addFile(u"../../../images/svg_icons/icon_service.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agenda.setIcon(icon9)
        self.btn_agenda.setIconSize(QSize(41, 41))

        self.verticalLayout_7.addWidget(self.btn_agenda)

        self.btn_recibo = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu)
        self.btn_recibo.setObjectName(u"btn_recibo")
        self.btn_recibo.setMinimumSize(QSize(37, 37))
        self.btn_recibo.setMaximumSize(QSize(1234, 37))
        icon10 = QIcon()
        icon10.addFile(u"../../../images/svg_icons/receipt-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_recibo.setIcon(icon10)
        self.btn_recibo.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.btn_recibo)

        self.btn_copia_seguranca = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu)
        self.btn_copia_seguranca.setObjectName(u"btn_copia_seguranca")
        self.btn_copia_seguranca.setMinimumSize(QSize(37, 37))
        self.btn_copia_seguranca.setMaximumSize(QSize(1234, 37))
        icon11 = QIcon()
        icon11.addFile(u"../../../images/svg_icons/icon_cloud.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_copia_seguranca.setIcon(icon11)
        self.btn_copia_seguranca.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.btn_copia_seguranca)


        self.verticalLayout_4.addWidget(self.frame_continer_scroll_area_widget_contents_left_menu)

        self.scroll_area_left_menu.setWidget(self.scroll_area_widget_contents_left_menu)

        self.horizontalLayout_5.addWidget(self.scroll_area_left_menu)


        self.verticalLayout_6.addWidget(self.frame_continer_scroll_area_widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.frame_conteiner_left_menu_bottom = QFrame(self.frame_left_menu)
        self.frame_conteiner_left_menu_bottom.setObjectName(u"frame_conteiner_left_menu_bottom")
        self.frame_conteiner_left_menu_bottom.setStyleSheet(u"")
        self.frame_conteiner_left_menu_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_conteiner_left_menu_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_conteiner_left_menu_bottom)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 0, 6, 4)
        self.btn_setting = PyPushButton(self.frame_conteiner_left_menu_bottom)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setMinimumSize(QSize(37, 37))
        self.btn_setting.setMaximumSize(QSize(1234, 37))
        icon12 = QIcon()
        icon12.addFile(u"../../../images/svg_icons/icon_setting.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting.setIcon(icon12)
        self.btn_setting.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.btn_setting)

        self.btn_info = PyPushButton(self.frame_conteiner_left_menu_bottom)
        self.btn_info.setObjectName(u"btn_info")
        self.btn_info.setMinimumSize(QSize(37, 37))
        self.btn_info.setMaximumSize(QSize(1234, 37))
        icon13 = QIcon()
        icon13.addFile(u"../../../images/svg_icons/icon_information.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_info.setIcon(icon13)
        self.btn_info.setIconSize(QSize(27, 27))

        self.verticalLayout_2.addWidget(self.btn_info)

        self.btn_user = PyPushButton(self.frame_conteiner_left_menu_bottom)
        self.btn_user.setObjectName(u"btn_user")
        self.btn_user.setMinimumSize(QSize(37, 37))
        self.btn_user.setMaximumSize(QSize(1234, 37))
        icon14 = QIcon()
        icon14.addFile(u"../../../images/svg_images/daniel.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_user.setIcon(icon14)
        self.btn_user.setIconSize(QSize(34, 39))

        self.verticalLayout_2.addWidget(self.btn_user)


        self.verticalLayout_6.addWidget(self.frame_conteiner_left_menu_bottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_notificacoes = QFrame(self.central_widget)
        self.frame_notificacoes.setObjectName(u"frame_notificacoes")
        self.frame_notificacoes.setMaximumSize(QSize(0, 0))
        self.frame_notificacoes.setFrameShape(QFrame.StyledPanel)
        self.frame_notificacoes.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_notificacoes)

        self.central_frame = QFrame(self.central_widget)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setStyleSheet(u"")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.central_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.central_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 33))
        self.title_bar.setMaximumSize(QSize(16777215, 33))
        self.title_bar.setStyleSheet(u"")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(3, 0, 0, 0)
        self.frame_logo = QFrame(self.title_bar)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setMinimumSize(QSize(65, 0))
        self.frame_logo.setStyleSheet(u"")
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_logo)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.horizontalLayout_4.addWidget(self.frame_logo)

        self.horizontalSpacer = QSpacerItem(427, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.frame_continer_control_window = QFrame(self.title_bar)
        self.frame_continer_control_window.setObjectName(u"frame_continer_control_window")
        self.frame_continer_control_window.setMinimumSize(QSize(97, 0))
        self.frame_continer_control_window.setStyleSheet(u"")
        self.frame_continer_control_window.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_control_window.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_continer_control_window)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = PyPushButton(self.frame_continer_control_window)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(25, 25))
        self.btn_minimize.setMaximumSize(QSize(25, 25))
        icon15 = QIcon()
        icon15.addFile(u"../../../images/svg_icons/icon_minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon15)
        self.btn_minimize.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.btn_minimize)

        self.btn_maximize = PyPushButton(self.frame_continer_control_window)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(25, 25))
        self.btn_maximize.setMaximumSize(QSize(25, 25))
        icon16 = QIcon()
        icon16.addFile(u"../../../images/svg_icons/icon_maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize.setIcon(icon16)
        self.btn_maximize.setIconSize(QSize(19, 19))

        self.horizontalLayout_3.addWidget(self.btn_maximize)

        self.btn_close = PyPushButton(self.frame_continer_control_window)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(25, 25))
        self.btn_close.setMaximumSize(QSize(25, 25))
        icon17 = QIcon()
        icon17.addFile(u"../../../images/svg_icons/icon_close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon17)
        self.btn_close.setIconSize(QSize(19, 19))

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_continer_control_window)


        self.verticalLayout.addWidget(self.title_bar)

        self.container_central_frame = QFrame(self.central_frame)
        self.container_central_frame.setObjectName(u"container_central_frame")
        self.container_central_frame.setStyleSheet(u"")
        self.container_central_frame.setFrameShape(QFrame.StyledPanel)
        self.container_central_frame.setFrameShadow(QFrame.Raised)
        self.pushButton_test = PyPushButton(self.container_central_frame)
        self.pushButton_test.setObjectName(u"pushButton_test")
        self.pushButton_test.setGeometry(QRect(160, 220, 171, 37))
        self.pushButton_test.setMinimumSize(QSize(37, 37))
        self.pushButton_test.setMaximumSize(QSize(1234, 37))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.pushButton_test.setFont(font)
        self.label_3 = QLabel(self.container_central_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 220, 91, 41))
        self.label_3.setStyleSheet(u"background-color: rgb(233, 234, 236);")
        self.pushButton_test_2 = PyPushButton(self.container_central_frame)
        self.pushButton_test_2.setObjectName(u"pushButton_test_2")
        self.pushButton_test_2.setGeometry(QRect(160, 60, 37, 37))
        self.pushButton_test_2.setMinimumSize(QSize(37, 37))
        self.pushButton_test_2.setMaximumSize(QSize(1234, 37))
        self.pushButton_test_2.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: rgb(38, 39, 43);\n"
"            padding-left: 55px;\n"
"            text-align: left;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}\n"
" QPushButton:hover {\n"
" 	background-color: rgb(49, 50, 55)\n"
" }\n"
"QPushButton:pressed {\n"
" 	background-color: rgb(38, 39, 43);\n"
"}")
        self.pushButton_test_3 = PyPushButton(self.container_central_frame)
        self.pushButton_test_3.setObjectName(u"pushButton_test_3")
        self.pushButton_test_3.setGeometry(QRect(270, 60, 37, 37))
        self.pushButton_test_3.setMinimumSize(QSize(37, 37))
        self.pushButton_test_3.setMaximumSize(QSize(1234, 37))
        self.pushButton_25 = QPushButton(self.container_central_frame)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(230, 310, 38, 37))
        self.pushButton_25.setMinimumSize(QSize(37, 37))
        self.pushButton_25.setMaximumSize(QSize(1234, 37))
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet(u"background-color: rgb(38, 39, 43);\n"
"border-radius: 8px")
        icon18 = QIcon()
        icon18.addFile(u"../../../../../../../Downloads/existinginventorymajor-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_25.setIcon(icon18)
        self.pushButton_25.setIconSize(QSize(20, 20))
        self.pushButton_12 = PyPushButton(self.container_central_frame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(90, 330, 37, 37))
        self.pushButton_12.setMinimumSize(QSize(37, 37))
        self.pushButton_12.setMaximumSize(QSize(1234, 37))
        self.pushButton_12.setStyleSheet(u" 	background-color: rgb(65, 80, 173);\n"
"border-radius: 8px;\n"
"padding-left:1px;\n"
"color: rgb(255, 255, 255);\n"
"text-align: left")
        icon19 = QIcon()
        icon19.addFile(u"../../../../../../../Downloads/shopping-bag-4-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon19)
        self.pushButton_12.setIconSize(QSize(36, 36))
        self.pushButton_test_4 = PyPushButton(self.container_central_frame)
        self.pushButton_test_4.setObjectName(u"pushButton_test_4")
        self.pushButton_test_4.setGeometry(QRect(160, 110, 37, 37))
        self.pushButton_test_4.setMinimumSize(QSize(37, 37))
        self.pushButton_test_4.setMaximumSize(QSize(1234, 37))
        self.pushButton_test_4.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: rgb(38, 39, 43);\n"
"            padding-left: 55px;\n"
"            text-align: left;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}\n"
" QPushButton:hover {\n"
" 	background-color: rgb(65, 80, 173);\n"
" }\n"
"QPushButton:pressed {\n"
" 	background-color: rgb(88, 106, 233);\n"
"}")
        self.pushButton_26 = QPushButton(self.container_central_frame)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(260, 360, 38, 37))
        self.pushButton_26.setMinimumSize(QSize(37, 37))
        self.pushButton_26.setMaximumSize(QSize(1234, 37))
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet(u"background-color: rgb(38, 39, 43);\n"
"border-radius: 8px")
        self.pushButton_26.setIcon(icon9)
        self.pushButton_26.setIconSize(QSize(43, 43))
        self.pushButton_27 = QPushButton(self.container_central_frame)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setGeometry(QRect(140, 330, 38, 37))
        self.pushButton_27.setMinimumSize(QSize(37, 37))
        self.pushButton_27.setMaximumSize(QSize(1234, 37))
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet(u" 	background-color: rgb(88, 106, 233);\n"
"border-radius: 8px")
        self.pushButton_27.setIcon(icon11)
        self.pushButton_27.setIconSize(QSize(30, 30))
        self.label_2 = QLabel(self.container_central_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 170, 91, 41))
        self.label_2.setStyleSheet(u"\n"
"background-color: rgb(89, 109, 235);")
        self.label_4 = QLabel(self.container_central_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 120, 91, 41))
        self.label_4.setStyleSheet(u"background-color: rgb(64, 80, 170);")
        self.label_5 = QLabel(self.container_central_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 20, 91, 41))
        self.label_5.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.label_6 = QLabel(self.container_central_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 70, 91, 41))
        self.label_6.setStyleSheet(u"background-color: rgb(49, 50, 55);")
        self.pushButton_test_5 = PyPushButton(self.container_central_frame)
        self.pushButton_test_5.setObjectName(u"pushButton_test_5")
        self.pushButton_test_5.setGeometry(QRect(160, 160, 37, 37))
        self.pushButton_test_5.setMinimumSize(QSize(37, 37))
        self.pushButton_test_5.setMaximumSize(QSize(1234, 37))
        self.pushButton_test_5.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: rgb(88, 106, 233);\n"
"            padding-left: 55px;\n"
"            text-align: left;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}\n"
" QPushButton:hover {\n"
" 	background-color: rgb(65, 80, 173);\n"
" }\n"
"QPushButton:pressed {\n"
" 	\n"
"	background-color: rgb(88, 106, 233);\n"
"}")

        self.verticalLayout.addWidget(self.container_central_frame)


        self.horizontalLayout_2.addWidget(self.central_frame)


        self.horizontalLayout.addWidget(self.central_widget)

        MainWindow.setCentralWidget(self.widget_style_sheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_back.setText("")
        self.btn_menu.setText("")
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_compra.setText(QCoreApplication.translate("MainWindow", u"Compra", None))
        self.btn_venda.setText(QCoreApplication.translate("MainWindow", u"Venda", None))
        self.btn_relatorio.setText(QCoreApplication.translate("MainWindow", u"Relatorio", None))
        self.btn_service.setText(QCoreApplication.translate("MainWindow", u"Servi\u00e7os", None))
        self.btn_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio", None))
        self.btn_cliente.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.btn_agenda.setText(QCoreApplication.translate("MainWindow", u"Agenda", None))
        self.btn_recibo.setText(QCoreApplication.translate("MainWindow", u"Recibo", None))
        self.btn_copia_seguranca.setText(QCoreApplication.translate("MainWindow", u"C\u00f3pia de seguran\u00e7a", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o", None))
        self.btn_info.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00e3o", None))
        self.btn_user.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.pushButton_test.setText(QCoreApplication.translate("MainWindow", u"relatorio", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"#e9eaec", None))
        self.pushButton_test_2.setText(QCoreApplication.translate("MainWindow", u"Test mais uma vez", None))
        self.pushButton_test_3.setText(QCoreApplication.translate("MainWindow", u"Test mais uma vez", None))
        self.pushButton_25.setText("")
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Venda", None))
        self.pushButton_test_4.setText(QCoreApplication.translate("MainWindow", u"Test mais uma vez", None))
        self.pushButton_26.setText("")
        self.pushButton_27.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"#596deb", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"#4050aa", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"#26272b", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"#313237", None))
        self.pushButton_test_5.setText(QCoreApplication.translate("MainWindow", u"Test mais uma vez", None))
    # retranslateUi

