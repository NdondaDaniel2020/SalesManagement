# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro_produtoyMjAHS.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
import cv2
import locale
import traceback
from rembg import remove
from src.qt_core import *
from qfluentwidgets import Slider
from src.gui.core.imagepath import ImagePath
from src.gui.widgets.py_editable_comboBox.editable_combo_box import PyEditableComboBox
from src.gui.widgets.py_slide_stacked_widgets.py_slide_stacked_widgets import PySlidingStackedWidget


class PyProductRegistration(QWidget):
    def __init__(self, widget=None) -> None:
        super().__init__(widget)

        # /////////////////////////////////////////////////////////////////
        self.setupUi(self)
        self.validator()

        # ////////////////////////////////////////////////////////////////
        self.shadow_window = QGraphicsDropShadowEffect(self)
        self.shadow_window.setBlurRadius(30)
        self.shadow_window.setXOffset(0)
        self.shadow_window.setYOffset(0)
        self.shadow_window.setColor(QColor(47, 54, 100, 40))
        self.frame_central.setGraphicsEffect(self.shadow_window)

        # ////////////////////////////////////////////////////////////////
        self.thread_pool = QThreadPool()
        self.cap = cv2.VideoCapture(0)  #'http://192.168.0.120:8080/video'

        # Create a QTimer to update the image every 100ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateImage)
        # ////////////////////////////////////////////////////////////////
        self.can_close = False
        self.first_exe = False
        self.render_file = None
        self.btn_sender = self.btn_nav_camera
        self.file_path = ImagePath().set_svg_icon("icon_gallery.svg")

        self.stackedWidget.enterEvent = self.stacked_Widget_enter_event
        self.stackedWidget.leaveEvent = self.stacked_Widget_leave_event
        self.frame_style.mousePressEvent = self.close_window_pressed_frame_style
        self.image.mousePressEvent = self.mouse_press_event_menu_image

        # ////////////////////////////////////////////////////////////////

        self.btn_del.clicked.connect(self.close)

        self.btn_nav_key.clicked.connect(self.changePosition)
        self.btn_nav_edit.clicked.connect(self.changePosition)
        self.btn_nav_camera.clicked.connect(self.changePosition)
        self.btn_nav_setting.clicked.connect(self.changePosition)

        self.btn_foto_back.clicked.connect(self.backToMainPage)

    # VALIDAÇÃO E CÓDIGO DO PAINEL
    # /////////////////////////////////////////////////////
    def addImage(self):

        languege = str(locale.getlocale()[0].lower())
        path = '~\Imagens'

        if 'en' in languege:
            path = '~\Pictures'

        path = os.path.expanduser(path)
        path = os.path.normpath(path)

        self.file_path = QFileDialog.getOpenFileName(
            parent=self,
            dir=path,
            filter=self.tr('img file (*.png *.jpeg *.jpg *.PNG *.JPG) ')
        )[0]

        if self.file_path:
            icon = QIcon()
            icon.addFile(self.file_path)

            self.image.setIconSize(QSize(250, 250))
            self.icon_img.setIconSize(QSize(30, 30))

            self.image.setIcon(icon)
            self.icon_img.setIcon(icon)

    def closeImage(self):
        icon = QIcon()
        icon.addFile(ImagePath().set_svg_icon("icon_gallery.svg"))

        self.image.setIconSize(QSize(25, 25))
        self.icon_img.setIconSize(QSize(18, 18))

        self.image.setIcon(icon)
        self.icon_img.setIcon(icon)

    def validator(self) -> None:
        """
        método de validação usando Expressões regulares
        :return:
        """
        regex_nu = QRegularExpressionValidator(QRegularExpression("^[0-9]*$"), self)
        self.lineEdit_chave.setValidator(regex_nu)
        self.lineEdit_unidade.setValidator(regex_nu)
        self.lineEdit_quantidade.setValidator(regex_nu)
        self.lineEdit_preco_venda.setValidator(regex_nu)
        self.lineEdit_preco_compra.setValidator(regex_nu)
        self.lineEdit_quantidade_reserva.setValidator(regex_nu)

    def changePosition(self):
        btn = self.sender()

        self.btn_sender = btn

        self.posAnimation = QPropertyAnimation(self.btn_activate, b'pos')
        self.posAnimation.setStartValue(QPoint(self.btn_activate.x(), self.btn_activate.y()))
        self.posAnimation.setDuration(400)
        self.posAnimation.setEndValue(
            QPoint(btn.x() + self.frame_segmented_nav.x(), btn.y() + self.frame_segmented_nav.y()))
        self.posAnimation.setEasingCurve(QEasingCurve.Type.InOutExpo)
        self.posAnimation.finished.connect(self.btn_activate.setIcon(btn.icon()))
        self.posAnimation.start()

        i1 = 0
        i2 = 0
        if btn.objectName() == 'btn_nav_camera':
            i1 = 0
        elif btn.objectName() == 'btn_nav_key':
            i1 = 1
            i2 = 0
        elif btn.objectName() == 'btn_nav_edit':
            i1 = 1
            i2 = 1

        self.stackedWidget.slideInIdx(i1)
        self.stackedWidget_2.slideInIdx(i2)

    def removeBackgroundImage(self):

        if not 'icon_gallery' in self.file_path:

            self.render_file = cv2.imread(self.file_path)
            try:
                self.render_file = remove(self.render_file)
                cv2.imwrite(self.file_path, self.render_file)
                return True
            except:
                return False

        return False

    def rotateImage(self):

        if not 'icon_gallery' in self.file_path:
            imagem = cv2.imread(self.file_path)

            height, width = imagem.shape[:2]
            center = (height / 2, width / 2)

            rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
            rotated_image = cv2.warpAffine(imagem, rotation_matrix, (width, height))

            cv2.imwrite(self.file_path, rotated_image)
            return True

        return False

    def updateImage(self, is_true):

        if is_true:
            icon = QIcon(self.file_path)

            self.image.setIconSize(QSize(250, 250))
            self.icon_img.setIconSize(QSize(30, 30))

            self.image.setIcon(icon)
            self.icon_img.setIcon(icon)

    def startBackgroundTask(self):
        btn = self.sender()

        worker = None

        if btn.objectName() == 'rembg':
            worker = Worker(self.removeBackgroundImage)  # Any other args, kwargs are passed to the run function

        elif btn.objectName() == 'rotate':
            worker = Worker(self.rotateImage)  # Any other args, kwargs are passed to the run function

        if worker:
            worker.signals.result.connect(lambda is_true: self.updateImage(is_true))
            # worker.signals.finished.connect(lambda: print("finish"))
            worker.signals.error.connect(lambda a: print("Error", a))

            # Execute
            self.thread_pool.start(worker)


    def backToMainPage(self):
        ### ///////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.group_sequential_animation = QSequentialAnimationGroup()

        ## ////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.group_animation_pos = QParallelAnimationGroup()
        self.group_animation_pos.finished.connect(lambda: self.btn_nav_key.show())
        self.group_animation_pos.finished.connect(lambda: self.btn_nav_setting.show())
        self.group_animation_pos.finished.connect(lambda: self.btn_nav_edit.show())

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.segmented_navigation_animation = QPropertyAnimation(self.frame_segmented_nav, b'pos')
        self.segmented_navigation_animation.setStartValue(QPoint(127, 405))
        self.segmented_navigation_animation.setDuration(500)
        self.segmented_navigation_animation.setEndValue(QPoint(60, 405))
        self.segmented_navigation_animation.setEasingCurve(QEasingCurve.Type.InOutExpo)

        ## ////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.group_animation_pos.addAnimation(self.segmented_navigation_animation)

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.btn_pos_animation = QPropertyAnimation(self.btn_activate, b'pos')
        self.btn_pos_animation.setStartValue(QPoint(130, 408))
        self.btn_pos_animation.setDuration(500)
        self.btn_pos_animation.setEndValue(QPoint(63, 408))
        self.btn_pos_animation.setEasingCurve(QEasingCurve.Type.InOutExpo)
        self.group_animation_pos.addAnimation(self.btn_pos_animation)

        ### ///////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.group_sequential_animation.addAnimation(self.group_animation_pos)

        ## ////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.group_animation_width = QParallelAnimationGroup()

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.segmented_navigation_animation2 = QPropertyAnimation(self.frame_segmented_nav, b'minimumWidth')
        self.segmented_navigation_animation2.setStartValue(47)
        self.segmented_navigation_animation2.setDuration(500)
        self.segmented_navigation_animation2.setEndValue(182)
        self.segmented_navigation_animation2.setEasingCurve(QEasingCurve.Type.InOutExpo)

        ## ////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.group_animation_width.addAnimation(self.segmented_navigation_animation2)

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.segmented_navigation_animation2 = QPropertyAnimation(self.frame_segmented_nav, b'maximumWidth')
        self.segmented_navigation_animation2.setStartValue(47)
        self.segmented_navigation_animation2.setDuration(500)
        self.segmented_navigation_animation2.setEndValue(182)
        self.segmented_navigation_animation2.setEasingCurve(QEasingCurve.Type.InOutExpo)

        ## ////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.group_animation_width.addAnimation(self.segmented_navigation_animation2)

        ### ///////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.group_sequential_animation.addAnimation(self.group_animation_width)

        ### ///////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.group_sequential_animation.start()
        self.stackedWidget.slideInIdx(0)
        self.timer.stop()
        print(self.cap.isOpened())
        if self.cap.isOpened():
            self.cap.release()
        self.lbl_camera.setPixmap(QPixmap())



    def makePhoto(self):
        # ///////////////////////////////////////////////////////////
        self.btn_nav_key.hide()
        self.btn_nav_setting.hide()
        self.btn_nav_edit.hide()

        # ///////////////////////////////////////////////////////////
        # self.frame_segmented_nav.setGeometry(60, 405, 47, 47)
        self.frame_segmented_nav.setMinimumSize(47, 47)
        self.frame_segmented_nav.setMaximumSize(47, 47)

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.segmented_navigation_animation = QPropertyAnimation(self.frame_segmented_nav, b'pos')
        self.segmented_navigation_animation.setStartValue(QPoint(60, 405))
        self.segmented_navigation_animation.setDuration(500)
        self.segmented_navigation_animation.setEndValue(QPoint(127, 405))
        self.segmented_navigation_animation.setEasingCurve(QEasingCurve.Type.InOutExpo)
        self.segmented_navigation_animation.start()

        self.btn_pos_animation = QPropertyAnimation(self.btn_activate, b'pos')
        self.btn_pos_animation.setStartValue(QPoint(63, 408))
        self.btn_pos_animation.setDuration(500)
        self.btn_pos_animation.setEndValue(QPoint(130, 408))
        self.btn_pos_animation.setEasingCurve(QEasingCurve.Type.InOutExpo)
        self.btn_pos_animation.start()

        # ///////////////////////////////////////////////////////////////////////
        self.btn_activate.clicked.connect(self.saveImage)
        self.lbl_camera.mouseReleaseEvent = self.saveImage
        self.stackedWidget.slideInIdx(2)
        if self.cap.isOpened():
            QTimer().singleShot(500, lambda: self.startRecording())  # 'http://192.168.0.120:8080/video'
        QTimer().singleShot(500, lambda: self.timer.start(100))

    def startRecording(self):
        self.cap = cv2.VideoCapture(0)

    def updateImage(self):
        # Read the frame from the video capture object
        ret, frame = self.cap.read()

        # Convert the frame to QImage
        try:
            height, width, channels = frame.shape
            bytes_per_line = channels * width
            qimg = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

            # centralizando 286
            rest = 0
            if width > self.lbl_camera.width():
                rest = (width - self.lbl_camera.width()) / 2
                width = width - rest

            # Convert the QImage to QPixmap
            pixmap = QPixmap.fromImage(qimg.copy(rest, 0, width, height))

            # Set the pixmap to the label
            self.lbl_camera.setPixmap(pixmap)
        except:
            pass

    def saveImage(self, event):
        # Get the current frame
        ret, frame = self.cap.read()

        # Convert the frame to QImage
        height, width, channels = frame.shape
        bytes_per_line = channels * width
        qimg = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

        # Convert the QImage to a bytes object
        qimg.save("photo1.png")

        self.file_path = "photo1.png"

        if self.file_path:
            icon = QIcon()
            icon.addFile(self.file_path)

            self.image.setIconSize(QSize(250, 250))
            self.icon_img.setIconSize(QSize(30, 30))

            self.image.setIcon(icon)
            self.icon_img.setIcon(icon)

        print("foto")

        #### levar a imagem na principal
        #### salvar o caminho da img na bd

    # /////////////////////////////////////////////////////
    def stacked_Widget_enter_event(self, event):
        self.can_close = False

    def stacked_Widget_leave_event(self, event):
        self.can_close = True

    def close_window_pressed_frame_style(self, event):
        if self.can_close:
            self.close()

    def mouse_press_event_menu_image(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton:
            self.addImage()

        if event.buttons() == Qt.RightButton:
            self.menu = Menu(self.page_foto)
            self.menu.move(event.position().x() - 50, event.position().y() + 20)

            self.menu.add.clicked.connect(self.addImage)
            self.menu.foto.clicked.connect(self.makePhoto)
            self.menu.deletar.clicked.connect(self.closeImage)
            self.menu.rembg.clicked.connect(self.startBackgroundTask)
            self.menu.rotate.clicked.connect(self.startBackgroundTask)

            self.menu.showMethod()

    # MONTAGEM DO WIDGET
    # /////////////////////////////////////////////////////
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(298, 455)
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_style = QFrame(Form)
        self.frame_style.setObjectName(u"frame_style")
        self.frame_style.setStyleSheet(u"#frame_style{\n"
                                       "   border-radius: 10px;\n"
                                       "   background-color: rgba(19, 20, 22, 50);}\n"
                                       "QStackedWidget, #btn_calendario, #icon_tag{\n"
                                       "	background-color: transparent;}\n"
                                       "\n"
                                       "#frame_chave_qrcode, #btn_chave_qrcode,\n"
                                       "#frame_continer_prima_info, #frame_quantidade,\n"
                                       "#frame_continer_preco, #frame_continer_information_adicionais{\n"
                                       "	background-color: rgb(23, 24, 26);\n"
                                       "	border-radius: 7px;}\n"
                                       "\n"
                                       "#frame_central{\n"
                                       "	background-color: rgb(19, 20, 22);\n"
                                       "	border-radius: 7px;}\n"
                                       "\n"
                                       "#btn_chave_qrcode{\n"
                                       "	background-color: rgb(32, 33, 37);\n"
                                       "	border-radius:7px;\n"
                                       "	border: 1px solid rgb(47, 54, 100)}\n"
                                       "\n"
                                       "#btn_chave_qrcode:hover{background-color: rgb(39, 40, 45);}\n"
                                       "\n"
                                       "#btn_chave_qrcode:pressed{background-color: rgb(35, 36, 41);}\n"
                                       "\n"
                                       "#informacoes_adicionais, #frame_preco_adicional,\n"
                                       "#frame_calendario, #frame_preco_adicional {\n"
                                       "	border: 1px solid rgb(47, 54, 100);\n"
                                       "	background-color: rgb(34, 35, 38);\n"
                                       "	border-radius: 6px;\n"
                                       "	color: rgb(233, 234, 236);\n"
                                       "	padding-left:5px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton{\n"
                                       "	background-color:  rgb(19, 20, 22);\n"
                                       "	border"
                                       "-radius:7px;}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "	background-color: rgb(28, 29, 32)}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "	background-color: rgb(19, 20, 22)}\n"
                                       "\n"
                                       "QLineEdit, QPlainTextEdit{\n"
                                       "border: 1px solid rgb(47, 54, 100);\n"
                                       "border-radius: 5px;\n"
                                       "background-color: rgb(32, 33, 36);\n"
                                       "color: white;padding-left:5px;}\n"
                                       "\n"
                                       "QLineEdit:hover, QPlainTextEdit:hover{background-color: rgb(30, 31, 34);}\n"
                                       "\n"
                                       "QLineEdit:focus, QPlainTextEdit:focus{background-color: rgb(37, 39, 42);}\n"
                                       "\n"
                                       "\n"
                                       "#btn_add_data, #btn_add_preco{\n"
                                       "background-color: rgb(24, 25, 27);\n"
                                       "border-radius:17px;\n"
                                       "color: rgb(233, 234, 236);}\n"
                                       "\n"
                                       "#btn_add_data:hover, #btn_add_preco:hover{background-color: rgb(39, 40, 45);}\n"
                                       "\n"
                                       "#btn_add_data:pressed, #btn_add_preco:pressed{background-color: rgb(35, 36, 41);}")
        self.frame_style.setFrameShape(QFrame.StyledPanel)
        self.frame_style.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_style)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_central = QFrame(self.frame_style)
        self.frame_central.setObjectName(u"frame_central")
        self.frame_central.setMinimumSize(QSize(296, 464))
        self.frame_central.setMaximumSize(QSize(296, 464))
        self.frame_central.setFrameShape(QFrame.StyledPanel)
        self.frame_central.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_central)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = PySlidingStackedWidget(self.frame_central)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_foto = QWidget()
        self.page_foto.setObjectName(u"page_foto")
        self.image = QPushButton(self.page_foto)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(40, 30, 220, 390))
        self.image.setStyleSheet(u"background-color: transparent;\n"
                                 "border-radius: 12px;")
        icon = QIcon()
        icon.addFile(ImagePath().set_svg_icon("icon_gallery.svg"))
        self.image.setIcon(icon)
        self.image.setIconSize(QSize(25, 25))
        self.icon_img = QPushButton(self.page_foto)
        self.icon_img.setObjectName(u"icon_img")
        self.icon_img.setGeometry(QRect(10, 10, 37, 37))
        self.icon_img.setMinimumSize(QSize(37, 37))
        self.icon_img.setMaximumSize(QSize(37, 37))
        self.icon_img.setStyleSheet(u"background-color: rgb(32, 33, 37);\n"
                                    "border-radius:7px;\n"
                                    "color: #ffffff;\n"
                                    "border: 1px solid rgb(255, 255, 255)")
        self.icon_img.setIcon(icon)
        self.icon_img.setIconSize(QSize(18, 18))
        self.frame_segmented_nav = QFrame(self.frame_central)
        self.frame_segmented_nav.setObjectName(u"frame_segmented_nav")
        self.frame_segmented_nav.setGeometry(QRect(60, 405, 182, 47))
        self.frame_segmented_nav.setMinimumSize(QSize(100, 30))
        self.frame_segmented_nav.setMaximumSize(QSize(1234578, 16777215))
        self.frame_segmented_nav.setStyleSheet(u"QFrame{background-color: rgb(19, 20, 22);"
                                               "border-radius: 10px}\n"
                                               "QPushButton{\n"
                                               "border-radius: 10px;\n"
                                               "background-color: rgb(19, 20, 22);\n"
                                               "color: rgb(233, 234, 236);}\n"
                                               "\n"
                                               "QPushButton:hover{background-color: rgb(39, 40, 45);}\n"
                                               "\n"
                                               "QPushButton:pressed{background-color: rgb(35, 36, 41);}")
        self.frame_segmented_nav.setFrameShape(QFrame.StyledPanel)
        self.frame_segmented_nav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_segmented_nav)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 0, 5, 0)
        self.btn_nav_camera = QPushButton(self.frame_segmented_nav)
        self.btn_nav_camera.setObjectName(u"btn_nav_camera")
        self.btn_nav_camera.setMinimumSize(QSize(40, 40))
        self.btn_nav_camera.setMaximumSize(QSize(40, 40))
        self.btn_nav_camera.setStyleSheet("""
        QPushButton{
                background-color: rgb(19, 20, 22);
                color: rgb(233, 234, 236);}
        QPushButton:hover{background-color: rgb(39, 40, 45);}
        QPushButton:pressed{background-color: rgb(35, 36, 41);}""")
        icon1 = QIcon()
        icon1.addFile(ImagePath().set_svg_icon("icon_camera.svg"))
        self.btn_nav_camera.setIcon(icon1)
        self.btn_nav_camera.setIconSize(QSize(27, 27))

        self.horizontalLayout_3.addWidget(self.btn_nav_camera)

        self.btn_nav_key = QPushButton(self.frame_segmented_nav)
        self.btn_nav_key.setObjectName(u"btn_nav_key")
        self.btn_nav_key.setMinimumSize(QSize(40, 40))
        self.btn_nav_key.setMaximumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(ImagePath().set_svg_icon("icon_key.svg"))
        self.btn_nav_key.setIcon(icon2)
        self.btn_nav_key.setIconSize(QSize(27, 27))

        self.horizontalLayout_3.addWidget(self.btn_nav_key)

        self.btn_nav_edit = QPushButton(self.frame_segmented_nav)
        self.btn_nav_edit.setObjectName(u"btn_nav_edit")
        self.btn_nav_edit.setMinimumSize(QSize(40, 40))
        self.btn_nav_edit.setMaximumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(ImagePath().set_svg_icon("icon_edit_text.svg"))
        self.btn_nav_edit.setIcon(icon3)
        self.btn_nav_edit.setIconSize(QSize(27, 27))

        self.horizontalLayout_3.addWidget(self.btn_nav_edit)

        self.btn_nav_setting = QPushButton(self.frame_segmented_nav)
        self.btn_nav_setting.setObjectName(u"btn_nav_setting")
        self.btn_nav_setting.setMinimumSize(QSize(40, 40))
        self.btn_nav_setting.setMaximumSize(QSize(40, 40))
        icon4 = QIcon()
        icon4.addFile(ImagePath().set_svg_icon("icon_setting.svg"))
        self.btn_nav_setting.setIcon(icon4)
        self.btn_nav_setting.setIconSize(QSize(28, 28))

        self.horizontalLayout_3.addWidget(self.btn_nav_setting)

        self.btn_activate = QPushButton(self.frame_central)
        self.btn_activate.setObjectName(u"btn_activate")
        self.btn_activate.setGeometry(QRect(63, 408, 40, 40))
        self.btn_activate.setMinimumSize(QSize(40, 40))
        self.btn_activate.setMaximumSize(QSize(40, 40))
        self.btn_activate.setStyleSheet(u"QPushButton{\n"
                                        "background-color: rgb(47, 54, 100);\n"
                                        "border-radius: 10px;\n"
                                        "color: rgb(233, 234, 236);}\n"
                                        "\n"
                                        "QPushButton:hover{background-color: rgb(50, 57, 106);}\n"
                                        "\n"
                                        "QPushButton:pressed{background-color: rgb(48, 55, 102);}\n"
                                        "")
        self.btn_activate.setIcon(icon1)
        self.btn_activate.setIconSize(QSize(27, 27))
        self.stackedWidget.addWidget(self.page_foto)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.frame_nav_bar = QFrame(self.page_3)
        self.frame_nav_bar.setObjectName(u"frame_nave_bar")
        self.frame_nav_bar.setGeometry(QRect(10, 10, 278, 45))
        self.frame_nav_bar.setMinimumSize(QSize(0, 33))
        self.frame_nav_bar.setMaximumSize(QSize(1234578, 16777215))
        self.frame_nav_bar.setStyleSheet(u"QFrame{background-color: rgb(47, 54, 100); border-radius: 7px}\n"
                                         "\n"
                                         "QPushButton{\n"
                                         "background-color: rgb(19, 20, 22);\n"
                                         "color: rgb(233, 234, 236);}\n"
                                         "\n"
                                         "QPushButton:hover{background-color: rgb(39, 40, 45);}\n"
                                         "\n"
                                         "QPushButton:pressed{background-color: rgb(35, 36, 41);}")
        self.frame_nav_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_nav_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_nav_bar)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.btn_ok = QPushButton(self.frame_nav_bar)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setMinimumSize(QSize(10, 33))
        font = QFont()
        font.setPointSize(10)
        self.btn_ok.setFont(font)
        icon5 = QIcon()
        icon5.addFile(ImagePath().set_svg_icon("icon_check_ok.svg"))
        self.btn_ok.setIcon(icon5)
        self.btn_ok.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.btn_ok)

        self.btn_scan = QPushButton(self.frame_nav_bar)
        self.btn_scan.setObjectName(u"btn_scan")
        self.btn_scan.setMinimumSize(QSize(10, 33))
        self.btn_scan.setFont(font)
        icon6 = QIcon()
        icon6.addFile(ImagePath().set_svg_icon("icon_qr_code.svg"))
        self.btn_scan.setIcon(icon6)
        self.btn_scan.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.btn_scan)

        self.btn_add = QPushButton(self.frame_nav_bar)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMinimumSize(QSize(10, 33))
        self.btn_add.setFont(font)
        icon7 = QIcon()
        icon7.addFile(ImagePath().set_svg_icon("icon_add.svg"))
        self.btn_add.setIcon(icon7)
        self.btn_add.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.btn_add)

        self.btn_camera = QPushButton(self.frame_nav_bar)
        self.btn_camera.setObjectName(u"btn_camera")
        self.btn_camera.setMinimumSize(QSize(10, 33))
        self.btn_camera.setFont(font)
        self.btn_camera.setIcon(icon1)
        self.btn_camera.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.btn_camera)

        self.btn_setting = QPushButton(self.frame_nav_bar)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setMinimumSize(QSize(10, 33))
        self.btn_setting.setFont(font)
        icon8 = QIcon()
        icon8.addFile(ImagePath().set_svg_icon("icon_setting.svg"))
        self.btn_setting.setIcon(icon8)
        self.btn_setting.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.btn_setting)

        self.btn_del = QPushButton(self.frame_nav_bar)
        self.btn_del.setObjectName(u"btn_del")
        self.btn_del.setMinimumSize(QSize(10, 33))
        self.btn_del.setFont(font)
        icon9 = QIcon()
        icon9.addFile(ImagePath().set_svg_icon("icon_delete.svg"))
        self.btn_del.setIcon(icon9)
        self.btn_del.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.btn_del)

        self.stackedWidget_2 = PySlidingStackedWidget(self.page_3)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(0, 70, 300, 371))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame_quantidade = QFrame(self.page)
        self.frame_quantidade.setObjectName(u"frame_quantidade")
        self.frame_quantidade.setGeometry(QRect(10, 270, 272, 55))
        self.frame_quantidade.setFrameShape(QFrame.StyledPanel)
        self.frame_quantidade.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_quantidade)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lineEdit_quantidade = QLineEdit(self.frame_quantidade)
        self.lineEdit_quantidade.setObjectName(u"lineEdit_quantidade")
        self.lineEdit_quantidade.setMinimumSize(QSize(0, 37))
        self.lineEdit_quantidade.setFont(font)
        self.lineEdit_quantidade.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lineEdit_quantidade)

        self.lineEdit_quantidade_reserva = QLineEdit(self.frame_quantidade)
        self.lineEdit_quantidade_reserva.setObjectName(u"lineEdit_quantidade_reserva")
        self.lineEdit_quantidade_reserva.setMinimumSize(QSize(0, 37))
        self.lineEdit_quantidade_reserva.setFont(font)
        self.lineEdit_quantidade_reserva.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lineEdit_quantidade_reserva)

        self.frame_chave_qrcode = QFrame(self.page)
        self.frame_chave_qrcode.setObjectName(u"frame_chave_qrcode")
        self.frame_chave_qrcode.setGeometry(QRect(10, 10, 272, 55))
        self.frame_chave_qrcode.setFrameShape(QFrame.StyledPanel)
        self.frame_chave_qrcode.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_chave_qrcode)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit_chave = QLineEdit(self.frame_chave_qrcode)
        self.lineEdit_chave.setObjectName(u"lineEdit_chave")
        self.lineEdit_chave.setMinimumSize(QSize(0, 37))
        self.lineEdit_chave.setFont(font)

        self.horizontalLayout_11.addWidget(self.lineEdit_chave)

        self.btn_chave_qrcode = QPushButton(self.frame_chave_qrcode)
        self.btn_chave_qrcode.setObjectName(u"btn_chave_qrcode")
        self.btn_chave_qrcode.setMinimumSize(QSize(37, 37))
        self.btn_chave_qrcode.setMaximumSize(QSize(37, 37))
        self.btn_chave_qrcode.setIcon(icon6)
        self.btn_chave_qrcode.setIconSize(QSize(22, 22))

        self.horizontalLayout_11.addWidget(self.btn_chave_qrcode)

        self.frame_continer_prima_info = QFrame(self.page)
        self.frame_continer_prima_info.setObjectName(u"frame_continer_prima_info")
        self.frame_continer_prima_info.setGeometry(QRect(10, 90, 272, 160))
        self.frame_continer_prima_info.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_prima_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_continer_prima_info)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lineEdit_unidade = QLineEdit(self.frame_continer_prima_info)
        self.lineEdit_unidade.setObjectName(u"lineEdit_unidade")
        self.lineEdit_unidade.setMinimumSize(QSize(0, 37))
        self.lineEdit_unidade.setFont(font)
        self.lineEdit_unidade.setClearButtonEnabled(False)

        self.verticalLayout_7.addWidget(self.lineEdit_unidade)

        self.combo_box_categoria = PyEditableComboBox(self.frame_continer_prima_info)
        self.combo_box_categoria.addItem("")
        self.combo_box_categoria.addItem("")
        self.combo_box_categoria.addItem("")
        self.combo_box_categoria.setObjectName(u"combo_box_categoria")
        self.combo_box_categoria.setMinimumSize(QSize(0, 37))
        self.combo_box_categoria.setFont(font)
        self.combo_box_categoria.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo_box_categoria.setStyleSheet(u"QComboBox , QLineEdit{\n"
                                               "    border: 1px solid rgb(47, 54, 100);\n"
                                               "    border-radius: 5px;\n"
                                               "    padding-left: 5px;\n"
                                               "    padding-right: -187px;\n"
                                               "	color: rgb(133, 133, 136);\n"
                                               "    background-color: rgb(32, 33, 36);\n"
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
                                               "	selection-"
                                               "background-color: rgb(195, 155, 255);\n"
                                               "	border: 2px solid  rgb(47, 54, 100);\n"
                                               "	border-radius:5px;}")
        self.combo_box_categoria.setEditable(False)
        self.combo_box_categoria.setMinimumContentsLength(0)
        self.combo_box_categoria.setDuplicatesEnabled(False)

        self.verticalLayout_7.addWidget(self.combo_box_categoria)

        self.lineEdit_nome_produto = QLineEdit(self.frame_continer_prima_info)
        self.lineEdit_nome_produto.setObjectName(u"lineEdit_nome_produto")
        self.lineEdit_nome_produto.setMinimumSize(QSize(0, 37))
        self.lineEdit_nome_produto.setFont(font)

        self.verticalLayout_7.addWidget(self.lineEdit_nome_produto)

        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame_continer_preco = QFrame(self.page_2)
        self.frame_continer_preco.setObjectName(u"frame_continer_preco")
        self.frame_continer_preco.setGeometry(QRect(10, 10, 272, 55))
        self.frame_continer_preco.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_preco.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_continer_preco)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lineEdit_preco_compra = QLineEdit(self.frame_continer_preco)
        self.lineEdit_preco_compra.setObjectName(u"lineEdit_preco_compra")
        self.lineEdit_preco_compra.setMinimumSize(QSize(0, 37))
        self.lineEdit_preco_compra.setFont(font)
        self.lineEdit_preco_compra.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.lineEdit_preco_compra)

        self.lineEdit_preco_venda = QLineEdit(self.frame_continer_preco)
        self.lineEdit_preco_venda.setObjectName(u"lineEdit_preco_venda")
        self.lineEdit_preco_venda.setMinimumSize(QSize(0, 37))
        self.lineEdit_preco_venda.setFont(font)
        self.lineEdit_preco_venda.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.lineEdit_preco_venda)

        self.frame_continer_information_adicionais = QFrame(self.page_2)
        self.frame_continer_information_adicionais.setObjectName(u"frame_continer_information_adicionais")
        self.frame_continer_information_adicionais.setGeometry(QRect(10, 90, 273, 241))
        self.frame_continer_information_adicionais.setMaximumSize(QSize(286, 262))
        self.frame_continer_information_adicionais.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_information_adicionais.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_continer_information_adicionais)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_preco_adicional = QFrame(self.frame_continer_information_adicionais)
        self.frame_preco_adicional.setObjectName(u"frame_preco_adicional")
        self.frame_preco_adicional.setMaximumSize(QSize(16777215, 80))
        self.frame_preco_adicional.setStyleSheet(u"")
        self.frame_preco_adicional.setFrameShape(QFrame.StyledPanel)
        self.frame_preco_adicional.setFrameShadow(QFrame.Raised)
        self.lbl_tag = QLabel(self.frame_preco_adicional)
        self.lbl_tag.setObjectName(u"lbl_tag")
        self.lbl_tag.setGeometry(QRect(22, 7, 220, 20))
        self.lbl_tag.setFont(font)
        self.lbl_tag.setStyleSheet(u"color: rgb(134, 134, 137)")
        self.btn_add_preco = QPushButton(self.frame_preco_adicional)
        self.btn_add_preco.setObjectName(u"btn_add_preco")
        self.btn_add_preco.setGeometry(QRect(215, 40, 35, 35))
        self.btn_add_preco.setLayoutDirection(Qt.RightToLeft)
        self.btn_add_preco.setIcon(icon7)
        self.btn_add_preco.setIconSize(QSize(33, 33))
        self.icon_tag = QPushButton(self.frame_preco_adicional)
        self.icon_tag.setObjectName(u"icon_tag")
        self.icon_tag.setGeometry(QRect(3, 6, 20, 24))
        icon10 = QIcon()
        icon10.addFile(ImagePath().set_svg_icon("icon_tag.svg"))
        self.icon_tag.setIcon(icon10)
        self.icon_tag.setIconSize(QSize(17, 17))

        self.verticalLayout_9.addWidget(self.frame_preco_adicional)

        self.frame_calendario = QFrame(self.frame_continer_information_adicionais)
        self.frame_calendario.setObjectName(u"frame_calendario")
        self.frame_calendario.setMaximumSize(QSize(16777215, 80))
        self.frame_calendario.setFrameShape(QFrame.StyledPanel)
        self.frame_calendario.setFrameShadow(QFrame.Raised)
        self.lbl_calendario = QLabel(self.frame_calendario)
        self.lbl_calendario.setObjectName(u"lbl_calendario")
        self.lbl_calendario.setGeometry(QRect(22, 7, 230, 16))
        self.lbl_calendario.setFont(font)
        self.lbl_calendario.setStyleSheet(u"color: rgb(134, 134, 137)")
        self.btn_add_data = QPushButton(self.frame_calendario)
        self.btn_add_data.setObjectName(u"btn_add_data")
        self.btn_add_data.setGeometry(QRect(215, 40, 35, 35))
        self.btn_add_data.setLayoutDirection(Qt.RightToLeft)
        self.btn_add_data.setIcon(icon7)
        self.btn_add_data.setIconSize(QSize(31, 31))
        self.btn_calendario = QPushButton(self.frame_calendario)
        self.btn_calendario.setObjectName(u"btn_calendario")
        self.btn_calendario.setGeometry(QRect(2, 4, 20, 20))
        icon11 = QIcon()
        icon11.addFile(ImagePath().set_svg_icon("icon_service.svg"))
        self.btn_calendario.setIcon(icon11)
        self.btn_calendario.setIconSize(QSize(25, 25))

        self.verticalLayout_9.addWidget(self.frame_calendario)

        self.informacoes_adicionais = QPlainTextEdit(self.frame_continer_information_adicionais)
        self.informacoes_adicionais.setObjectName(u"informacoes_adicionais")
        self.informacoes_adicionais.setMaximumSize(QSize(16777215, 55))
        self.informacoes_adicionais.setFont(font)

        self.verticalLayout_9.addWidget(self.informacoes_adicionais)

        self.stackedWidget_2.addWidget(self.page_2)
        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_6.addWidget(self.stackedWidget)

        self.page_camera = QWidget()
        self.page_camera.setObjectName(u"page_camera")
        self.lbl_camera = QLabel(self.page_camera)
        self.lbl_camera.setObjectName(u"lbl_camera")
        self.lbl_camera.setGeometry(QRect(5, 5, 286, 454))

        self.btn_foto_back = QPushButton(self.page_camera)
        self.btn_foto_back.setObjectName(u"btn_foto_back")
        self.btn_foto_back.setGeometry(QRect(5, 5, 40, 40))
        self.btn_foto_back.setMinimumSize(QSize(40, 40))
        self.btn_foto_back.setMaximumSize(QSize(40, 40))
        self.btn_foto_back.setStyleSheet("""QPushButton{
                                            background-color: rgba(19, 20, 22, 0);
                                            color: rgb(233, 234, 236);}
                                            QPushButton:hover{background-color: rgba(39, 40, 45, 40);}
                                            QPushButton:pressed{background-color: rgba(35, 36, 41, 20);}""")
        icon12 = QIcon()
        icon12.addFile(ImagePath().set_svg_icon('icon_back.svg'))
        self.btn_foto_back.setIcon(icon12)
        self.btn_foto_back.setIconSize(QSize(27, 27))

        self.stackedWidget.addWidget(self.page_camera)

        self.verticalLayout_2.addWidget(self.frame_central, 0, Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.frame_style)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.combo_box_categoria.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(Form)
        # setupUi


class Menu(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__setUp__()

    def showMethod(self):
        self.show()

        self.animation_menu = QPropertyAnimation(self, b'minimumHeight')
        self.animation_menu.setStartValue(0)
        self.animation_menu.setDuration(300)
        self.animation_menu.setEndValue(172)
        self.animation_menu.setEasingCurve(QEasingCurve.Type.InOutExpo)
        self.animation_menu.start()

    def leaveEvent(self, event):
        self.animation_menu_min = QPropertyAnimation(self, b'minimumHeight')
        self.animation_menu_min.setStartValue(172)
        self.animation_menu_min.setDuration(400)
        self.animation_menu_min.setEndValue(0)
        self.animation_menu_min.setEasingCurve(QEasingCurve.Type.InOutExpo)

        self.animation_menu_max = QPropertyAnimation(self, b'maximumHeight')
        self.animation_menu_max.setStartValue(172)
        self.animation_menu_max.setDuration(400)
        self.animation_menu_max.setEndValue(0)
        self.animation_menu_max.setEasingCurve(QEasingCurve.Type.InOutExpo)

        self.parallel_animation = QParallelAnimationGroup()
        self.parallel_animation.addAnimation(self.animation_menu_max)
        self.parallel_animation.addAnimation(self.animation_menu_min)
        self.parallel_animation.finished.connect(lambda: self.close())
        self.parallel_animation.start()

    def __setUp__(self):
        self.setStyleSheet(u"background-color: rgba(32, 33, 37, 255); border-radius: 10px;")
        self.setGeometry(0, 0, 127, 0)

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
        self.verticalLayout_30.setContentsMargins(2, 2, 2, 3)

        self.add = QPushButton(self.frame_continer)
        self.add.setObjectName(u"add")
        self.add.setMinimumSize(QSize(0, 25))
        self.add.setSizeIncrement(QSize(0, 0))

        font1 = QFont()
        font1.setFamilies([u"Segoe UI Light"])
        font1.setPointSize(11)

        self.add.setFont(font1)
        self.add.setCursor(QCursor(Qt.PointingHandCursor))
        self.add.setStyleSheet(u"QPushButton{\n"
                               "background-color: rgb(19, 20, 22);\n"
                               "border-radius: 5px;\n"
                               "color: rgb(255, 255, 255);\n"
                               "text-align: left;\n"
                               "padding-left: 0px;}\n"
                               "\n"
                               "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
                               "\n"
                               "QPushButton:pressed{background-color: rgb(33, 38, 70);}")
        self.add.setIcon(QIcon(ImagePath().set_svg_icon('icon_add.svg')))
        self.add.setIconSize(QSize(32, 32))

        self.verticalLayout_30.addWidget(self.add)

        self.foto = QPushButton(self.frame_continer)
        self.foto.setObjectName(u"deletar")
        self.foto.setMinimumSize(QSize(0, 25))
        self.foto.setSizeIncrement(QSize(0, 0))
        self.foto.setFont(font1)
        self.foto.setCursor(QCursor(Qt.PointingHandCursor))
        self.foto.setStyleSheet(u"QPushButton{\n"
                                "background-color: rgb(19, 20, 22);\n"
                                "border-radius: 5px;\n"
                                "color: rgb(255, 255, 255);\n"
                                "text-align: left;\n"
                                "padding-left: 6px;}\n"
                                "\n"
                                "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
                                "\n"
                                "QPushButton:pressed{background-color: rgb(33, 38, 70);}")

        self.foto.setIcon(QIcon(ImagePath().set_svg_icon('icon_camera.svg')))
        self.foto.setIconSize(QSize(21, 21))

        self.verticalLayout_30.addWidget(self.foto)

        self.rembg = QPushButton(self.frame_continer)
        self.rembg.setObjectName(u"rembg")
        self.rembg.setMinimumSize(QSize(0, 25))
        self.rembg.setSizeIncrement(QSize(0, 0))
        self.rembg.setFont(font1)
        self.rembg.setCursor(QCursor(Qt.PointingHandCursor))
        self.rembg.setStyleSheet(u"QPushButton{\n"
                                 "background-color: rgb(19, 20, 22);\n"
                                 "border-radius: 5px;\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "text-align: left;\n"
                                 "padding-left: 6px;}\n"
                                 "\n"
                                 "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
                                 "\n"
                                 "QPushButton:pressed{background-color: rgb(33, 38, 70);}")

        self.rembg.setIcon(QIcon(ImagePath().set_svg_icon('icon_gallery_remove.svg')))
        self.rembg.setIconSize(QSize(20, 20))

        self.verticalLayout_30.addWidget(self.rembg)

        self.rotate = QPushButton(self.frame_continer)
        self.rotate.setObjectName(u"rotate")
        self.rotate.setMinimumSize(QSize(0, 25))
        self.rotate.setSizeIncrement(QSize(0, 0))
        self.rotate.setFont(font1)
        self.rotate.setCursor(QCursor(Qt.PointingHandCursor))
        self.rotate.setStyleSheet(u"QPushButton{\n"
                                  "background-color: rgb(19, 20, 22);\n"
                                  "border-radius: 5px;\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "text-align: left;\n"
                                  "padding-left: 7px;}\n"
                                  "\n"
                                  "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
                                  "\n"
                                  "QPushButton:pressed{background-color: rgb(33, 38, 70);}")

        self.rotate.setIcon(QIcon(ImagePath().set_svg_icon('icon_rotate.svg')))
        self.rotate.setIconSize(QSize(18, 18))

        self.verticalLayout_30.addWidget(self.rotate)

        self.resize_img = QPushButton(self.frame_continer)
        self.resize_img.setObjectName(u"resize_img")
        self.resize_img.setMinimumSize(QSize(0, 25))
        self.resize_img.setSizeIncrement(QSize(0, 0))
        self.resize_img.setFont(font1)
        self.resize_img.setCursor(QCursor(Qt.PointingHandCursor))
        self.resize_img.setStyleSheet(u"QPushButton{\n"
                                      "background-color: rgb(19, 20, 22);\n"
                                      "border-radius: 5px;\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "text-align: left;\n"
                                      "padding-left: 5px;}\n"
                                      "\n"
                                      "QPushButton:hover{background-color: rgb(47, 54, 100)}\n"
                                      "\n"
                                      "QPushButton:pressed{background-color: rgb(33, 38, 70);}")

        self.resize_img.setIcon(QIcon(ImagePath().set_svg_icon('icon_size_svgrepo.svg')))
        self.resize_img.setIconSize(QSize(23, 23))

        self.verticalLayout_30.addWidget(self.resize_img)

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
        self.deletar.setIconSize(QSize(25, 21))

        self.verticalLayout_30.addWidget(self.deletar)

        self.verticalLayout_29.addWidget(self.frame_continer)

        self.verticalLayout_28.addWidget(self.frame_center)

        self.verticalLayout_27.addWidget(self.frame_line)

        self.add.setText(QCoreApplication.translate("MainWindow", u" Adicionar", None))
        self.foto.setText(QCoreApplication.translate("MainWindow", u"  Fotografia", None))
        self.rembg.setText(QCoreApplication.translate("MainWindow", u"  Remover bg", None))
        self.rotate.setText(QCoreApplication.translate("MainWindow", u"  Rotacionar", None))
        self.resize_img.setText(QCoreApplication.translate("MainWindow", u" Tamanho", None))
        self.deletar.setText(QCoreApplication.translate("MainWindow", u"  Deletar", None))


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn()
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


if __name__ == '__main__':
    import sys

    app = QApplication([])
    window = PyProductRegistration()
    window.show()
    sys.exit(app.exec())
