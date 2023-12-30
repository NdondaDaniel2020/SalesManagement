# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowfpNbyl.ui'
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
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

from src.gui.widgets.py_circular_progress.py_circular_progress import PyCircularProgress
from src.gui.widgets.py_custom_push_button.py_custom_push_button import PyCustomPushButton
from src.gui.widgets.py_painel_button.py_painel_button import PyPanelButton
from src.gui.widgets.py_scroll_area.py_scroall_area import PyScrollArea
from src.gui.widgets.py_user_button.py_user_button import PyUserButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(805, 635)
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
        self.logo.setPixmap(QPixmap(u"../../../../../../../../../images/svg_images/logo_top_100x22.svg"))

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
        icon.addFile(u"../../../../../../../../../images/svg_images/SalesManagement.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.frame_30.setGeometry(QRect(20, 400, 191, 41))
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

        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(120, 220, 171, 171))
        self.frame_6.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.lineEdit_2 = QLineEdit(self.frame_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 20, 151, 35))
        self.lineEdit_2.setMinimumSize(QSize(0, 35))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(17, 18, 20);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLineEidit:hover{\n"
"border: 1px solid rgb(64, 80, 170);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 1px solid rgb(89, 109, 235);\n"
"border-bottom: 1px solid rgb(233, 234, 236);\n"
"}")
        self.lineEdit_3 = QLineEdit(self.frame_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 70, 151, 35))
        self.lineEdit_3.setMinimumSize(QSize(0, 35))
        font5 = QFont()
        font5.setPointSize(11)
        self.lineEdit_3.setFont(font5)
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"color: rgb(233, 234, 236);\n"
"border: 1px solid rgb(47, 54, 100);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLineEidit:hover{\n"
"border: 1px solid rgb(64, 80, 170);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 1px solid rgb(89, 109, 235);\n"
"border-bottom: 1px solid rgb(233, 234, 236);\n"
"}")
        self.lineEdit_4 = QLineEdit(self.frame_6)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(10, 120, 151, 35))
        self.lineEdit_4.setMinimumSize(QSize(0, 35))
        self.lineEdit_4.setStyleSheet(u"\n"
"QLineEdit:focus{\n"
"border: 1px solid rgb(89, 109, 235);\n"
"border-bottom: 4px solid rgb(233, 234, 236);\n"
"}")
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
        font6 = QFont()
        font6.setPointSize(8)
        self.pushButton_4.setFont(font6)
        self.pushButton_4.setStyleSheet(u"border:none")
        icon3 = QIcon()
        icon3.addFile(u"../../../../../../../../../images/svg_icons/icon_sale.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(60, 57))
        self.label_41 = QLabel(self.frame_1)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(75, 40, 71, 28))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI Semibold"])
        font7.setPointSize(14)
        self.label_41.setFont(font7)
        self.label_41.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_42 = QLabel(self.frame_1)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(9, 102, 157, 26))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI Semilight"])
        font8.setPointSize(11)
        self.label_42.setFont(font8)
        self.label_42.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_43 = QLabel(self.frame_1)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(10, 80, 110, 28))
        self.label_43.setFont(font8)
        self.label_43.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_44 = QLabel(self.frame_1)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(120, 80, 84, 28))
        self.label_44.setFont(font8)
        self.label_44.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_45 = QLabel(self.frame_1)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(145, 100, 59, 28))
        self.label_45.setFont(font8)
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
        self.pushButton_6.setFont(font6)
        self.pushButton_6.setStyleSheet(u"border:none")
        icon4 = QIcon()
        icon4.addFile(u"../../../../../../../../../images/svg_icons/icon_box.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(65, 65))
        self.label_46 = QLabel(self.frame_7)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(70, 40, 50, 28))
        self.label_46.setFont(font7)
        self.label_46.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_47 = QLabel(self.frame_7)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(140, 98, 59, 28))
        self.label_47.setFont(font8)
        self.label_47.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_49 = QLabel(self.frame_7)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(11, 78, 110, 28))
        self.label_49.setFont(font8)
        self.label_49.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_50 = QLabel(self.frame_7)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(10, 100, 157, 26))
        self.label_50.setFont(font8)
        self.label_50.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")

        self.horizontalLayout_8.addWidget(self.frame_7)

        self.frame_8 = PyPanelButton(self.scroll_area_widget_contents_home)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(246, 132))
        self.label_48 = QLabel(self.frame_8)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(70, 40, 50, 28))
        self.label_48.setFont(font7)
        self.label_48.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_51 = QLabel(self.frame_8)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(139, 100, 59, 28))
        self.label_51.setFont(font8)
        self.label_51.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_52 = QLabel(self.frame_8)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(9, 102, 157, 26))
        self.label_52.setFont(font8)
        self.label_52.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.pushButton_17 = QPushButton(self.frame_8)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(7, 12, 61, 61))
        self.pushButton_17.setFont(font6)
        self.pushButton_17.setStyleSheet(u"border:none")
        icon5 = QIcon()
        icon5.addFile(u"../../../../../../../../../images/svg_icons/icon_line_chart_down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon5)
        self.pushButton_17.setIconSize(QSize(63, 63))
        self.label_53 = QLabel(self.frame_8)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(10, 80, 110, 28))
        self.label_53.setFont(font8)
        self.label_53.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")

        self.horizontalLayout_8.addWidget(self.frame_8)

        self.frame_22 = PyPanelButton(self.scroll_area_widget_contents_home)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(245, 132))
        self.label_54 = QLabel(self.frame_22)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(69, 40, 80, 28))
        self.label_54.setFont(font7)
        self.label_54.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_55 = QLabel(self.frame_22)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(139, 98, 59, 28))
        self.label_55.setFont(font8)
        self.label_55.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_55.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_56 = QLabel(self.frame_22)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(9, 100, 157, 26))
        self.label_56.setFont(font8)
        self.label_56.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.pushButton_18 = QPushButton(self.frame_22)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(8, 13, 61, 61))
        self.pushButton_18.setFont(font6)
        self.pushButton_18.setStyleSheet(u"border:none")
        icon6 = QIcon()
        icon6.addFile(u"../../../../../../../../../images/svg_icons/Icon_receipt_svgrepo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon6)
        self.pushButton_18.setIconSize(QSize(53, 54))
        self.label_57 = QLabel(self.frame_22)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(10, 78, 110, 28))
        self.label_57.setFont(font8)
        self.label_57.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")

        self.horizontalLayout_8.addWidget(self.frame_22)

        self.scroll_area_home.setWidget(self.scroll_area_widget_contents_home)

        self.verticalLayout_6.addWidget(self.scroll_area_home)


        self.verticalLayout_2.addWidget(self.frame_continer)

        self.scroll_area_home_bottom = QScrollArea(self.page_home)
        self.scroll_area_home_bottom.setObjectName(u"scroll_area_home_bottom")
        self.scroll_area_home_bottom.setWidgetResizable(True)
        self.scroll_area_widget_contents_home_bottom = QWidget()
        self.scroll_area_widget_contents_home_bottom.setObjectName(u"scroll_area_widget_contents_home_bottom")
        self.scroll_area_widget_contents_home_bottom.setGeometry(QRect(0, 0, 713, 400))
        self.scroll_area_widget_contents_home_bottom.setStyleSheet(u"background-color: rgb(19, 20, 22);")
        self.verticalLayout_3 = QVBoxLayout(self.scroll_area_widget_contents_home_bottom)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.scroll_area_widget_contents_home_bottom)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 400))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_4 = QStackedWidget(self.frame_2)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_4.sizePolicy().hasHeightForWidth())
        self.stackedWidget_4.setSizePolicy(sizePolicy)
        self.stackedWidget_4.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget_4.setFrameShadow(QFrame.Raised)
        self.stackedWidget_4Page1 = QWidget()
        self.stackedWidget_4Page1.setObjectName(u"stackedWidget_4Page1")
        self.verticalLayout_5 = QVBoxLayout(self.stackedWidget_4Page1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.stackedWidget_4Page1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 205))
        self.frame_11.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 70, 470, 71))
        font9 = QFont()
        font9.setPointSize(20)
        self.label_12.setFont(font9)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.stackedWidget_4Page1)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 9, 0, 0)
        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.frame_13)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 90, 261, 71))
        self.label_11.setFont(font9)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 70, 261, 71))
        self.label_13.setFont(font9)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.frame_12)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.stackedWidget_4.addWidget(self.stackedWidget_4Page1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setSpacing(9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 12345678))
        self.frame_4.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 90, 261, 71))
        self.label.setFont(font9)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.frame_4)

        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 12345678))
        self.frame.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 70, 261, 71))
        self.label_8.setFont(font9)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.frame)

        self.stackedWidget_4.addWidget(self.page_2)

        self.horizontalLayout_3.addWidget(self.stackedWidget_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(290, 0))
        self.frame_3.setMaximumSize(QSize(123045, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(240, 200))
        self.frame_5.setStyleSheet(u"background-color: rgb(54, 63, 118);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font9)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_9)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(240, 173))
        self.frame_9.setStyleSheet(u"background-color: rgb(233, 234, 236);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 70, 261, 71))
        self.label_10.setFont(font9)
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_4.addWidget(self.frame_9)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.scroll_area_home_bottom.setWidget(self.scroll_area_widget_contents_home_bottom)

        self.verticalLayout_2.addWidget(self.scroll_area_home_bottom)

        self.stacked_widget.addWidget(self.page_home)
        self.page_inventario = QWidget()
        self.page_inventario.setObjectName(u"page_inventario")
        self.verticalLayout_9 = QVBoxLayout(self.page_inventario)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_81 = QFrame(self.page_inventario)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(0, 190))
        self.frame_81.setMaximumSize(QSize(16777215, 190))
        self.frame_81.setStyleSheet(u"background-color:rgb(32, 33, 37)")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_9.setSpacing(8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_chart_inventario = QFrame(self.frame_81)
        self.frame_chart_inventario.setObjectName(u"frame_chart_inventario")
        self.frame_chart_inventario.setStyleSheet(u"background-color: rgb(47, 54, 100);")
        self.frame_chart_inventario.setFrameShape(QFrame.StyledPanel)
        self.frame_chart_inventario.setFrameShadow(QFrame.Raised)
        self.vertical_layout_chart_inevntario = QVBoxLayout(self.frame_chart_inventario)
        self.vertical_layout_chart_inevntario.setSpacing(0)
        self.vertical_layout_chart_inevntario.setObjectName(u"vertical_layout_chart_inevntario")
        self.vertical_layout_chart_inevntario.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_9.addWidget(self.frame_chart_inventario)

        self.frame_circular_progress_bar = QFrame(self.frame_81)
        self.frame_circular_progress_bar.setObjectName(u"frame_circular_progress_bar")
        self.frame_circular_progress_bar.setMinimumSize(QSize(215, 172))
        self.frame_circular_progress_bar.setMaximumSize(QSize(215, 172))
        self.frame_circular_progress_bar.setStyleSheet(u"background-color: rgb(47, 54, 100);\n"
"border-radius: 10px")
        self.circupar_progress_bar = PyCircularProgress(self.frame_circular_progress_bar)
        self.circupar_progress_bar.setObjectName(u"circupar_progress_bar")
        self.circupar_progress_bar.setGeometry(QRect(9, 9, 197, 154))

        self.horizontalLayout_9.addWidget(self.frame_circular_progress_bar)


        self.verticalLayout_9.addWidget(self.frame_81)

        self.frame_80 = QFrame(self.page_inventario)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(0, 44))
        self.frame_80.setMaximumSize(QSize(16777215, 44))
        self.frame_80.setStyleSheet(u"background-color: rgb(32, 33, 37)")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_12.setSpacing(4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(4, 0, 4, 0)
        self.pushButton_test_3 = QPushButton(self.frame_80)
        self.pushButton_test_3.setObjectName(u"pushButton_test_3")
        self.pushButton_test_3.setMinimumSize(QSize(37, 37))
        self.pushButton_test_3.setMaximumSize(QSize(37, 37))
        self.pushButton_test_3.setStyleSheet(u"QPushButton {\n"
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
        icon7 = QIcon()
        icon7.addFile(u"../../../../../../../Downloads/Imagens/search-magnifying-glass-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_test_3.setIcon(icon7)
        self.pushButton_test_3.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.pushButton_test_3)

        self.lineEdit = QLineEdit(self.frame_80)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 35))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"color: rgb(233, 234, 236);\n"
"border: 1px solid rgb(47, 54, 100);\n"
"border-radius: 5px;\n"
"padding-left: 5px;\n"
"}\n"
"QLineEidit:hover{\n"
"border: 1px solid rgb(64, 80, 170);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 1px solid rgb(89, 109, 235);\n"
"border-bottom: 1px solid rgb(233, 234, 236);\n"
"}")
        self.lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_12.addWidget(self.lineEdit)

        self.pushButton_test_7 = QPushButton(self.frame_80)
        self.pushButton_test_7.setObjectName(u"pushButton_test_7")
        self.pushButton_test_7.setMinimumSize(QSize(37, 37))
        self.pushButton_test_7.setMaximumSize(QSize(37, 37))
        self.pushButton_test_7.setStyleSheet(u"QPushButton {\n"
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
        icon8 = QIcon()
        icon8.addFile(u"../../../images/svg_icons/icon_more.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_test_7.setIcon(icon8)
        self.pushButton_test_7.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.pushButton_test_7)

        self.pushButton_test_6 = QPushButton(self.frame_80)
        self.pushButton_test_6.setObjectName(u"pushButton_test_6")
        self.pushButton_test_6.setMinimumSize(QSize(37, 37))
        self.pushButton_test_6.setMaximumSize(QSize(37, 37))
        self.pushButton_test_6.setStyleSheet(u"QPushButton {\n"
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
        icon9 = QIcon()
        icon9.addFile(u"../../../../../../../Downloads/Imagens/add-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_test_6.setIcon(icon9)
        self.pushButton_test_6.setIconSize(QSize(35, 35))

        self.horizontalLayout_12.addWidget(self.pushButton_test_6)


        self.verticalLayout_9.addWidget(self.frame_80)

        self.frame_84 = QFrame(self.page_inventario)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMinimumSize(QSize(0, 20))
        self.frame_84.setMaximumSize(QSize(16777215, 20))
        self.frame_84.setStyleSheet(u"background-color: rgb(19, 20, 22);")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(10, 0, 10, 0)
        self.label_25 = QLabel(self.frame_84)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_25)

        self.label_22 = QLabel(self.frame_84)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_22)

        self.label_23 = QLabel(self.frame_84)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_84)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_24)

        self.label_26 = QLabel(self.frame_84)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_26)


        self.verticalLayout_9.addWidget(self.frame_84)

        self.frame_15 = QFrame(self.page_inventario)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_15)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(4, 4, 4, 4)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background-color: rgb(19, 20, 22);\n"
"border-radius:10px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_16)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(5, 5, 5, 5)
        self.scrollArea = QScrollArea(self.frame_16)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet(u"background-color: rgb(19, 20, 22);\n"
"border-radius: 10px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 695, 2846))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(3, 3, 4, 3)
        self.frame_17 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 40))
        self.frame_17.setMaximumSize(QSize(16777215, 40))
        self.frame_17.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_17)

        self.frame_19 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 50))
        self.frame_19.setMaximumSize(QSize(16777215, 50))
        self.frame_19.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_19)

        self.frame_67 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(0, 50))
        self.frame_67.setMaximumSize(QSize(16777215, 50))
        self.frame_67.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_67)

        self.frame_18 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 50))
        self.frame_18.setMaximumSize(QSize(16777215, 50))
        self.frame_18.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_18)

        self.frame_78 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(0, 50))
        self.frame_78.setMaximumSize(QSize(16777215, 50))
        self.frame_78.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_78)

        self.frame_20 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 50))
        self.frame_20.setMaximumSize(QSize(16777215, 50))
        self.frame_20.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_20)

        self.frame_66 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(0, 50))
        self.frame_66.setMaximumSize(QSize(16777215, 50))
        self.frame_66.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_66)

        self.frame_77 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(0, 50))
        self.frame_77.setMaximumSize(QSize(16777215, 50))
        self.frame_77.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_77)

        self.frame_65 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(0, 50))
        self.frame_65.setMaximumSize(QSize(16777215, 50))
        self.frame_65.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_65)

        self.frame_76 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(0, 50))
        self.frame_76.setMaximumSize(QSize(16777215, 50))
        self.frame_76.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_76)

        self.frame_61 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(0, 50))
        self.frame_61.setMaximumSize(QSize(16777215, 50))
        self.frame_61.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_61)

        self.frame_64 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(0, 50))
        self.frame_64.setMaximumSize(QSize(16777215, 50))
        self.frame_64.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_64)

        self.frame_54 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 50))
        self.frame_54.setMaximumSize(QSize(16777215, 50))
        self.frame_54.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_54)

        self.frame_21 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 50))
        self.frame_21.setMaximumSize(QSize(16777215, 50))
        self.frame_21.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_21)

        self.frame_53 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(0, 50))
        self.frame_53.setMaximumSize(QSize(16777215, 50))
        self.frame_53.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_53)

        self.frame_23 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 50))
        self.frame_23.setMaximumSize(QSize(16777215, 50))
        self.frame_23.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_23)

        self.frame_75 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(0, 50))
        self.frame_75.setMaximumSize(QSize(16777215, 50))
        self.frame_75.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_75)

        self.frame_55 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(0, 50))
        self.frame_55.setMaximumSize(QSize(16777215, 50))
        self.frame_55.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.frame_56 = QFrame(self.frame_55)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setGeometry(QRect(0, 0, 517, 50))
        self.frame_56.setMinimumSize(QSize(0, 50))
        self.frame_56.setMaximumSize(QSize(16777215, 50))
        self.frame_56.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_55)

        self.frame_63 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(0, 50))
        self.frame_63.setMaximumSize(QSize(16777215, 50))
        self.frame_63.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_63)

        self.frame_52 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(0, 50))
        self.frame_52.setMaximumSize(QSize(16777215, 50))
        self.frame_52.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_52)

        self.frame_62 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(0, 50))
        self.frame_62.setMaximumSize(QSize(16777215, 50))
        self.frame_62.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_62)

        self.frame_60 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 50))
        self.frame_60.setMaximumSize(QSize(16777215, 50))
        self.frame_60.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_60)

        self.frame_74 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(0, 50))
        self.frame_74.setMaximumSize(QSize(16777215, 50))
        self.frame_74.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_74)

        self.frame_51 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(0, 50))
        self.frame_51.setMaximumSize(QSize(16777215, 50))
        self.frame_51.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_51)

        self.frame_24 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 50))
        self.frame_24.setMaximumSize(QSize(16777215, 50))
        self.frame_24.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_24)

        self.frame_73 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(0, 50))
        self.frame_73.setMaximumSize(QSize(16777215, 50))
        self.frame_73.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_73)

        self.frame_47 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(0, 50))
        self.frame_47.setMaximumSize(QSize(16777215, 50))
        self.frame_47.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_47)

        self.frame_42 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(0, 50))
        self.frame_42.setMaximumSize(QSize(16777215, 50))
        self.frame_42.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_42)

        self.frame_41 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 50))
        self.frame_41.setMaximumSize(QSize(16777215, 50))
        self.frame_41.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_41)

        self.frame_72 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(0, 50))
        self.frame_72.setMaximumSize(QSize(16777215, 50))
        self.frame_72.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_72)

        self.frame_59 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(0, 50))
        self.frame_59.setMaximumSize(QSize(16777215, 50))
        self.frame_59.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_59)

        self.frame_50 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(0, 50))
        self.frame_50.setMaximumSize(QSize(16777215, 50))
        self.frame_50.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_50)

        self.frame_46 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(0, 50))
        self.frame_46.setMaximumSize(QSize(16777215, 50))
        self.frame_46.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_46)

        self.frame_40 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(0, 50))
        self.frame_40.setMaximumSize(QSize(16777215, 50))
        self.frame_40.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_40)

        self.frame_68 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(0, 50))
        self.frame_68.setMaximumSize(QSize(16777215, 50))
        self.frame_68.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_68)

        self.frame_57 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(0, 50))
        self.frame_57.setMaximumSize(QSize(16777215, 50))
        self.frame_57.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_57)

        self.frame_45 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 50))
        self.frame_45.setMaximumSize(QSize(16777215, 50))
        self.frame_45.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_45)

        self.frame_39 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(0, 50))
        self.frame_39.setMaximumSize(QSize(16777215, 50))
        self.frame_39.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_39)

        self.frame_71 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(0, 50))
        self.frame_71.setMaximumSize(QSize(16777215, 50))
        self.frame_71.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_71)

        self.frame_38 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 50))
        self.frame_38.setMaximumSize(QSize(16777215, 50))
        self.frame_38.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_38)

        self.frame_34 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 50))
        self.frame_34.setMaximumSize(QSize(16777215, 50))
        self.frame_34.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_34)

        self.frame_33 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 50))
        self.frame_33.setMaximumSize(QSize(16777215, 50))
        self.frame_33.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_33)

        self.frame_25 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 50))
        self.frame_25.setMaximumSize(QSize(16777215, 50))
        self.frame_25.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_25)

        self.frame_49 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(0, 50))
        self.frame_49.setMaximumSize(QSize(16777215, 50))
        self.frame_49.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_49)

        self.frame_43 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(0, 50))
        self.frame_43.setMaximumSize(QSize(16777215, 50))
        self.frame_43.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setGeometry(QRect(0, 0, 517, 50))
        self.frame_44.setMinimumSize(QSize(0, 50))
        self.frame_44.setMaximumSize(QSize(16777215, 50))
        self.frame_44.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_43)

        self.frame_48 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 50))
        self.frame_48.setMaximumSize(QSize(16777215, 50))
        self.frame_48.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_48)

        self.frame_32 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 50))
        self.frame_32.setMaximumSize(QSize(16777215, 50))
        self.frame_32.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_32)

        self.frame_58 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(0, 50))
        self.frame_58.setMaximumSize(QSize(16777215, 50))
        self.frame_58.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_58)

        self.frame_70 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(0, 50))
        self.frame_70.setMaximumSize(QSize(16777215, 50))
        self.frame_70.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_70)

        self.frame_69 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(0, 50))
        self.frame_69.setMaximumSize(QSize(16777215, 50))
        self.frame_69.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_69)

        self.frame_79 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(0, 50))
        self.frame_79.setMaximumSize(QSize(16777215, 50))
        self.frame_79.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_79)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_19.addWidget(self.scrollArea)


        self.verticalLayout_10.addWidget(self.frame_16)


        self.verticalLayout_9.addWidget(self.frame_15)

        self.stacked_widget.addWidget(self.page_inventario)

        self.horizontalLayout.addWidget(self.stacked_widget)


        self.verticalLayout.addWidget(self.frame_base)


        self.horizontalLayout_2.addWidget(self.central_frame)


        self.vertical_layout_frame_line.addWidget(self.central_widget)


        self.horizontal_layout_back_ground_frame_line.addWidget(self.frame_line)


        self.horizontal_layout_widget_style_sheet.addWidget(self.back_ground_frame_line)

        MainWindow.setCentralWidget(self.widget_style_sheet)

        self.retranslateUi(MainWindow)

        self.stacked_widget.setCurrentIndex(2)
        self.stackedWidget_4.setCurrentIndex(0)


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
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"dados dos produtos  (stock) ate agora", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"char barra", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"dados vendidos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dinamic char", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"lista de cliente", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Top produtos", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"produto mais vendido", None))
        self.pushButton_test_3.setText("")
        self.pushButton_test_7.setText("")
        self.pushButton_test_6.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"N\u00ba", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

