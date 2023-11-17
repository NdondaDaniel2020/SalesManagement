# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerBIKxTp.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from src.gui.widgets.py_push_button.py_push_button import PyPushButton

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(100, 541)
        self.vertical_layout_left_menu = QVBoxLayout(Form)
        self.vertical_layout_left_menu.setSpacing(0)
        self.vertical_layout_left_menu.setObjectName(u"vertical_layout_left_menu")
        self.vertical_layout_left_menu.setContentsMargins(0, 0, 0, 0)
        self.continer_left_menu = QFrame(Form)
        self.continer_left_menu.setObjectName(u"continer_left_menu")
        self.continer_left_menu.setMinimumSize(QSize(45, 0))
        self.continer_left_menu.setMaximumSize(QSize(45, 16777215))
        self.continer_left_menu.setStyleSheet(u"")
        self.continer_left_menu.setFrameShape(QFrame.StyledPanel)
        self.continer_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.continer_left_menu)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu_top_2 = QFrame(self.continer_left_menu)
        self.frame_left_menu_top_2.setObjectName(u"frame_left_menu_top_2")
        self.frame_left_menu_top_2.setStyleSheet(u"")
        self.frame_left_menu_top_2.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu_top_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu_top_2)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(1, 0, 5, 0)
        self.btn_menu_4 = PyPushButton(self.frame_left_menu_top_2)
        self.btn_menu_4.setObjectName(u"btn_menu_4")
        self.btn_menu_4.setMinimumSize(QSize(37, 37))
        self.btn_menu_4.setMaximumSize(QSize(1234, 37))
        icon = QIcon()
        icon.addFile(u"../../../../src/gui/images/svg_icons/icon_back.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_4.setIcon(icon)
        self.btn_menu_4.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.btn_menu_4)

        self.btn_menu_2 = PyPushButton(self.frame_left_menu_top_2)
        self.btn_menu_2.setObjectName(u"btn_menu_2")
        self.btn_menu_2.setMinimumSize(QSize(37, 37))
        self.btn_menu_2.setMaximumSize(QSize(1234, 37))
        icon1 = QIcon()
        icon1.addFile(u"../../../../src/gui/images/svg_icons/icon_menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_2.setIcon(icon1)
        self.btn_menu_2.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.btn_menu_2)

        self.btn_home_2 = PyPushButton(self.frame_left_menu_top_2)
        self.btn_home_2.setObjectName(u"btn_home_2")
        self.btn_home_2.setMinimumSize(QSize(37, 37))
        self.btn_home_2.setMaximumSize(QSize(1234, 37))
        icon2 = QIcon()
        icon2.addFile(u"../../../../src/gui/images/svg_icons/icon_home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home_2.setIcon(icon2)
        self.btn_home_2.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.btn_home_2)

        self.btn_compra_2 = PyPushButton(self.frame_left_menu_top_2)
        self.btn_compra_2.setObjectName(u"btn_compra_2")
        self.btn_compra_2.setMinimumSize(QSize(37, 37))
        self.btn_compra_2.setMaximumSize(QSize(1234, 37))
        icon3 = QIcon()
        icon3.addFile(u"../../../../src/gui/images/svg_icons/icon_compra.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_compra_2.setIcon(icon3)
        self.btn_compra_2.setIconSize(QSize(36, 36))

        self.verticalLayout_5.addWidget(self.btn_compra_2)

        self.btn_venda_2 = PyPushButton(self.frame_left_menu_top_2)
        self.btn_venda_2.setObjectName(u"btn_venda_2")
        self.btn_venda_2.setMinimumSize(QSize(37, 37))
        self.btn_venda_2.setMaximumSize(QSize(1234, 37))
        icon4 = QIcon()
        icon4.addFile(u"../../../../src/gui/images/svg_icons/icon_venda.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_venda_2.setIcon(icon4)
        self.btn_venda_2.setIconSize(QSize(36, 36))

        self.verticalLayout_5.addWidget(self.btn_venda_2)


        self.verticalLayout_8.addWidget(self.frame_left_menu_top_2)

        self.line_left_menu_2 = QFrame(self.continer_left_menu)
        self.line_left_menu_2.setObjectName(u"line_left_menu_2")
        self.line_left_menu_2.setMaximumSize(QSize(41, 2))
        self.line_left_menu_2.setStyleSheet(u"background-color: rgb(65, 80, 173);")
        self.line_left_menu_2.setFrameShape(QFrame.HLine)
        self.line_left_menu_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_left_menu_2)

        self.frame_continer_scroll_area_widget_2 = QFrame(self.continer_left_menu)
        self.frame_continer_scroll_area_widget_2.setObjectName(u"frame_continer_scroll_area_widget_2")
        self.frame_continer_scroll_area_widget_2.setMinimumSize(QSize(0, 123))
        self.frame_continer_scroll_area_widget_2.setMaximumSize(QSize(16777215, 123))
        self.frame_continer_scroll_area_widget_2.setStyleSheet(u"")
        self.frame_continer_scroll_area_widget_2.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_scroll_area_widget_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_continer_scroll_area_widget_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scroll_area_left_menu_2 = QScrollArea(self.frame_continer_scroll_area_widget_2)
        self.scroll_area_left_menu_2.setObjectName(u"scroll_area_left_menu_2")
        self.scroll_area_left_menu_2.setMinimumSize(QSize(0, 120))
        self.scroll_area_left_menu_2.setLineWidth(0)
        self.scroll_area_left_menu_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_left_menu_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_left_menu_2.setWidgetResizable(True)
        self.scroll_area_widget_contents_left_menu_2 = QWidget()
        self.scroll_area_widget_contents_left_menu_2.setObjectName(u"scroll_area_widget_contents_left_menu_2")
        self.scroll_area_widget_contents_left_menu_2.setGeometry(QRect(0, 0, 44, 291))
        self.verticalLayout_9 = QVBoxLayout(self.scroll_area_widget_contents_left_menu_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 5, 0)
        self.frame_continer_scroll_area_widget_contents_left_menu_2 = QFrame(self.scroll_area_widget_contents_left_menu_2)
        self.frame_continer_scroll_area_widget_contents_left_menu_2.setObjectName(u"frame_continer_scroll_area_widget_contents_left_menu_2")
        self.frame_continer_scroll_area_widget_contents_left_menu_2.setStyleSheet(u"")
        self.frame_continer_scroll_area_widget_contents_left_menu_2.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_scroll_area_widget_contents_left_menu_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_continer_scroll_area_widget_contents_left_menu_2)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_relatorio_2 = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu_2)
        self.btn_relatorio_2.setObjectName(u"btn_relatorio_2")
        self.btn_relatorio_2.setMinimumSize(QSize(37, 37))
        self.btn_relatorio_2.setMaximumSize(QSize(1234, 37))
        icon5 = QIcon()
        icon5.addFile(u"../../../../src/gui/images/svg_icons/icon_inventory.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_relatorio_2.setIcon(icon5)
        self.btn_relatorio_2.setIconSize(QSize(40, 40))

        self.verticalLayout_10.addWidget(self.btn_relatorio_2)

        self.btn_service_2 = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu_2)
        self.btn_service_2.setObjectName(u"btn_service_2")
        self.btn_service_2.setMinimumSize(QSize(37, 37))
        self.btn_service_2.setMaximumSize(QSize(1234, 37))
        icon6 = QIcon()
        icon6.addFile(u"../../../../src/gui/images/svg_icons/icon_sevice.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_service_2.setIcon(icon6)
        self.btn_service_2.setIconSize(QSize(22, 22))

        self.verticalLayout_10.addWidget(self.btn_service_2)

        self.btn_fornecedor_2 = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu_2)
        self.btn_fornecedor_2.setObjectName(u"btn_fornecedor_2")
        self.btn_fornecedor_2.setMinimumSize(QSize(37, 37))
        self.btn_fornecedor_2.setMaximumSize(QSize(1234, 37))
        icon7 = QIcon()
        icon7.addFile(u"../../../../src/gui/images/svg_icons/icon_employee.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fornecedor_2.setIcon(icon7)
        self.btn_fornecedor_2.setIconSize(QSize(28, 28))

        self.verticalLayout_10.addWidget(self.btn_fornecedor_2)

        self.btn_cliente_2 = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu_2)
        self.btn_cliente_2.setObjectName(u"btn_cliente_2")
        self.btn_cliente_2.setMinimumSize(QSize(37, 37))
        self.btn_cliente_2.setMaximumSize(QSize(1234, 37))
        icon8 = QIcon()
        icon8.addFile(u"../../../../src/gui/images/svg_icons/icon_cliente.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cliente_2.setIcon(icon8)
        self.btn_cliente_2.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.btn_cliente_2)

        self.btn_agenda_2 = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu_2)
        self.btn_agenda_2.setObjectName(u"btn_agenda_2")
        self.btn_agenda_2.setMinimumSize(QSize(37, 37))
        self.btn_agenda_2.setMaximumSize(QSize(1234, 37))
        icon9 = QIcon()
        icon9.addFile(u"../../../../src/gui/images/svg_icons/icon_service.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agenda_2.setIcon(icon9)
        self.btn_agenda_2.setIconSize(QSize(41, 41))

        self.verticalLayout_10.addWidget(self.btn_agenda_2)

        self.btn_recibo_2 = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu_2)
        self.btn_recibo_2.setObjectName(u"btn_recibo_2")
        self.btn_recibo_2.setMinimumSize(QSize(37, 37))
        self.btn_recibo_2.setMaximumSize(QSize(1234, 37))
        icon10 = QIcon()
        icon10.addFile(u"../../../../src/gui/images/svg_icons/receipt-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_recibo_2.setIcon(icon10)
        self.btn_recibo_2.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.btn_recibo_2)

        self.btn_copia_seguranca_2 = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu_2)
        self.btn_copia_seguranca_2.setObjectName(u"btn_copia_seguranca_2")
        self.btn_copia_seguranca_2.setMinimumSize(QSize(37, 37))
        self.btn_copia_seguranca_2.setMaximumSize(QSize(1234, 37))
        icon11 = QIcon()
        icon11.addFile(u"../../../../src/gui/images/svg_icons/icon_cloud.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_copia_seguranca_2.setIcon(icon11)
        self.btn_copia_seguranca_2.setIconSize(QSize(25, 25))

        self.verticalLayout_10.addWidget(self.btn_copia_seguranca_2)


        self.verticalLayout_9.addWidget(self.frame_continer_scroll_area_widget_contents_left_menu_2)

        self.scroll_area_left_menu_2.setWidget(self.scroll_area_widget_contents_left_menu_2)

        self.horizontalLayout_6.addWidget(self.scroll_area_left_menu_2)


        self.verticalLayout_8.addWidget(self.frame_continer_scroll_area_widget_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.frame_conteiner_left_menu_bottom_2 = QFrame(self.continer_left_menu)
        self.frame_conteiner_left_menu_bottom_2.setObjectName(u"frame_conteiner_left_menu_bottom_2")
        self.frame_conteiner_left_menu_bottom_2.setStyleSheet(u"")
        self.frame_conteiner_left_menu_bottom_2.setFrameShape(QFrame.StyledPanel)
        self.frame_conteiner_left_menu_bottom_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_conteiner_left_menu_bottom_2)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 5, 4)
        self.btn_setting_2 = PyPushButton(self.frame_conteiner_left_menu_bottom_2)
        self.btn_setting_2.setObjectName(u"btn_setting_2")
        self.btn_setting_2.setMinimumSize(QSize(37, 37))
        self.btn_setting_2.setMaximumSize(QSize(1234, 37))
        icon12 = QIcon()
        icon12.addFile(u"../../../../src/gui/images/svg_icons/icon_setting.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting_2.setIcon(icon12)
        self.btn_setting_2.setIconSize(QSize(28, 28))

        self.verticalLayout_11.addWidget(self.btn_setting_2)

        self.btn_info_2 = PyPushButton(self.frame_conteiner_left_menu_bottom_2)
        self.btn_info_2.setObjectName(u"btn_info_2")
        self.btn_info_2.setMinimumSize(QSize(37, 37))
        self.btn_info_2.setMaximumSize(QSize(1234, 37))
        icon13 = QIcon()
        icon13.addFile(u"../../../../src/gui/images/svg_icons/icon_information.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_info_2.setIcon(icon13)
        self.btn_info_2.setIconSize(QSize(27, 27))

        self.verticalLayout_11.addWidget(self.btn_info_2)

        self.btn_user_2 = PyPushButton(self.frame_conteiner_left_menu_bottom_2)
        self.btn_user_2.setObjectName(u"btn_user_2")
        self.btn_user_2.setMinimumSize(QSize(37, 37))
        self.btn_user_2.setMaximumSize(QSize(1234, 37))
        icon14 = QIcon()
        icon14.addFile(u"../../../../src/gui/images/svg_images/daniel.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_user_2.setIcon(icon14)
        self.btn_user_2.setIconSize(QSize(34, 39))

        self.verticalLayout_11.addWidget(self.btn_user_2)


        self.verticalLayout_8.addWidget(self.frame_conteiner_left_menu_bottom_2)


        self.vertical_layout_left_menu.addWidget(self.continer_left_menu)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_menu_4.setText("")
        self.btn_menu_2.setText(QCoreApplication.translate("Form", u"Menu", None))
        self.btn_home_2.setText(QCoreApplication.translate("Form", u"Home", None))
        self.btn_compra_2.setText(QCoreApplication.translate("Form", u"Compra", None))
        self.btn_venda_2.setText(QCoreApplication.translate("Form", u"Venda", None))
        self.btn_relatorio_2.setText(QCoreApplication.translate("Form", u"Relatorio", None))
        self.btn_service_2.setText(QCoreApplication.translate("Form", u"Servi\u00e7os", None))
        self.btn_fornecedor_2.setText(QCoreApplication.translate("Form", u"Funcion\u00e1rio", None))
        self.btn_cliente_2.setText(QCoreApplication.translate("Form", u"Cliente", None))
        self.btn_agenda_2.setText(QCoreApplication.translate("Form", u"Agenda", None))
        self.btn_recibo_2.setText(QCoreApplication.translate("Form", u"Recibo", None))
        self.btn_copia_seguranca_2.setText(QCoreApplication.translate("Form", u"C\u00f3pia de seguran\u00e7a", None))
        self.btn_setting_2.setText(QCoreApplication.translate("Form", u"Configura\u00e7\u00e3o", None))
        self.btn_info_2.setText(QCoreApplication.translate("Form", u"Informa\u00e7\u00e3o", None))
        self.btn_user_2.setText(QCoreApplication.translate("Form", u"User", None))
    # retranslateUi

