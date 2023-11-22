import platform

from src.qt_core import *

from ui_main_window import Ui_MainWindow

from src.gui.widgets.py_grips.py_grips import PyGrips
from src.gui.widgets.py_left_menu.py_left_menu import LeftMenu
from src.gui.widgets.py_push_button.py_push_button import PyPushButton
from src.gui.core.functions import Functions

class SetUpMainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.set_title_bar = False


        if platform.system() == 'Windows':
            # ajustar as funções do title bar
            # adicionar sombra
            # remover borda do estilo
            self.windowsConfiguration()

        else:
            # ajustar float left menu
            self.nonWindowConfiguration()



        # /////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////

        self.left_menu = LeftMenu(self.ui.frame_left_menu, self.ui.central_widget, self.geometry().height())


        self.ui.btn_close.setTooltipText("Fechar", self.ui.central_widget,
                                         pos_tooltip="bottom", adjust_y=-10, adjust_x=-17)
        self.ui.btn_maximize.setTooltipText("Maximizar", self.ui.central_widget,
                                            pos_tooltip="bottom", adjust_y=-10)
        self.ui.btn_minimize.setTooltipText("Minimizar", self.ui.central_widget,
                                            pos_tooltip="bottom", adjust_y=-10)



    def windowsConfiguration(self):
        # falta ajustar a posição dos btn e # estilo da janela removendo as bordas

        self.set_title_bar = True

        self.ui.widget_style_sheet.setStyleSheet("""#central_widget, #line_left_menu, #line_title_bar{
                                                                    background-color: rgb(32, 33, 37);
                                                                    border-radius: 8px}

                                                                #container_central_frame{
                                                                    background-color: rgb(19, 20, 22);
                                                                    border-radius: 7px;}

                                                                #scroll_area_widget_contents_left_menu, #scroll_area_left_menu{
                                                                    background-color: rgb(32, 33, 37);
                                                                    border:none}

                                                                #line_left_menu, #line_title_bar{	border:none}""")

        self.setWindowFlags(Qt.FramelessWindowHint)  # este comando é responsavel por eliminar a barra de titulo
        self.setAttribute(Qt.WA_TranslucentBackground)  # este comando é responsavel por tornar o fundo transparente

        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_maximize.clicked.connect(self.restoreWinddow)

        # EVENTO PARA MOVER A JANELA
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self._dragPos)
                self._dragPos = event.globalPos()  ## event.globalPos() deprecated
                event.accept()

        # EVENTO PARA MAXIMIZAR E NORMALIZAR A JANELA
        def mouseDoubleClickEvent(event):
            if event.type() == QEvent.MouseButtonDblClick:
                self.restoreWinddow()

        self.ui.title_bar.mouseMoveEvent = moveWindow
        self.ui.title_bar.mouseDoubleClickEvent = mouseDoubleClickEvent

        self.left_grip = PyGrips(self, "left", True)
        self.right_grip = PyGrips(self, "right", True)
        self.top_grip = PyGrips(self, "top", True)
        self.bottom_grip = PyGrips(self, "bottom", True)
        self.top_left_grip = PyGrips(self, "top_left", True)
        self.top_right_grip = PyGrips(self, "top_right", True)
        self.bottom_left_grip = PyGrips(self, "bottom_left", True)
        self.bottom_right_grip = PyGrips(self, "bottom_right", True)

    def nonWindowConfiguration(self):
        self.ui.frame_logo.hide()
        self.ui.frame_control_window.hide()
        self.ui.title_bar.hide()

        self.ui.widget_style_sheet.setStyleSheet("""#central_widget, #line_left_menu, #line_title_bar{
                                                                    background-color: rgb(32, 33, 37);
                                                                    border-radius: 0px}

                                                                #container_central_frame{
                                                                    background-color: rgb(19, 20, 22);
                                                                    border-radius: 0px;}

                                                                #scroll_area_widget_contents_left_menu, #scroll_area_left_menu{
                                                                    background-color: rgb(32, 33, 37);
                                                                    border:none}

                                                                #line_left_menu, #line_title_bar{border:none}""")  # estes estes códigos não estão a se lidos

        self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ui.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        # ajustar o left menu float

    def restoreWinddow(self):
        # falta ajustar a posição dos btn e # estilo da janela removendo as bordas
        if not self.isMaximized():
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.showMaximized()

            self.ui.btn_maximize.setIcon(QIcon(Functions().set_svg_icon('icon_restore2.svg')))
            self.ui.btn_maximize.setIconSize(QSize(20, 20))
            self.ui.btn_maximize.set_style(btn_hover="#313237",
                                           btn_pressed="#26272b",
                                           btn_radius=4, text_padding=3)

        else:
            self.showNormal()
            self.ui.horizontalLayout.setContentsMargins(5, 5, 5, 5)

            self.ui.btn_maximize.setIcon(QIcon(Functions().set_svg_icon('icon_maximize.svg')))
            self.ui.btn_maximize.setIconSize(QSize(17, 17))
            self.ui.btn_maximize.set_style(btn_hover="#313237",
                                           btn_pressed="#26272b",
                                           btn_radius=4, text_padding=4.5)

    def mousePressEvent(self, event):
        self._dragPos = event.globalPos()

    def resizeEvent(self, event):
        self.resizeLeftMenu(event)
        self.resizeGgrips()

    def resizeLeftMenu(self, event):
        self.left_menu.setResize(self.ui.frame_left_menu.geometry())

    def resizeGgrips(self):
        if self.set_title_bar:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)




if __name__ == "__main__":

    # sys.argv += ['-platform', 'windows:darkmode=2']
    # app = QApplication(sys.argv)
    # app.setApplicationDisplayName("Should be Dark Theme")
    # app.setStyle("Universal")

    app = QApplication(sys.argv)
    window = SetUpMainWindow()
    window.show()
    sys.exit(app.exec())
