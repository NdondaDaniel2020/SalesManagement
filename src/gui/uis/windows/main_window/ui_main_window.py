# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowQuBhKS.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QStackedWidget, QVBoxLayout, QWidget)

from src.gui.widgets.py_custom_push_button.py_custom_push_button import PyCustomPushButton
from src.gui.widgets.py_painel_button.py_painel_button import PyPanelButton
from src.gui.widgets.py_scroll_area.py_scroall_area import PyScrollArea
from src.gui.widgets.py_user_button.py_user_button import PyUserButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(601, 679)
        self.widget_style_sheet = QWidget(MainWindow)
        self.widget_style_sheet.setObjectName(u"widget_style_sheet")
        self.widget_style_sheet.setStyleSheet(u"#central_widget,\n"
"#line_left_menu,\n"
"#line_title_bar{\n"
"background-color: rgb(32, 33, 37);\n"
"border-radius: 7px}\n"
"\n"
"#back_ground_frame_line{\n"
"    background-color: rgb(32, 33, 37);\n"
"    border-radius: 8.4px}\n"
"\n"
"#frame_line{\n"
"	background-color: rgb(64, 80, 170);\n"
"	border-radius: 8px}\n"
"\n"
"#stacked_widget, #stacked_widget > QWidget{\n"
"    background-color: rgb(19, 20, 22);\n"
"    border-radius: 7px;}\n"
"\n"
"#scroll_area_widget_contents_left_menu,\n"
"#scroll_area_left_menu{\n"
"    background-color: rgb(32, 33, 37);\n"
"    border:none}\n"
"\n"
"#frame_continer > Qwidget, QFrame{\n"
"background-color: rgb(32, 33, 37);\n"
"border-radius: 10px;\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"/* style all QScrollBar*/\n"
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
""
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
"    subcontrol-origin: margin;\n"
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
"     m"
                        "argin: 21px 0 21px 0;\n"
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
"     background: #313237;\n"
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
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vert"
                        "ical {\n"
"     background: none;\n"
"}\n"
"")
        self.horizontal_layout_widget_style_sheet = QHBoxLayout(self.widget_style_sheet)
        self.horizontal_layout_widget_style_sheet.setSpacing(0)
        self.horizontal_layout_widget_style_sheet.setObjectName(u"horizontal_layout_widget_style_sheet")
        self.horizontal_layout_widget_style_sheet.setContentsMargins(5, 5, 5, 5)
        self.back_ground_frame_line = QFrame(self.widget_style_sheet)
        self.back_ground_frame_line.setObjectName(u"back_ground_frame_line")
        self.back_ground_frame_line.setFrameShape(QFrame.StyledPanel)
        self.back_ground_frame_line.setFrameShadow(QFrame.Raised)
        self.horizontal_layout_back_ground_frame_line = QHBoxLayout(self.back_ground_frame_line)
        self.horizontal_layout_back_ground_frame_line.setSpacing(0)
        self.horizontal_layout_back_ground_frame_line.setObjectName(u"horizontal_layout_back_ground_frame_line")
        self.horizontal_layout_back_ground_frame_line.setContentsMargins(1, 1, 1, 1)
        self.frame_line = QFrame(self.back_ground_frame_line)
        self.frame_line.setObjectName(u"frame_line")
        self.frame_line.setFrameShape(QFrame.StyledPanel)
        self.frame_line.setFrameShadow(QFrame.Raised)
        self.vertical_layout_frame_line = QVBoxLayout(self.frame_line)
        self.vertical_layout_frame_line.setSpacing(0)
        self.vertical_layout_frame_line.setObjectName(u"vertical_layout_frame_line")
        self.vertical_layout_frame_line.setContentsMargins(1, 1, 1, 1)
        self.central_widget = QWidget(self.frame_line)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.frame_left_menu = QFrame(self.central_widget)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setEnabled(True)
        self.frame_left_menu.setMinimumSize(QSize(46, 0))
        self.frame_left_menu.setMaximumSize(QSize(46, 16777215))
        self.frame_left_menu.setStyleSheet(u"")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_left_menu)

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
        self.frame_logo.setMinimumSize(QSize(110, 0))
        self.frame_logo.setStyleSheet(u"")
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_logo)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.frame_logo)
        self.logo.setObjectName(u"logo")
        self.logo.setPixmap(QPixmap(u"../../../../../../../../images/svg_images/logo_top_100x22.svg"))

        self.horizontalLayout_6.addWidget(self.logo)


        self.horizontalLayout_4.addWidget(self.frame_logo)

        self.horizontalSpacer = QSpacerItem(427, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.frame_control_window = QFrame(self.title_bar)
        self.frame_control_window.setObjectName(u"frame_control_window")
        self.frame_control_window.setMinimumSize(QSize(97, 0))
        self.frame_control_window.setStyleSheet(u"")
        self.frame_control_window.setFrameShape(QFrame.StyledPanel)
        self.frame_control_window.setFrameShadow(QFrame.Raised)
        self.horizontal_layout_frame_control_window = QHBoxLayout(self.frame_control_window)
        self.horizontal_layout_frame_control_window.setSpacing(7)
        self.horizontal_layout_frame_control_window.setObjectName(u"horizontal_layout_frame_control_window")
        self.horizontal_layout_frame_control_window.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4.addWidget(self.frame_control_window)


        self.verticalLayout.addWidget(self.title_bar)

        self.frame_base = QFrame(self.central_frame)
        self.frame_base.setObjectName(u"frame_base")
        self.frame_base.setFrameShape(QFrame.StyledPanel)
        self.frame_base.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_base)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_column = QFrame(self.frame_base)
        self.left_column.setObjectName(u"left_column")
        self.left_column.setMinimumSize(QSize(0, 0))
        self.left_column.setMaximumSize(QSize(0, 16777215))
        font = QFont()
        font.setPointSize(13)
        self.left_column.setFont(font)
        self.left_column.setStyleSheet(u"")
        self.left_column.setFrameShape(QFrame.StyledPanel)
        self.left_column.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.left_column)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_qrcode = QFrame(self.left_column)
        self.frame_qrcode.setObjectName(u"frame_qrcode")
        self.frame_qrcode.setMinimumSize(QSize(180, 0))
        self.frame_qrcode.setMaximumSize(QSize(16777215, 146))
        self.frame_qrcode.setStyleSheet(u"")
        self.frame_qrcode.setFrameShape(QFrame.StyledPanel)
        self.frame_qrcode.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_qrcode)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.qrcode = QPushButton(self.frame_qrcode)
        self.qrcode.setObjectName(u"qrcode")
        self.qrcode.setMinimumSize(QSize(0, 130))
        self.qrcode.setStyleSheet(u"QPushButton {border: none;}\n"
"QPushButton:hover{border: none;}\n"
"QPushButton:pressed {border: none;}\n"
"")
        icon = QIcon()
        icon.addFile(u"../../../images/svg_images/SalesManagement.png", QSize(), QIcon.Normal, QIcon.Off)
        self.qrcode.setIcon(icon)
        self.qrcode.setIconSize(QSize(130, 130))

        self.verticalLayout_13.addWidget(self.qrcode)


        self.verticalLayout_11.addWidget(self.frame_qrcode, 0, Qt.AlignLeft)

        self.frame_26 = QFrame(self.left_column)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_26)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_28)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_28)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color: rgb(222, 223, 225);")

        self.verticalLayout_15.addWidget(self.label_17, 0, Qt.AlignHCenter)

        self.label_16 = QLabel(self.frame_28)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 16))
        self.label_16.setStyleSheet(u"color: rgb(222, 223, 225);")

        self.verticalLayout_15.addWidget(self.label_16)

        self.label_18 = QLabel(self.frame_28)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: rgb(222, 223, 225);")

        self.verticalLayout_15.addWidget(self.label_18, 0, Qt.AlignHCenter)

        self.frame_35 = QFrame(self.frame_28)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 19))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_35)

        self.label_19 = QLabel(self.frame_28)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(13)
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.verticalLayout_15.addWidget(self.label_19)

        self.frame_27 = QFrame(self.frame_28)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_27)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 4, 0, 0)
        self.widget_1 = PyCustomPushButton(self.frame_27)
        self.widget_1.setObjectName(u"widget_1")
        self.widget_1.setMinimumSize(QSize(0, 37))
        self.widget_1.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(32, 33, 37);\n"
"	border: 1px solid rgb(44, 45, 50);\n"
"	border-radius: 8px;\n"
"}\n"
"QWidget:hover{\n"
"	background-color: rgb(65, 80, 173);\n"
"	border-radius: 8px;\n"
"}\n"
"QWidget:focus {\n"
" 	background-color: rgb(88, 106, 233);\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_1)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 0, 2, 0)

        self.verticalLayout_17.addWidget(self.widget_1)

        self.widget_2 = PyCustomPushButton(self.frame_27)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 37))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(32, 33, 37);\n"
"	border: 1px solid rgb(44, 45, 50);\n"
"	border-radius: 8px;\n"
"}\n"
"QWidget:hover{\n"
"	background-color: rgb(65, 80, 173);\n"
"	border-radius: 8px;\n"
"}\n"
"QWidget:focus {\n"
" 	background-color: rgb(88, 106, 233);\n"
"}")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(2, 0, 2, 0)

        self.verticalLayout_17.addWidget(self.widget_2)

        self.widget_3 = PyCustomPushButton(self.frame_27)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 37))
        self.widget_3.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(32, 33, 37);\n"
"	border: 1px solid rgb(44, 45, 50);\n"
"	border-radius: 8px;\n"
"}\n"
"QWidget:hover{\n"
"	background-color: rgb(65, 80, 173);\n"
"	border-radius: 8px;\n"
"}\n"
"QWidget:focus {\n"
" 	background-color: rgb(88, 106, 233);\n"
"}")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(2, 0, 2, 0)

        self.verticalLayout_17.addWidget(self.widget_3)


        self.verticalLayout_15.addWidget(self.frame_27)

        self.frame_31 = QFrame(self.frame_28)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 19))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_31)

        self.label_15 = QLabel(self.frame_28)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.verticalLayout_15.addWidget(self.label_15)

        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_29)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(2, 0, 0, 0)
        self.frest_user = PyUserButton(self.frame_29)
        self.frest_user.setObjectName(u"frest_user")
        self.frest_user.setMinimumSize(QSize(0, 37))
        font2 = QFont()
        font2.setPointSize(9)
        self.frest_user.setFont(font2)
        self.frest_user.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(38, 39, 43);\n"
"	border: 1px solid rgb(47, 54, 100);\n"
"	border-radius: 8px;\n"
"}\n"
"QWidget:hover{\n"
"	background-color: rgb(65, 80, 173);\n"
"	border-radius: 8px;\n"
"}\n"
"QWidget:focus {\n"
" 	background-color: rgb(88, 106, 233);\n"
"}")
        self.horizontalLayout_20 = QHBoxLayout(self.frest_user)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(2, 0, 2, 0)

        self.verticalLayout_16.addWidget(self.frest_user)

        self.verticalSpacer = QSpacerItem(20, 228, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer)


        self.verticalLayout_15.addWidget(self.frame_29)


        self.verticalLayout_14.addWidget(self.frame_28)


        self.verticalLayout_11.addWidget(self.frame_26)


        self.horizontalLayout.addWidget(self.left_column, 0, Qt.AlignLeft)

        self.stacked_widget = QStackedWidget(self.frame_base)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 280, 91, 41))
        self.label_3.setStyleSheet(u"background-color: rgb(233, 234, 236);")
        self.pushButton_test_4 = QPushButton(self.page)
        self.pushButton_test_4.setObjectName(u"pushButton_test_4")
        self.pushButton_test_4.setGeometry(QRect(140, 120, 37, 37))
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
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 230, 91, 41))
        self.label_2.setStyleSheet(u"\n"
"background-color: rgb(89, 109, 235);")
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 30, 91, 41))
        self.label_5.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 180, 91, 41))
        self.label_4.setStyleSheet(u"background-color: rgb(64, 80, 170);")
        self.pushButton_test_5 = QPushButton(self.page)
        self.pushButton_test_5.setObjectName(u"pushButton_test_5")
        self.pushButton_test_5.setGeometry(QRect(140, 170, 37, 37))
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
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 80, 91, 41))
        self.label_6.setStyleSheet(u"background-color: rgb(49, 50, 55);")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 130, 91, 41))
        self.label_7.setStyleSheet(u"background-color: #2f3664;")
        self.pushButton_test_2 = QPushButton(self.page)
        self.pushButton_test_2.setObjectName(u"pushButton_test_2")
        self.pushButton_test_2.setGeometry(QRect(140, 70, 37, 37))
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
        self.frame_30 = QFrame(self.page)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setGeometry(QRect(70, 350, 191, 41))
        self.frame_30.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(38, 39, 43);\n"
"	border-radius: 8px;\n"
"}\n"
"QFrame:hover{\n"
"	background-color: rgb(65, 80, 173);\n"
"	border-radius: 8px;\n"
"}\n"
"QFrame:focus {\n"
" 	background-color: rgb(88, 106, 233);\n"
"}")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 0, 2, 0)
        self.pushButton_test_9 = QPushButton(self.frame_30)
        self.pushButton_test_9.setObjectName(u"pushButton_test_9")
        self.pushButton_test_9.setMinimumSize(QSize(37, 37))
        self.pushButton_test_9.setMaximumSize(QSize(1234, 37))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semibold"])
        font3.setPointSize(10)
        self.pushButton_test_9.setFont(font3)
        self.pushButton_test_9.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: transparent;\n"
"			 padding-left: 7px;\n"
"            text-align: left;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../../../../../../../../../Downloads/Imagens/analytics-hands-report-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_test_9.setIcon(icon1)
        self.pushButton_test_9.setIconSize(QSize(26, 26))

        self.horizontalLayout_5.addWidget(self.pushButton_test_9)

        self.pushButton_test_10 = QPushButton(self.frame_30)
        self.pushButton_test_10.setObjectName(u"pushButton_test_10")
        self.pushButton_test_10.setMinimumSize(QSize(36, 37))
        self.pushButton_test_10.setMaximumSize(QSize(36, 37))
        self.pushButton_test_10.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: transparent;;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../../../../../../../../../Downloads/more-horizontal-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_test_10.setIcon(icon2)
        self.pushButton_test_10.setIconSize(QSize(21, 21))

        self.horizontalLayout_5.addWidget(self.pushButton_test_10)

        self.frame_36 = QFrame(self.page)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setGeometry(QRect(20, 460, 190, 36))
        self.frame_36.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(32, 33, 37);\n"
"	border: 1px solid rgb(44, 45, 50);\n"
"	border-radius: 8px;\n"
"}\n"
"QFrame:hover{\n"
"	background-color: rgb(65, 80, 173);\n"
"	border-radius: 8px;\n"
"}\n"
"QFrame:focus {\n"
" 	background-color: rgb(88, 106, 233);\n"
"}")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(2, 0, 2, 0)
        self.pushButton_test_19 = QPushButton(self.frame_36)
        self.pushButton_test_19.setObjectName(u"pushButton_test_19")
        self.pushButton_test_19.setMinimumSize(QSize(37, 37))
        self.pushButton_test_19.setMaximumSize(QSize(36, 37))
        self.pushButton_test_19.setFont(font3)
        self.pushButton_test_19.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: rgb(255, 170, 255);\n"
"			 padding-left: 7px;\n"
"            text-align: left;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}\n"
"")
        self.pushButton_test_19.setIcon(icon1)
        self.pushButton_test_19.setIconSize(QSize(26, 26))

        self.horizontalLayout_18.addWidget(self.pushButton_test_19, 0, Qt.AlignLeft)

        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"border:none;\n"
"background-color: transparent;")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_37)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_37)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 10))
        self.label_14.setMaximumSize(QSize(16777215, 13))
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border:none")

        self.verticalLayout_18.addWidget(self.label_14, 0, Qt.AlignLeft)

        self.label_20 = QLabel(self.frame_37)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 10))
        self.label_20.setMaximumSize(QSize(16777215, 10))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Light"])
        font4.setPointSize(7)
        self.label_20.setFont(font4)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border:none;\n"
"padding-left: 0.4px;")

        self.verticalLayout_18.addWidget(self.label_20, 0, Qt.AlignLeft)


        self.horizontalLayout_18.addWidget(self.frame_37, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_2)

        self.pushButton_test_20 = QPushButton(self.frame_36)
        self.pushButton_test_20.setObjectName(u"pushButton_test_20")
        self.pushButton_test_20.setMinimumSize(QSize(36, 37))
        self.pushButton_test_20.setMaximumSize(QSize(36, 37))
        self.pushButton_test_20.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: transparent;;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}")
        self.pushButton_test_20.setIcon(icon2)
        self.pushButton_test_20.setIconSize(QSize(21, 21))

        self.horizontalLayout_18.addWidget(self.pushButton_test_20)

        self.stacked_widget.addWidget(self.page)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_2 = QVBoxLayout(self.page_home)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.frame_continer = QFrame(self.page_home)
        self.frame_continer.setObjectName(u"frame_continer")
        self.frame_continer.setMinimumSize(QSize(0, 160))
        self.frame_continer.setMaximumSize(QSize(16777215, 160))
        self.frame_continer.setStyleSheet(u"")
        self.frame_continer.setFrameShape(QFrame.StyledPanel)
        self.frame_continer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_continer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.scroll_area_home = PyScrollArea(self.frame_continer)
        self.scroll_area_home.setObjectName(u"scroll_area_home")
        self.scroll_area_home.setMinimumSize(QSize(513, 156))
        self.scroll_area_home.setMaximumSize(QSize(16777215, 156))
        self.scroll_area_home.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_home.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area_home.setWidgetResizable(True)
        self.scroll_area_widget_contents_home = QWidget()
        self.scroll_area_widget_contents_home.setObjectName(u"scroll_area_widget_contents_home")
        self.scroll_area_widget_contents_home.setGeometry(QRect(0, 0, 1021, 148))
        self.scroll_area_widget_contents_home.setStyleSheet(u"#scroll_area_home, #scroll_area_widget_contents_home{\n"
"background-color:rgb(32, 33, 37);\n"
"border-radius:10px}")
        self.horizontalLayout_8 = QHBoxLayout(self.scroll_area_widget_contents_home)
        self.horizontalLayout_8.setSpacing(9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.frame_1 = PyPanelButton(self.scroll_area_widget_contents_home)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setMinimumSize(QSize(246, 132))
        self.pushButton_4 = QPushButton(self.frame_1)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(9, 13, 61, 61))
        font5 = QFont()
        font5.setPointSize(8)
        self.pushButton_4.setFont(font5)
        self.pushButton_4.setStyleSheet(u"border:none")
        icon3 = QIcon()
        icon3.addFile(u"../../../images/svg_icons/icon_sale.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(60, 57))
        self.label_41 = QLabel(self.frame_1)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(75, 40, 71, 28))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI Semibold"])
        font6.setPointSize(14)
        self.label_41.setFont(font6)
        self.label_41.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_42 = QLabel(self.frame_1)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(9, 102, 157, 26))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI Semilight"])
        font7.setPointSize(11)
        self.label_42.setFont(font7)
        self.label_42.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_43 = QLabel(self.frame_1)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(10, 80, 110, 28))
        self.label_43.setFont(font7)
        self.label_43.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_44 = QLabel(self.frame_1)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(120, 80, 84, 28))
        self.label_44.setFont(font7)
        self.label_44.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_45 = QLabel(self.frame_1)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(145, 100, 59, 28))
        self.label_45.setFont(font7)
        self.label_45.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.frame_1)

        self.frame_7 = PyPanelButton(self.scroll_area_widget_contents_home)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(245, 132))
        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(6, 10, 61, 61))
        self.pushButton_6.setFont(font5)
        self.pushButton_6.setStyleSheet(u"border:none")
        icon4 = QIcon()
        icon4.addFile(u"../../../images/svg_icons/icon_box.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(65, 65))
        self.label_46 = QLabel(self.frame_7)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(70, 40, 50, 28))
        self.label_46.setFont(font6)
        self.label_46.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_47 = QLabel(self.frame_7)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(140, 98, 59, 28))
        self.label_47.setFont(font7)
        self.label_47.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_49 = QLabel(self.frame_7)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(11, 78, 110, 28))
        self.label_49.setFont(font7)
        self.label_49.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_50 = QLabel(self.frame_7)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(10, 100, 157, 26))
        self.label_50.setFont(font7)
        self.label_50.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")

        self.horizontalLayout_8.addWidget(self.frame_7)

        self.frame_8 = PyPanelButton(self.scroll_area_widget_contents_home)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(246, 132))
        self.label_48 = QLabel(self.frame_8)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(70, 40, 50, 28))
        self.label_48.setFont(font6)
        self.label_48.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_51 = QLabel(self.frame_8)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(139, 100, 59, 28))
        self.label_51.setFont(font7)
        self.label_51.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_52 = QLabel(self.frame_8)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(9, 102, 157, 26))
        self.label_52.setFont(font7)
        self.label_52.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.pushButton_17 = QPushButton(self.frame_8)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(7, 12, 61, 61))
        self.pushButton_17.setFont(font5)
        self.pushButton_17.setStyleSheet(u"border:none")
        icon5 = QIcon()
        icon5.addFile(u"../../../images/svg_icons/icon_line_chart_down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon5)
        self.pushButton_17.setIconSize(QSize(63, 63))
        self.label_53 = QLabel(self.frame_8)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(10, 80, 110, 28))
        self.label_53.setFont(font7)
        self.label_53.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")

        self.horizontalLayout_8.addWidget(self.frame_8)

        self.frame_22 = PyPanelButton(self.scroll_area_widget_contents_home)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(245, 132))
        self.label_54 = QLabel(self.frame_22)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(69, 40, 80, 28))
        self.label_54.setFont(font6)
        self.label_54.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_55 = QLabel(self.frame_22)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(139, 98, 59, 28))
        self.label_55.setFont(font7)
        self.label_55.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_55.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_56 = QLabel(self.frame_22)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(9, 100, 157, 26))
        self.label_56.setFont(font7)
        self.label_56.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.pushButton_18 = QPushButton(self.frame_22)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(8, 13, 61, 61))
        self.pushButton_18.setFont(font5)
        self.pushButton_18.setStyleSheet(u"border:none")
        icon6 = QIcon()
        icon6.addFile(u"../../../images/svg_icons/Icon_receipt_svgrepo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon6)
        self.pushButton_18.setIconSize(QSize(53, 54))
        self.label_57 = QLabel(self.frame_22)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(10, 78, 110, 28))
        self.label_57.setFont(font7)
        self.label_57.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")

        self.horizontalLayout_8.addWidget(self.frame_22)

        self.scroll_area_home.setWidget(self.scroll_area_widget_contents_home)

        self.verticalLayout_6.addWidget(self.scroll_area_home)


        self.verticalLayout_2.addWidget(self.frame_continer)

        self.frame_3 = QFrame(self.page_home)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(19, 20, 22);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QSize(12345678, 16777215))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(191, 121))
        self.frame_12.setStyleSheet(u"background-color: rgb(19, 20, 22);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(191, 121))
        self.frame_14.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(191, 121))
        self.frame_13.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_13)


        self.verticalLayout_5.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(191, 121))
        self.frame_11.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_23 = QFrame(self.frame_11)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(40, 40, 201, 71))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.widget = QWidget(self.frame_11)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(400, 9, 251, 121))

        self.verticalLayout_5.addWidget(self.frame_11)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 0))
        self.frame_4.setMaximumSize(QSize(250, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(19, 20, 22);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(191, 143))
        self.frame_10.setMaximumSize(QSize(16777215, 187))
        self.frame_10.setStyleSheet(u"background-color: rgb(64, 80, 170);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_10)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_20)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(9, 3, 150, 30))
        font8 = QFont()
        font8.setPointSize(12)
        self.label_8.setFont(font8)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_10)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 70))
        self.frame_21.setStyleSheet(u"background-color: rgb(45, 52, 96);\n"
"border-radius: 10px;\n"
"border-top-left-radius: 35px;\n"
"border-top-right-radius: 35px;\n"
"\n"
"background-image: url(:/img/Captura_azul.png);\n"
"background-position: center center;\n"
"background-reapite:norepite;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_21)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(191, 116))
        self.frame_9.setMaximumSize(QSize(16777215, 276))
        self.frame_9.setStyleSheet(u"background-color: #2f3664;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 0, 0)
        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 16))
        font9 = QFont()
        font9.setFamilies([u"Segoe UI Semibold"])
        font9.setPointSize(12)
        font9.setBold(False)
        self.label_9.setFont(font9)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_9)

        self.frame_6 = QFrame(self.frame_9)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 50))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton = QPushButton(self.frame_15)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(38, 38))
        self.pushButton.setMaximumSize(QSize(38, 38))
        icon7 = QIcon()
        icon7.addFile(u"../../../../../../../../../Downloads/alarm-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(35, 35))

        self.horizontalLayout_9.addWidget(self.pushButton)

        self.splitter = QSplitter(self.frame_15)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.label_10 = QLabel(self.splitter)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 16))
        font10 = QFont()
        font10.setFamilies([u"Segoe UI Semibold"])
        font10.setPointSize(9)
        font10.setBold(False)
        self.label_10.setFont(font10)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter.addWidget(self.label_10)
        self.label_11 = QLabel(self.splitter)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(71, 0))
        font11 = QFont()
        font11.setFamilies([u"Segoe UI"])
        font11.setPointSize(11)
        self.label_11.setFont(font11)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter.addWidget(self.label_11)

        self.horizontalLayout_9.addWidget(self.splitter)

        self.label_13 = QLabel(self.frame_15)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(70, 24))
        self.label_13.setPixmap(QPixmap(u"../../../../../../../../../OneDrive/Imagens/Capturas de Ecr\u00e3/Captura de ecr\u00e3 2023-11-29 023052.png"))

        self.horizontalLayout_9.addWidget(self.label_13)

        self.label_12 = QLabel(self.frame_15)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.label_12)

        self.pushButton_2 = QPushButton(self.frame_15)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 30))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(64, 80, 170);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.pushButton_2)


        self.verticalLayout_8.addWidget(self.frame_15)

        self.frame_19 = QFrame(self.frame_6)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 50))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_13 = QPushButton(self.frame_19)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(38, 38))
        self.pushButton_13.setMaximumSize(QSize(38, 38))
        self.pushButton_13.setIcon(icon7)
        self.pushButton_13.setIconSize(QSize(35, 35))

        self.horizontalLayout_15.addWidget(self.pushButton_13)

        self.splitter_7 = QSplitter(self.frame_19)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Vertical)
        self.label_34 = QLabel(self.splitter_7)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 16))
        self.label_34.setFont(font10)
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter_7.addWidget(self.label_34)
        self.label_35 = QLabel(self.splitter_7)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(71, 0))
        self.label_35.setFont(font11)
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter_7.addWidget(self.label_35)

        self.horizontalLayout_15.addWidget(self.splitter_7)

        self.label_36 = QLabel(self.frame_19)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(70, 24))
        self.label_36.setPixmap(QPixmap(u"../../../../../../../../../OneDrive/Imagens/Capturas de Ecr\u00e3/Captura de ecr\u00e3 2023-11-29 023052.png"))

        self.horizontalLayout_15.addWidget(self.label_36)

        self.label_37 = QLabel(self.frame_19)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)
        self.label_37.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.label_37)

        self.pushButton_14 = QPushButton(self.frame_19)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(40, 30))
        self.pushButton_14.setStyleSheet(u"background-color: rgb(64, 80, 170);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.pushButton_14)


        self.verticalLayout_8.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.frame_6)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 50))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_11 = QPushButton(self.frame_18)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(38, 38))
        self.pushButton_11.setMaximumSize(QSize(38, 38))
        self.pushButton_11.setIcon(icon7)
        self.pushButton_11.setIconSize(QSize(35, 35))

        self.horizontalLayout_14.addWidget(self.pushButton_11)

        self.splitter_6 = QSplitter(self.frame_18)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Vertical)
        self.label_30 = QLabel(self.splitter_6)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(16777215, 16))
        self.label_30.setFont(font10)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter_6.addWidget(self.label_30)
        self.label_31 = QLabel(self.splitter_6)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(71, 0))
        self.label_31.setFont(font11)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter_6.addWidget(self.label_31)

        self.horizontalLayout_14.addWidget(self.splitter_6)

        self.label_32 = QLabel(self.frame_18)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(70, 24))
        self.label_32.setPixmap(QPixmap(u"../../../../../../../../../OneDrive/Imagens/Capturas de Ecr\u00e3/Captura de ecr\u00e3 2023-11-29 023052.png"))

        self.horizontalLayout_14.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_18)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.label_33)

        self.pushButton_12 = QPushButton(self.frame_18)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(40, 30))
        self.pushButton_12.setStyleSheet(u"background-color: rgb(64, 80, 170);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.pushButton_12)


        self.verticalLayout_8.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.frame_6)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 50))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_9 = QPushButton(self.frame_17)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(38, 38))
        self.pushButton_9.setMaximumSize(QSize(38, 38))
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setIconSize(QSize(35, 35))

        self.horizontalLayout_13.addWidget(self.pushButton_9)

        self.splitter_5 = QSplitter(self.frame_17)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Vertical)
        self.label_26 = QLabel(self.splitter_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 16))
        self.label_26.setFont(font10)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter_5.addWidget(self.label_26)
        self.label_27 = QLabel(self.splitter_5)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(71, 0))
        self.label_27.setFont(font11)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter_5.addWidget(self.label_27)

        self.horizontalLayout_13.addWidget(self.splitter_5)

        self.label_28 = QLabel(self.frame_17)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(70, 24))
        self.label_28.setPixmap(QPixmap(u"../../../../../../../../../OneDrive/Imagens/Capturas de Ecr\u00e3/Captura de ecr\u00e3 2023-11-29 023052.png"))

        self.horizontalLayout_13.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_17)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.label_29)

        self.pushButton_10 = QPushButton(self.frame_17)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(40, 30))
        self.pushButton_10.setStyleSheet(u"background-color: rgb(64, 80, 170);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.pushButton_10)


        self.verticalLayout_8.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.frame_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 50))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_7 = QPushButton(self.frame_16)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(38, 38))
        self.pushButton_7.setMaximumSize(QSize(38, 38))
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setIconSize(QSize(35, 35))

        self.horizontalLayout_12.addWidget(self.pushButton_7)

        self.splitter_4 = QSplitter(self.frame_16)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.label_22 = QLabel(self.splitter_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 16))
        self.label_22.setFont(font10)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter_4.addWidget(self.label_22)
        self.label_23 = QLabel(self.splitter_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(71, 0))
        self.label_23.setFont(font11)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter_4.addWidget(self.label_23)

        self.horizontalLayout_12.addWidget(self.splitter_4)

        self.label_24 = QLabel(self.frame_16)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(70, 24))
        self.label_24.setPixmap(QPixmap(u"../../../../../../../../../OneDrive/Imagens/Capturas de Ecr\u00e3/Captura de ecr\u00e3 2023-11-29 023052.png"))

        self.horizontalLayout_12.addWidget(self.label_24)

        self.label_25 = QLabel(self.frame_16)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.label_25)

        self.pushButton_8 = QPushButton(self.frame_16)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(40, 30))
        self.pushButton_8.setStyleSheet(u"background-color: rgb(64, 80, 170);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.pushButton_8)


        self.verticalLayout_8.addWidget(self.frame_16)


        self.verticalLayout_7.addWidget(self.frame_6)


        self.verticalLayout_4.addWidget(self.frame_9)


        self.horizontalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.stacked_widget.addWidget(self.page_home)
        self.page_test = QWidget()
        self.page_test.setObjectName(u"page_test")
        self.stacked_widget.addWidget(self.page_test)

        self.horizontalLayout.addWidget(self.stacked_widget)


        self.verticalLayout.addWidget(self.frame_base)


        self.horizontalLayout_2.addWidget(self.central_frame)


        self.vertical_layout_frame_line.addWidget(self.central_widget)


        self.horizontal_layout_back_ground_frame_line.addWidget(self.frame_line)


        self.horizontal_layout_widget_style_sheet.addWidget(self.back_ground_frame_line)

        MainWindow.setCentralWidget(self.widget_style_sheet)

        self.retranslateUi(MainWindow)

        self.stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.qrcode.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Version: 0.0.1", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"GitHub: github.com/NdondaDaniel2020/SalesManagement", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Outros", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"#e9eaec", None))
        self.pushButton_test_4.setText(QCoreApplication.translate("MainWindow", u"Test mais uma vez", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"#596deb", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"#26272b", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"#4050aa", None))
        self.pushButton_test_5.setText(QCoreApplication.translate("MainWindow", u"Test mais uma vez", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"#313237", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"#2f3664", None))
        self.pushButton_test_2.setText(QCoreApplication.translate("MainWindow", u"Test mais uma vez", None))
        self.pushButton_test_9.setText(QCoreApplication.translate("MainWindow", u"Test mais uma vez", None))
        self.pushButton_test_10.setText("")
        self.pushButton_test_19.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"  Daniel", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"    Admin", None))
        self.pushButton_test_20.setText("")
        self.pushButton_4.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Venda", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Numero de vendas", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Total de Venda", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"14,4k", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.pushButton_6.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"997", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"N\u00edvel do stock", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Total de produtos", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Perda", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"997", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Total de perda", None))
        self.pushButton_17.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"N\u00edvel de perda", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Recibos", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"997", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Total de produtos", None))
        self.pushButton_18.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Total de recibos", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"MAIS REQUISITADO", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"  TOP MOVERS", None))
        self.pushButton.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Weke up", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"$1.123.34", None))
        self.label_13.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"+7.99", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
        self.pushButton_13.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Weke up", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"$1.123.34", None))
        self.label_36.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"+7.99", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
        self.pushButton_11.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Weke up", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"$1.123.34", None))
        self.label_32.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"+7.99", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
        self.pushButton_9.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Weke up", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"$1.123.34", None))
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"+7.99", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
        self.pushButton_7.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Weke up", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"$1.123.34", None))
        self.label_24.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"+7.99", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
    # retranslateUi

