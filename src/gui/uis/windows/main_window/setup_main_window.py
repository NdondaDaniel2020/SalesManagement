import platform

from src.qt_core import *

from src.gui.uis.windows.main_window.ui_main_window import Ui_MainWindow

from src.gui.widgets.py_grips.py_grips import PyGrips
from src.gui.widgets.py_left_menu.py_left_menu import LeftMenu
from src.gui.widgets.py_push_button.py_push_button import PyPushButton
from src.gui.widgets.py_painel_button.py_painel_button import PyPanelButton

from src.gui.core.imagepath import ImagePath
from src.gui.core.qss_themes import QssThemes



# from src.main import MainWindow


#################### add a atualiza;\ao do left menu floa no mousePreesEvent,
# para ele atualizar o left menu, cria um metodo para atualizar o tamanho na class left menu


class SetUpMainWindow:

    def __init__(self):
        # QMainWindow.__init__(self)
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.set_title_bar = False



    def configIconPath(self):

        self.ui.logo.setIcon(QIcon(ImagePath().set_svg_image('img-removebg-preview.png')))

        # //////////////////////////////////////////////////////////////////////////////////////////////////////
        self.ui.btn_log_extra_venda.setIcon(QIcon(ImagePath().set_svg_icon('icon_push_notification.svg')))
        self.ui.btn_log_extra_perda.setIcon(QIcon(ImagePath().set_svg_icon('icon_push_notification.svg')))
        self.ui.btn_logo_extra_perda.setIcon(QIcon(ImagePath().set_svg_icon('icon_push_notification.svg')))
        self.ui.btn_log_extra_inventario.setIcon(QIcon(ImagePath().set_svg_icon('icon_push_notification.svg')))

        # ////////////////////////////////////////////////////////////////////////////////////////////
        self.ui.btn_logo_venda.setIcon(QIcon(ImagePath().set_svg_icon('icon_coin.svg')))
        self.ui.btn_logo_inventario.setIcon(QIcon(ImagePath().set_svg_icon('icon_box.svg')))
        self.ui.btn_logo_recibo.setIcon(QIcon(ImagePath().set_svg_icon('icon_inventory.svg')))
        self.ui.btn_logo_perda.setIcon(QIcon(ImagePath().set_svg_icon('icon_line_chart_down.svg')))

        # //////////////////////////////////////////////////////////////////////////////////////////
        self.ui.widget_1.setIcon("icon_line_chart_down.svg")
        self.ui.widget_1.setText("Pizza Char")
        self.ui.widget_1.clicked.connect(lambda: print("test1"))

        self.ui.widget_2.setIcon("icon_inbox.svg")
        self.ui.widget_2.setText("SMS")
        self.ui.widget_2.clicked.connect(lambda: print("test2"))

        self.ui.widget_3.setIcon("icon_analytics.svg")
        self.ui.widget_3.setText("Char")
        self.ui.widget_3.clicked.connect(lambda: print("test3"))

        # ////////////////////////////////////////////////////////////////////////
        self.ui.icon_img_28.setIcon(QIcon(ImagePath().set_svg_image('tatiana-removebg-preview.png')))
        self.ui.icon_img_29.setIcon(QIcon(ImagePath().set_svg_image('daniel-removebg-preview.png')))
        self.ui.icon_img_30.setIcon(QIcon(ImagePath().set_svg_image('john-removebg-preview.png')))

        # ////////////////////////////////////////////////////////////////////////
        self.ui.frest_user.setPathImage(ImagePath().set_svg_image('daniel.jpg'))
        self.ui.frest_user.clicked.connect(lambda: print("test user"))

        self.ui.qrcode.setIcon(QIcon(ImagePath().set_svg_image("SalesManagement.svg")))

        # ////////////////////////////////////////////////////////////////////////
        self.ui.btn_pesquisa_produto.setIcon(QIcon(ImagePath().set_svg_icon('icon_search.svg')))
        self.ui.btn_mais_opcoes.setIcon(QIcon(ImagePath().set_svg_icon('icon_more.svg')))
        self.ui.btn_adicionar_produto.setIcon(QIcon(ImagePath().set_svg_icon('icon_add.svg')))




    def configCircularProgress(self):

        self.ui.circupar_progress_bar.width = 150
        self.ui.circupar_progress_bar.height = 150
        self.ui.circupar_progress_bar.value = 80
        self.ui.circupar_progress_bar.setFixedSize(215, 172)
        self.ui.circupar_progress_bar.move(30, 10)
        self.ui.circupar_progress_bar.font_size = 12
        self.ui.circupar_progress_bar.progress_width = 6
        self.ui.circupar_progress_bar.ad_shadow(True)
        self.ui.circupar_progress_bar.progress_color = 0x596deb
        self.ui.circupar_progress_bar.text_color = 0xE9EAEC


    def configSystem(self):

        if platform.system() == 'Windows':
            # ////////////////////////////////////////////////////////////////////////////////
            self.set_title_bar = True

            # ////////////////////////////////////////////////////////////////////////////////
            SetUpMainWindow.windowsConfiguration(self)

        else:
            # ////////////////////////////////////////////////////////////////////////////////
            SetUpMainWindow.nonWindowConfiguration(self)

        # ////////////////////////////////////////////////////////////////////////////////
        self.move((QApplication.primaryScreen().size().width() - self.width()) / 2,
                  (QApplication.primaryScreen().size().height() - self.height()) / 4.8)

    def addControlWindow(self):

        # CREATE AND CONFIG BTN MINIMIZE
        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_minimize = PyPushButton(self.ui.frame_control_window, btn_hover="#313237",
                                         btn_pressed="#26272b", btn_radius=4, text_padding=4.5)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(26, 26))
        self.btn_minimize.setMaximumSize(QSize(26, 26))

        # ADD ICON
        # ////////////////////////////////////////////////////////////////////////////////
        icon = QIcon()
        icon.addFile(ImagePath().set_svg_icon("icon_minimize.svg"), QSize(), QIcon.Normal, QIcon.Off)

        # CONFIG ICON SIZE
        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setIconSize(QSize(17, 17))

        # ADD BTN ON LAYOUT
        # ////////////////////////////////////////////////////////////////////////////////
        self.ui.horizontal_layout_frame_control_window.addWidget(self.btn_minimize)

        # CREATE AND CONFIG BTN MINIMIZE
        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_maximize = PyPushButton(self.ui.frame_control_window, btn_hover="#313237",
                                         btn_pressed="#26272b", btn_radius=4, text_padding=4)

        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(26, 26))
        self.btn_maximize.setMaximumSize(QSize(26, 26))

        # ADD ICON
        # ////////////////////////////////////////////////////////////////////////////////
        icon1 = QIcon()
        icon1.addFile(ImagePath().set_svg_icon("icon_maximize.svg"), QSize(), QIcon.Normal, QIcon.Off)

        # CONFIG ICON SIZE
        # //////////////////////////////
        self.btn_maximize.setIcon(icon1)
        self.btn_maximize.setIconSize(QSize(17, 17))

        # ADD BTN ON LAYOUT
        # /////////////////////////////////////////////////////////////////////////
        self.ui.horizontal_layout_frame_control_window.addWidget(self.btn_maximize)

        # CREATE AND CONFIG BTN CLOSE
        # //////////////////////////////////////////////////////////////////////////////
        self.btn_close = PyPushButton(self.ui.frame_control_window, btn_hover="#313237",
                                      btn_pressed="#e10000", btn_radius=4, text_padding=5)

        # //////////////////////////////////////////////////////////////////////////////
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(26, 26))
        self.btn_close.setMaximumSize(QSize(26, 26))

        # ADD ICON
        # //////////////////////////////////////////////////////////////////////////////
        icon2 = QIcon()
        icon2.addFile(ImagePath().set_svg_icon("icon_close.svg"), QSize(), QIcon.Normal, QIcon.Off)

        # ICON SIZE
        # //////////////////////////////////////////////////////////////////////////////
        self.btn_close.setIcon(icon2)
        self.btn_close.setIconSize(QSize(16, 16))

        # ADD BTN ON LAYOUT
        # //////////////////////////////////////////////////////////////////////////////
        self.ui.horizontal_layout_frame_control_window.addWidget(self.btn_close)

        # CONFIGURATION TOOLTIP
        # //////////////////////////////////////////////////////////////////////////////
        self.btn_close.setTooltipText("Fechar", self.ui.central_widget,
                                      pos_tooltip="bottom", adjust_y=-10, adjust_x=-17)

        # //////////////////////////////////////////////////////////////////////////////
        self.btn_maximize.setTooltipText("Maximizar", self.ui.central_widget,
                                         pos_tooltip="bottom", adjust_y=-10)

        # //////////////////////////////////////////////////////////////////////////////
        self.btn_minimize.setTooltipText("Minimizar", self.ui.central_widget,
                                         pos_tooltip="bottom", adjust_y=-10)

    def windowsConfiguration(self):

        # falta ajustar a posição dos btn e # estilo da janela removendo as bordas
        # ////////////////////////////////////////////////////////////////////////////////
        self.set_title_bar = True

        # ADD STYLE WINDOW
        # ////////////////////////////////////////////////////////////////////////////////
        self.ui.widget_style_sheet.setStyleSheet(QssThemes().set_qss(file_name='window_normal.qss', theme='dark'))


        # ////////////////////////////////////////////////////////////////////////////////
        self.setWindowFlags(Qt.FramelessWindowHint)  # este comando é responsavel por eliminar a barra de titulo
        self.setAttribute(Qt.WA_TranslucentBackground)  # este comando é responsavel por tornar o fundo transself.uie


        # CONENCTION
        # ////////////////////////////////////////////////////////////////////////////////
        self.btn_close.clicked.connect(lambda: self.close())
        self.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.btn_maximize.clicked.connect(lambda: SetUpMainWindow.restoreWindow(self))


        # ADD LOGO AND SVG WIDGET
        # ////////////////////////////////////////////////////////////////////////////////


        # EVENTO PARA MOVER A JANELA
        # ////////////////////////////////////////////////////////////////////////////////
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self._dragPos)
                self._dragPos = event.globalPos()  ## event.globalPos() deprecated
                event.accept()


        # EVENTO PARA MAXIMIZAR E NORMALIZAR A JANELA
        # ////////////////////////////////////////////////////////////////////////////////
        def mouseDoubleClickEvent(event):
            if event.type() == QEvent.MouseButtonDblClick:
                self.restoreWindow()

        self.ui.title_bar.mouseMoveEvent = moveWindow
        self.ui.title_bar.mouseDoubleClickEvent = mouseDoubleClickEvent


        # ADICIONAR SOMBRA NA JANELA PRINCIPAL
        # ////////////////////////////////////////////////////////////////////////////////
        self.shadow_window = QGraphicsDropShadowEffect(self)
        self.shadow_window.setBlurRadius(30)
        self.shadow_window.setXOffset(0)
        self.shadow_window.setYOffset(0)
        self.shadow_window.setColor(QColor(0, 0, 0, 60))
        self.ui.central_widget.setGraphicsEffect(self.shadow_window)


        # PONTOS DE MOVIMENTAÇÃO INSTANCIADOS
        # INSTANCED MOVEMENT POINTS
        # ////////////////////////////////////////////////////////////////////////////////
        self.left_grip = PyGrips(self, "left", True)
        self.right_grip = PyGrips(self, "right", True)
        self.top_grip = PyGrips(self, "top", True)
        self.bottom_grip = PyGrips(self, "bottom", True)
        self.top_left_grip = PyGrips(self, "top_left", True)
        self.top_right_grip = PyGrips(self, "top_right", True)
        self.bottom_left_grip = PyGrips(self, "bottom_left", True)
        self.bottom_right_grip = PyGrips(self, "bottom_right", True)

    def nonWindowConfiguration(self):

        self.set_title_bar = False

        # REMOVE WIDGETS
        # ///////////////////////////////////////////////////////////////////////////////
        self.ui.frame_logo.hide()
        self.ui.frame_control_window.hide()
        self.ui.title_bar.hide()

        # CONFIG INTERFACE NO WINDOW
        #///////////////////////////////////////////////////////////////////////////////
        self.ui.widget_style_sheet.setStyleSheet(
            QssThemes().set_qss(file_name='non_window_configuration.qss', theme='dark'))

        # REMOVE MARGIN ON WINDOW
        # //////////////////////////////////////////////////////////////////////////////
        self.ui.horizontal_layout_widget_style_sheet.setContentsMargins(0, 0, 0, 0)
        self.ui.vertical_layout_frame_line.setContentsMargins(0, 0, 0, 0)

        # ajustar o left menu float

    def restoreWindow(self):

        if not self.isMaximized():

            # REMOVE MARGIN OF WINDOW
            # //////////////////////////////////////////////////////////////////////////
            self.ui.horizontal_layout_back_ground_frame_line.setContentsMargins(0, 0, 0, 0)
            self.ui.horizontal_layout_widget_style_sheet.setContentsMargins(0, 0, 0, 0)
            self.ui.vertical_layout_frame_line.setContentsMargins(0, 0, 0, 0)

            # SHOW WINDOW MAXIMIZED
            # //////////////////////////////////////////////////////////////////////////
            self.showMaximized()

            # ADJUST STYLE OF BUTTON MAXIMIZE
            # //////////////////////////////////////////////////////////////////////////
            self.btn_maximize.setIcon(QIcon(ImagePath().set_svg_icon('icon_restore2.svg')))
            self.btn_maximize.setIconSize(QSize(20, 20))
            # self.btn_maximize.set_style(btn_hover="#313237", btn_pressed="#26272b",
            #                             btn_radius=4, text_padding=3)

            # REPLACE STYLE OF WINDOW
            # //////////////////////////////////////////////////////////////////////////
            self.ui.widget_style_sheet.setStyleSheet(QssThemes().set_qss(file_name='window_maximized.qss',
                                                                            theme='dark'))

            # Hide GRIP'S
            # ////////////////////////////////////////////////////////////////////////////////
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
            self.top_left_grip.hide()
            self.top_right_grip.hide()
            self.bottom_left_grip.hide()
            self.bottom_right_grip.hide()

        else:

            # SHOW WINDOW NORMAL
            # //////////////////////////////////////////////////////////////////////////
            self.showNormal()

            # ADD MARGIN ON WINDOW
            # //////////////////////////////////////////////////////////////////////////
            self.ui.horizontal_layout_back_ground_frame_line.setContentsMargins(1, 1, 1, 1)
            self.ui.horizontal_layout_widget_style_sheet.setContentsMargins(5, 5, 5, 5)
            self.ui.vertical_layout_frame_line.setContentsMargins(1, 1, 1, 1)

            # REPLACE STYLE BUTTON MAXIMIZE
            # //////////////////////////////////////////////////////////////////////////
            self.btn_maximize.setIcon(QIcon(ImagePath().set_svg_icon('icon_maximize.svg')))
            self.btn_maximize.setIconSize(QSize(17, 17))

            # ADJUST STYLE OF BUTTON MAXIMIZE
            # //////////////////////////////////////////////////////////////////////////
            # self.btn_maximize.set_style(btn_hover="#313237", btn_pressed="#26272b",
            #                             btn_radius=4, text_padding=4)

            # REPLACE STYLE OF WINDOW
            # //////////////////////////////////////////////////////////////////////////
            self.ui.widget_style_sheet.setStyleSheet(QssThemes().set_qss(file_name='window_normal.qss', theme='dark'))

            # Hide GRIP'S
            # ////////////////////////////////////////////////////////////////////////////////
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()
            self.top_left_grip.show()
            self.top_right_grip.show()
            self.bottom_left_grip.show()
            self.bottom_right_grip.show()

    def resizeGrips(self):
        if self.set_title_bar:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)

    def resizeLeftMenu(self, event):
        """
        RESIZE LEFT MENU FLOAT
        REDIMENSIONAR MENU ESQUERDO FLUTUANTE
        :param event:
        :return:
        """
        self.left_menu.setResize(self.ui.frame_left_menu.geometry())



if __name__ == "__main__":
    # sys.argv += ['-platform', 'windows:darkmode=2']
    # app = QApplication(sys.argv)
    # app.setApplicationDisplayName("Should be Dark Theme")
    # app.setStyle("Universal")

    app = QApplication(sys.argv)
    window = SetUpMainWindow()
    window.show()
    sys.exit(app.exec())
