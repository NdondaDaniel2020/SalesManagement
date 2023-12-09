# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowMsePYj.ui'
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
    QSpacerItem, QSplitter, QStackedWidget, QVBoxLayout,
    QWidget)

from src.gui.core.functions import Functions

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(990, 661)
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
"#line_left_menu, #line_title_bar{border:none}")
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
        self.frame_logo.setMinimumSize(QSize(65, 0))
        self.frame_logo.setStyleSheet(u"")
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_logo)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_logo)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"images/svg_images/logo_top_100x22.svg"))

        self.horizontalLayout_6.addWidget(self.label)


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

        self.frame = QFrame(self.central_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_colum = QFrame(self.frame)
        self.left_colum.setObjectName(u"left_colum")
        self.left_colum.setMinimumSize(QSize(200, 0))
        self.left_colum.setMaximumSize(QSize(0, 16777215))
        self.left_colum.setStyleSheet(u"")
        self.left_colum.setFrameShape(QFrame.StyledPanel)
        self.left_colum.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.left_colum)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 3, 5)
        self.frame_23 = QFrame(self.left_colum)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_23)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_23)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 119))
        self.frame_22.setStyleSheet(u"")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_22)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pushButton_3 = QPushButton(self.frame_22)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"border:none")
        icon = QIcon()
        icon.addFile(u"images/svg_images/SalesManagement.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(130, 130))

        self.verticalLayout_13.addWidget(self.pushButton_3)


        self.verticalLayout_12.addWidget(self.frame_22)

        self.frame_26 = QFrame(self.frame_23)
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
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(14)
        self.label_19.setFont(font)
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
        self.frame_32 = QFrame(self.frame_27)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"QFrame{\n"
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
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 0, 2, 0)
        self.pushButton_test_11 = QPushButton(self.frame_32)
        self.pushButton_test_11.setObjectName(u"pushButton_test_11")
        self.pushButton_test_11.setMinimumSize(QSize(37, 37))
        self.pushButton_test_11.setMaximumSize(QSize(1234, 37))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(10)
        self.pushButton_test_11.setFont(font1)
        self.pushButton_test_11.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: transparent;\n"
"			 padding-left: 7px;\n"
"            text-align: left;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../../../../../Downloads/Imagens/analytics-hands-report-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_test_11.setIcon(icon1)
        self.pushButton_test_11.setIconSize(QSize(26, 26))

        self.horizontalLayout_10.addWidget(self.pushButton_test_11)

        self.pushButton_test_12 = QPushButton(self.frame_32)
        self.pushButton_test_12.setObjectName(u"pushButton_test_12")
        self.pushButton_test_12.setMinimumSize(QSize(36, 37))
        self.pushButton_test_12.setMaximumSize(QSize(36, 37))
        self.pushButton_test_12.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: transparent;;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"/../../../../Downloads/more-horizontal-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_test_12.setIcon(icon2)
        self.pushButton_test_12.setIconSize(QSize(21, 21))

        self.horizontalLayout_10.addWidget(self.pushButton_test_12)


        self.verticalLayout_17.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_27)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"QFrame{\n"
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
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(2, 0, 2, 0)
        self.pushButton_test_13 = QPushButton(self.frame_33)
        self.pushButton_test_13.setObjectName(u"pushButton_test_13")
        self.pushButton_test_13.setMinimumSize(QSize(37, 37))
        self.pushButton_test_13.setMaximumSize(QSize(1234, 37))
        self.pushButton_test_13.setFont(font1)
        self.pushButton_test_13.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: transparent;\n"
"			 padding-left: 7px;\n"
"            text-align: left;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"/../../../../Downloads/Imagens/inbox-2-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_test_13.setIcon(icon3)
        self.pushButton_test_13.setIconSize(QSize(26, 26))

        self.horizontalLayout_11.addWidget(self.pushButton_test_13)

        self.pushButton_test_14 = QPushButton(self.frame_33)
        self.pushButton_test_14.setObjectName(u"pushButton_test_14")
        self.pushButton_test_14.setMinimumSize(QSize(36, 37))
        self.pushButton_test_14.setMaximumSize(QSize(36, 37))
        self.pushButton_test_14.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: transparent;;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}")
        self.pushButton_test_14.setIcon(icon2)
        self.pushButton_test_14.setIconSize(QSize(21, 21))

        self.horizontalLayout_11.addWidget(self.pushButton_test_14)


        self.verticalLayout_17.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_27)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"QFrame{\n"
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
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(2, 0, 2, 0)
        self.pushButton_test_15 = QPushButton(self.frame_34)
        self.pushButton_test_15.setObjectName(u"pushButton_test_15")
        self.pushButton_test_15.setMinimumSize(QSize(37, 37))
        self.pushButton_test_15.setMaximumSize(QSize(1234, 37))
        self.pushButton_test_15.setFont(font1)
        self.pushButton_test_15.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: transparent;\n"
"			 padding-left: 7px;\n"
"            text-align: left;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"/../../../../Downloads/Imagens/analytics-svgrepo-com (2).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_test_15.setIcon(icon4)
        self.pushButton_test_15.setIconSize(QSize(26, 26))

        self.horizontalLayout_16.addWidget(self.pushButton_test_15)

        self.pushButton_test_16 = QPushButton(self.frame_34)
        self.pushButton_test_16.setObjectName(u"pushButton_test_16")
        self.pushButton_test_16.setMinimumSize(QSize(36, 37))
        self.pushButton_test_16.setMaximumSize(QSize(36, 37))
        self.pushButton_test_16.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: transparent;;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}")
        self.pushButton_test_16.setIcon(icon2)
        self.pushButton_test_16.setIconSize(QSize(21, 21))

        self.horizontalLayout_16.addWidget(self.pushButton_test_16)


        self.verticalLayout_17.addWidget(self.frame_34)


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
        self.label_15.setFont(font)
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
        self.frame_38 = QFrame(self.frame_29)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"QFrame{\n"
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
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(2, 0, 2, 0)
        self.pushButton_test_23 = QPushButton(self.frame_38)
        self.pushButton_test_23.setObjectName(u"pushButton_test_23")
        self.pushButton_test_23.setMinimumSize(QSize(37, 37))
        self.pushButton_test_23.setMaximumSize(QSize(36, 37))
        self.pushButton_test_23.setFont(font1)
        self.pushButton_test_23.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: transparent;\n"
"			 padding-left: 5px;\n"
"            text-align: left;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"/images/svg_images/daniel.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_test_23.setIcon(icon5)
        self.pushButton_test_23.setIconSize(QSize(26, 26))

        self.horizontalLayout_20.addWidget(self.pushButton_test_23)

        self.frame_40 = QFrame(self.frame_38)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"border:none;\n"
"background-color: transparent;")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_40)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_40)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(0, 10))
        self.label_39.setMaximumSize(QSize(16777215, 13))
        self.label_39.setFont(font1)
        self.label_39.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border:none")

        self.verticalLayout_20.addWidget(self.label_39)

        self.label_40 = QLabel(self.frame_40)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(0, 10))
        self.label_40.setMaximumSize(QSize(16777215, 10))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Light"])
        font2.setPointSize(8)
        self.label_40.setFont(font2)
        self.label_40.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border:none;\n"
"padding-left: 0.4px;")

        self.verticalLayout_20.addWidget(self.label_40)


        self.horizontalLayout_20.addWidget(self.frame_40)

        self.pushButton_test_24 = QPushButton(self.frame_38)
        self.pushButton_test_24.setObjectName(u"pushButton_test_24")
        self.pushButton_test_24.setMinimumSize(QSize(36, 37))
        self.pushButton_test_24.setMaximumSize(QSize(36, 37))
        self.pushButton_test_24.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: transparent;;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}")
        self.pushButton_test_24.setIcon(icon2)
        self.pushButton_test_24.setIconSize(QSize(21, 21))

        self.horizontalLayout_20.addWidget(self.pushButton_test_24)


        self.verticalLayout_16.addWidget(self.frame_38)

        self.verticalSpacer = QSpacerItem(20, 228, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer)


        self.verticalLayout_15.addWidget(self.frame_29)


        self.verticalLayout_14.addWidget(self.frame_28)


        self.verticalLayout_12.addWidget(self.frame_26)


        self.verticalLayout_11.addWidget(self.frame_23)


        self.horizontalLayout.addWidget(self.left_colum)

        self.stacked_widget = QStackedWidget(self.frame)
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
        self.pushButton_test_9.setFont(font1)
        self.pushButton_test_9.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: transparent;\n"
"			 padding-left: 7px;\n"
"            text-align: left;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}\n"
"")
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
        self.pushButton_test_10.setIcon(icon2)
        self.pushButton_test_10.setIconSize(QSize(21, 21))

        self.horizontalLayout_5.addWidget(self.pushButton_test_10)

        self.frame_36 = QFrame(self.page)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setGeometry(QRect(80, 450, 180, 36))
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
        self.pushButton_test_19.setFont(font1)
        self.pushButton_test_19.setStyleSheet(u"QPushButton {\n"
"            color: rgb(233, 234, 236);\n"
"            background-color: transparent;\n"
"			 padding-left: 7px;\n"
"            text-align: left;\n"
"            border: none;\n"
"            border-radius: 8px;\n"
"}\n"
"")
        self.pushButton_test_19.setIcon(icon1)
        self.pushButton_test_19.setIconSize(QSize(26, 26))

        self.horizontalLayout_18.addWidget(self.pushButton_test_19)

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
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border:none")

        self.verticalLayout_18.addWidget(self.label_14)

        self.label_20 = QLabel(self.frame_37)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 10))
        self.label_20.setMaximumSize(QSize(16777215, 10))
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border:none;\n"
"padding-left: 0.4px;")

        self.verticalLayout_18.addWidget(self.label_20)


        self.horizontalLayout_18.addWidget(self.frame_37)

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
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.scrollArea_3 = QScrollArea(self.page_home)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMaximumSize(QSize(16777215, 149))
        self.scrollArea_3.setStyleSheet(u"background-color:rgb(32, 33, 37);\n"
"border-radius:10px")
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 809, 139))
        self.horizontalLayout_8 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_8.setSpacing(9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.frame_24 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(191, 121))
        self.frame_24.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(191, 121))
        self.frame_25.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_25)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(191, 121))
        self.frame_7.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(191, 121))
        self.frame_8.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_8)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_2.addWidget(self.scrollArea_3)

        self.frame_2 = QFrame(self.page_home)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border-radius:10px")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 9, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
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
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(191, 121))
        self.frame_14.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pushButton_15 = QPushButton(self.frame_14)
        self.pushButton_15.setObjectName(u"pushButton_15")
        icon6 = QIcon()
        icon6.addFile(u"../../../../../../../OneDrive/Imagens/Capturas de Ecr\u00e3/Captura de ecr\u00e3 2023-11-29 024855.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon6)
        self.pushButton_15.setIconSize(QSize(271, 189))

        self.verticalLayout_9.addWidget(self.pushButton_15)


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
        self.verticalLayout_6 = QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_16 = QPushButton(self.frame_11)
        self.pushButton_16.setObjectName(u"pushButton_16")
        icon7 = QIcon()
        icon7.addFile(u"../../../../../../../OneDrive/Imagens/Capturas de Ecr\u00e3/Captura de ecr\u00e3 2023-11-29 024618.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon7)
        self.pushButton_16.setIconSize(QSize(451, 194))

        self.verticalLayout_6.addWidget(self.pushButton_16)


        self.verticalLayout_5.addWidget(self.frame_11)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 0))
        self.frame_4.setMaximumSize(QSize(250, 16777215))
        self.frame_4.setStyleSheet(u"")
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
        font3 = QFont()
        font3.setPointSize(12)
        self.label_8.setFont(font3)
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
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Semibold"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.label_9.setFont(font4)
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
        icon8 = QIcon()
        icon8.addFile(u"../../../../Downloads/alarm-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon8)
        self.pushButton.setIconSize(QSize(35, 35))

        self.horizontalLayout_9.addWidget(self.pushButton)

        self.splitter = QSplitter(self.frame_15)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.label_10 = QLabel(self.splitter)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI Semibold"])
        font5.setPointSize(9)
        font5.setBold(False)
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter.addWidget(self.label_10)
        self.label_11 = QLabel(self.splitter)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(71, 0))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(11)
        self.label_11.setFont(font6)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter.addWidget(self.label_11)

        self.horizontalLayout_9.addWidget(self.splitter)

        self.label_13 = QLabel(self.frame_15)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(70, 24))
        self.label_13.setPixmap(QPixmap(u"../../../../../../../OneDrive/Imagens/Capturas de Ecr\u00e3/Captura de ecr\u00e3 2023-11-29 023052.png"))

        self.horizontalLayout_9.addWidget(self.label_13)

        self.label_12 = QLabel(self.frame_15)
        self.label_12.setObjectName(u"label_12")
        font7 = QFont()
        font7.setPointSize(13)
        self.label_12.setFont(font7)
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
        self.pushButton_13.setIcon(icon8)
        self.pushButton_13.setIconSize(QSize(35, 35))

        self.horizontalLayout_15.addWidget(self.pushButton_13)

        self.splitter_7 = QSplitter(self.frame_19)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Vertical)
        self.label_34 = QLabel(self.splitter_7)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 16))
        self.label_34.setFont(font5)
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter_7.addWidget(self.label_34)
        self.label_35 = QLabel(self.splitter_7)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(71, 0))
        self.label_35.setFont(font6)
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter_7.addWidget(self.label_35)

        self.horizontalLayout_15.addWidget(self.splitter_7)

        self.label_36 = QLabel(self.frame_19)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(70, 24))
        self.label_36.setPixmap(QPixmap(u"../../../../../../../OneDrive/Imagens/Capturas de Ecr\u00e3/Captura de ecr\u00e3 2023-11-29 023052.png"))

        self.horizontalLayout_15.addWidget(self.label_36)

        self.label_37 = QLabel(self.frame_19)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font7)
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
        self.pushButton_11.setIcon(icon8)
        self.pushButton_11.setIconSize(QSize(35, 35))

        self.horizontalLayout_14.addWidget(self.pushButton_11)

        self.splitter_6 = QSplitter(self.frame_18)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Vertical)
        self.label_30 = QLabel(self.splitter_6)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(16777215, 16))
        self.label_30.setFont(font5)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter_6.addWidget(self.label_30)
        self.label_31 = QLabel(self.splitter_6)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(71, 0))
        self.label_31.setFont(font6)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter_6.addWidget(self.label_31)

        self.horizontalLayout_14.addWidget(self.splitter_6)

        self.label_32 = QLabel(self.frame_18)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(70, 24))
        self.label_32.setPixmap(QPixmap(u"../../../../../../../OneDrive/Imagens/Capturas de Ecr\u00e3/Captura de ecr\u00e3 2023-11-29 023052.png"))

        self.horizontalLayout_14.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_18)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font7)
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
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QSize(35, 35))

        self.horizontalLayout_13.addWidget(self.pushButton_9)

        self.splitter_5 = QSplitter(self.frame_17)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Vertical)
        self.label_26 = QLabel(self.splitter_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 16))
        self.label_26.setFont(font5)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter_5.addWidget(self.label_26)
        self.label_27 = QLabel(self.splitter_5)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(71, 0))
        self.label_27.setFont(font6)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter_5.addWidget(self.label_27)

        self.horizontalLayout_13.addWidget(self.splitter_5)

        self.label_28 = QLabel(self.frame_17)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(70, 24))
        self.label_28.setPixmap(QPixmap(u"../../../../../../../OneDrive/Imagens/Capturas de Ecr\u00e3/Captura de ecr\u00e3 2023-11-29 023052.png"))

        self.horizontalLayout_13.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_17)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font7)
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
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setIconSize(QSize(35, 35))

        self.horizontalLayout_12.addWidget(self.pushButton_7)

        self.splitter_4 = QSplitter(self.frame_16)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.label_22 = QLabel(self.splitter_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 16))
        self.label_22.setFont(font5)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter_4.addWidget(self.label_22)
        self.label_23 = QLabel(self.splitter_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(71, 0))
        self.label_23.setFont(font6)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.splitter_4.addWidget(self.label_23)

        self.horizontalLayout_12.addWidget(self.splitter_4)

        self.label_24 = QLabel(self.frame_16)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(70, 24))
        self.label_24.setPixmap(QPixmap(u"../../../../../../../OneDrive/Imagens/Capturas de Ecr\u00e3/Captura de ecr\u00e3 2023-11-29 023052.png"))

        self.horizontalLayout_12.addWidget(self.label_24)

        self.label_25 = QLabel(self.frame_16)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font7)
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


        self.verticalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.stacked_widget.addWidget(self.page_home)

        self.horizontalLayout.addWidget(self.stacked_widget)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.central_frame)


        self.vertical_layout_frame_line.addWidget(self.central_widget)


        self.horizontal_layout_back_ground_frame_line.addWidget(self.frame_line)


        self.horizontal_layout_widget_style_sheet.addWidget(self.back_ground_frame_line)

        MainWindow.setCentralWidget(self.widget_style_sheet)

        self.retranslateUi(MainWindow)

        self.stacked_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton_3.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Version: 0.0.1", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"GitHub: github.com/NdondaDaniel2020/SalesManagement", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Outros", None))
        self.pushButton_test_11.setText(QCoreApplication.translate("MainWindow", u"  Pizza Chart", None))
        self.pushButton_test_12.setText("")
        self.pushButton_test_13.setText(QCoreApplication.translate("MainWindow", u"  SMS", None))
        self.pushButton_test_14.setText("")
        self.pushButton_test_15.setText(QCoreApplication.translate("MainWindow", u"  Char", None))
        self.pushButton_test_16.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.pushButton_test_23.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u" Daniel", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u" Daniel", None))
        self.pushButton_test_24.setText("")
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
        self.label_14.setText(QCoreApplication.translate("MainWindow", u" Daniel", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u" Daniel", None))
        self.pushButton_test_20.setText("")
        self.pushButton_15.setText("")
        self.pushButton_16.setText("")
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

