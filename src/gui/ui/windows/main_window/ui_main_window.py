# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowiBpxmf.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from src.gui.widgets.py_circular_progress.py_circular_progress import PyCircularProgress
from src.gui.widgets.py_custom_push_button.py_custom_push_button import PyCustomPushButton
from src.gui.widgets.py_painel_button.py_painel_button import PyPanelButton
from src.gui.widgets.py_scroll_area.py_scroall_area import PyScrollArea
from src.gui.widgets.py_user_button.py_user_button import PyUserButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(724, 568)
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
"/*Inventario*/\n"
"#frame_nav_busca,\n"
"#frame_border,\n"
"#frame_char\n"
"{background-color: rgb(32, 33, 37);}\n"
"\n"
"#lbl_nome_n,\n"
"#lbl_quantidade,\n"
"#lbl_nome_inventario,\n"
"#lbl_venda_inventario,\n"
"#frame_info_inventario,\n"
"#frame_continer_border,\n"
"#scroll_area_list_regitro_inventa"
                        "rio,\n"
"#scroll_area_widget_contents_inventario\n"
"{background-color: rgb(19, 20, 22);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;}\n"
"\n"
"#frame_chart_inventario,\n"
"#frame_circular_progress_bar\n"
"{background-color: rgb(47, 54, 100);}\n"
"\n"
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
"QScrollBar::sub-lin"
                        "e:horizontal {\n"
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
"	 border-bo"
                        "ttom-left-radius: 4px;\n"
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
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
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
        self.logo = QPushButton(self.frame_logo)
        self.logo.setObjectName(u"logo")
        self.logo.setLayoutDirection(Qt.LeftToRight)
        self.logo.setStyleSheet(u"background-color: transparent;\n"
"text-align: left;")
        icon = QIcon()
        icon.addFile(u"../../../images/svg_images/img-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo.setIcon(icon)
        self.logo.setIconSize(QSize(115, 115))

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
        icon1 = QIcon()
        icon1.addFile(u"../../../../../../../../../images/svg_images/SalesManagement.png", QSize(), QIcon.Normal, QIcon.Off)
        self.qrcode.setIcon(icon1)
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

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_3)

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


        self.verticalLayout_15.addWidget(self.frame_29)


        self.verticalLayout_14.addWidget(self.frame_28)


        self.verticalLayout_11.addWidget(self.frame_26)


        self.horizontalLayout.addWidget(self.left_column, 0, Qt.AlignLeft)

        self.stacked_widget = QStackedWidget(self.frame_base)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.page_configuracoes = QWidget()
        self.page_configuracoes.setObjectName(u"page_configuracoes")
        self.horizontalLayout_27 = QHBoxLayout(self.page_configuracoes)
        self.horizontalLayout_27.setSpacing(6)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(7, 7, 7, 7)
        self.frame_14 = QFrame(self.page_configuracoes)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"background-color: transparent;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_14)
        self.verticalLayout_28.setSpacing(5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_60 = QFrame(self.frame_14)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 170))
        self.frame_60.setMaximumSize(QSize(16777215, 170))
        self.frame_60.setStyleSheet(u"border-radius: 10px;")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_60)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_60)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border-radois: 8px;")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 624, 170))
        self.verticalLayout_30 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_nav_continer_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_nav_continer_3.setObjectName(u"frame_nav_continer_3")
        self.frame_nav_continer_3.setMinimumSize(QSize(0, 170))
        self.frame_nav_continer_3.setMaximumSize(QSize(16777215, 170))
        self.frame_nav_continer_3.setStyleSheet(u"background-color: rgb(54, 63, 118);")
        self.frame_nav_continer_3.setFrameShape(QFrame.StyledPanel)
        self.frame_nav_continer_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_nav_continer_3)
        self.horizontalLayout_32.setSpacing(4)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(4, 4, 4, 4)
        self.frame_inventario_3 = QFrame(self.frame_nav_continer_3)
        self.frame_inventario_3.setObjectName(u"frame_inventario_3")
        self.frame_inventario_3.setMinimumSize(QSize(151, 161))
        self.frame_inventario_3.setMaximumSize(QSize(123456, 123456))
        self.frame_inventario_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(32, 33, 37, 200);\n"
"	background-image: url(none);}\n"
"\n"
"QFrame:hover\n"
"{border: 0.5px solid rgba(255, 255, 255, 80)}")
        self.frame_inventario_3.setFrameShape(QFrame.StyledPanel)
        self.frame_inventario_3.setFrameShadow(QFrame.Raised)
        self.btn_logo_inventario_3 = QPushButton(self.frame_inventario_3)
        self.btn_logo_inventario_3.setObjectName(u"btn_logo_inventario_3")
        self.btn_logo_inventario_3.setGeometry(QRect(20, 25, 52, 55))
        self.btn_logo_inventario_3.setStyleSheet(u"background-color: transparent")
        icon2 = QIcon()
        icon2.addFile(u"../../../images/svg_icons/icon_box.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logo_inventario_3.setIcon(icon2)
        self.btn_logo_inventario_3.setIconSize(QSize(58, 58))
        self.lbl_inventario_3 = QLabel(self.frame_inventario_3)
        self.lbl_inventario_3.setObjectName(u"lbl_inventario_3")
        self.lbl_inventario_3.setGeometry(QRect(20, 90, 71, 16))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semilight"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.lbl_inventario_3.setFont(font3)
        self.lbl_inventario_3.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.lbl_info_inventario_5 = QLabel(self.frame_inventario_3)
        self.lbl_info_inventario_5.setObjectName(u"lbl_info_inventario_5")
        self.lbl_info_inventario_5.setGeometry(QRect(22, 112, 70, 10))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Light"])
        font4.setPointSize(7)
        self.lbl_info_inventario_5.setFont(font4)
        self.lbl_info_inventario_5.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_inventario_5.setScaledContents(False)
        self.btn_log_extra_inventario_3 = QPushButton(self.frame_inventario_3)
        self.btn_log_extra_inventario_3.setObjectName(u"btn_log_extra_inventario_3")
        self.btn_log_extra_inventario_3.setGeometry(QRect(128, 137, 20, 20))
        self.btn_log_extra_inventario_3.setStyleSheet(u"background-color: transparent")
        icon3 = QIcon()
        icon3.addFile(u"../../../images/svg_icons/icon_push_notification.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_log_extra_inventario_3.setIcon(icon3)
        self.btn_log_extra_inventario_3.setIconSize(QSize(20, 20))
        self.lbl_info_inventario_6 = QLabel(self.frame_inventario_3)
        self.lbl_info_inventario_6.setObjectName(u"lbl_info_inventario_6")
        self.lbl_info_inventario_6.setGeometry(QRect(22, 126, 90, 10))
        self.lbl_info_inventario_6.setFont(font4)
        self.lbl_info_inventario_6.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_inventario_6.setScaledContents(False)

        self.horizontalLayout_32.addWidget(self.frame_inventario_3)

        self.frame_venda_3 = QFrame(self.frame_nav_continer_3)
        self.frame_venda_3.setObjectName(u"frame_venda_3")
        self.frame_venda_3.setMinimumSize(QSize(151, 161))
        self.frame_venda_3.setMaximumSize(QSize(123456, 123456))
        self.frame_venda_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(32, 33, 37, 200);\n"
"	background-image: url(none);}\n"
"\n"
"QFrame:hover\n"
"{border: 0.5px solid rgba(255, 255, 255, 80)}")
        self.frame_venda_3.setFrameShape(QFrame.StyledPanel)
        self.frame_venda_3.setFrameShadow(QFrame.Raised)
        self.btn_logo_venda_3 = QPushButton(self.frame_venda_3)
        self.btn_logo_venda_3.setObjectName(u"btn_logo_venda_3")
        self.btn_logo_venda_3.setGeometry(QRect(18, 25, 51, 51))
        self.btn_logo_venda_3.setStyleSheet(u"background-color: transparent")
        icon4 = QIcon()
        icon4.addFile(u"../../../images/svg_icons/icon_coin.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logo_venda_3.setIcon(icon4)
        self.btn_logo_venda_3.setIconSize(QSize(49, 49))
        self.lbl_venda_3 = QLabel(self.frame_venda_3)
        self.lbl_venda_3.setObjectName(u"lbl_venda_3")
        self.lbl_venda_3.setGeometry(QRect(20, 90, 50, 16))
        self.lbl_venda_3.setFont(font3)
        self.lbl_venda_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border:none;")
        self.btn_log_extra_venda_3 = QPushButton(self.frame_venda_3)
        self.btn_log_extra_venda_3.setObjectName(u"btn_log_extra_venda_3")
        self.btn_log_extra_venda_3.setGeometry(QRect(128, 137, 20, 20))
        self.btn_log_extra_venda_3.setStyleSheet(u"background-color: transparent")
        self.btn_log_extra_venda_3.setIcon(icon3)
        self.btn_log_extra_venda_3.setIconSize(QSize(20, 20))
        self.lbl_info_venda_7 = QLabel(self.frame_venda_3)
        self.lbl_info_venda_7.setObjectName(u"lbl_info_venda_7")
        self.lbl_info_venda_7.setGeometry(QRect(22, 140, 50, 10))
        self.lbl_info_venda_7.setFont(font4)
        self.lbl_info_venda_7.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_venda_7.setScaledContents(False)
        self.lbl_info_venda_8 = QLabel(self.frame_venda_3)
        self.lbl_info_venda_8.setObjectName(u"lbl_info_venda_8")
        self.lbl_info_venda_8.setGeometry(QRect(22, 112, 90, 10))
        self.lbl_info_venda_8.setFont(font4)
        self.lbl_info_venda_8.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_venda_8.setScaledContents(False)
        self.lbl_info_venda_9 = QLabel(self.frame_venda_3)
        self.lbl_info_venda_9.setObjectName(u"lbl_info_venda_9")
        self.lbl_info_venda_9.setGeometry(QRect(22, 126, 110, 10))
        self.lbl_info_venda_9.setFont(font4)
        self.lbl_info_venda_9.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_venda_9.setScaledContents(False)

        self.horizontalLayout_32.addWidget(self.frame_venda_3)

        self.frame_perda_3 = QFrame(self.frame_nav_continer_3)
        self.frame_perda_3.setObjectName(u"frame_perda_3")
        self.frame_perda_3.setMinimumSize(QSize(151, 161))
        self.frame_perda_3.setMaximumSize(QSize(123456, 123456))
        self.frame_perda_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(32, 33, 37, 200);\n"
"	background-image: url(none);}\n"
"\n"
"QFrame:hover\n"
"{border: 0.5px solid rgba(255, 255, 255, 80)}")
        self.frame_perda_3.setFrameShape(QFrame.StyledPanel)
        self.frame_perda_3.setFrameShadow(QFrame.Raised)
        self.btn_logo_perda_3 = QPushButton(self.frame_perda_3)
        self.btn_logo_perda_3.setObjectName(u"btn_logo_perda_3")
        self.btn_logo_perda_3.setGeometry(QRect(19, 25, 50, 51))
        self.btn_logo_perda_3.setStyleSheet(u"background-color: transparent")
        icon5 = QIcon()
        icon5.addFile(u"../../../images/svg_icons/icon_line_chart_down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logo_perda_3.setIcon(icon5)
        self.btn_logo_perda_3.setIconSize(QSize(57, 57))
        self.lbl_perda_3 = QLabel(self.frame_perda_3)
        self.lbl_perda_3.setObjectName(u"lbl_perda_3")
        self.lbl_perda_3.setGeometry(QRect(20, 90, 50, 16))
        self.lbl_perda_3.setFont(font3)
        self.lbl_perda_3.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_perda_7 = QLabel(self.frame_perda_3)
        self.lbl_info_perda_7.setObjectName(u"lbl_info_perda_7")
        self.lbl_info_perda_7.setGeometry(QRect(22, 112, 101, 10))
        self.lbl_info_perda_7.setFont(font4)
        self.lbl_info_perda_7.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_perda_7.setScaledContents(False)
        self.btn_log_extra_perda_3 = QPushButton(self.frame_perda_3)
        self.btn_log_extra_perda_3.setObjectName(u"btn_log_extra_perda_3")
        self.btn_log_extra_perda_3.setGeometry(QRect(128, 137, 20, 20))
        self.btn_log_extra_perda_3.setStyleSheet(u"background-color: transparent")
        self.btn_log_extra_perda_3.setIcon(icon3)
        self.btn_log_extra_perda_3.setIconSize(QSize(20, 20))
        self.lbl_info_perda_8 = QLabel(self.frame_perda_3)
        self.lbl_info_perda_8.setObjectName(u"lbl_info_perda_8")
        self.lbl_info_perda_8.setGeometry(QRect(22, 126, 111, 10))
        self.lbl_info_perda_8.setFont(font4)
        self.lbl_info_perda_8.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_perda_8.setScaledContents(False)
        self.lbl_info_perda_9 = QLabel(self.frame_perda_3)
        self.lbl_info_perda_9.setObjectName(u"lbl_info_perda_9")
        self.lbl_info_perda_9.setGeometry(QRect(22, 140, 50, 10))
        self.lbl_info_perda_9.setFont(font4)
        self.lbl_info_perda_9.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_perda_9.setScaledContents(False)

        self.horizontalLayout_32.addWidget(self.frame_perda_3)

        self.frame_recibo_3 = QFrame(self.frame_nav_continer_3)
        self.frame_recibo_3.setObjectName(u"frame_recibo_3")
        self.frame_recibo_3.setMinimumSize(QSize(151, 161))
        self.frame_recibo_3.setMaximumSize(QSize(123456, 123456))
        self.frame_recibo_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(32, 33, 37, 200);\n"
"	background-image: url(none);}\n"
"\n"
"QFrame:hover\n"
"{border: 0.5px solid rgba(255, 255, 255, 80)}")
        self.frame_recibo_3.setFrameShape(QFrame.StyledPanel)
        self.frame_recibo_3.setFrameShadow(QFrame.Raised)
        self.btn_logo_recibo_3 = QPushButton(self.frame_recibo_3)
        self.btn_logo_recibo_3.setObjectName(u"btn_logo_recibo_3")
        self.btn_logo_recibo_3.setGeometry(QRect(18, 26, 50, 48))
        self.btn_logo_recibo_3.setStyleSheet(u"background-color: transparent")
        icon6 = QIcon()
        icon6.addFile(u"../../../images/svg_icons/icon_inventory.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logo_recibo_3.setIcon(icon6)
        self.btn_logo_recibo_3.setIconSize(QSize(75, 75))
        self.lbl_recibo_3 = QLabel(self.frame_recibo_3)
        self.lbl_recibo_3.setObjectName(u"lbl_recibo_3")
        self.lbl_recibo_3.setGeometry(QRect(20, 90, 50, 16))
        self.lbl_recibo_3.setFont(font3)
        self.lbl_recibo_3.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_extra_recibo_7 = QLabel(self.frame_recibo_3)
        self.lbl_info_extra_recibo_7.setObjectName(u"lbl_info_extra_recibo_7")
        self.lbl_info_extra_recibo_7.setGeometry(QRect(22, 112, 110, 10))
        self.lbl_info_extra_recibo_7.setFont(font4)
        self.lbl_info_extra_recibo_7.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_extra_recibo_7.setScaledContents(False)
        self.btn_log_extra_recibo_3 = QPushButton(self.frame_recibo_3)
        self.btn_log_extra_recibo_3.setObjectName(u"btn_log_extra_recibo_3")
        self.btn_log_extra_recibo_3.setGeometry(QRect(128, 137, 20, 20))
        self.btn_log_extra_recibo_3.setStyleSheet(u"background-color: transparent")
        self.btn_log_extra_recibo_3.setIcon(icon3)
        self.btn_log_extra_recibo_3.setIconSize(QSize(20, 20))
        self.lbl_info_extra_recibo_8 = QLabel(self.frame_recibo_3)
        self.lbl_info_extra_recibo_8.setObjectName(u"lbl_info_extra_recibo_8")
        self.lbl_info_extra_recibo_8.setGeometry(QRect(22, 126, 110, 10))
        self.lbl_info_extra_recibo_8.setFont(font4)
        self.lbl_info_extra_recibo_8.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_extra_recibo_8.setScaledContents(False)
        self.lbl_info_extra_recibo_9 = QLabel(self.frame_recibo_3)
        self.lbl_info_extra_recibo_9.setObjectName(u"lbl_info_extra_recibo_9")
        self.lbl_info_extra_recibo_9.setGeometry(QRect(22, 140, 90, 10))
        self.lbl_info_extra_recibo_9.setFont(font4)
        self.lbl_info_extra_recibo_9.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_extra_recibo_9.setScaledContents(False)

        self.horizontalLayout_32.addWidget(self.frame_recibo_3)


        self.verticalLayout_30.addWidget(self.frame_nav_continer_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_29.addWidget(self.scrollArea)


        self.verticalLayout_28.addWidget(self.frame_60)

        self.frame_64 = QFrame(self.frame_14)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)

        self.verticalLayout_28.addWidget(self.frame_64)


        self.horizontalLayout_27.addWidget(self.frame_14)

        self.frame_6 = QFrame(self.page_configuracoes)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(188, 0))
        self.frame_6.setMaximumSize(QSize(188, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 156))
        self.frame_15.setMaximumSize(QSize(16777215, 156))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.label_21 = QLabel(self.frame_15)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(57, 135, 55, 20))
        font5 = QFont()
        font5.setPointSize(11)
        self.label_21.setFont(font5)
        self.label_21.setStyleSheet(u"color: rgb(233, 234, 236)")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_20 = QLabel(self.frame_15)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(46, 116, 80, 18))
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"color: rgb(233, 234, 236)")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.frame_15)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 0, 110, 110))
        self.pushButton.setMinimumSize(QSize(110, 110))
        self.pushButton.setMaximumSize(QSize(110, 110))
        self.pushButton.setStyleSheet(u"border-radius: 55px;\n"
"border: 2px solid rgb(54, 63, 118);\n"
"background-color: rgb(19, 20, 22);")
        icon7 = QIcon()
        icon7.addFile(u"../../../images/svg_images/daniel-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(100, 100))

        self.verticalLayout_25.addWidget(self.frame_15)

        self.line = QFrame(self.frame_6)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color:rgb(19, 20, 22)")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_25.addWidget(self.line)

        self.frame_16 = QFrame(self.frame_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 82))
        self.frame_16.setMaximumSize(QSize(16777215, 82))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_16)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(3, 3, 3, 3)
        self.frame_43 = QFrame(self.frame_16)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"background-color: rgb(17, 18, 20);\n"
"border-radius:15px;")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)

        self.verticalLayout_26.addWidget(self.frame_43)


        self.verticalLayout_25.addWidget(self.frame_16)

        self.frame_18 = QFrame(self.frame_6)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_18)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(-1, 19, -1, -1)
        self.frame_45 = QFrame(self.frame_18)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_45)
        self.label_22.setObjectName(u"label_22")
        font6 = QFont()
        font6.setPointSize(10)
        self.label_22.setFont(font6)
        self.label_22.setStyleSheet(u"color: rgb(233, 234, 236)")
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.label_22)

        self.label_25 = QLabel(self.frame_45)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font6)
        self.label_25.setStyleSheet(u"color: rgb(233, 234, 236)")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.label_25)


        self.verticalLayout_27.addWidget(self.frame_45)

        self.line_2 = QFrame(self.frame_18)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(170, 16777215))
        self.line_2.setStyleSheet(u"background-color:rgb(19, 20, 22)")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line_2)

        self.frame_46 = QFrame(self.frame_18)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_46)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font6)
        self.label_23.setStyleSheet(u"color: rgb(233, 234, 236)")
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_46)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font6)
        self.label_24.setStyleSheet(u"color: rgb(233, 234, 236)")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.label_24)


        self.verticalLayout_27.addWidget(self.frame_46)

        self.frame_44 = QFrame(self.frame_18)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)

        self.verticalLayout_27.addWidget(self.frame_44)

        self.verticalSpacer_8 = QSpacerItem(20, 162, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_8)


        self.verticalLayout_25.addWidget(self.frame_18)


        self.horizontalLayout_27.addWidget(self.frame_6)

        self.stacked_widget.addWidget(self.page_configuracoes)
        self.page_historico_venda = QWidget()
        self.page_historico_venda.setObjectName(u"page_historico_venda")
        self.verticalLayout_24 = QVBoxLayout(self.page_historico_venda)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(7, 7, 7, 7)
        self.frame_base_chart = QFrame(self.page_historico_venda)
        self.frame_base_chart.setObjectName(u"frame_base_chart")
        self.frame_base_chart.setMinimumSize(QSize(0, 225))
        self.frame_base_chart.setMaximumSize(QSize(16777215, 225))
        self.frame_base_chart.setStyleSheet(u"#frame_base_chart{background-color: rgb(54, 63, 118);}\n"
"#frame_base_chart > QFrame{background-color: rgb(32, 33, 37);}")
        self.frame_base_chart.setFrameShape(QFrame.StyledPanel)
        self.frame_base_chart.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_base_chart)
        self.horizontalLayout_24.setSpacing(4)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(4, 4, 4, 4)
        self.frame_chart_historicode_venda = QFrame(self.frame_base_chart)
        self.frame_chart_historicode_venda.setObjectName(u"frame_chart_historicode_venda")
        self.frame_chart_historicode_venda.setMinimumSize(QSize(396, 207))
        self.frame_chart_historicode_venda.setMaximumSize(QSize(123456, 123456))
        self.frame_chart_historicode_venda.setFrameShape(QFrame.StyledPanel)
        self.frame_chart_historicode_venda.setFrameShadow(QFrame.Raised)
        self.vertical_layout_chart_historico_de_venda_bar = QVBoxLayout(self.frame_chart_historicode_venda)
        self.vertical_layout_chart_historico_de_venda_bar.setSpacing(0)
        self.vertical_layout_chart_historico_de_venda_bar.setObjectName(u"vertical_layout_chart_historico_de_venda_bar")
        self.vertical_layout_chart_historico_de_venda_bar.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_24.addWidget(self.frame_chart_historicode_venda)


        self.verticalLayout_24.addWidget(self.frame_base_chart)

        self.frame_barra_busca_do_historico = QFrame(self.page_historico_venda)
        self.frame_barra_busca_do_historico.setObjectName(u"frame_barra_busca_do_historico")
        self.frame_barra_busca_do_historico.setMinimumSize(QSize(0, 44))
        self.frame_barra_busca_do_historico.setMaximumSize(QSize(16777215, 44))
        self.frame_barra_busca_do_historico.setStyleSheet(u"background-color: rgb(32, 33, 37)")
        self.frame_barra_busca_do_historico.setFrameShape(QFrame.StyledPanel)
        self.frame_barra_busca_do_historico.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_barra_busca_do_historico)
        self.horizontalLayout_26.setSpacing(4)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(4, 0, 4, 0)
        self.btn_pesquisa_historico_de_venda = QPushButton(self.frame_barra_busca_do_historico)
        self.btn_pesquisa_historico_de_venda.setObjectName(u"btn_pesquisa_historico_de_venda")
        self.btn_pesquisa_historico_de_venda.setMinimumSize(QSize(37, 37))
        self.btn_pesquisa_historico_de_venda.setMaximumSize(QSize(37, 37))
        self.btn_pesquisa_historico_de_venda.setStyleSheet(u"QPushButton {\n"
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
        icon8.addFile(u"../../../images/svg_icons/icon_search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisa_historico_de_venda.setIcon(icon8)
        self.btn_pesquisa_historico_de_venda.setIconSize(QSize(25, 25))

        self.horizontalLayout_26.addWidget(self.btn_pesquisa_historico_de_venda)

        self.line_edit_pesquisa_historico_de_venda = QLineEdit(self.frame_barra_busca_do_historico)
        self.line_edit_pesquisa_historico_de_venda.setObjectName(u"line_edit_pesquisa_historico_de_venda")
        self.line_edit_pesquisa_historico_de_venda.setMinimumSize(QSize(0, 35))
        self.line_edit_pesquisa_historico_de_venda.setStyleSheet(u"QLineEdit{\n"
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
        self.line_edit_pesquisa_historico_de_venda.setClearButtonEnabled(False)

        self.horizontalLayout_26.addWidget(self.line_edit_pesquisa_historico_de_venda)

        self.btn_mais_opcoes_historico_de_venda = QPushButton(self.frame_barra_busca_do_historico)
        self.btn_mais_opcoes_historico_de_venda.setObjectName(u"btn_mais_opcoes_historico_de_venda")
        self.btn_mais_opcoes_historico_de_venda.setMinimumSize(QSize(37, 37))
        self.btn_mais_opcoes_historico_de_venda.setMaximumSize(QSize(37, 37))
        self.btn_mais_opcoes_historico_de_venda.setStyleSheet(u"QPushButton {\n"
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
        icon9.addFile(u"../../../images/svg_icons/icon_controller_adjust.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_mais_opcoes_historico_de_venda.setIcon(icon9)
        self.btn_mais_opcoes_historico_de_venda.setIconSize(QSize(30, 30))

        self.horizontalLayout_26.addWidget(self.btn_mais_opcoes_historico_de_venda)


        self.verticalLayout_24.addWidget(self.frame_barra_busca_do_historico)

        self.frame_58 = QFrame(self.page_historico_venda)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_58)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(4, 4, 4, 4)
        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setStyleSheet(u"background-color: rgb(19, 20, 22);\n"
"border-radius:10px;")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.vertical_layout_inventario_3 = QVBoxLayout(self.frame_59)
        self.vertical_layout_inventario_3.setSpacing(0)
        self.vertical_layout_inventario_3.setObjectName(u"vertical_layout_inventario_3")
        self.vertical_layout_inventario_3.setContentsMargins(5, 5, 5, 5)
        self.scrollArea_4 = QScrollArea(self.frame_59)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setStyleSheet(u"background-color: rgb(19, 20, 22);\n"
"border-radius: 10px;")
        self.scrollArea_4.setWidgetResizable(True)
        self.scroll_area_widget_contents_venda_2 = QWidget()
        self.scroll_area_widget_contents_venda_2.setObjectName(u"scroll_area_widget_contents_venda_2")
        self.scroll_area_widget_contents_venda_2.setGeometry(QRect(0, 0, 626, 202))
        self.vertical_layout_venda_2 = QVBoxLayout(self.scroll_area_widget_contents_venda_2)
        self.vertical_layout_venda_2.setSpacing(0)
        self.vertical_layout_venda_2.setObjectName(u"vertical_layout_venda_2")
        self.vertical_layout_venda_2.setContentsMargins(0, 0, 0, 0)
        self.tabela_widget_de_historico_de_venda = QTableWidget(self.scroll_area_widget_contents_venda_2)
        if (self.tabela_widget_de_historico_de_venda.columnCount() < 13):
            self.tabela_widget_de_historico_de_venda.setColumnCount(13)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        if (self.tabela_widget_de_historico_de_venda.rowCount() < 9):
            self.tabela_widget_de_historico_de_venda.setRowCount(9)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setVerticalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setVerticalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setVerticalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setVerticalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setVerticalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setVerticalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setVerticalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setVerticalHeaderItem(7, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabela_widget_de_historico_de_venda.setVerticalHeaderItem(8, __qtablewidgetitem21)
        self.tabela_widget_de_historico_de_venda.setObjectName(u"tabela_widget_de_historico_de_venda")
        self.tabela_widget_de_historico_de_venda.setStyleSheet(u"QTableWidget {	\n"
"    background-color: transparent;\n"
"	color: rgb(233, 234, 236);\n"
"    padding: 0px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(54, 63, 118);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(54, 63, 118);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(239, 236, 231);\n"
"	color: rgb(233, 234, 236);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(49, 50, 55);\n"
"	color: rgb(233, 234, 236);\n"
"}\n"
"QHeaderView::section{\n"
"    background-color: rgb(38, 39, 43);\n"
"    border: 1px solid  rgb(38, 39, 43);\n"
"	color: rgb(233, 234, 236);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"    background-color: rgb(239, 236, 231);\n"
"	color: rgb(233, 234, 236);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(49, 50, 55);\n"
"	background-color: rgb(38, 39, 43);\n"
"	color: rgb(233, 234, 236);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px\n"
"}\n"
""
                        "QHeaderView::section:vertical\n"
"{\n"
"	text-align:center;\n"
"}\n"
"QTableView QTableCornerButton::section {\n"
"	background: rgb(38, 39, 43);\n"
"	color: rgb(233, 234, 236);\n"
"}")
        self.tabela_widget_de_historico_de_venda.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.vertical_layout_venda_2.addWidget(self.tabela_widget_de_historico_de_venda)

        self.scrollArea_4.setWidget(self.scroll_area_widget_contents_venda_2)

        self.vertical_layout_inventario_3.addWidget(self.scrollArea_4)


        self.verticalLayout_23.addWidget(self.frame_59)


        self.verticalLayout_24.addWidget(self.frame_58)

        self.stacked_widget.addWidget(self.page_historico_venda)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_36 = QVBoxLayout(self.page_5)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_17 = QFrame(self.page_5)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 50))
        self.frame_17.setMaximumSize(QSize(16777215, 50))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.verticalLayout_36.addWidget(self.frame_17)

        self.frame_37 = QFrame(self.page_5)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(16777215, 86))
        self.frame_37.setStyleSheet(u"background-color: rgb(19, 20, 22);")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_37)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.frame_37)
        self.label_58.setObjectName(u"label_58")
        font7 = QFont()
        font7.setFamilies([u"Segoe UI Semibold"])
        font7.setPointSize(16)
        self.label_58.setFont(font7)
        self.label_58.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_37.addWidget(self.label_58)

        self.frame_81 = QFrame(self.frame_37)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(0, 44))
        self.frame_81.setMaximumSize(QSize(16777215, 44))
        self.frame_81.setStyleSheet(u"background-color: rgb(32, 33, 37)")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_17.setSpacing(4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(4, 0, 4, 0)
        self.btn_pesquisa_produto_2 = QPushButton(self.frame_81)
        self.btn_pesquisa_produto_2.setObjectName(u"btn_pesquisa_produto_2")
        self.btn_pesquisa_produto_2.setMinimumSize(QSize(37, 37))
        self.btn_pesquisa_produto_2.setMaximumSize(QSize(37, 37))
        self.btn_pesquisa_produto_2.setStyleSheet(u"QPushButton {\n"
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
        self.btn_pesquisa_produto_2.setIcon(icon8)
        self.btn_pesquisa_produto_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_17.addWidget(self.btn_pesquisa_produto_2)

        self.line_edit_pesquisa_produto_3 = QLineEdit(self.frame_81)
        self.line_edit_pesquisa_produto_3.setObjectName(u"line_edit_pesquisa_produto_3")
        self.line_edit_pesquisa_produto_3.setMinimumSize(QSize(0, 35))
        self.line_edit_pesquisa_produto_3.setStyleSheet(u"QLineEdit{\n"
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
"}")
        self.line_edit_pesquisa_produto_3.setClearButtonEnabled(False)

        self.horizontalLayout_17.addWidget(self.line_edit_pesquisa_produto_3)

        self.btn_mais_opcoes_27 = QPushButton(self.frame_81)
        self.btn_mais_opcoes_27.setObjectName(u"btn_mais_opcoes_27")
        self.btn_mais_opcoes_27.setMinimumSize(QSize(37, 37))
        self.btn_mais_opcoes_27.setMaximumSize(QSize(37, 37))
        self.btn_mais_opcoes_27.setStyleSheet(u"QPushButton {\n"
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
        icon10 = QIcon()
        icon10.addFile(u"../../../images/svg_icons/icon_more.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_mais_opcoes_27.setIcon(icon10)
        self.btn_mais_opcoes_27.setIconSize(QSize(25, 25))

        self.horizontalLayout_17.addWidget(self.btn_mais_opcoes_27)

        self.btn_adicionar_produto_2 = QPushButton(self.frame_81)
        self.btn_adicionar_produto_2.setObjectName(u"btn_adicionar_produto_2")
        self.btn_adicionar_produto_2.setMinimumSize(QSize(37, 37))
        self.btn_adicionar_produto_2.setMaximumSize(QSize(37, 37))
        self.btn_adicionar_produto_2.setStyleSheet(u"QPushButton {\n"
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
        icon11 = QIcon()
        icon11.addFile(u"../../../images/svg_icons/icon_add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_adicionar_produto_2.setIcon(icon11)
        self.btn_adicionar_produto_2.setIconSize(QSize(35, 35))

        self.horizontalLayout_17.addWidget(self.btn_adicionar_produto_2)


        self.verticalLayout_37.addWidget(self.frame_81)

        self.label_59 = QLabel(self.frame_37)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_37.addWidget(self.label_59)


        self.verticalLayout_36.addWidget(self.frame_37)

        self.scrollArea_2 = QScrollArea(self.page_5)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 876, 427))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.scrollAreaWidgetContents)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"background-color: rgb(19, 20, 22);")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_34)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_34)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(140, 55))
        self.frame_21.setMaximumSize(QSize(16777215, 55))
        self.frame_21.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.icon_img_22 = QPushButton(self.frame_21)
        self.icon_img_22.setObjectName(u"icon_img_22")
        self.icon_img_22.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_22.setMinimumSize(QSize(37, 37))
        self.icon_img_22.setMaximumSize(QSize(37, 37))
        self.icon_img_22.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        icon12 = QIcon()
        icon12.addFile(u"../../../../../../imagem de modelo/transferir-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_img_22.setIcon(icon12)
        self.icon_img_22.setIconSize(QSize(50, 50))
        self.nome_produto_22 = QLabel(self.frame_21)
        self.nome_produto_22.setObjectName(u"nome_produto_22")
        self.nome_produto_22.setGeometry(QRect(60, 30, 60, 13))
        font8 = QFont()
        font8.setFamilies([u"Zilla Slab Medium"])
        font8.setPointSize(10)
        self.nome_produto_22.setFont(font8)
        self.nome_produto_22.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_22 = QLabel(self.frame_21)
        self.chave_22.setObjectName(u"chave_22")
        self.chave_22.setGeometry(QRect(60, 10, 30, 13))
        font9 = QFont()
        font9.setFamilies([u"Segoe UI Semibold"])
        font9.setPointSize(10)
        self.chave_22.setFont(font9)
        self.chave_22.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_21, 1, 0, 1, 1)

        self.frame_79 = QFrame(self.frame_34)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(140, 55))
        self.frame_79.setMaximumSize(QSize(16777215, 55))
        self.frame_79.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.icon_img_50 = QPushButton(self.frame_79)
        self.icon_img_50.setObjectName(u"icon_img_50")
        self.icon_img_50.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_50.setMinimumSize(QSize(37, 37))
        self.icon_img_50.setMaximumSize(QSize(37, 37))
        self.icon_img_50.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_50.setIcon(icon12)
        self.icon_img_50.setIconSize(QSize(50, 50))
        self.nome_produto_50 = QLabel(self.frame_79)
        self.nome_produto_50.setObjectName(u"nome_produto_50")
        self.nome_produto_50.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_50.setFont(font8)
        self.nome_produto_50.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_50 = QLabel(self.frame_79)
        self.chave_50.setObjectName(u"chave_50")
        self.chave_50.setGeometry(QRect(60, 10, 30, 13))
        self.chave_50.setFont(font9)
        self.chave_50.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_79, 0, 5, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 6, 1, 1)

        self.frame_73 = QFrame(self.frame_34)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(140, 55))
        self.frame_73.setMaximumSize(QSize(16777215, 55))
        self.frame_73.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.icon_img_44 = QPushButton(self.frame_73)
        self.icon_img_44.setObjectName(u"icon_img_44")
        self.icon_img_44.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_44.setMinimumSize(QSize(37, 37))
        self.icon_img_44.setMaximumSize(QSize(37, 37))
        self.icon_img_44.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_44.setIcon(icon12)
        self.icon_img_44.setIconSize(QSize(50, 50))
        self.nome_produto_44 = QLabel(self.frame_73)
        self.nome_produto_44.setObjectName(u"nome_produto_44")
        self.nome_produto_44.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_44.setFont(font8)
        self.nome_produto_44.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_44 = QLabel(self.frame_73)
        self.chave_44.setObjectName(u"chave_44")
        self.chave_44.setGeometry(QRect(60, 10, 30, 13))
        self.chave_44.setFont(font9)
        self.chave_44.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_73, 8, 0, 1, 1)

        self.frame_83 = QFrame(self.frame_34)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(140, 55))
        self.frame_83.setMaximumSize(QSize(16777215, 55))
        self.frame_83.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.icon_img_52 = QPushButton(self.frame_83)
        self.icon_img_52.setObjectName(u"icon_img_52")
        self.icon_img_52.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_52.setMinimumSize(QSize(37, 37))
        self.icon_img_52.setMaximumSize(QSize(37, 37))
        self.icon_img_52.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_52.setIcon(icon12)
        self.icon_img_52.setIconSize(QSize(50, 50))
        self.nome_produto_52 = QLabel(self.frame_83)
        self.nome_produto_52.setObjectName(u"nome_produto_52")
        self.nome_produto_52.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_52.setFont(font8)
        self.nome_produto_52.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_52 = QLabel(self.frame_83)
        self.chave_52.setObjectName(u"chave_52")
        self.chave_52.setGeometry(QRect(60, 10, 30, 13))
        self.chave_52.setFont(font9)
        self.chave_52.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_83, 5, 0, 1, 1)

        self.frame_25 = QFrame(self.frame_34)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(140, 55))
        self.frame_25.setMaximumSize(QSize(16777215, 55))
        self.frame_25.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.icon_img_25 = QPushButton(self.frame_25)
        self.icon_img_25.setObjectName(u"icon_img_25")
        self.icon_img_25.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_25.setMinimumSize(QSize(37, 37))
        self.icon_img_25.setMaximumSize(QSize(37, 37))
        self.icon_img_25.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_25.setIcon(icon12)
        self.icon_img_25.setIconSize(QSize(50, 50))
        self.nome_produto_25 = QLabel(self.frame_25)
        self.nome_produto_25.setObjectName(u"nome_produto_25")
        self.nome_produto_25.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_25.setFont(font8)
        self.nome_produto_25.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_25 = QLabel(self.frame_25)
        self.chave_25.setObjectName(u"chave_25")
        self.chave_25.setGeometry(QRect(60, 10, 30, 13))
        self.chave_25.setFont(font9)
        self.chave_25.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_25, 0, 2, 1, 1)

        self.frame_72 = QFrame(self.frame_34)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(140, 55))
        self.frame_72.setMaximumSize(QSize(16777215, 55))
        self.frame_72.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.icon_img_43 = QPushButton(self.frame_72)
        self.icon_img_43.setObjectName(u"icon_img_43")
        self.icon_img_43.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_43.setMinimumSize(QSize(37, 37))
        self.icon_img_43.setMaximumSize(QSize(37, 37))
        self.icon_img_43.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_43.setIcon(icon12)
        self.icon_img_43.setIconSize(QSize(50, 50))
        self.nome_produto_43 = QLabel(self.frame_72)
        self.nome_produto_43.setObjectName(u"nome_produto_43")
        self.nome_produto_43.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_43.setFont(font8)
        self.nome_produto_43.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_43 = QLabel(self.frame_72)
        self.chave_43.setObjectName(u"chave_43")
        self.chave_43.setGeometry(QRect(60, 10, 30, 13))
        self.chave_43.setFont(font9)
        self.chave_43.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_72, 0, 0, 1, 1)

        self.frame_82 = QFrame(self.frame_34)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMinimumSize(QSize(140, 55))
        self.frame_82.setMaximumSize(QSize(16777215, 55))
        self.frame_82.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.icon_img_51 = QPushButton(self.frame_82)
        self.icon_img_51.setObjectName(u"icon_img_51")
        self.icon_img_51.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_51.setMinimumSize(QSize(37, 37))
        self.icon_img_51.setMaximumSize(QSize(37, 37))
        self.icon_img_51.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_51.setIcon(icon12)
        self.icon_img_51.setIconSize(QSize(50, 50))
        self.nome_produto_51 = QLabel(self.frame_82)
        self.nome_produto_51.setObjectName(u"nome_produto_51")
        self.nome_produto_51.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_51.setFont(font8)
        self.nome_produto_51.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_51 = QLabel(self.frame_82)
        self.chave_51.setObjectName(u"chave_51")
        self.chave_51.setGeometry(QRect(60, 10, 30, 13))
        self.chave_51.setFont(font9)
        self.chave_51.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_82, 0, 4, 1, 1)

        self.frame_85 = QFrame(self.frame_34)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMinimumSize(QSize(140, 55))
        self.frame_85.setMaximumSize(QSize(16777215, 55))
        self.frame_85.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.icon_img_53 = QPushButton(self.frame_85)
        self.icon_img_53.setObjectName(u"icon_img_53")
        self.icon_img_53.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_53.setMinimumSize(QSize(37, 37))
        self.icon_img_53.setMaximumSize(QSize(37, 37))
        self.icon_img_53.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_53.setIcon(icon12)
        self.icon_img_53.setIconSize(QSize(50, 50))
        self.nome_produto_53 = QLabel(self.frame_85)
        self.nome_produto_53.setObjectName(u"nome_produto_53")
        self.nome_produto_53.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_53.setFont(font8)
        self.nome_produto_53.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_53 = QLabel(self.frame_85)
        self.chave_53.setObjectName(u"chave_53")
        self.chave_53.setGeometry(QRect(60, 10, 30, 13))
        self.chave_53.setFont(font9)
        self.chave_53.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_85, 4, 0, 1, 1)

        self.frame_19 = QFrame(self.frame_34)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(140, 55))
        self.frame_19.setMaximumSize(QSize(16777215, 55))
        self.frame_19.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.icon_img_2 = QPushButton(self.frame_19)
        self.icon_img_2.setObjectName(u"icon_img_2")
        self.icon_img_2.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_2.setMinimumSize(QSize(37, 37))
        self.icon_img_2.setMaximumSize(QSize(37, 37))
        self.icon_img_2.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_2.setIcon(icon12)
        self.icon_img_2.setIconSize(QSize(50, 50))
        self.nome_produto_2 = QLabel(self.frame_19)
        self.nome_produto_2.setObjectName(u"nome_produto_2")
        self.nome_produto_2.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_2.setFont(font8)
        self.nome_produto_2.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_2 = QLabel(self.frame_19)
        self.chave_2.setObjectName(u"chave_2")
        self.chave_2.setGeometry(QRect(60, 10, 30, 13))
        self.chave_2.setFont(font9)
        self.chave_2.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_19, 1, 1, 1, 1)

        self.frame_71 = QFrame(self.frame_34)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(140, 55))
        self.frame_71.setMaximumSize(QSize(16777215, 55))
        self.frame_71.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.icon_img_42 = QPushButton(self.frame_71)
        self.icon_img_42.setObjectName(u"icon_img_42")
        self.icon_img_42.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_42.setMinimumSize(QSize(37, 37))
        self.icon_img_42.setMaximumSize(QSize(37, 37))
        self.icon_img_42.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_42.setIcon(icon12)
        self.icon_img_42.setIconSize(QSize(50, 50))
        self.nome_produto_42 = QLabel(self.frame_71)
        self.nome_produto_42.setObjectName(u"nome_produto_42")
        self.nome_produto_42.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_42.setFont(font8)
        self.nome_produto_42.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_42 = QLabel(self.frame_71)
        self.chave_42.setObjectName(u"chave_42")
        self.chave_42.setGeometry(QRect(60, 10, 30, 13))
        self.chave_42.setFont(font9)
        self.chave_42.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_71, 0, 1, 1, 1)

        self.frame_87 = QFrame(self.frame_34)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(140, 55))
        self.frame_87.setMaximumSize(QSize(16777215, 55))
        self.frame_87.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.icon_img_55 = QPushButton(self.frame_87)
        self.icon_img_55.setObjectName(u"icon_img_55")
        self.icon_img_55.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_55.setMinimumSize(QSize(37, 37))
        self.icon_img_55.setMaximumSize(QSize(37, 37))
        self.icon_img_55.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_55.setIcon(icon12)
        self.icon_img_55.setIconSize(QSize(50, 50))
        self.nome_produto_55 = QLabel(self.frame_87)
        self.nome_produto_55.setObjectName(u"nome_produto_55")
        self.nome_produto_55.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_55.setFont(font8)
        self.nome_produto_55.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_55 = QLabel(self.frame_87)
        self.chave_55.setObjectName(u"chave_55")
        self.chave_55.setGeometry(QRect(60, 10, 30, 13))
        self.chave_55.setFont(font9)
        self.chave_55.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_87, 0, 3, 1, 1)

        self.frame_75 = QFrame(self.frame_34)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(140, 55))
        self.frame_75.setMaximumSize(QSize(16777215, 55))
        self.frame_75.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.icon_img_46 = QPushButton(self.frame_75)
        self.icon_img_46.setObjectName(u"icon_img_46")
        self.icon_img_46.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_46.setMinimumSize(QSize(37, 37))
        self.icon_img_46.setMaximumSize(QSize(37, 37))
        self.icon_img_46.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_46.setIcon(icon12)
        self.icon_img_46.setIconSize(QSize(50, 50))
        self.nome_produto_46 = QLabel(self.frame_75)
        self.nome_produto_46.setObjectName(u"nome_produto_46")
        self.nome_produto_46.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_46.setFont(font8)
        self.nome_produto_46.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_46 = QLabel(self.frame_75)
        self.chave_46.setObjectName(u"chave_46")
        self.chave_46.setGeometry(QRect(60, 10, 30, 13))
        self.chave_46.setFont(font9)
        self.chave_46.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_75, 6, 0, 1, 1)

        self.frame_74 = QFrame(self.frame_34)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(140, 55))
        self.frame_74.setMaximumSize(QSize(16777215, 55))
        self.frame_74.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.icon_img_45 = QPushButton(self.frame_74)
        self.icon_img_45.setObjectName(u"icon_img_45")
        self.icon_img_45.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_45.setMinimumSize(QSize(37, 37))
        self.icon_img_45.setMaximumSize(QSize(37, 37))
        self.icon_img_45.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_45.setIcon(icon12)
        self.icon_img_45.setIconSize(QSize(50, 50))
        self.nome_produto_45 = QLabel(self.frame_74)
        self.nome_produto_45.setObjectName(u"nome_produto_45")
        self.nome_produto_45.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_45.setFont(font8)
        self.nome_produto_45.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_45 = QLabel(self.frame_74)
        self.chave_45.setObjectName(u"chave_45")
        self.chave_45.setGeometry(QRect(60, 10, 30, 13))
        self.chave_45.setFont(font9)
        self.chave_45.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_74, 7, 0, 1, 1)

        self.frame_70 = QFrame(self.frame_34)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(140, 55))
        self.frame_70.setMaximumSize(QSize(16777215, 55))
        self.frame_70.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.icon_img_41 = QPushButton(self.frame_70)
        self.icon_img_41.setObjectName(u"icon_img_41")
        self.icon_img_41.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_41.setMinimumSize(QSize(37, 37))
        self.icon_img_41.setMaximumSize(QSize(37, 37))
        self.icon_img_41.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_41.setIcon(icon12)
        self.icon_img_41.setIconSize(QSize(50, 50))
        self.nome_produto_41 = QLabel(self.frame_70)
        self.nome_produto_41.setObjectName(u"nome_produto_41")
        self.nome_produto_41.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_41.setFont(font8)
        self.nome_produto_41.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_41 = QLabel(self.frame_70)
        self.chave_41.setObjectName(u"chave_41")
        self.chave_41.setGeometry(QRect(60, 10, 30, 13))
        self.chave_41.setFont(font9)
        self.chave_41.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_70, 4, 1, 1, 1)

        self.frame_86 = QFrame(self.frame_34)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(140, 55))
        self.frame_86.setMaximumSize(QSize(16777215, 55))
        self.frame_86.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.icon_img_54 = QPushButton(self.frame_86)
        self.icon_img_54.setObjectName(u"icon_img_54")
        self.icon_img_54.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_54.setMinimumSize(QSize(37, 37))
        self.icon_img_54.setMaximumSize(QSize(37, 37))
        self.icon_img_54.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_54.setIcon(icon12)
        self.icon_img_54.setIconSize(QSize(50, 50))
        self.nome_produto_54 = QLabel(self.frame_86)
        self.nome_produto_54.setObjectName(u"nome_produto_54")
        self.nome_produto_54.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_54.setFont(font8)
        self.nome_produto_54.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_54 = QLabel(self.frame_86)
        self.chave_54.setObjectName(u"chave_54")
        self.chave_54.setGeometry(QRect(60, 10, 30, 13))
        self.chave_54.setFont(font9)
        self.chave_54.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_86, 1, 2, 1, 1)

        self.frame_78 = QFrame(self.frame_34)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(140, 55))
        self.frame_78.setMaximumSize(QSize(16777215, 55))
        self.frame_78.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.icon_img_49 = QPushButton(self.frame_78)
        self.icon_img_49.setObjectName(u"icon_img_49")
        self.icon_img_49.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_49.setMinimumSize(QSize(37, 37))
        self.icon_img_49.setMaximumSize(QSize(37, 37))
        self.icon_img_49.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_49.setIcon(icon12)
        self.icon_img_49.setIconSize(QSize(50, 50))
        self.nome_produto_49 = QLabel(self.frame_78)
        self.nome_produto_49.setObjectName(u"nome_produto_49")
        self.nome_produto_49.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_49.setFont(font8)
        self.nome_produto_49.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_49 = QLabel(self.frame_78)
        self.chave_49.setObjectName(u"chave_49")
        self.chave_49.setGeometry(QRect(60, 10, 30, 13))
        self.chave_49.setFont(font9)
        self.chave_49.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_78, 4, 2, 1, 1)

        self.frame_77 = QFrame(self.frame_34)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(140, 55))
        self.frame_77.setMaximumSize(QSize(16777215, 55))
        self.frame_77.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.icon_img_48 = QPushButton(self.frame_77)
        self.icon_img_48.setObjectName(u"icon_img_48")
        self.icon_img_48.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_48.setMinimumSize(QSize(37, 37))
        self.icon_img_48.setMaximumSize(QSize(37, 37))
        self.icon_img_48.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_48.setIcon(icon12)
        self.icon_img_48.setIconSize(QSize(50, 50))
        self.nome_produto_48 = QLabel(self.frame_77)
        self.nome_produto_48.setObjectName(u"nome_produto_48")
        self.nome_produto_48.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_48.setFont(font8)
        self.nome_produto_48.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_48 = QLabel(self.frame_77)
        self.chave_48.setObjectName(u"chave_48")
        self.chave_48.setGeometry(QRect(60, 10, 30, 13))
        self.chave_48.setFont(font9)
        self.chave_48.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_77, 1, 3, 1, 1)

        self.frame_76 = QFrame(self.frame_34)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(140, 55))
        self.frame_76.setMaximumSize(QSize(16777215, 55))
        self.frame_76.setStyleSheet(u"background-color: rgb(38, 39, 43);")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.icon_img_47 = QPushButton(self.frame_76)
        self.icon_img_47.setObjectName(u"icon_img_47")
        self.icon_img_47.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img_47.setMinimumSize(QSize(37, 37))
        self.icon_img_47.setMaximumSize(QSize(37, 37))
        self.icon_img_47.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_47.setIcon(icon12)
        self.icon_img_47.setIconSize(QSize(50, 50))
        self.nome_produto_47 = QLabel(self.frame_76)
        self.nome_produto_47.setObjectName(u"nome_produto_47")
        self.nome_produto_47.setGeometry(QRect(60, 30, 60, 13))
        self.nome_produto_47.setFont(font8)
        self.nome_produto_47.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_47 = QLabel(self.frame_76)
        self.chave_47.setObjectName(u"chave_47")
        self.chave_47.setGeometry(QRect(60, 10, 30, 13))
        self.chave_47.setFont(font9)
        self.chave_47.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.gridLayout.addWidget(self.frame_76, 4, 3, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_34)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_36.addWidget(self.scrollArea_2)

        self.stacked_widget.addWidget(self.page_5)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_12 = QVBoxLayout(self.page_home)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(7, 7, 7, 7)
        self.frame_nav_continer = QFrame(self.page_home)
        self.frame_nav_continer.setObjectName(u"frame_nav_continer")
        self.frame_nav_continer.setMinimumSize(QSize(0, 179))
        self.frame_nav_continer.setMaximumSize(QSize(16777215, 179))
        self.frame_nav_continer.setStyleSheet(u"background-color: rgb(54, 63, 118);")
        self.frame_nav_continer.setFrameShape(QFrame.StyledPanel)
        self.frame_nav_continer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_nav_continer)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_inventario = QFrame(self.frame_nav_continer)
        self.frame_inventario.setObjectName(u"frame_inventario")
        self.frame_inventario.setMinimumSize(QSize(151, 161))
        self.frame_inventario.setMaximumSize(QSize(123456, 123456))
        self.frame_inventario.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(32, 33, 37, 200);\n"
"	background-image: url(none);}\n"
"\n"
"QFrame:hover\n"
"{border: 0.5px solid rgba(255, 255, 255, 80)}")
        self.frame_inventario.setFrameShape(QFrame.StyledPanel)
        self.frame_inventario.setFrameShadow(QFrame.Raised)
        self.btn_logo_inventario = QPushButton(self.frame_inventario)
        self.btn_logo_inventario.setObjectName(u"btn_logo_inventario")
        self.btn_logo_inventario.setGeometry(QRect(20, 25, 52, 55))
        self.btn_logo_inventario.setStyleSheet(u"background-color: transparent")
        self.btn_logo_inventario.setIcon(icon2)
        self.btn_logo_inventario.setIconSize(QSize(58, 58))
        self.lbl_inventario = QLabel(self.frame_inventario)
        self.lbl_inventario.setObjectName(u"lbl_inventario")
        self.lbl_inventario.setGeometry(QRect(20, 90, 71, 16))
        self.lbl_inventario.setFont(font3)
        self.lbl_inventario.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.lbl_info_inventario_1 = QLabel(self.frame_inventario)
        self.lbl_info_inventario_1.setObjectName(u"lbl_info_inventario_1")
        self.lbl_info_inventario_1.setGeometry(QRect(22, 112, 70, 10))
        self.lbl_info_inventario_1.setFont(font4)
        self.lbl_info_inventario_1.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_inventario_1.setScaledContents(False)
        self.btn_log_extra_inventario = QPushButton(self.frame_inventario)
        self.btn_log_extra_inventario.setObjectName(u"btn_log_extra_inventario")
        self.btn_log_extra_inventario.setGeometry(QRect(128, 137, 20, 20))
        self.btn_log_extra_inventario.setStyleSheet(u"background-color: transparent")
        self.btn_log_extra_inventario.setIcon(icon3)
        self.btn_log_extra_inventario.setIconSize(QSize(20, 20))
        self.lbl_info_inventario_2 = QLabel(self.frame_inventario)
        self.lbl_info_inventario_2.setObjectName(u"lbl_info_inventario_2")
        self.lbl_info_inventario_2.setGeometry(QRect(22, 126, 90, 10))
        self.lbl_info_inventario_2.setFont(font4)
        self.lbl_info_inventario_2.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_inventario_2.setScaledContents(False)

        self.horizontalLayout_21.addWidget(self.frame_inventario)

        self.frame_venda = QFrame(self.frame_nav_continer)
        self.frame_venda.setObjectName(u"frame_venda")
        self.frame_venda.setMinimumSize(QSize(151, 161))
        self.frame_venda.setMaximumSize(QSize(123456, 123456))
        self.frame_venda.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(32, 33, 37, 200);\n"
"	background-image: url(none);}\n"
"\n"
"QFrame:hover\n"
"{border: 0.5px solid rgba(255, 255, 255, 80)}")
        self.frame_venda.setFrameShape(QFrame.StyledPanel)
        self.frame_venda.setFrameShadow(QFrame.Raised)
        self.btn_logo_venda = QPushButton(self.frame_venda)
        self.btn_logo_venda.setObjectName(u"btn_logo_venda")
        self.btn_logo_venda.setGeometry(QRect(18, 25, 51, 51))
        self.btn_logo_venda.setStyleSheet(u"background-color: transparent")
        self.btn_logo_venda.setIcon(icon4)
        self.btn_logo_venda.setIconSize(QSize(49, 49))
        self.lbl_venda = QLabel(self.frame_venda)
        self.lbl_venda.setObjectName(u"lbl_venda")
        self.lbl_venda.setGeometry(QRect(20, 90, 50, 16))
        self.lbl_venda.setFont(font3)
        self.lbl_venda.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border:none;")
        self.btn_log_extra_venda = QPushButton(self.frame_venda)
        self.btn_log_extra_venda.setObjectName(u"btn_log_extra_venda")
        self.btn_log_extra_venda.setGeometry(QRect(128, 137, 20, 20))
        self.btn_log_extra_venda.setStyleSheet(u"background-color: transparent")
        self.btn_log_extra_venda.setIcon(icon3)
        self.btn_log_extra_venda.setIconSize(QSize(20, 20))
        self.lbl_info_venda_3 = QLabel(self.frame_venda)
        self.lbl_info_venda_3.setObjectName(u"lbl_info_venda_3")
        self.lbl_info_venda_3.setGeometry(QRect(22, 140, 50, 10))
        self.lbl_info_venda_3.setFont(font4)
        self.lbl_info_venda_3.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_venda_3.setScaledContents(False)
        self.lbl_info_venda_1 = QLabel(self.frame_venda)
        self.lbl_info_venda_1.setObjectName(u"lbl_info_venda_1")
        self.lbl_info_venda_1.setGeometry(QRect(22, 112, 90, 10))
        self.lbl_info_venda_1.setFont(font4)
        self.lbl_info_venda_1.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_venda_1.setScaledContents(False)
        self.lbl_info_venda_2 = QLabel(self.frame_venda)
        self.lbl_info_venda_2.setObjectName(u"lbl_info_venda_2")
        self.lbl_info_venda_2.setGeometry(QRect(22, 126, 110, 10))
        self.lbl_info_venda_2.setFont(font4)
        self.lbl_info_venda_2.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_venda_2.setScaledContents(False)

        self.horizontalLayout_21.addWidget(self.frame_venda)

        self.frame_perda = QFrame(self.frame_nav_continer)
        self.frame_perda.setObjectName(u"frame_perda")
        self.frame_perda.setMinimumSize(QSize(151, 161))
        self.frame_perda.setMaximumSize(QSize(123456, 123456))
        self.frame_perda.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(32, 33, 37, 200);\n"
"	background-image: url(none);}\n"
"\n"
"QFrame:hover\n"
"{border: 0.5px solid rgba(255, 255, 255, 80)}")
        self.frame_perda.setFrameShape(QFrame.StyledPanel)
        self.frame_perda.setFrameShadow(QFrame.Raised)
        self.btn_logo_perda = QPushButton(self.frame_perda)
        self.btn_logo_perda.setObjectName(u"btn_logo_perda")
        self.btn_logo_perda.setGeometry(QRect(19, 25, 50, 51))
        self.btn_logo_perda.setStyleSheet(u"background-color: transparent")
        self.btn_logo_perda.setIcon(icon5)
        self.btn_logo_perda.setIconSize(QSize(57, 57))
        self.lbl_perda = QLabel(self.frame_perda)
        self.lbl_perda.setObjectName(u"lbl_perda")
        self.lbl_perda.setGeometry(QRect(20, 90, 50, 16))
        self.lbl_perda.setFont(font3)
        self.lbl_perda.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_perda_1 = QLabel(self.frame_perda)
        self.lbl_info_perda_1.setObjectName(u"lbl_info_perda_1")
        self.lbl_info_perda_1.setGeometry(QRect(22, 112, 101, 10))
        self.lbl_info_perda_1.setFont(font4)
        self.lbl_info_perda_1.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_perda_1.setScaledContents(False)
        self.btn_log_extra_perda = QPushButton(self.frame_perda)
        self.btn_log_extra_perda.setObjectName(u"btn_log_extra_perda")
        self.btn_log_extra_perda.setGeometry(QRect(128, 137, 20, 20))
        self.btn_log_extra_perda.setStyleSheet(u"background-color: transparent")
        self.btn_log_extra_perda.setIcon(icon3)
        self.btn_log_extra_perda.setIconSize(QSize(20, 20))
        self.lbl_info_perda_2 = QLabel(self.frame_perda)
        self.lbl_info_perda_2.setObjectName(u"lbl_info_perda_2")
        self.lbl_info_perda_2.setGeometry(QRect(22, 126, 111, 10))
        self.lbl_info_perda_2.setFont(font4)
        self.lbl_info_perda_2.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_perda_2.setScaledContents(False)
        self.lbl_info_perda_3 = QLabel(self.frame_perda)
        self.lbl_info_perda_3.setObjectName(u"lbl_info_perda_3")
        self.lbl_info_perda_3.setGeometry(QRect(22, 140, 50, 10))
        self.lbl_info_perda_3.setFont(font4)
        self.lbl_info_perda_3.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_perda_3.setScaledContents(False)

        self.horizontalLayout_21.addWidget(self.frame_perda)

        self.frame_recibo = QFrame(self.frame_nav_continer)
        self.frame_recibo.setObjectName(u"frame_recibo")
        self.frame_recibo.setMinimumSize(QSize(151, 161))
        self.frame_recibo.setMaximumSize(QSize(123456, 123456))
        self.frame_recibo.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(32, 33, 37, 200);\n"
"	background-image: url(none);}\n"
"\n"
"QFrame:hover\n"
"{border: 0.5px solid rgba(255, 255, 255, 80)}")
        self.frame_recibo.setFrameShape(QFrame.StyledPanel)
        self.frame_recibo.setFrameShadow(QFrame.Raised)
        self.btn_logo_recibo = QPushButton(self.frame_recibo)
        self.btn_logo_recibo.setObjectName(u"btn_logo_recibo")
        self.btn_logo_recibo.setGeometry(QRect(18, 26, 50, 48))
        self.btn_logo_recibo.setStyleSheet(u"background-color: transparent")
        self.btn_logo_recibo.setIcon(icon6)
        self.btn_logo_recibo.setIconSize(QSize(75, 75))
        self.lbl_recibo = QLabel(self.frame_recibo)
        self.lbl_recibo.setObjectName(u"lbl_recibo")
        self.lbl_recibo.setGeometry(QRect(20, 90, 50, 16))
        self.lbl_recibo.setFont(font3)
        self.lbl_recibo.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_extra_recibo_1 = QLabel(self.frame_recibo)
        self.lbl_info_extra_recibo_1.setObjectName(u"lbl_info_extra_recibo_1")
        self.lbl_info_extra_recibo_1.setGeometry(QRect(22, 112, 110, 10))
        self.lbl_info_extra_recibo_1.setFont(font4)
        self.lbl_info_extra_recibo_1.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_extra_recibo_1.setScaledContents(False)
        self.btn_log_extra_recibo = QPushButton(self.frame_recibo)
        self.btn_log_extra_recibo.setObjectName(u"btn_log_extra_recibo")
        self.btn_log_extra_recibo.setGeometry(QRect(128, 137, 20, 20))
        self.btn_log_extra_recibo.setStyleSheet(u"background-color: transparent")
        self.btn_log_extra_recibo.setIcon(icon3)
        self.btn_log_extra_recibo.setIconSize(QSize(20, 20))
        self.lbl_info_extra_recibo_2 = QLabel(self.frame_recibo)
        self.lbl_info_extra_recibo_2.setObjectName(u"lbl_info_extra_recibo_2")
        self.lbl_info_extra_recibo_2.setGeometry(QRect(22, 126, 110, 10))
        self.lbl_info_extra_recibo_2.setFont(font4)
        self.lbl_info_extra_recibo_2.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_extra_recibo_2.setScaledContents(False)
        self.lbl_info_extra_recibo_3 = QLabel(self.frame_recibo)
        self.lbl_info_extra_recibo_3.setObjectName(u"lbl_info_extra_recibo_3")
        self.lbl_info_extra_recibo_3.setGeometry(QRect(22, 140, 90, 10))
        self.lbl_info_extra_recibo_3.setFont(font4)
        self.lbl_info_extra_recibo_3.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_extra_recibo_3.setScaledContents(False)

        self.horizontalLayout_21.addWidget(self.frame_recibo)


        self.verticalLayout_12.addWidget(self.frame_nav_continer)

        self.frame_20 = QFrame(self.page_home)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"background-color: rgb(19, 20, 22);")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_20)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 150))
        self.frame_23.setStyleSheet(u"")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_dinamic_chart = QFrame(self.frame_23)
        self.frame_dinamic_chart.setObjectName(u"frame_dinamic_chart")
        self.frame_dinamic_chart.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_dinamic_chart.setFrameShape(QFrame.StyledPanel)
        self.frame_dinamic_chart.setFrameShadow(QFrame.Raised)
        self.vertical_layout_dynamic_chart = QVBoxLayout(self.frame_dinamic_chart)
        self.vertical_layout_dynamic_chart.setSpacing(0)
        self.vertical_layout_dynamic_chart.setObjectName(u"vertical_layout_dynamic_chart")
        self.vertical_layout_dynamic_chart.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.frame_dinamic_chart)

        self.frame_chart_bar = QFrame(self.frame_23)
        self.frame_chart_bar.setObjectName(u"frame_chart_bar")
        self.frame_chart_bar.setMinimumSize(QSize(200, 0))
        self.frame_chart_bar.setMaximumSize(QSize(200, 16777215))
        self.frame_chart_bar.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_chart_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_chart_bar.setFrameShadow(QFrame.Raised)
        self.vertical_layout_char_bar = QVBoxLayout(self.frame_chart_bar)
        self.vertical_layout_char_bar.setSpacing(0)
        self.vertical_layout_char_bar.setObjectName(u"vertical_layout_char_bar")
        self.vertical_layout_char_bar.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.frame_chart_bar)


        self.verticalLayout_21.addWidget(self.frame_23)

        self.frame_33 = QFrame(self.frame_20)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 150))
        self.frame_33.setStyleSheet(u"background-color: rgb(32, 33, 37)")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_33)
        self.verticalLayout_22.setSpacing(5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 10, 5, 5)
        self.frame_42 = QFrame(self.frame_33)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMaximumSize(QSize(16777215, 40))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(9, 0, 9, 0)
        self.frame_56 = QFrame(self.frame_42)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(140, 40))
        self.frame_56.setMaximumSize(QSize(16777215, 40))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.icon_img_29 = QPushButton(self.frame_56)
        self.icon_img_29.setObjectName(u"icon_img_29")
        self.icon_img_29.setGeometry(QRect(1, 1, 37, 37))
        self.icon_img_29.setMinimumSize(QSize(37, 37))
        self.icon_img_29.setMaximumSize(QSize(37, 37))
        self.icon_img_29.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        self.icon_img_29.setIcon(icon7)
        self.icon_img_29.setIconSize(QSize(32, 32))
        self.nome_produto_32 = QLabel(self.frame_56)
        self.nome_produto_32.setObjectName(u"nome_produto_32")
        self.nome_produto_32.setGeometry(QRect(49, 24, 130, 10))
        self.nome_produto_32.setFont(font8)
        self.nome_produto_32.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_33 = QLabel(self.frame_56)
        self.chave_33.setObjectName(u"chave_33")
        self.chave_33.setGeometry(QRect(50, 5, 30, 10))
        self.chave_33.setFont(font9)
        self.chave_33.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.horizontalLayout_14.addWidget(self.frame_56)

        self.progressBar_9 = QProgressBar(self.frame_42)
        self.progressBar_9.setObjectName(u"progressBar_9")
        self.progressBar_9.setMaximumSize(QSize(16777215, 12))
        self.progressBar_9.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb( 255, 255, 255);\n"
"	color: rgb(200, 200, 200);\n"
"	border-radius: 5px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(54, 63, 118, 255), stop:1 rgba(64, 80, 170, 255));\n"
"}")
        self.progressBar_9.setValue(90)

        self.horizontalLayout_14.addWidget(self.progressBar_9)


        self.verticalLayout_22.addWidget(self.frame_42)

        self.frame_32 = QFrame(self.frame_33)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(16777215, 40))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.frame_55 = QFrame(self.frame_32)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(140, 40))
        self.frame_55.setMaximumSize(QSize(16777215, 40))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.icon_img_28 = QPushButton(self.frame_55)
        self.icon_img_28.setObjectName(u"icon_img_28")
        self.icon_img_28.setGeometry(QRect(1, 1, 37, 37))
        self.icon_img_28.setMinimumSize(QSize(37, 37))
        self.icon_img_28.setMaximumSize(QSize(37, 37))
        self.icon_img_28.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        icon13 = QIcon()
        icon13.addFile(u"../../../images/svg_images/tatiana-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_img_28.setIcon(icon13)
        self.icon_img_28.setIconSize(QSize(32, 32))
        self.nome_produto_31 = QLabel(self.frame_55)
        self.nome_produto_31.setObjectName(u"nome_produto_31")
        self.nome_produto_31.setGeometry(QRect(49, 24, 130, 10))
        self.nome_produto_31.setFont(font8)
        self.nome_produto_31.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_32 = QLabel(self.frame_55)
        self.chave_32.setObjectName(u"chave_32")
        self.chave_32.setGeometry(QRect(50, 5, 30, 10))
        self.chave_32.setFont(font9)
        self.chave_32.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.horizontalLayout_22.addWidget(self.frame_55)

        self.progressBar_7 = QProgressBar(self.frame_32)
        self.progressBar_7.setObjectName(u"progressBar_7")
        self.progressBar_7.setMaximumSize(QSize(16777215, 12))
        self.progressBar_7.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb( 255, 255, 255);\n"
"	color: rgb(200, 200, 200);\n"
"	border-radius: 5px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(54, 63, 118, 255), stop:1 rgba(64, 80, 170, 255));\n"
"}")
        self.progressBar_7.setValue(70)

        self.horizontalLayout_22.addWidget(self.progressBar_7)


        self.verticalLayout_22.addWidget(self.frame_32)

        self.frame_24 = QFrame(self.frame_33)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 40))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.frame_54 = QFrame(self.frame_24)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(140, 40))
        self.frame_54.setMaximumSize(QSize(16777215, 40))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.icon_img_30 = QPushButton(self.frame_54)
        self.icon_img_30.setObjectName(u"icon_img_30")
        self.icon_img_30.setGeometry(QRect(1, 1, 37, 37))
        self.icon_img_30.setMinimumSize(QSize(37, 37))
        self.icon_img_30.setMaximumSize(QSize(37, 37))
        self.icon_img_30.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
"border-radius:7px;\n"
"color: #ffffff;\n"
"border: 1px solid rgb(255, 255, 255)")
        icon14 = QIcon()
        icon14.addFile(u"../../../images/svg_images/john-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_img_30.setIcon(icon14)
        self.icon_img_30.setIconSize(QSize(32, 32))
        self.nome_produto_28 = QLabel(self.frame_54)
        self.nome_produto_28.setObjectName(u"nome_produto_28")
        self.nome_produto_28.setGeometry(QRect(49, 24, 130, 10))
        self.nome_produto_28.setFont(font8)
        self.nome_produto_28.setStyleSheet(u"color: rgb(233, 234, 236);")
        self.chave_34 = QLabel(self.frame_54)
        self.chave_34.setObjectName(u"chave_34")
        self.chave_34.setGeometry(QRect(50, 5, 30, 10))
        self.chave_34.setFont(font9)
        self.chave_34.setStyleSheet(u"color: rgb(233, 234, 236);")

        self.horizontalLayout_15.addWidget(self.frame_54)

        self.progressBar_8 = QProgressBar(self.frame_24)
        self.progressBar_8.setObjectName(u"progressBar_8")
        self.progressBar_8.setMaximumSize(QSize(16777215, 12))
        self.progressBar_8.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb( 255, 255, 255);\n"
"	color: rgb(200, 200, 200);\n"
"	border-radius: 5px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(54, 63, 118, 255), stop:1 rgba(64, 80, 170, 255));\n"
"}")
        self.progressBar_8.setValue(40)

        self.horizontalLayout_15.addWidget(self.progressBar_8)


        self.verticalLayout_22.addWidget(self.frame_24)


        self.verticalLayout_21.addWidget(self.frame_33)


        self.verticalLayout_12.addWidget(self.frame_20)

        self.stacked_widget.addWidget(self.page_home)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_38 = QVBoxLayout(self.page_6)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame_36 = QFrame(self.page_6)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(0, 110))
        self.frame_36.setMaximumSize(QSize(16777215, 110))
        self.frame_36.setStyleSheet(u"background-color: rgb(19, 20, 22);")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_7 = QPushButton(self.frame_36)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(50, 50))
        font10 = QFont()
        font10.setFamilies([u"Segoe Script"])
        self.pushButton_7.setFont(font10)
        self.pushButton_7.setIcon(icon12)
        self.pushButton_7.setIconSize(QSize(100, 100))

        self.horizontalLayout_19.addWidget(self.pushButton_7)

        self.frame_52 = QFrame(self.frame_36)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_52)
        self.verticalLayout_40.setSpacing(8)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_62 = QLabel(self.frame_52)
        self.label_62.setObjectName(u"label_62")
        font11 = QFont()
        font11.setFamilies([u"Segoe UI Variable Text Semibold"])
        font11.setPointSize(13)
        self.label_62.setFont(font11)
        self.label_62.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_62.setWordWrap(True)

        self.verticalLayout_40.addWidget(self.label_62)

        self.label_61 = QLabel(self.frame_52)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_61.setWordWrap(True)

        self.verticalLayout_40.addWidget(self.label_61)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_4)


        self.horizontalLayout_19.addWidget(self.frame_52)


        self.verticalLayout_38.addWidget(self.frame_36)

        self.frame_41 = QFrame(self.page_6)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 2))
        self.frame_41.setMaximumSize(QSize(16777215, 2))
        self.frame_41.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)

        self.verticalLayout_38.addWidget(self.frame_41)

        self.frame_38 = QFrame(self.page_6)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"background-color: rgb(19, 20, 22);")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_39)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_64 = QLabel(self.frame_39)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(0, 0))
        self.label_64.setMaximumSize(QSize(16777215, 12345666))
        font12 = QFont()
        font12.setFamilies([u"Segoe UI Semibold"])
        font12.setPointSize(15)
        font12.setBold(True)
        self.label_64.setFont(font12)
        self.label_64.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_64.setWordWrap(True)

        self.verticalLayout_41.addWidget(self.label_64)

        self.frame_53 = QFrame(self.frame_39)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_53)
        self.verticalLayout_45.setSpacing(30)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setSpacing(4)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_67 = QLabel(self.frame_53)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"color: rgba(255, 255, 255, 120);")

        self.verticalLayout_44.addWidget(self.label_67)

        self.comboBox = QComboBox(self.frame_53)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(300, 42))
        self.comboBox.setFont(font6)
        self.comboBox.setStyleSheet(u"QComboBox , QLineEdit{\n"
"    border: 1px solid rgba(255, 255, 255, 80);\n"
"    border-radius: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: -187px;\n"
"	color: rgb(133, 133, 136);\n"
"    background-color: rgb(19, 20, 22);\n"
"    text-align: left;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	background-color: rgb(30, 31, 34);\n"
"}\n"
"\n"
"QComboBox:pressed , QComboBox:focus{\n"
"    background-color: rgb(37, 39, 42);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"	color: rgb(133, 133, 136);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"	color: rgb(133, 133, 136);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.06);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
"}\n"
"                        \n"
"QComboBox::drop-down {\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"	width: 34px; }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(133, 133, 136);\n"
"	background-color: rgb(23, 24, 26);\n"
"	padding: 10px;\n"
"	se"
                        "lection-background-color: rgb(195, 155, 255);\n"
"	border: 2px solid  rgba(255, 255, 255, 80);\n"
"	border-radius:5px;}")
        self.comboBox.setEditable(False)
        self.comboBox.setMinimumContentsLength(0)

        self.verticalLayout_44.addWidget(self.comboBox)


        self.verticalLayout_45.addLayout(self.verticalLayout_44)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setSpacing(4)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_66 = QLabel(self.frame_53)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setStyleSheet(u"color: rgba(255, 255, 255, 120);")

        self.verticalLayout_43.addWidget(self.label_66)

        self.lineEdit = QLineEdit(self.frame_53)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 40))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"color: rgb(233, 234, 236);\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 1px solid rgba(255, 255, 255, 140);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 1px solid rgba(255, 255, 255, 200);\n"
"}")

        self.verticalLayout_43.addWidget(self.lineEdit)


        self.verticalLayout_45.addLayout(self.verticalLayout_43)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setSpacing(4)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_65 = QLabel(self.frame_53)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"color: rgba(255, 255, 255, 120);")

        self.verticalLayout_42.addWidget(self.label_65)

        self.lineEdit_2 = QLineEdit(self.frame_53)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(300, 40))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"color: rgba(255, 255, 255, 120);\n"
"border: 1px solid rgba(255, 255, 255, 80);\n"
"border-radius: 10px;\n"
"padding-left: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 1px solid rgba(255, 255, 255, 140);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 1px solid rgba(255, 255, 255, 200);\n"
"}")

        self.verticalLayout_42.addWidget(self.lineEdit_2)


        self.verticalLayout_45.addLayout(self.verticalLayout_42)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_45.addItem(self.verticalSpacer_6)


        self.verticalLayout_41.addWidget(self.frame_53)


        self.horizontalLayout_18.addWidget(self.frame_39)

        self.frame_51 = QFrame(self.frame_38)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMaximumSize(QSize(2, 16777215))
        self.frame_51.setStyleSheet(u"background-color: rgb(32, 33, 37);")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_18.addWidget(self.frame_51)

        self.frame_40 = QFrame(self.frame_38)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(400, 16777215))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_40)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_63 = QLabel(self.frame_40)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font12)
        self.label_63.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_39.addWidget(self.label_63)

        self.label_60 = QLabel(self.frame_40)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_60.setWordWrap(True)
        self.label_60.setIndent(-1)

        self.verticalLayout_39.addWidget(self.label_60)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_5)


        self.horizontalLayout_18.addWidget(self.frame_40)


        self.verticalLayout_38.addWidget(self.frame_38)

        self.stacked_widget.addWidget(self.page_6)
        self.page_home_ = QWidget()
        self.page_home_.setObjectName(u"page_home_")
        self.verticalLayout_2 = QVBoxLayout(self.page_home_)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.frame_continer = QFrame(self.page_home_)
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
        font13 = QFont()
        font13.setPointSize(8)
        self.pushButton_4.setFont(font13)
        self.pushButton_4.setStyleSheet(u"border:none")
        icon15 = QIcon()
        icon15.addFile(u"../../../images/svg_icons/icon_sale.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon15)
        self.pushButton_4.setIconSize(QSize(60, 57))
        self.label_41 = QLabel(self.frame_1)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(75, 40, 71, 28))
        font14 = QFont()
        font14.setFamilies([u"Segoe UI Semibold"])
        font14.setPointSize(14)
        self.label_41.setFont(font14)
        self.label_41.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_42 = QLabel(self.frame_1)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(9, 102, 157, 26))
        font15 = QFont()
        font15.setFamilies([u"Segoe UI Semilight"])
        font15.setPointSize(11)
        self.label_42.setFont(font15)
        self.label_42.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_43 = QLabel(self.frame_1)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(10, 80, 110, 28))
        self.label_43.setFont(font15)
        self.label_43.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_44 = QLabel(self.frame_1)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(120, 80, 84, 28))
        self.label_44.setFont(font15)
        self.label_44.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_45 = QLabel(self.frame_1)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(145, 100, 59, 28))
        self.label_45.setFont(font15)
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
        self.pushButton_6.setFont(font13)
        self.pushButton_6.setStyleSheet(u"border:none")
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QSize(65, 65))
        self.label_46 = QLabel(self.frame_7)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(70, 40, 100, 28))
        self.label_46.setFont(font14)
        self.label_46.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_47 = QLabel(self.frame_7)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(140, 98, 59, 28))
        self.label_47.setFont(font15)
        self.label_47.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_49 = QLabel(self.frame_7)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(11, 78, 110, 28))
        self.label_49.setFont(font15)
        self.label_49.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_50 = QLabel(self.frame_7)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(10, 100, 157, 26))
        self.label_50.setFont(font15)
        self.label_50.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")

        self.horizontalLayout_8.addWidget(self.frame_7)

        self.frame_8 = PyPanelButton(self.scroll_area_widget_contents_home)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(246, 132))
        self.label_48 = QLabel(self.frame_8)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(70, 40, 50, 28))
        self.label_48.setFont(font14)
        self.label_48.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_51 = QLabel(self.frame_8)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(139, 100, 59, 28))
        self.label_51.setFont(font15)
        self.label_51.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_52 = QLabel(self.frame_8)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(9, 102, 157, 26))
        self.label_52.setFont(font15)
        self.label_52.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.pushButton_17 = QPushButton(self.frame_8)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(7, 12, 61, 61))
        self.pushButton_17.setFont(font13)
        self.pushButton_17.setStyleSheet(u"border:none")
        self.pushButton_17.setIcon(icon5)
        self.pushButton_17.setIconSize(QSize(63, 63))
        self.label_53 = QLabel(self.frame_8)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(10, 80, 110, 28))
        self.label_53.setFont(font15)
        self.label_53.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")

        self.horizontalLayout_8.addWidget(self.frame_8)

        self.frame_22 = PyPanelButton(self.scroll_area_widget_contents_home)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(245, 132))
        self.label_54 = QLabel(self.frame_22)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(69, 40, 80, 28))
        self.label_54.setFont(font14)
        self.label_54.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_55 = QLabel(self.frame_22)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(139, 98, 59, 28))
        self.label_55.setFont(font15)
        self.label_55.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.label_55.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_56 = QLabel(self.frame_22)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(9, 100, 157, 26))
        self.label_56.setFont(font15)
        self.label_56.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")
        self.pushButton_18 = QPushButton(self.frame_22)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(8, 13, 61, 61))
        self.pushButton_18.setFont(font13)
        self.pushButton_18.setStyleSheet(u"border:none")
        icon16 = QIcon()
        icon16.addFile(u"../../../images/svg_icons/Icon_receipt_svgrepo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon16)
        self.pushButton_18.setIconSize(QSize(53, 54))
        self.label_57 = QLabel(self.frame_22)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(10, 78, 110, 28))
        self.label_57.setFont(font15)
        self.label_57.setStyleSheet(u"border:none;\n"
"color: #e9eaec;")

        self.horizontalLayout_8.addWidget(self.frame_22)

        self.scroll_area_home.setWidget(self.scroll_area_widget_contents_home)

        self.verticalLayout_6.addWidget(self.scroll_area_home)


        self.verticalLayout_2.addWidget(self.frame_continer)

        self.scroll_area_home_bottom = QScrollArea(self.page_home_)
        self.scroll_area_home_bottom.setObjectName(u"scroll_area_home_bottom")
        self.scroll_area_home_bottom.setWidgetResizable(True)
        self.scroll_area_widget_contents_home_bottom = QWidget()
        self.scroll_area_widget_contents_home_bottom.setObjectName(u"scroll_area_widget_contents_home_bottom")
        self.scroll_area_widget_contents_home_bottom.setGeometry(QRect(0, 0, 632, 400))
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
        font16 = QFont()
        font16.setPointSize(20)
        self.label_12.setFont(font16)
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
        self.label_11.setFont(font16)
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
        self.label_13.setFont(font16)
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
        self.label.setFont(font16)
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
        self.label_8.setFont(font16)
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
        self.label_9.setFont(font16)
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
        self.label_10.setGeometry(QRect(10, 60, 271, 71))
        self.label_10.setFont(font16)
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_4.addWidget(self.frame_9)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.scroll_area_home_bottom.setWidget(self.scroll_area_widget_contents_home_bottom)

        self.verticalLayout_2.addWidget(self.scroll_area_home_bottom)

        self.stacked_widget.addWidget(self.page_home_)
        self.page_inventario = QWidget()
        self.page_inventario.setObjectName(u"page_inventario")
        self.verticalLayout_9 = QVBoxLayout(self.page_inventario)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 7)
        self.frame_char = QFrame(self.page_inventario)
        self.frame_char.setObjectName(u"frame_char")
        self.frame_char.setMinimumSize(QSize(0, 190))
        self.frame_char.setMaximumSize(QSize(16777215, 190))
        self.frame_char.setFrameShape(QFrame.StyledPanel)
        self.frame_char.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_char)
        self.horizontalLayout_9.setSpacing(8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_chart_inventario = QFrame(self.frame_char)
        self.frame_chart_inventario.setObjectName(u"frame_chart_inventario")
        self.frame_chart_inventario.setFrameShape(QFrame.StyledPanel)
        self.frame_chart_inventario.setFrameShadow(QFrame.Raised)
        self.vertical_layout_chart_inevntario = QVBoxLayout(self.frame_chart_inventario)
        self.vertical_layout_chart_inevntario.setSpacing(0)
        self.vertical_layout_chart_inevntario.setObjectName(u"vertical_layout_chart_inevntario")
        self.vertical_layout_chart_inevntario.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_9.addWidget(self.frame_chart_inventario)

        self.frame_circular_progress_bar = QFrame(self.frame_char)
        self.frame_circular_progress_bar.setObjectName(u"frame_circular_progress_bar")
        self.frame_circular_progress_bar.setMinimumSize(QSize(215, 172))
        self.frame_circular_progress_bar.setMaximumSize(QSize(215, 172))
        self.frame_circular_progress_bar.setStyleSheet(u"background-color: rgb(47, 54, 100);")
        self.frame_circular_progress_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_circular_progress_bar.setFrameShadow(QFrame.Raised)
        self.circular_progress_bar = PyCircularProgress(self.frame_circular_progress_bar)
        self.circular_progress_bar.setObjectName(u"circular_progress_bar")
        self.circular_progress_bar.setGeometry(QRect(9, 6, 197, 157))
        self.circular_progress_bar.setMinimumSize(QSize(197, 157))
        self.circular_progress_bar.setMaximumSize(QSize(197, 157))

        self.horizontalLayout_9.addWidget(self.frame_circular_progress_bar)


        self.verticalLayout_9.addWidget(self.frame_char)

        self.frame_nav_busca = QFrame(self.page_inventario)
        self.frame_nav_busca.setObjectName(u"frame_nav_busca")
        self.frame_nav_busca.setMinimumSize(QSize(0, 44))
        self.frame_nav_busca.setMaximumSize(QSize(16777215, 44))
        self.frame_nav_busca.setStyleSheet(u"\n"
"QPushButton {\n"
"    color: rgb(233, 234, 236);\n"
"    background-color: rgb(38, 39, 43);\n"
"    border: none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover \n"
"{\n"
" 	background-color: rgb(49, 50, 55)\n"
" }\n"
"\n"
"QPushButton:pressed \n"
"{\n"
" 	background-color: rgb(38, 39, 43);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: transparent;\n"
"	color: rgb(233, 234, 236);\n"
"	border: 1px solid rgb(47, 54, 100);\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 1px solid rgb(64, 80, 170);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1px solid rgb(89, 109, 235);\n"
"}")
        self.frame_nav_busca.setFrameShape(QFrame.StyledPanel)
        self.frame_nav_busca.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_nav_busca)
        self.horizontalLayout_12.setSpacing(4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(4, 0, 4, 0)
        self.btn_pesquisa_produto = QPushButton(self.frame_nav_busca)
        self.btn_pesquisa_produto.setObjectName(u"btn_pesquisa_produto")
        self.btn_pesquisa_produto.setMinimumSize(QSize(37, 37))
        self.btn_pesquisa_produto.setMaximumSize(QSize(37, 37))
        self.btn_pesquisa_produto.setIcon(icon8)
        self.btn_pesquisa_produto.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.btn_pesquisa_produto)

        self.line_edit_pesquisa_produto = QLineEdit(self.frame_nav_busca)
        self.line_edit_pesquisa_produto.setObjectName(u"line_edit_pesquisa_produto")
        self.line_edit_pesquisa_produto.setMinimumSize(QSize(0, 35))
        self.line_edit_pesquisa_produto.setClearButtonEnabled(False)

        self.horizontalLayout_12.addWidget(self.line_edit_pesquisa_produto)

        self.btn_adicionar_produto = QPushButton(self.frame_nav_busca)
        self.btn_adicionar_produto.setObjectName(u"btn_adicionar_produto")
        self.btn_adicionar_produto.setMinimumSize(QSize(37, 37))
        self.btn_adicionar_produto.setMaximumSize(QSize(37, 37))
        self.btn_adicionar_produto.setIcon(icon11)
        self.btn_adicionar_produto.setIconSize(QSize(35, 35))

        self.horizontalLayout_12.addWidget(self.btn_adicionar_produto)

        self.btn_entrada_produto = QPushButton(self.frame_nav_busca)
        self.btn_entrada_produto.setObjectName(u"btn_entrada_produto")
        self.btn_entrada_produto.setMinimumSize(QSize(37, 37))
        self.btn_entrada_produto.setMaximumSize(QSize(37, 37))
        icon17 = QIcon()
        icon17.addFile(u"../../../images/svg_icons/icon_produt_insert.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_entrada_produto.setIcon(icon17)
        self.btn_entrada_produto.setIconSize(QSize(26, 25))

        self.horizontalLayout_12.addWidget(self.btn_entrada_produto)


        self.verticalLayout_9.addWidget(self.frame_nav_busca)

        self.frame_info_inventario = QFrame(self.page_inventario)
        self.frame_info_inventario.setObjectName(u"frame_info_inventario")
        self.frame_info_inventario.setMinimumSize(QSize(0, 20))
        self.frame_info_inventario.setMaximumSize(QSize(16777215, 20))
        self.frame_info_inventario.setStyleSheet(u"#frame_info_inventario\n"
"{background-color: rgb(19, 20, 22);}\n"
"\n"
"#frame_info_inventario > QLabel\n"
"{background-color: rgb(19, 20, 22); \n"
"color: rgb(255, 255, 255);}")
        self.frame_info_inventario.setFrameShape(QFrame.StyledPanel)
        self.frame_info_inventario.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_info_inventario)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(10, 0, 10, 0)
        self.lbl_nome_n = QLabel(self.frame_info_inventario)
        self.lbl_nome_n.setObjectName(u"lbl_nome_n")
        self.lbl_nome_n.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.lbl_nome_n)

        self.lbl_nome_inventario = QLabel(self.frame_info_inventario)
        self.lbl_nome_inventario.setObjectName(u"lbl_nome_inventario")
        self.lbl_nome_inventario.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lbl_nome_inventario)

        self.lbl_quantidade = QLabel(self.frame_info_inventario)
        self.lbl_quantidade.setObjectName(u"lbl_quantidade")
        self.lbl_quantidade.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lbl_quantidade)

        self.lbl_venda_inventario = QLabel(self.frame_info_inventario)
        self.lbl_venda_inventario.setObjectName(u"lbl_venda_inventario")
        self.lbl_venda_inventario.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lbl_venda_inventario)


        self.verticalLayout_9.addWidget(self.frame_info_inventario)

        self.frame_border = QFrame(self.page_inventario)
        self.frame_border.setObjectName(u"frame_border")
        self.frame_border.setFrameShape(QFrame.StyledPanel)
        self.frame_border.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_border)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(4, 4, 4, 4)
        self.frame_continer_border = QFrame(self.frame_border)
        self.frame_continer_border.setObjectName(u"frame_continer_border")
        self.frame_continer_border.setStyleSheet(u"background-color: rgb(19, 20, 22);")
        self.frame_continer_border.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_border.setFrameShadow(QFrame.Raised)
        self.vertical_layout_inventario = QVBoxLayout(self.frame_continer_border)
        self.vertical_layout_inventario.setSpacing(0)
        self.vertical_layout_inventario.setObjectName(u"vertical_layout_inventario")
        self.vertical_layout_inventario.setContentsMargins(5, 5, 5, 5)
        self.scroll_area_list_regitro_inventario = QScrollArea(self.frame_continer_border)
        self.scroll_area_list_regitro_inventario.setObjectName(u"scroll_area_list_regitro_inventario")
        sizePolicy.setHeightForWidth(self.scroll_area_list_regitro_inventario.sizePolicy().hasHeightForWidth())
        self.scroll_area_list_regitro_inventario.setSizePolicy(sizePolicy)
        self.scroll_area_list_regitro_inventario.setStyleSheet(u"background-color: rgb(19, 20, 22);")
        self.scroll_area_list_regitro_inventario.setWidgetResizable(True)
        self.scroll_area_widget_contents_inventario = QWidget()
        self.scroll_area_widget_contents_inventario.setObjectName(u"scroll_area_widget_contents_inventario")
        self.scroll_area_widget_contents_inventario.setGeometry(QRect(0, 0, 622, 209))
        self.vertical_layout_registro = QVBoxLayout(self.scroll_area_widget_contents_inventario)
        self.vertical_layout_registro.setObjectName(u"vertical_layout_registro")
        self.vertical_layout_registro.setContentsMargins(2, 3, 2, 3)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vertical_layout_registro.addItem(self.verticalSpacer_2)

        self.scroll_area_list_regitro_inventario.setWidget(self.scroll_area_widget_contents_inventario)

        self.vertical_layout_inventario.addWidget(self.scroll_area_list_regitro_inventario)


        self.verticalLayout_10.addWidget(self.frame_continer_border)


        self.verticalLayout_9.addWidget(self.frame_border)

        self.stacked_widget.addWidget(self.page_inventario)
        self.page_venda = QWidget()
        self.page_venda.setObjectName(u"page_venda")
        self.verticalLayout_19 = QVBoxLayout(self.page_venda)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(7, 7, 7, 7)
        self.frame_nav_continer_venda = QFrame(self.page_venda)
        self.frame_nav_continer_venda.setObjectName(u"frame_nav_continer_venda")
        self.frame_nav_continer_venda.setMinimumSize(QSize(0, 179))
        self.frame_nav_continer_venda.setMaximumSize(QSize(16777215, 179))
        self.frame_nav_continer_venda.setStyleSheet(u"background-color: rgb(54, 63, 118);")
        self.frame_nav_continer_venda.setFrameShape(QFrame.StyledPanel)
        self.frame_nav_continer_venda.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_nav_continer_venda)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_historico_de_venda = QFrame(self.frame_nav_continer_venda)
        self.frame_historico_de_venda.setObjectName(u"frame_historico_de_venda")
        self.frame_historico_de_venda.setMinimumSize(QSize(151, 161))
        self.frame_historico_de_venda.setMaximumSize(QSize(123456, 123456))
        self.frame_historico_de_venda.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(32, 33, 37, 200);\n"
"	background-image: url(none);}\n"
"\n"
"QFrame:hover\n"
"{border: 0.5px solid rgba(255, 255, 255, 80)}")
        self.frame_historico_de_venda.setFrameShape(QFrame.StyledPanel)
        self.frame_historico_de_venda.setFrameShadow(QFrame.Raised)
        self.btn_logo_historico_de_venda = QPushButton(self.frame_historico_de_venda)
        self.btn_logo_historico_de_venda.setObjectName(u"btn_logo_historico_de_venda")
        self.btn_logo_historico_de_venda.setGeometry(QRect(18, 25, 51, 55))
        self.btn_logo_historico_de_venda.setStyleSheet(u"background-color: transparent")
        icon18 = QIcon()
        icon18.addFile(u"../../../images/svg_icons/icon_clipboar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logo_historico_de_venda.setIcon(icon18)
        self.btn_logo_historico_de_venda.setIconSize(QSize(63, 63))
        self.lbl_venda_historico_de_venda = QLabel(self.frame_historico_de_venda)
        self.lbl_venda_historico_de_venda.setObjectName(u"lbl_venda_historico_de_venda")
        self.lbl_venda_historico_de_venda.setGeometry(QRect(20, 90, 131, 16))
        self.lbl_venda_historico_de_venda.setFont(font3)
        self.lbl_venda_historico_de_venda.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border:none;")
        self.btn_log_extra_historico_de_venda = QPushButton(self.frame_historico_de_venda)
        self.btn_log_extra_historico_de_venda.setObjectName(u"btn_log_extra_historico_de_venda")
        self.btn_log_extra_historico_de_venda.setGeometry(QRect(128, 137, 20, 20))
        self.btn_log_extra_historico_de_venda.setStyleSheet(u"background-color: transparent")
        self.btn_log_extra_historico_de_venda.setIcon(icon3)
        self.btn_log_extra_historico_de_venda.setIconSize(QSize(20, 20))
        self.lbl_info_historico_de_venda = QLabel(self.frame_historico_de_venda)
        self.lbl_info_historico_de_venda.setObjectName(u"lbl_info_historico_de_venda")
        self.lbl_info_historico_de_venda.setGeometry(QRect(22, 140, 50, 10))
        self.lbl_info_historico_de_venda.setFont(font4)
        self.lbl_info_historico_de_venda.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_historico_de_venda.setScaledContents(False)
        self.lbl_info_historico_de_venda_2 = QLabel(self.frame_historico_de_venda)
        self.lbl_info_historico_de_venda_2.setObjectName(u"lbl_info_historico_de_venda_2")
        self.lbl_info_historico_de_venda_2.setGeometry(QRect(22, 112, 90, 10))
        self.lbl_info_historico_de_venda_2.setFont(font4)
        self.lbl_info_historico_de_venda_2.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_historico_de_venda_2.setScaledContents(False)
        self.lbl_info_historico_de_venda_3 = QLabel(self.frame_historico_de_venda)
        self.lbl_info_historico_de_venda_3.setObjectName(u"lbl_info_historico_de_venda_3")
        self.lbl_info_historico_de_venda_3.setGeometry(QRect(22, 126, 110, 10))
        self.lbl_info_historico_de_venda_3.setFont(font4)
        self.lbl_info_historico_de_venda_3.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_historico_de_venda_3.setScaledContents(False)
        self.btn_logo_historico_de_venda_ = QPushButton(self.frame_historico_de_venda)
        self.btn_logo_historico_de_venda_.setObjectName(u"btn_logo_historico_de_venda_")
        self.btn_logo_historico_de_venda_.setGeometry(QRect(48, 56, 24, 24))
        self.btn_logo_historico_de_venda_.setStyleSheet(u"background-color: transparent")
        self.btn_logo_historico_de_venda_.setIcon(icon4)
        self.btn_logo_historico_de_venda_.setIconSize(QSize(24, 24))

        self.horizontalLayout_23.addWidget(self.frame_historico_de_venda)

        self.frame_recibo_venda = QFrame(self.frame_nav_continer_venda)
        self.frame_recibo_venda.setObjectName(u"frame_recibo_venda")
        self.frame_recibo_venda.setMinimumSize(QSize(151, 161))
        self.frame_recibo_venda.setMaximumSize(QSize(123456, 123456))
        self.frame_recibo_venda.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(32, 33, 37, 200);\n"
"	background-image: url(none);}\n"
"\n"
"QFrame:hover\n"
"{border: 0.5px solid rgba(255, 255, 255, 80)}")
        self.frame_recibo_venda.setFrameShape(QFrame.StyledPanel)
        self.frame_recibo_venda.setFrameShadow(QFrame.Raised)
        self.btn_logo_recibo_venda = QPushButton(self.frame_recibo_venda)
        self.btn_logo_recibo_venda.setObjectName(u"btn_logo_recibo_venda")
        self.btn_logo_recibo_venda.setGeometry(QRect(18, 26, 52, 52))
        self.btn_logo_recibo_venda.setStyleSheet(u"background-color: transparent")
        self.btn_logo_recibo_venda.setIcon(icon6)
        self.btn_logo_recibo_venda.setIconSize(QSize(80, 80))
        self.lbl_recibo_venda = QLabel(self.frame_recibo_venda)
        self.lbl_recibo_venda.setObjectName(u"lbl_recibo_venda")
        self.lbl_recibo_venda.setGeometry(QRect(20, 90, 50, 16))
        self.lbl_recibo_venda.setFont(font3)
        self.lbl_recibo_venda.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_extra_recibo_venda = QLabel(self.frame_recibo_venda)
        self.lbl_info_extra_recibo_venda.setObjectName(u"lbl_info_extra_recibo_venda")
        self.lbl_info_extra_recibo_venda.setGeometry(QRect(22, 112, 110, 10))
        self.lbl_info_extra_recibo_venda.setFont(font4)
        self.lbl_info_extra_recibo_venda.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_extra_recibo_venda.setScaledContents(False)
        self.btn_log_extra_recibo_venda = QPushButton(self.frame_recibo_venda)
        self.btn_log_extra_recibo_venda.setObjectName(u"btn_log_extra_recibo_venda")
        self.btn_log_extra_recibo_venda.setGeometry(QRect(128, 137, 20, 20))
        self.btn_log_extra_recibo_venda.setStyleSheet(u"background-color: transparent")
        self.btn_log_extra_recibo_venda.setIcon(icon3)
        self.btn_log_extra_recibo_venda.setIconSize(QSize(20, 20))
        self.lbl_info_extra_recibo_venda_2 = QLabel(self.frame_recibo_venda)
        self.lbl_info_extra_recibo_venda_2.setObjectName(u"lbl_info_extra_recibo_venda_2")
        self.lbl_info_extra_recibo_venda_2.setGeometry(QRect(22, 126, 110, 10))
        self.lbl_info_extra_recibo_venda_2.setFont(font4)
        self.lbl_info_extra_recibo_venda_2.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_extra_recibo_venda_2.setScaledContents(False)
        self.lbl_info_extra_recibo_venda_3 = QLabel(self.frame_recibo_venda)
        self.lbl_info_extra_recibo_venda_3.setObjectName(u"lbl_info_extra_recibo_venda_3")
        self.lbl_info_extra_recibo_venda_3.setGeometry(QRect(22, 140, 90, 10))
        self.lbl_info_extra_recibo_venda_3.setFont(font4)
        self.lbl_info_extra_recibo_venda_3.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_extra_recibo_venda_3.setScaledContents(False)

        self.horizontalLayout_23.addWidget(self.frame_recibo_venda)

        self.frame_criar_produto = QFrame(self.frame_nav_continer_venda)
        self.frame_criar_produto.setObjectName(u"frame_criar_produto")
        self.frame_criar_produto.setMinimumSize(QSize(151, 161))
        self.frame_criar_produto.setMaximumSize(QSize(123456, 123456))
        self.frame_criar_produto.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(32, 33, 37, 200);\n"
"	background-image: url(none);}\n"
"\n"
"QFrame:hover\n"
"{border: 0.5px solid rgba(255, 255, 255, 80)}")
        self.frame_criar_produto.setFrameShape(QFrame.StyledPanel)
        self.frame_criar_produto.setFrameShadow(QFrame.Raised)
        self.btn_logo_criar_produto = QPushButton(self.frame_criar_produto)
        self.btn_logo_criar_produto.setObjectName(u"btn_logo_criar_produto")
        self.btn_logo_criar_produto.setGeometry(QRect(18, 25, 56, 56))
        self.btn_logo_criar_produto.setStyleSheet(u"background-color: transparent")
        icon19 = QIcon()
        icon19.addFile(u"../../../images/svg_icons/icon_existinginventory.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logo_criar_produto.setIcon(icon19)
        self.btn_logo_criar_produto.setIconSize(QSize(55, 55))
        self.lbl_criar_produto = QLabel(self.frame_criar_produto)
        self.lbl_criar_produto.setObjectName(u"lbl_criar_produto")
        self.lbl_criar_produto.setGeometry(QRect(20, 90, 91, 16))
        self.lbl_criar_produto.setFont(font3)
        self.lbl_criar_produto.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_criar_produto = QLabel(self.frame_criar_produto)
        self.lbl_info_criar_produto.setObjectName(u"lbl_info_criar_produto")
        self.lbl_info_criar_produto.setGeometry(QRect(22, 112, 101, 10))
        self.lbl_info_criar_produto.setFont(font4)
        self.lbl_info_criar_produto.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_criar_produto.setScaledContents(False)
        self.btn_log_extra_criar_produto = QPushButton(self.frame_criar_produto)
        self.btn_log_extra_criar_produto.setObjectName(u"btn_log_extra_criar_produto")
        self.btn_log_extra_criar_produto.setGeometry(QRect(128, 137, 20, 20))
        self.btn_log_extra_criar_produto.setStyleSheet(u"background-color: transparent")
        self.btn_log_extra_criar_produto.setIcon(icon3)
        self.btn_log_extra_criar_produto.setIconSize(QSize(20, 20))
        self.lbl_info_criar_produto_2 = QLabel(self.frame_criar_produto)
        self.lbl_info_criar_produto_2.setObjectName(u"lbl_info_criar_produto_2")
        self.lbl_info_criar_produto_2.setGeometry(QRect(22, 126, 111, 10))
        self.lbl_info_criar_produto_2.setFont(font4)
        self.lbl_info_criar_produto_2.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_criar_produto_2.setScaledContents(False)
        self.lbl_info_criar_produto_3 = QLabel(self.frame_criar_produto)
        self.lbl_info_criar_produto_3.setObjectName(u"lbl_info_criar_produto_3")
        self.lbl_info_criar_produto_3.setGeometry(QRect(22, 140, 50, 10))
        self.lbl_info_criar_produto_3.setFont(font4)
        self.lbl_info_criar_produto_3.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_criar_produto_3.setScaledContents(False)

        self.horizontalLayout_23.addWidget(self.frame_criar_produto)

        self.frame_pedido_de_compra = QFrame(self.frame_nav_continer_venda)
        self.frame_pedido_de_compra.setObjectName(u"frame_pedido_de_compra")
        self.frame_pedido_de_compra.setMinimumSize(QSize(151, 161))
        self.frame_pedido_de_compra.setMaximumSize(QSize(123456, 123456))
        self.frame_pedido_de_compra.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(32, 33, 37, 200);\n"
"	background-image: url(none);}\n"
"\n"
"QFrame:hover\n"
"{border: 0.5px solid rgba(255, 255, 255, 80)}")
        self.frame_pedido_de_compra.setFrameShape(QFrame.StyledPanel)
        self.frame_pedido_de_compra.setFrameShadow(QFrame.Raised)
        self.btn_logo_pedido_de_compra = QPushButton(self.frame_pedido_de_compra)
        self.btn_logo_pedido_de_compra.setObjectName(u"btn_logo_pedido_de_compra")
        self.btn_logo_pedido_de_compra.setGeometry(QRect(18, 25, 52, 55))
        self.btn_logo_pedido_de_compra.setStyleSheet(u"background-color: transparent")
        icon20 = QIcon()
        icon20.addFile(u"../../../images/svg_icons/icon_receipt.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logo_pedido_de_compra.setIcon(icon20)
        self.btn_logo_pedido_de_compra.setIconSize(QSize(48, 48))
        self.lbl_pedido_de_compra = QLabel(self.frame_pedido_de_compra)
        self.lbl_pedido_de_compra.setObjectName(u"lbl_pedido_de_compra")
        self.lbl_pedido_de_compra.setGeometry(QRect(20, 90, 131, 16))
        self.lbl_pedido_de_compra.setFont(font3)
        self.lbl_pedido_de_compra.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.lbl_info_pedido_de_compra = QLabel(self.frame_pedido_de_compra)
        self.lbl_info_pedido_de_compra.setObjectName(u"lbl_info_pedido_de_compra")
        self.lbl_info_pedido_de_compra.setGeometry(QRect(22, 112, 70, 10))
        self.lbl_info_pedido_de_compra.setFont(font4)
        self.lbl_info_pedido_de_compra.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_pedido_de_compra.setScaledContents(False)
        self.btn_log_extra_pedido_de_compra = QPushButton(self.frame_pedido_de_compra)
        self.btn_log_extra_pedido_de_compra.setObjectName(u"btn_log_extra_pedido_de_compra")
        self.btn_log_extra_pedido_de_compra.setGeometry(QRect(128, 137, 20, 20))
        self.btn_log_extra_pedido_de_compra.setStyleSheet(u"background-color: transparent")
        self.btn_log_extra_pedido_de_compra.setIcon(icon3)
        self.btn_log_extra_pedido_de_compra.setIconSize(QSize(20, 20))
        self.lbl_info_pedido_de_compra_2 = QLabel(self.frame_pedido_de_compra)
        self.lbl_info_pedido_de_compra_2.setObjectName(u"lbl_info_pedido_de_compra_2")
        self.lbl_info_pedido_de_compra_2.setGeometry(QRect(22, 126, 90, 10))
        self.lbl_info_pedido_de_compra_2.setFont(font4)
        self.lbl_info_pedido_de_compra_2.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent")
        self.lbl_info_pedido_de_compra_2.setScaledContents(False)

        self.horizontalLayout_23.addWidget(self.frame_pedido_de_compra)


        self.verticalLayout_19.addWidget(self.frame_nav_continer_venda)

        self.frame_barra_busca = QFrame(self.page_venda)
        self.frame_barra_busca.setObjectName(u"frame_barra_busca")
        self.frame_barra_busca.setMinimumSize(QSize(0, 44))
        self.frame_barra_busca.setMaximumSize(QSize(16777215, 44))
        self.frame_barra_busca.setStyleSheet(u"background-color: rgb(32, 33, 37)")
        self.frame_barra_busca.setFrameShape(QFrame.StyledPanel)
        self.frame_barra_busca.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_barra_busca)
        self.horizontalLayout_25.setSpacing(4)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(4, 0, 4, 0)
        self.btn_pesquisa_produto_de_venda = QPushButton(self.frame_barra_busca)
        self.btn_pesquisa_produto_de_venda.setObjectName(u"btn_pesquisa_produto_de_venda")
        self.btn_pesquisa_produto_de_venda.setMinimumSize(QSize(37, 37))
        self.btn_pesquisa_produto_de_venda.setMaximumSize(QSize(37, 37))
        self.btn_pesquisa_produto_de_venda.setStyleSheet(u"QPushButton {\n"
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
        self.btn_pesquisa_produto_de_venda.setIcon(icon8)
        self.btn_pesquisa_produto_de_venda.setIconSize(QSize(25, 25))

        self.horizontalLayout_25.addWidget(self.btn_pesquisa_produto_de_venda)

        self.line_edit_pesquisa_produto_devenda = QLineEdit(self.frame_barra_busca)
        self.line_edit_pesquisa_produto_devenda.setObjectName(u"line_edit_pesquisa_produto_devenda")
        self.line_edit_pesquisa_produto_devenda.setMinimumSize(QSize(0, 35))
        self.line_edit_pesquisa_produto_devenda.setStyleSheet(u"QLineEdit{\n"
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
        self.line_edit_pesquisa_produto_devenda.setClearButtonEnabled(False)

        self.horizontalLayout_25.addWidget(self.line_edit_pesquisa_produto_devenda)

        self.btn_mais_opcoes_de_venda = QPushButton(self.frame_barra_busca)
        self.btn_mais_opcoes_de_venda.setObjectName(u"btn_mais_opcoes_de_venda")
        self.btn_mais_opcoes_de_venda.setMinimumSize(QSize(37, 37))
        self.btn_mais_opcoes_de_venda.setMaximumSize(QSize(37, 37))
        self.btn_mais_opcoes_de_venda.setStyleSheet(u"QPushButton {\n"
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
        self.btn_mais_opcoes_de_venda.setIcon(icon10)
        self.btn_mais_opcoes_de_venda.setIconSize(QSize(25, 25))

        self.horizontalLayout_25.addWidget(self.btn_mais_opcoes_de_venda)


        self.verticalLayout_19.addWidget(self.frame_barra_busca)

        self.frame_30 = QFrame(self.page_venda)
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
        self.vertical_layout_inventario_2.setContentsMargins(5, 5, 5, 5)
        self.scrollArea_3 = QScrollArea(self.frame_57)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setStyleSheet(u"background-color: rgb(19, 20, 22);\n"
"border-radius: 10px;")
        self.scrollArea_3.setWidgetResizable(True)
        self.scroll_area_widget_contents_venda = QWidget()
        self.scroll_area_widget_contents_venda.setObjectName(u"scroll_area_widget_contents_venda")
        self.scroll_area_widget_contents_venda.setGeometry(QRect(0, 0, 626, 248))
        self.vertical_layout_venda = QVBoxLayout(self.scroll_area_widget_contents_venda)
        self.vertical_layout_venda.setObjectName(u"vertical_layout_venda")
        self.vertical_layout_venda.setContentsMargins(2, 3, 2, 3)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vertical_layout_venda.addItem(self.verticalSpacer_7)

        self.scrollArea_3.setWidget(self.scroll_area_widget_contents_venda)

        self.vertical_layout_inventario_2.addWidget(self.scrollArea_3)


        self.verticalLayout_18.addWidget(self.frame_57)


        self.verticalLayout_19.addWidget(self.frame_30)

        self.stacked_widget.addWidget(self.page_venda)

        self.horizontalLayout.addWidget(self.stacked_widget)


        self.verticalLayout.addWidget(self.frame_base)


        self.horizontalLayout_2.addWidget(self.central_frame)


        self.vertical_layout_frame_line.addWidget(self.central_widget)


        self.horizontal_layout_back_ground_frame_line.addWidget(self.frame_line)


        self.horizontal_layout_widget_style_sheet.addWidget(self.back_ground_frame_line)

        MainWindow.setCentralWidget(self.widget_style_sheet)

        self.retranslateUi(MainWindow)

        self.stacked_widget.setCurrentIndex(6)
        self.stackedWidget_4.setCurrentIndex(1)


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
        self.btn_logo_inventario_3.setText("")
        self.lbl_inventario_3.setText(QCoreApplication.translate("MainWindow", u"Inventario", None))
        self.lbl_info_inventario_5.setText(QCoreApplication.translate("MainWindow", u"Gerencie eficientemente ", None))
        self.lbl_info_inventario_6.setText(QCoreApplication.translate("MainWindow", u"o seu Inventario", None))
        self.btn_logo_venda_3.setText("")
        self.lbl_venda_3.setText(QCoreApplication.translate("MainWindow", u"Venda", None))
        self.lbl_info_venda_7.setText(QCoreApplication.translate("MainWindow", u"clientes fi\u00e9is", None))
        self.lbl_info_venda_8.setText(QCoreApplication.translate("MainWindow", u"Aprimore a experi\u00eancia", None))
        self.lbl_info_venda_9.setText(QCoreApplication.translate("MainWindow", u"de compra para garantir", None))
        self.btn_logo_perda_3.setText("")
        self.lbl_perda_3.setText(QCoreApplication.translate("MainWindow", u"Perda", None))
        self.lbl_info_perda_7.setText(QCoreApplication.translate("MainWindow", u"Gerencie efetivamente", None))
        self.lbl_info_perda_8.setText(QCoreApplication.translate("MainWindow", u"as perdas para maximizar", None))
        self.lbl_info_perda_9.setText(QCoreApplication.translate("MainWindow", u"os lucros", None))
        self.btn_logo_recibo_3.setText("")
        self.lbl_recibo_3.setText(QCoreApplication.translate("MainWindow", u"Recibo", None))
        self.lbl_info_extra_recibo_7.setText(QCoreApplication.translate("MainWindow", u"Crie recibos personalizados", None))
        self.lbl_info_extra_recibo_8.setText(QCoreApplication.translate("MainWindow", u"para uma experi\u00eancia do", None))
        self.lbl_info_extra_recibo_9.setText(QCoreApplication.translate("MainWindow", u"cliente excepcional", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"NdDaniel", None))
        self.pushButton.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Total de Usuario", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Vers\u00e3o", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"0.4.0", None))
        self.btn_pesquisa_historico_de_venda.setText("")
        self.btn_mais_opcoes_historico_de_venda.setText("")
        ___qtablewidgetitem = self.tabela_widget_de_historico_de_venda.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"N\u00ba", None));
        ___qtablewidgetitem1 = self.tabela_widget_de_historico_de_venda.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem2 = self.tabela_widget_de_historico_de_venda.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Chave", None));
        ___qtablewidgetitem3 = self.tabela_widget_de_historico_de_venda.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem4 = self.tabela_widget_de_historico_de_venda.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Categoria", None));
        ___qtablewidgetitem5 = self.tabela_widget_de_historico_de_venda.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem6 = self.tabela_widget_de_historico_de_venda.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Unidade", None));
        ___qtablewidgetitem7 = self.tabela_widget_de_historico_de_venda.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtablewidgetitem8 = self.tabela_widget_de_historico_de_venda.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Desconto", None));
        ___qtablewidgetitem9 = self.tabela_widget_de_historico_de_venda.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Troco", None));
        ___qtablewidgetitem10 = self.tabela_widget_de_historico_de_venda.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem11 = self.tabela_widget_de_historico_de_venda.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Vendedor", None));
        ___qtablewidgetitem12 = self.tabela_widget_de_historico_de_venda.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem13 = self.tabela_widget_de_historico_de_venda.verticalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tabela_widget_de_historico_de_venda.verticalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tabela_widget_de_historico_de_venda.verticalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tabela_widget_de_historico_de_venda.verticalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tabela_widget_de_historico_de_venda.verticalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tabela_widget_de_historico_de_venda.verticalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tabela_widget_de_historico_de_venda.verticalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem20 = self.tabela_widget_de_historico_de_venda.verticalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem21 = self.tabela_widget_de_historico_de_venda.verticalHeaderItem(8)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Selecione uma nova conta", None))
        self.btn_pesquisa_produto_2.setText("")
        self.btn_mais_opcoes_27.setText("")
        self.btn_adicionar_produto_2.setText("")
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_img_22.setText("")
        self.nome_produto_22.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_22.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_50.setText("")
        self.nome_produto_50.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_50.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_44.setText("")
        self.nome_produto_44.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_44.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_52.setText("")
        self.nome_produto_52.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_52.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_25.setText("")
        self.nome_produto_25.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_25.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_43.setText("")
        self.nome_produto_43.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_43.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_51.setText("")
        self.nome_produto_51.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_51.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_53.setText("")
        self.nome_produto_53.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_53.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_2.setText("")
        self.nome_produto_2.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_2.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_42.setText("")
        self.nome_produto_42.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_42.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_55.setText("")
        self.nome_produto_55.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_55.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_46.setText("")
        self.nome_produto_46.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_46.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_45.setText("")
        self.nome_produto_45.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_45.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_41.setText("")
        self.nome_produto_41.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_41.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_54.setText("")
        self.nome_produto_54.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_54.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_49.setText("")
        self.nome_produto_49.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_49.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_48.setText("")
        self.nome_produto_48.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_48.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.icon_img_47.setText("")
        self.nome_produto_47.setText(QCoreApplication.translate("MainWindow", u"Coca Cola", None))
        self.chave_47.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.btn_logo_inventario.setText("")
        self.lbl_inventario.setText(QCoreApplication.translate("MainWindow", u"Inventario", None))
        self.lbl_info_inventario_1.setText(QCoreApplication.translate("MainWindow", u"Gerencie eficientemente ", None))
        self.lbl_info_inventario_2.setText(QCoreApplication.translate("MainWindow", u"o seu Inventario", None))
        self.btn_logo_venda.setText("")
        self.lbl_venda.setText(QCoreApplication.translate("MainWindow", u"Venda", None))
        self.lbl_info_venda_3.setText(QCoreApplication.translate("MainWindow", u"clientes fi\u00e9is", None))
        self.lbl_info_venda_1.setText(QCoreApplication.translate("MainWindow", u"Aprimore a experi\u00eancia", None))
        self.lbl_info_venda_2.setText(QCoreApplication.translate("MainWindow", u"de compra para garantir", None))
        self.btn_logo_perda.setText("")
        self.lbl_perda.setText(QCoreApplication.translate("MainWindow", u"Perda", None))
        self.lbl_info_perda_1.setText(QCoreApplication.translate("MainWindow", u"Gerencie efetivamente", None))
        self.lbl_info_perda_2.setText(QCoreApplication.translate("MainWindow", u"as perdas para maximizar", None))
        self.lbl_info_perda_3.setText(QCoreApplication.translate("MainWindow", u"os lucros", None))
        self.btn_logo_recibo.setText("")
        self.lbl_recibo.setText(QCoreApplication.translate("MainWindow", u"Recibo", None))
        self.lbl_info_extra_recibo_1.setText(QCoreApplication.translate("MainWindow", u"Crie recibos personalizados", None))
        self.lbl_info_extra_recibo_2.setText(QCoreApplication.translate("MainWindow", u"para uma experi\u00eancia do", None))
        self.lbl_info_extra_recibo_3.setText(QCoreApplication.translate("MainWindow", u"cliente excepcional", None))
        self.icon_img_29.setText("")
        self.nome_produto_32.setText(QCoreApplication.translate("MainWindow", u"Nd Daniel", None))
        self.chave_33.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.icon_img_28.setText("")
        self.nome_produto_31.setText(QCoreApplication.translate("MainWindow", u"Tati", None))
        self.chave_32.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.icon_img_30.setText("")
        self.nome_produto_28.setText(QCoreApplication.translate("MainWindow", u"Jo\u00e3o", None))
        self.chave_34.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.pushButton_7.setText("")
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"A express\u00e3o Lorem ipsum", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"A express\u00e3o Lorem ipsum em design gr\u00e1fico e editora\u00e7\u00e3o \u00e9 um texto padr\u00e3o em latim utilizado na produ\u00e7\u00e3o gr\u00e1fica para preencher os espa\u00e7os de texto em publica\u00e7\u00f5es.", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Em documentos utilizados para testes, este tipo", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Enter your wallet adress *", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Enter wallet adress *", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Adress", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Tag (opcional)", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"You may enter  wallet's screen name here", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es ", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"A express\u00e3o Lorem ipsum em design gr\u00e1fico e editora\u00e7\u00e3o \u00e9 um texto padr\u00e3o em latim utilizado na produ\u00e7\u00e3o gr\u00e1fica para preencher os espa\u00e7os de texto em publica\u00e7\u00f5es (jornais, revistas, e sites) para testar e ajustar aspectos visuais (layout, tipografia, formata\u00e7\u00e3o, etc.) antes de utilizar conte\u00fado real. Tamb\u00e9m \u00e9 utilizado em cat\u00e1logos tipogr\u00e1ficos, para demonstrar textos e t\u00edtulos escritos com as fontes.[1]\n"
"\n"
"Composi\u00e7\u00e3o\n"
"Em sua forma mais comum, o texto \u00e9 como se segue:\n"
"\n"
"\"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla at risus. Quisque purus magna, auctor et, sagittis ac, posuere eu, lectus. Nam mattis, felis ut adipiscing.\"\n"
"Nos pa\u00edses de l\u00edngua inglesa o texto apresenta-se em for"
                        "ma um pouco diferente, apresentada a seguir:\n"
"\n"
"\"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"", None))
        self.pushButton_4.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Venda", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Numero de vendas", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Total de Venda", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"14,4k", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.pushButton_6.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Inventario", None))
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
        self.btn_pesquisa_produto.setText("")
        self.btn_adicionar_produto.setText("")
        self.btn_entrada_produto.setText("")
        self.lbl_nome_n.setText(QCoreApplication.translate("MainWindow", u"               N\u00ba/Nome", None))
        self.lbl_nome_inventario.setText(QCoreApplication.translate("MainWindow", u"       Valor total/Percentual", None))
        self.lbl_quantidade.setText(QCoreApplication.translate("MainWindow", u"Quantidade       ", None))
        self.lbl_venda_inventario.setText(QCoreApplication.translate("MainWindow", u"Venda                      ", None))
        self.btn_logo_historico_de_venda.setText("")
        self.lbl_venda_historico_de_venda.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico de venda", None))
        self.lbl_info_historico_de_venda.setText(QCoreApplication.translate("MainWindow", u"clientes fi\u00e9is", None))
        self.lbl_info_historico_de_venda_2.setText(QCoreApplication.translate("MainWindow", u"Aprimore a experi\u00eancia", None))
        self.lbl_info_historico_de_venda_3.setText(QCoreApplication.translate("MainWindow", u"de compra para garantir", None))
        self.btn_logo_historico_de_venda_.setText("")
        self.btn_logo_recibo_venda.setText("")
        self.lbl_recibo_venda.setText(QCoreApplication.translate("MainWindow", u"Recibo", None))
        self.lbl_info_extra_recibo_venda.setText(QCoreApplication.translate("MainWindow", u"Crie recibos personalizados", None))
        self.lbl_info_extra_recibo_venda_2.setText(QCoreApplication.translate("MainWindow", u"para uma experi\u00eancia do", None))
        self.lbl_info_extra_recibo_venda_3.setText(QCoreApplication.translate("MainWindow", u"cliente excepcional", None))
        self.btn_logo_criar_produto.setText("")
        self.lbl_criar_produto.setText(QCoreApplication.translate("MainWindow", u"Criar produto", None))
        self.lbl_info_criar_produto.setText(QCoreApplication.translate("MainWindow", u"Gerencie efetivamente", None))
        self.lbl_info_criar_produto_2.setText(QCoreApplication.translate("MainWindow", u"as perdas para maximizar", None))
        self.lbl_info_criar_produto_3.setText(QCoreApplication.translate("MainWindow", u"os lucros", None))
        self.btn_logo_pedido_de_compra.setText("")
        self.lbl_pedido_de_compra.setText(QCoreApplication.translate("MainWindow", u"Pedido de compra", None))
        self.lbl_info_pedido_de_compra.setText(QCoreApplication.translate("MainWindow", u"Gerencie eficientemente ", None))
        self.lbl_info_pedido_de_compra_2.setText(QCoreApplication.translate("MainWindow", u"o seu Inventario", None))
        self.btn_pesquisa_produto_de_venda.setText("")
        self.btn_mais_opcoes_de_venda.setText("")
    # retranslateUi

