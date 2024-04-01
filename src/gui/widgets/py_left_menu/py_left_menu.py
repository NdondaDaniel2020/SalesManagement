# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerpugIFk.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from src.qt_core import *

from src.gui.widgets.py_push_button.py_push_button import PyPushButton
from src.gui.core.absolute_path import AbsolutePath


class LeftMenu(QWidget):
    def __init__(self, parent=None, app_parent=None, app_height=QRect, title_bar=True) -> None:
        super().__init__(parent)


        self.title_bar = title_bar

        if title_bar:
            self._pos_x = 6
            self._pos_y = 6
            self._pos_height = app_height - 25.5
        else:
            self._pos_x = 6
            self._pos_y = 6
            self._pos_height = app_height - 13.9



        self._pos_width = 44


        self._base_left_menu_width_animation = self._pos_width + 2
        self._float_left_menu_width_animation = self._pos_width + 2
        self._size_screen = QApplication.primaryScreen().size()

        self.button_settings = {
            'btn_home': {'btn_radius': 8, 'text_padding': 5},

            'btn_compra': {'btn_radius': 8, 'text_padding': 2},

            'btn_venda': {'btn_radius': 8, 'text_padding': 1},

            'btn_relatorio': {'btn_radius': 8, 'text_padding': 0},

            'btn_service': {'btn_radius': 8, 'text_padding': 7},

            'btn_fornecedor': {'btn_radius': 8, 'text_padding': 6},

            'btn_cliente': {'btn_radius': 8, 'text_padding': 6},

            'btn_agenda': {'btn_radius': 8, 'text_padding': -2},

            'btn_recibo': {'btn_radius': 8, 'text_padding': 6},

            'btn_copia_seguranca': {'btn_radius': 8, 'text_padding': 7},

            'btn_setting': {'btn_radius': 8, 'text_padding': 5},

            'btn_info': {'btn_radius': 8, 'text_padding': 6},

            'btn_user': {'btn_radius': 8, 'text_padding': 1.3}
        }

        self.expand = 200

        self._app_parent = app_parent
        self._parent = parent

        # INICIALIZAÇÃO (INSTACIA) E CONFIGURAÇÃO DOS LEFT MENU
        # INITIALIZATION (INSTACIA) AND LEFT MENU CONFIGURATION
        # /////////////////////////////////////////////////////
        self._initUiFloat_()

        # CONEXÃO ENTRE OS BOTÕES E OS METODOS
        # CONNECTION BETWEEN BUTTONS AND METHODS
        # //////////////////////////////////////////////////////
        self._connections_()

        # ADICIONAR O TEXTO NO TOOLTIP DOS BUTTONS
        # ADD TEXT TO THE BUTTONS TOOLTIP
        # //////////////////////////////////////////////////////
        self.__addToolTip__()


    def _initUiFloat_(self):
        """
        CONSTRUCTION AND CONFIGUARATION OF THE LEFT MENU
        CONSTRUÇÃO E CONFIGUARAÇÃO DAS LEFT MENU
        :return:
        """
        # ADICIONAR O MENU NA BASE DA INTERFACE, TORNADO ELE PARTE DO LAYOUT
        # ADD THE MENU AT THE BASE OF THE INTERFACE, MAKING IT PART OF THE LAYOUT
        # //////////////////////////////////////////////////////
        self.left_menu_base = UiLeftMenu(self._parent)



        # CRIADO UM FRAME QUE FIQUE POR CIMA DA INTERFACE ONDE FICARÁ O LEFT MENU FLUTUANTE
        # CREATED A FRAME THAT IS ON TOP OF THE INTERFACE WHERE THE FLOATING LEFT MENU WILL BE
        # //////////////////////////////////////////////////////
        self.frame_left_menu_float = QFrame(self._app_parent)
        self.frame_left_menu_float.setGeometry(self._pos_x, self._pos_y, self._pos_width, self._pos_height)
        self.frame_left_menu_float.setMaximumWidth(self._pos_width)
        self.frame_left_menu_float.setMinimumWidth(self._pos_width)
        self.frame_left_menu_float.setStyleSheet("""*{background-color: rgb(32, 33, 37); border-radius:6px;}
                                                    #scroll_area_widget_contents_left_menu,
                                                    #scroll_area_left_menu{
                                                        background-color: rgb(32, 33, 37);
                                                        border:none}""")


        # SET DROP SHADOW
        # //////////////////////////////////////////////////////
        self.shadow_float = QGraphicsDropShadowEffect(self)
        self.shadow_float.setBlurRadius(30)
        self.shadow_float.setXOffset(0)
        self.shadow_float.setYOffset(0)
        self.shadow_float.setColor(QColor(0, 0, 0, 80))
        self.frame_left_menu_float.setGraphicsEffect(self.shadow_float)


        self.frame_left_menu_float.hide()

        # ADICIONAR O MENU NA FLUTUANTE DA INTERFACE, TORNADO ELE PARTE DO LAYOUT
        # ADD THE MENU AT THE FLOATIN OF THE INTERFACE, MAKING IT PART OF THE LAYOUT
        # //////////////////////////////////////////////////////
        self.left_menu_float = UiLeftMenu(self.frame_left_menu_float)

        self.shadow_frame_left_menu = QGraphicsDropShadowEffect(self)
        self.shadow_frame_left_menu.setBlurRadius(30)
        self.shadow_frame_left_menu.setXOffset(0)
        self.shadow_frame_left_menu.setYOffset(0)
        self.shadow_frame_left_menu.setColor(QColor(0, 0, 0, 80))
        self.left_menu_float.frame_left_menu.setGraphicsEffect(self.shadow_frame_left_menu)


        # POR NÃO ESTAR EM UM LAYOU, HOUVE NA NECECIADADE DE DACER AJUSTES
        # BECAUSE IT IS NOT IN A LAYOUT, THERE WAS A NEED TO MAKE ADJUSTMENTS
        # //////////////////////////////////////////////////////
        self.left_menu_float.verticalLayout_4.setContentsMargins(1, 3, 7, 0)
        self.left_menu_float.frame_left_menu.setMinimumSize(QSize(43, 0))
        self.left_menu_float.frame_left_menu.setMaximumSize(QSize(43, 16777215))
        # //////////////////////////////////////////////////////

    def _connections_(self) -> None:
        """
        # CONEXÃO ENTRE OS BOTÕES E OS METODOS
        # CONNECTION BETWEEN BUTTONS AND METHODS
        :return:
        """
        self.left_menu_float.btn_menu.clicked.connect(self._hideLeftMenuFloat_)
        self.left_menu_base.btn_menu.clicked.connect(self._showLeftMenuFloat_)

        self.left_menu_base.scroll_area_left_menu.verticalScrollBar().valueChanged.connect(self._onScrollValueChanged_)
        self.left_menu_float.scroll_area_left_menu.verticalScrollBar().valueChanged.connect(self._onScrollValueChanged_)


        self.left_menu_base.btn_home.clicked.connect(self._connections_buttons_)
        self.left_menu_float.btn_home.clicked.connect(self._connections_buttons_)

        self.left_menu_base.btn_compra.clicked.connect(self._connections_buttons_)
        self.left_menu_float.btn_compra.clicked.connect(self._connections_buttons_)

        self.left_menu_base.btn_venda.clicked.connect(self._connections_buttons_)
        self.left_menu_float.btn_venda.clicked.connect(self._connections_buttons_)

        self.left_menu_base.btn_inventario.clicked.connect(self._connections_buttons_)
        self.left_menu_float.btn_inventario.clicked.connect(self._connections_buttons_)

        self.left_menu_base.btn_relatorio.clicked.connect(self._connections_buttons_)
        self.left_menu_float.btn_relatorio.clicked.connect(self._connections_buttons_)

        self.left_menu_base.btn_service.clicked.connect(self._connections_buttons_)
        self.left_menu_float.btn_service.clicked.connect(self._connections_buttons_)

        self.left_menu_base.btn_fornecedor.clicked.connect(self._connections_buttons_)
        self.left_menu_float.btn_fornecedor.clicked.connect(self._connections_buttons_)

        self.left_menu_base.btn_cliente.clicked.connect(self._connections_buttons_)
        self.left_menu_float.btn_cliente.clicked.connect(self._connections_buttons_)

        self.left_menu_base.btn_agenda.clicked.connect(self._connections_buttons_)
        self.left_menu_float.btn_agenda.clicked.connect(self._connections_buttons_)

        self.left_menu_base.btn_copia_seguranca.clicked.connect(self._connections_buttons_)
        self.left_menu_float.btn_copia_seguranca.clicked.connect(self._connections_buttons_)

        self.left_menu_base.btn_recibo.clicked.connect(self._connections_buttons_)
        self.left_menu_float.btn_recibo.clicked.connect(self._connections_buttons_)

        self.left_menu_base.btn_setting.clicked.connect(self._connections_buttons_)
        self.left_menu_float.btn_setting.clicked.connect(self._connections_buttons_)

        # self.left_menu_base.btn_info.clicked.connect(self._connections_buttons_)
        # self.left_menu_float.btn_info.clicked.connect(self._connections_buttons_)

        self.left_menu_base.btn_user.clicked.connect(self._connections_buttons_)
        self.left_menu_float.btn_user.clicked.connect(self._connections_buttons_)

        ## voltar a conectar os marcados os e refazer o self._connections_top_buttons_
        # para self._connections_ e nao add o btn_info neles ele sera cria do fora em uma outra class

    @Slot(str)
    def _connections_buttons_(self) -> None:

        print(self.sender().objectName())
        # PEGAR OS BTNS PARA ALTERAR O ESTILO
        # GET THE BTNS TO CHANGE THE STYLE
        # //////////////////////////////////////////////////////
        list_float_top = self.left_menu_float.frame_left_menu_top.findChildren(QPushButton)
        list_base_top = self.left_menu_base.frame_left_menu_top.findChildren(QPushButton)

        list_float = self.left_menu_float.frame_continer_scroll_area_widget_contents_left_menu.findChildren(QPushButton)
        list_base = self.left_menu_base.frame_continer_scroll_area_widget_contents_left_menu.findChildren(QPushButton)

        list_float_bottom = self.left_menu_float.frame_conteiner_left_menu_bottom.findChildren(QPushButton)
        list_base_bottom = self.left_menu_base.frame_conteiner_left_menu_bottom.findChildren(QPushButton)


        # ADICIONAR ESTILO DE BTN ATIVO AO BTN SELECIONADO
        # ADD ACTIVE BTN STYLE TO SELECTED BTN
        # //////////////////////////////////////////////////////
        for btn_base_top, btn_float_top in zip(list_float_top, list_base_top):
            for obj_name, obj_item in zip(self.button_settings.keys(), self.button_settings.values()):

                if btn_base_top.objectName() == obj_name == self.sender().objectName():

                    btn_base_top.set_style(is_active=True,
                                           btn_radius=obj_item['btn_radius'],
                                           text_padding=obj_item['text_padding'])

                    btn_float_top.set_style(is_active=True,
                                            btn_radius=obj_item['btn_radius'],
                                            text_padding=obj_item['text_padding'])
                else:
                    if btn_base_top.objectName() == obj_name:

                        btn_base_top.set_style(is_active=False,
                                               btn_radius=obj_item['btn_radius'],
                                               text_padding=obj_item['text_padding'])

                        btn_float_top.set_style(is_active=False,
                                                btn_radius=obj_item['btn_radius'],
                                                text_padding=obj_item['text_padding'])


        for btn_base, btn_float in zip(list_float, list_base):
            for obj_name, obj_item in zip(self.button_settings.keys(), self.button_settings.values()):

                if btn_base.objectName() == obj_name == self.sender().objectName():

                    btn_base.set_style(is_active=True,
                                       btn_radius=obj_item['btn_radius'],
                                       text_padding=obj_item['text_padding'])

                    btn_float.set_style(is_active=True,
                                        btn_radius=obj_item['btn_radius'],
                                        text_padding=obj_item['text_padding'])
                else:

                    if btn_base.objectName() == obj_name:

                        btn_base.set_style(is_active=False,
                                           btn_radius=obj_item['btn_radius'],
                                           text_padding=obj_item['text_padding'])

                        btn_float.set_style(is_active=False,
                                            btn_radius=obj_item['btn_radius'],
                                            text_padding=obj_item['text_padding'])


        for btn_base_bottom, btn_float_bottom in zip(list_float_bottom, list_base_bottom):
            for obj_name, obj_item in zip(self.button_settings.keys(), self.button_settings.values()):

                if btn_base_bottom.objectName() == obj_name == self.sender().objectName():

                    btn_base_bottom.set_style(is_active=True,
                                              btn_radius=obj_item['btn_radius'],
                                              text_padding=obj_item['text_padding'])

                    btn_float_bottom.set_style(is_active=True,
                                               btn_radius=obj_item['btn_radius'],
                                               text_padding=obj_item['text_padding'])
                else:

                    if btn_base_bottom.objectName() == obj_name and obj_name != 'btn_info':
                        btn_base_bottom.set_style(is_active=False,
                                                  btn_radius=obj_item['btn_radius'],
                                                  text_padding=obj_item['text_padding'])

                        btn_float_bottom.set_style(is_active=False,
                                                   btn_radius=obj_item['btn_radius'],
                                                   text_padding=obj_item['text_padding'])


    @Slot()
    def _showLeftMenuFloat_(self) -> None:
        """
        MOSTRAR O LEFT MENU FLUTUANTE E REDIMENCIONAR
        SHOW THE FLOATING LEFT MENU AND RESIZE
        :return:
        """


        # REDIMENCIONAR O TAMANHO DO LEFT MENU FLOAT
        # RESIZE LEFT MENU FLOAT SIZE
        #/////////////////////////////////////////////////////////////
        self.frame_left_menu_float.setGeometry(self._pos_x, self._pos_y, self._pos_width, self._pos_height)


        if self._pos_height > self._size_screen.height()-75:



            # CREATE ANIMATION FLOAT
            self.left_menu_base_animation = QPropertyAnimation(self._parent, b"minimumWidth")
            self.frame_left_menu_base_animation = QPropertyAnimation(self.left_menu_base.frame_left_menu, b"minimumWidth")
            self.line_left_menu_base_animation = QPropertyAnimation(self.left_menu_base.line_left_menu, b"minimumWidth")

            self.left_menu_base_animation.stop()
            self.frame_left_menu_base_animation.stop()
            self.line_left_menu_base_animation.stop()


            if self._base_left_menu_width_animation == 46:
                self._hideVisibilityToolTip_()

                self.left_menu_base_animation.setStartValue(46)
                self.left_menu_base_animation.setEndValue(self.expand)
                self.left_menu_base_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
                self.left_menu_base_animation.setDuration(200)

                self.frame_left_menu_base_animation.setStartValue(44)
                self.frame_left_menu_base_animation.setEndValue(self.expand)
                self.frame_left_menu_base_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
                self.frame_left_menu_base_animation.setDuration(200)

                self.line_left_menu_base_animation.setStartValue(40)
                self.line_left_menu_base_animation.setEndValue(self.expand-4)
                self.line_left_menu_base_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
                self.line_left_menu_base_animation.setDuration(200)
            else:
                self._showVisibilityToolTip_()

                self.left_menu_base_animation.setStartValue(self.expand)
                self.left_menu_base_animation.setEndValue(46)
                self.left_menu_base_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
                self.left_menu_base_animation.setDuration(200)

                self.frame_left_menu_base_animation.setStartValue(self.expand)
                self.frame_left_menu_base_animation.setEndValue(44)
                self.frame_left_menu_base_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
                self.frame_left_menu_base_animation.setDuration(200)

                self.line_left_menu_base_animation.setStartValue(self.expand-4)
                self.line_left_menu_base_animation.setEndValue(40)
                self.line_left_menu_base_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
                self.line_left_menu_base_animation.setDuration(200)


            self.base_animation_group = QParallelAnimationGroup()
            self.base_animation_group.addAnimation(self.left_menu_base_animation)
            self.base_animation_group.addAnimation(self.frame_left_menu_base_animation)
            self.base_animation_group.addAnimation(self.line_left_menu_base_animation)
            self.base_animation_group.start()

            self._base_left_menu_width_animation = 200 if self._base_left_menu_width_animation == 46 else 46

        else:

            if self._parent.width() < self.expand:

                self.left_menu_base.line_left_menu.hide()

                self.frame_left_menu_float.show()

                self._hideVisibilityToolTip_()

                # # CREATE ANIMATION FLOAT
                self.left_menu_base_animation = QPropertyAnimation(self.frame_left_menu_float, b"minimumWidth")
                self.left_menu_base_animation_max = QPropertyAnimation(self.frame_left_menu_float, b"maximumWidth")
                self.frame_left_menu_float_animation = QPropertyAnimation(self.left_menu_float.frame_left_menu,
                                                                          b"minimumWidth")
                self.line_left_menu_float_animation = QPropertyAnimation(self.left_menu_float.line_left_menu,
                                                                         b"minimumWidth")


                self.left_menu_base_animation.setStartValue(46)
                self.left_menu_base_animation.setEndValue(self.expand)
                self.left_menu_base_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
                self.left_menu_base_animation.setDuration(200)

                self.left_menu_base_animation_max.setStartValue(46)
                self.left_menu_base_animation_max.setEndValue(self.expand)
                self.left_menu_base_animation_max.setEasingCurve(QEasingCurve.Type.InOutCubic)
                self.left_menu_base_animation_max.setDuration(200)
                self.left_menu_base_animation_max.start()

                self.frame_left_menu_float_animation.setStartValue(44)
                self.frame_left_menu_float_animation.setEndValue(self.expand)
                self.frame_left_menu_float_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
                self.frame_left_menu_float_animation.setDuration(200)

                self.line_left_menu_float_animation.setStartValue(40)
                self.line_left_menu_float_animation.setEndValue(self.expand-4)
                self.line_left_menu_float_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
                self.line_left_menu_float_animation.setDuration(200)


                self.float_animation_group = QParallelAnimationGroup()
                self.float_animation_group.addAnimation(self.left_menu_base_animation)
                self.float_animation_group.addAnimation(self.left_menu_base_animation_max)
                self.float_animation_group.addAnimation(self.frame_left_menu_float_animation)
                self.float_animation_group.addAnimation(self.line_left_menu_float_animation)
                self.float_animation_group.start()

            else:
                self._hideLeftMenuFloat_()

    @Slot()
    def _hideLeftMenuFloat_(self) -> None:
        """
        ESCONDER O LEFT MENU FLUTUANTE E REDIMENCIONAR
        HIDE THE FLOATING LEFT MENU AND RESIZE
        :return:
        """

        self.left_menu_base.line_left_menu.show()


        self._showVisibilityToolTip_()
        self.left_menu_base_animation_max = QPropertyAnimation(self.frame_left_menu_float, b"maximumWidth")
        self.left_menu_base_animation = QPropertyAnimation(self.frame_left_menu_float, b"minimumWidth")
        self.frame_left_menu_float_animation = QPropertyAnimation(self.left_menu_float.frame_left_menu,
                                                                  b"minimumWidth")
        self.line_left_menu_float_animation = QPropertyAnimation(self.left_menu_float.line_left_menu,
                                                                 b"minimumWidth")


        self.left_menu_base_animation_max.setStartValue(self.expand)
        self.left_menu_base_animation_max.setEndValue(40)
        self.left_menu_base_animation_max.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.left_menu_base_animation_max.setDuration(200)

        self.left_menu_base_animation.setStartValue(self.expand)
        self.left_menu_base_animation.setEndValue(40)
        self.left_menu_base_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.left_menu_base_animation.setDuration(200)

        self.frame_left_menu_float_animation.setStartValue(self.expand)
        self.frame_left_menu_float_animation.setEndValue(40)
        self.frame_left_menu_float_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.frame_left_menu_float_animation.setDuration(200)

        self.line_left_menu_float_animation.setStartValue(self.expand - 4)
        self.line_left_menu_float_animation.setEndValue(40)
        self.line_left_menu_float_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.line_left_menu_float_animation.setDuration(200)


        self.float_animation_group = QParallelAnimationGroup()
        self.float_animation_group.addAnimation(self.left_menu_base_animation)
        self.float_animation_group.addAnimation(self.left_menu_base_animation_max)
        self.float_animation_group.addAnimation(self.frame_left_menu_float_animation)
        self.float_animation_group.addAnimation(self.line_left_menu_float_animation)
        self.float_animation_group.start()
        self.float_animation_group.finished.connect(lambda:
                                                    QTimer.singleShot(50, lambda: self.frame_left_menu_float.hide()))

    def _onScrollValueChanged_(self, value) -> None:
        """
        sincronizar os dois QScrollArea
        synchronize the two QScrollArea
        :param value:
        :return:
        """
        if not self.sender().orientation() == Qt.Horizontal:
            self.left_menu_base.scroll_area_left_menu.verticalScrollBar().setValue(value)
            self.left_menu_float.scroll_area_left_menu.verticalScrollBar().setValue(value)

    def setExpand(self, value) -> None:
        self.expand = value

    def setPosHeight(self, height) -> None:

        if self.title_bar:
            self._pos_x = 6
            self._pos_y = 6
            self._pos_height = height - 25.5
        else:
            self._pos_x = 6
            self._pos_y = 6
            self._pos_height = height - 13.9

    def setResize(self, object: QRect) -> None:
        """
        REDIMENCIONAR O MENU FLUTUANTE
        :param object:
        :return:
        """

        height = 0
        if self.title_bar:
            height = object.height() - 6
        else:
            height = object.height() - 20

        self.frame_left_menu_float.setGeometry(self._pos_x, self._pos_y, object.width(), height)

        self._pos_width = object.width()

        if self.title_bar:
            self._pos_height = object.height() - 6 if object.height() - 6 > 100 else self._pos_height
        else:
            self._pos_height = object.height() - 6 if object.height() > 100 else self._pos_height

        ## PARA ATIVAR O AUTO SCRO DO QScrolArea mude o maximumsize. cria outra def
        # self.left_menu_base.frame_continer_scroll_area_widget
        # self.left_menu_float.frame_continer_scroll_area_widget
        # .setMaximumSize(QSize(16777215, 295))
        # if object.height() - 378 >= 122 and object.height() - 378 <= 295:
        #     print(object.height() - 378)

    def activeBtbInfo(self):

        if not self.left_menu_base.btn_info.is_active:
            self.left_menu_base.btn_info.set_style(is_active=True, btn_radius=8, text_padding=6)
            self.left_menu_float.btn_info.set_style(is_active=True, btn_radius=8, text_padding=6)

        else:
            self.left_menu_base.btn_info.set_style(is_active=False, btn_radius=8, text_padding=6)
            self.left_menu_float.btn_info.set_style(is_active=False, btn_radius=8, text_padding=6)

    def _showVisibilityToolTip_(self) -> None:
        """
        PERMITIR QUE TOOLTIP APARECE
        ALLOW TOOLTIP TO APPEAR
        :return:
        """

        self.left_menu_base.btn_back.setPermissionShowTooltip(True)
        self.left_menu_float.btn_back.setPermissionShowTooltip(True)

        self.left_menu_base.btn_menu.setPermissionShowTooltip(True)
        self.left_menu_float.btn_menu.setPermissionShowTooltip(True)

        self.left_menu_base.btn_home.setPermissionShowTooltip(True)
        self.left_menu_float.btn_home.setPermissionShowTooltip(True)

        self.left_menu_base.btn_compra.setPermissionShowTooltip(True)
        self.left_menu_float.btn_compra.setPermissionShowTooltip(True)

        self.left_menu_base.btn_venda.setPermissionShowTooltip(True)
        self.left_menu_float.btn_venda.setPermissionShowTooltip(True)

        self.left_menu_base.btn_relatorio.setPermissionShowTooltip(True)
        self.left_menu_float.btn_relatorio.setPermissionShowTooltip(True)

        self.left_menu_base.btn_service.setPermissionShowTooltip(True)
        self.left_menu_float.btn_service.setPermissionShowTooltip(True)

        self.left_menu_base.btn_fornecedor.setPermissionShowTooltip(True)
        self.left_menu_float.btn_fornecedor.setPermissionShowTooltip(True)

        self.left_menu_base.btn_cliente.setPermissionShowTooltip(True)
        self.left_menu_float.btn_cliente.setPermissionShowTooltip(True)

        self.left_menu_base.btn_agenda.setPermissionShowTooltip(True)
        self.left_menu_float.btn_agenda.setPermissionShowTooltip(True)

        self.left_menu_base.btn_recibo.setPermissionShowTooltip(True)
        self.left_menu_float.btn_recibo.setPermissionShowTooltip(True)

        self.left_menu_base.btn_copia_seguranca.setPermissionShowTooltip(True)
        self.left_menu_float.btn_copia_seguranca.setPermissionShowTooltip(True)

        self.left_menu_base.btn_setting.setPermissionShowTooltip(True)
        self.left_menu_float.btn_setting.setPermissionShowTooltip(True)

        self.left_menu_base.btn_info.setPermissionShowTooltip(True)
        self.left_menu_float.btn_info.setPermissionShowTooltip(True)

        self.left_menu_base.btn_user.setPermissionShowTooltip(True)
        self.left_menu_float.btn_user.setPermissionShowTooltip(True)

    def _hideVisibilityToolTip_(self) -> None:
        """
        NÃO PERMITIR QUE TOOLTIP APARECE
        DO NOT ALLOW TOOLTIP TO APPEAR
        :return:
        """

        self.left_menu_base.btn_back.setPermissionShowTooltip(False)
        self.left_menu_float.btn_back.setPermissionShowTooltip(False)

        self.left_menu_base.btn_menu.setPermissionShowTooltip(False)
        self.left_menu_float.btn_menu.setPermissionShowTooltip(False)

        self.left_menu_base.btn_home.setPermissionShowTooltip(False)
        self.left_menu_float.btn_home.setPermissionShowTooltip(False)

        self.left_menu_base.btn_compra.setPermissionShowTooltip(False)
        self.left_menu_float.btn_compra.setPermissionShowTooltip(False)

        self.left_menu_base.btn_venda.setPermissionShowTooltip(False)
        self.left_menu_float.btn_venda.setPermissionShowTooltip(False)

        self.left_menu_base.btn_relatorio.setPermissionShowTooltip(False)
        self.left_menu_float.btn_relatorio.setPermissionShowTooltip(False)

        self.left_menu_base.btn_service.setPermissionShowTooltip(False)
        self.left_menu_float.btn_service.setPermissionShowTooltip(False)

        self.left_menu_base.btn_fornecedor.setPermissionShowTooltip(False)
        self.left_menu_float.btn_fornecedor.setPermissionShowTooltip(False)

        self.left_menu_base.btn_cliente.setPermissionShowTooltip(False)
        self.left_menu_float.btn_cliente.setPermissionShowTooltip(False)

        self.left_menu_base.btn_agenda.setPermissionShowTooltip(False)
        self.left_menu_float.btn_agenda.setPermissionShowTooltip(False)

        self.left_menu_base.btn_recibo.setPermissionShowTooltip(False)
        self.left_menu_float.btn_recibo.setPermissionShowTooltip(False)

        self.left_menu_base.btn_copia_seguranca.setPermissionShowTooltip(False)
        self.left_menu_float.btn_copia_seguranca.setPermissionShowTooltip(False)

        self.left_menu_base.btn_setting.setPermissionShowTooltip(False)
        self.left_menu_float.btn_setting.setPermissionShowTooltip(False)

        self.left_menu_base.btn_info.setPermissionShowTooltip(False)
        self.left_menu_float.btn_info.setPermissionShowTooltip(False)

        self.left_menu_base.btn_user.setPermissionShowTooltip(False)
        self.left_menu_float.btn_user.setPermissionShowTooltip(False)

    def __addToolTip__(self) -> None:
        """
        ADICIONAR O TEXTO NO TOOLTIP DOS BUTTONS
        ADD TEXT TO THE BUTTONS TOOLTIP
        :return:
        """

        self.left_menu_base.btn_back.setTooltipText("Voltar", self._app_parent,
                                                    pos_tooltip="right", adjust_x=14, adjust_y=3)
        self.left_menu_float.btn_back.setTooltipText("Voltar", self._app_parent,
                                                     pos_tooltip="right", adjust_x=14, adjust_y=3)

        self.left_menu_base.btn_menu.setTooltipText("Menu", self._app_parent,
                                                    pos_tooltip="right", adjust_x=15, adjust_y=3)
        self.left_menu_float.btn_menu.setTooltipText("Menu", self._app_parent,
                                                     pos_tooltip="right", adjust_x=15, adjust_y=3)

        self.left_menu_base.btn_home.setTooltipText("Home", self._app_parent,
                                                    pos_tooltip="right", adjust_x=15, adjust_y=3)
        self.left_menu_float.btn_home.setTooltipText("Home", self._app_parent,
                                                     pos_tooltip="right", adjust_x=15, adjust_y=3)

        self.left_menu_base.btn_compra.setTooltipText("Compra", self._app_parent,
                                                      pos_tooltip="right", adjust_x=12, adjust_y=3)
        self.left_menu_float.btn_compra.setTooltipText("Compra", self._app_parent,
                                                       pos_tooltip="right", adjust_x=12, adjust_y=3)



        self.left_menu_base.btn_venda.setTooltipText("Venda", self._app_parent,
                                                     pos_tooltip="right", adjust_x=15, adjust_y=3)
        self.left_menu_float.btn_venda.setTooltipText("Venda", self._app_parent,
                                                      pos_tooltip="right", adjust_x=15, adjust_y=3)


        self.left_menu_base.btn_inventario.setTooltipText("Inventario", self._app_parent,
                                                         pos_tooltip="right", adjust_x=10, adjust_y=3)
        self.left_menu_float.btn_inventario.setTooltipText("Inventario", self._app_parent,
                                                          pos_tooltip="right", adjust_x=10, adjust_y=3)

        self.left_menu_base.btn_relatorio.setTooltipText("Relatório", self._app_parent,
                                                         pos_tooltip="right", adjust_x=10, adjust_y=3)
        self.left_menu_float.btn_relatorio.setTooltipText("Relatório", self._app_parent,
                                                          pos_tooltip="right", adjust_x=10, adjust_y=3)

        self.left_menu_base.btn_service.setTooltipText("Serviço", self._app_parent,
                                                       pos_tooltip="right", adjust_x=12, adjust_y=3)
        self.left_menu_float.btn_service.setTooltipText("Serviço", self._app_parent,
                                                        pos_tooltip="right", adjust_x=12, adjust_y=3)

        self.left_menu_base.btn_fornecedor.setTooltipText("Fornecedor", self._app_parent,
                                                          pos_tooltip="right", adjust_x=7, adjust_y=3)
        self.left_menu_float.btn_fornecedor.setTooltipText("Fornecedor", self._app_parent,
                                                           pos_tooltip="right", adjust_x=7, adjust_y=3)

        self.left_menu_base.btn_cliente.setTooltipText("Cliente", self._app_parent,
                                                       pos_tooltip="right", adjust_x=12, adjust_y=3)
        self.left_menu_float.btn_cliente.setTooltipText("Cliente", self._app_parent,
                                                        pos_tooltip="right", adjust_x=12, adjust_y=3)

        self.left_menu_base.btn_agenda.setTooltipText("Agenda", self._app_parent,
                                                      pos_tooltip="right", adjust_x=12, adjust_y=3)
        self.left_menu_float.btn_agenda.setTooltipText("Agenda", self._app_parent,
                                                       pos_tooltip="right", adjust_x=12, adjust_y=3)

        self.left_menu_base.btn_recibo.setTooltipText("Recibo", self._app_parent,
                                                      pos_tooltip="right", adjust_x=14, adjust_y=3)
        self.left_menu_float.btn_recibo.setTooltipText("Recibo", self._app_parent,
                                                       pos_tooltip="right", adjust_x=14, adjust_y=3)

        self.left_menu_base.btn_copia_seguranca.setTooltipText("cópia segurança", self._app_parent,
                                                               pos_tooltip="right", adjust_x=0, adjust_y=3)
        self.left_menu_float.btn_copia_seguranca.setTooltipText("cópia segurança", self._app_parent,
                                                                pos_tooltip="right", adjust_x=14, adjust_y=3)



        self.left_menu_base.btn_setting.setTooltipText("Configuração", self._app_parent,
                                                       pos_tooltip="right", adjust_x=4, adjust_y=3)
        self.left_menu_float.btn_setting.setTooltipText("Configuração", self._app_parent,
                                                        pos_tooltip="right", adjust_x=4, adjust_y=3)

        self.left_menu_base.btn_info.setTooltipText("Informações", self._app_parent,
                                                    pos_tooltip="right", adjust_x=5, adjust_y=3)
        self.left_menu_float.btn_info.setTooltipText("Informações", self._app_parent,
                                                     pos_tooltip="right", adjust_x=5, adjust_y=3)

        self.left_menu_base.btn_user.setTooltipText("Usuario", self._app_parent,
                                                    pos_tooltip="right", adjust_x=12, adjust_y=3)
        self.left_menu_float.btn_user.setTooltipText("Usuario", self._app_parent,
                                                     pos_tooltip="right", adjust_x=12, adjust_y=3)






class UiLeftMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.vertical_layout_left_menu_continer = QVBoxLayout(parent)
        self.vertical_layout_left_menu_continer.setObjectName(u"vertical_layout_left_menu")
        self.vertical_layout_left_menu_continer.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_left_menu_continer.setSpacing(0)
        self.frame_left_menu = QFrame(parent)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(46, 0))
        self.frame_left_menu.setMaximumSize(QSize(46, 16777215))
        self.frame_left_menu.setStyleSheet(u"")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.vertical_layout_left_menu = QVBoxLayout(self.frame_left_menu)
        self.vertical_layout_left_menu.setSpacing(2)
        self.vertical_layout_left_menu.setObjectName(u"vertical_layout_left_menu_2")
        self.vertical_layout_left_menu.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu_top = QFrame(self.frame_left_menu)
        self.frame_left_menu_top.setObjectName(u"frame_left_menu_top")
        self.frame_left_menu_top.setStyleSheet(u"")
        self.frame_left_menu_top.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu_top)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 0, 6, 0)
        self.btn_back = PyPushButton(self.frame_left_menu_top,
                                     btn_radius=8, text_padding=8,
                                     btn_hover="#3e4046",
                                     btn_pressed="#474950")

        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setMinimumSize(QSize(37, 37))
        self.btn_back.setMaximumSize(QSize(1234, 37))
        icon_back = QIcon()
        icon_back.addFile(AbsolutePath().getPathIcon("icon_back.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon_back)
        self.btn_back.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.btn_back)

        self.btn_menu = PyPushButton(self.frame_left_menu_top,
                                     btn_radius=8, text_padding=4,
                                     btn_hover="#3e4046",
                                     btn_pressed="#474950")

        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(37, 37))
        self.btn_menu.setMaximumSize(QSize(1234, 37))
        icon_menu = QIcon()
        icon_menu.addFile(AbsolutePath().getPathIcon("icon_menu.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon_menu)
        self.btn_menu.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.btn_menu)

        self.btn_home = PyPushButton(self.frame_left_menu_top,
                                     btn_radius=8, text_padding=5,
                                     is_active=True)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(37, 37))
        self.btn_home.setMaximumSize(QSize(1234, 37))
        icon_home = QIcon()
        icon_home.addFile(AbsolutePath().getPathIcon("icon_home.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon_home)
        self.btn_home.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_compra = PyPushButton(self.frame_left_menu_top, btn_radius=8, text_padding=2)
        self.btn_compra.setObjectName(u"btn_compra")
        self.btn_compra.setMinimumSize(QSize(37, 37))
        self.btn_compra.setMaximumSize(QSize(1234, 37))
        icon_compra = QIcon()
        icon_compra.addFile(AbsolutePath().getPathIcon("icon_compra.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_compra.setIcon(icon_compra)
        self.btn_compra.setIconSize(QSize(36, 36))

        self.verticalLayout_3.addWidget(self.btn_compra)

        self.btn_venda = PyPushButton(self.frame_left_menu_top, btn_radius=8, text_padding=1)
        self.btn_venda.setObjectName(u"btn_venda")
        self.btn_venda.setMinimumSize(QSize(37, 37))
        self.btn_venda.setMaximumSize(QSize(1234, 37))
        icon_venda = QIcon()
        icon_venda.addFile(AbsolutePath().getPathIcon("icon_venda.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_venda.setIcon(icon_venda)
        self.btn_venda.setIconSize(QSize(36, 36))

        self.verticalLayout_3.addWidget(self.btn_venda)

        self.vertical_layout_left_menu.addWidget(self.frame_left_menu_top)

        self.line_left_menu = QFrame(self.frame_left_menu)
        self.line_left_menu.setObjectName(u"line_left_menu")
        self.line_left_menu.setMaximumSize(QSize(42, 2))
        self.line_left_menu.setStyleSheet(u"background-color: rgb(63, 78, 169);")
        self.line_left_menu.setFrameShape(QFrame.HLine)
        self.line_left_menu.setFrameShadow(QFrame.Sunken)

        self.vertical_layout_left_menu.addWidget(self.line_left_menu)

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
        self.scroll_area_left_menu.setMinimumSize(QSize(0, 122))
        self.scroll_area_left_menu.setMaximumSize(QSize(16777215, 122))
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
        self.frame_continer_scroll_area_widget_contents_left_menu.setObjectName(
            u"frame_continer_scroll_area_widget_contents_left_menu")
        self.frame_continer_scroll_area_widget_contents_left_menu.setStyleSheet(u"")
        self.frame_continer_scroll_area_widget_contents_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_scroll_area_widget_contents_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_continer_scroll_area_widget_contents_left_menu)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.btn_inventario = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu,
                                          btn_radius=8, text_padding=5)

        self.btn_inventario.setObjectName(u"btn_inventario")
        self.btn_inventario.setMinimumSize(QSize(37, 37))
        self.btn_inventario.setMaximumSize(QSize(1234, 37))
        icon_inventario = QIcon()
        icon_inventario.addFile(AbsolutePath().getPathIcon("icon_box.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_inventario.setIcon(icon_inventario)
        self.btn_inventario.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.btn_inventario)

        self.btn_relatorio = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu,
                                          btn_radius=8, text_padding=0)

        self.btn_relatorio.setObjectName(u"btn_relatorio")
        self.btn_relatorio.setMinimumSize(QSize(37, 37))
        self.btn_relatorio.setMaximumSize(QSize(1234, 37))
        icon_relatorio = QIcon()
        icon_relatorio.addFile(AbsolutePath().getPathIcon("icon_inventory.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_relatorio.setIcon(icon_relatorio)
        self.btn_relatorio.setIconSize(QSize(38, 38))

        self.verticalLayout_7.addWidget(self.btn_relatorio)

        self.btn_service = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu,
                                        btn_radius=8, text_padding=7)

        self.btn_service.setObjectName(u"btn_service")
        self.btn_service.setMinimumSize(QSize(37, 37))
        self.btn_service.setMaximumSize(QSize(1234, 37))
        icon_service = QIcon()
        icon_service.addFile(AbsolutePath().getPathIcon("icon_sevice.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_service.setIcon(icon_service)
        self.btn_service.setIconSize(QSize(23, 23))

        self.verticalLayout_7.addWidget(self.btn_service)

        self.btn_fornecedor = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu,
                                           btn_radius=8, text_padding=6)
        self.btn_fornecedor.setObjectName(u"btn_fornecedor")
        self.btn_fornecedor.setMinimumSize(QSize(37, 37))
        self.btn_fornecedor.setMaximumSize(QSize(1234, 37))
        icon_fornecedor = QIcon()
        icon_fornecedor.addFile(AbsolutePath().getPathIcon("icon_employee.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fornecedor.setIcon(icon_fornecedor)
        self.btn_fornecedor.setIconSize(QSize(26, 26))

        self.verticalLayout_7.addWidget(self.btn_fornecedor)

        self.btn_cliente = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu,
                                        btn_radius=8, text_padding=6)

        self.btn_cliente.setObjectName(u"btn_cliente")
        self.btn_cliente.setMinimumSize(QSize(37, 37))
        self.btn_cliente.setMaximumSize(QSize(1234, 37))
        icon_cliente = QIcon()
        icon_cliente.addFile(AbsolutePath().getPathIcon("icon_cliente.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cliente.setIcon(icon_cliente)
        self.btn_cliente.setIconSize(QSize(26, 26))

        self.verticalLayout_7.addWidget(self.btn_cliente)

        self.btn_agenda = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu,
                                       btn_radius=8, text_padding=-2)
        self.btn_agenda.setObjectName(u"btn_agenda")
        self.btn_agenda.setMinimumSize(QSize(37, 37))
        self.btn_agenda.setMaximumSize(QSize(1234, 37))
        icon_agenda = QIcon()
        icon_agenda.addFile(AbsolutePath().getPathIcon("icon_service.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agenda.setIcon(icon_agenda)
        self.btn_agenda.setIconSize(QSize(41, 41))

        self.verticalLayout_7.addWidget(self.btn_agenda)

        self.btn_recibo = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu,
                                       btn_radius=8, text_padding=6)
        self.btn_recibo.setObjectName(u"btn_recibo")
        self.btn_recibo.setMinimumSize(QSize(37, 37))
        self.btn_recibo.setMaximumSize(QSize(1234, 37))
        icon_recibo = QIcon()
        icon_recibo.addFile(AbsolutePath().getPathIcon("icon_receipt"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_recibo.setIcon(icon_recibo)
        self.btn_recibo.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.btn_recibo)

        self.btn_copia_seguranca = PyPushButton(self.frame_continer_scroll_area_widget_contents_left_menu,
                                                btn_radius=8, text_padding=7)
        self.btn_copia_seguranca.setObjectName(u"btn_copia_seguranca")
        self.btn_copia_seguranca.setMinimumSize(QSize(37, 37))
        self.btn_copia_seguranca.setMaximumSize(QSize(1234, 37))
        icon_copia_seguranca = QIcon()
        icon_copia_seguranca.addFile(AbsolutePath().getPathIcon("icon_cloud.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_copia_seguranca.setIcon(icon_copia_seguranca)
        self.btn_copia_seguranca.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.btn_copia_seguranca)

        self.verticalLayout_4.addWidget(self.frame_continer_scroll_area_widget_contents_left_menu)

        self.scroll_area_left_menu.setWidget(self.scroll_area_widget_contents_left_menu)

        self.horizontalLayout_5.addWidget(self.scroll_area_left_menu)

        self.vertical_layout_left_menu.addWidget(self.frame_continer_scroll_area_widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vertical_layout_left_menu.addItem(self.verticalSpacer)

        self.frame_conteiner_left_menu_bottom = QFrame(self.frame_left_menu)
        self.frame_conteiner_left_menu_bottom.setObjectName(u"frame_conteiner_left_menu_bottom")
        self.frame_conteiner_left_menu_bottom.setStyleSheet(u"")
        self.frame_conteiner_left_menu_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_conteiner_left_menu_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_conteiner_left_menu_bottom)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 0, 6, 4)
        self.btn_setting = PyPushButton(self.frame_conteiner_left_menu_bottom, btn_radius=8, text_padding=5)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setMinimumSize(QSize(37, 37))
        self.btn_setting.setMaximumSize(QSize(1234, 37))
        icon_setting = QIcon()
        icon_setting.addFile(AbsolutePath().getPathIcon("icon_setting.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting.setIcon(icon_setting)
        self.btn_setting.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.btn_setting)

        self.btn_info = PyPushButton(self.frame_conteiner_left_menu_bottom, btn_radius=8, text_padding=6)
        self.btn_info.setObjectName(u"btn_info")
        self.btn_info.setMinimumSize(QSize(37, 37))
        self.btn_info.setMaximumSize(QSize(1234, 37))
        icon_info = QIcon()
        icon_info.addFile(AbsolutePath().getPathIcon("icon_information.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_info.setIcon(icon_info)
        self.btn_info.setIconSize(QSize(27, 27))

        self.verticalLayout_2.addWidget(self.btn_info)

        self.btn_user = PyPushButton(self.frame_conteiner_left_menu_bottom, btn_radius=8, text_padding=1.3)
        self.btn_user.setObjectName(u"btn_user")
        self.btn_user.setMinimumSize(QSize(37, 37))
        self.btn_user.setMaximumSize(QSize(1234, 37))
        icon_user = QIcon()
        icon_user.addFile(AbsolutePath().getPathImage("daniel.jpg"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_user.setIcon(icon_user)
        self.btn_user.setIconSize(QSize(34, 39))

        self.verticalLayout_2.addWidget(self.btn_user)

        self.vertical_layout_left_menu.addWidget(self.frame_conteiner_left_menu_bottom)

        self.vertical_layout_left_menu_continer.addWidget(self.frame_left_menu)

        self.retranslateUi()

    # setupUi

    def retranslateUi(self):
        # Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_back.setText(QCoreApplication.translate("Form", u"    Back", None))
        self.btn_menu.setText(QCoreApplication.translate("Form", u"  Menu", None))
        self.btn_home.setText(QCoreApplication.translate("Form", u"  Home", None))
        self.btn_compra.setText(QCoreApplication.translate("Form", u"Compra", None))
        self.btn_venda.setText(QCoreApplication.translate("Form", u" Venda", None))
        self.btn_inventario.setText(QCoreApplication.translate("Form", u"  Inventario", None))
        self.btn_relatorio.setText(QCoreApplication.translate("Form", u" Relatório", None))
        self.btn_service.setText(QCoreApplication.translate("Form", u"   Servi\u00e7os", None))
        self.btn_fornecedor.setText(QCoreApplication.translate("Form", u"  Funcion\u00e1rio", None))
        self.btn_cliente.setText(QCoreApplication.translate("Form", u" Cliente", None))
        self.btn_agenda.setText(QCoreApplication.translate("Form", u" Agenda", None))
        self.btn_recibo.setText(QCoreApplication.translate("Form", u" Recibo", None))
        self.btn_copia_seguranca.setText(QCoreApplication.translate("Form", u" C\u00f3pia de seguran\u00e7a", None))
        self.btn_setting.setText(QCoreApplication.translate("Form", u"  Configura\u00e7\u00f5es", None))
        self.btn_info.setText(QCoreApplication.translate("Form", u"   Informa\u00e7\u00f5es", None))
        self.btn_user.setText(QCoreApplication.translate("Form", u"  User", None))
    # retranslateUi

