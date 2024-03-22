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
import json
import pathlib
from rembg import remove
from src.qt_core import *
from qfluentwidgets import Slider
from src.gui.core.imagepath import ImagePath
from src.gui.core.json_settings import JsonSetting
from src.gui.widgets.py_editable_comboBox.editable_combo_box import PyEditableComboBox
from src.gui.widgets.py_slide_stacked_widgets.py_slide_stacked_widgets import PySlidingStackedWidget


class PyProductRegistration(QWidget):
    def __init__(self, widget=None) -> None:
        super().__init__(widget)

        # /////////////////////////////////////////////////////////////////
        self.setupUi(self)
        self.validator()
        self.getSettings()

        # ////////////////////////////////////////////////////////////////
        self.shadow_window = QGraphicsDropShadowEffect(self)
        self.shadow_window.setBlurRadius(30)
        self.shadow_window.setXOffset(0)
        self.shadow_window.setYOffset(0)
        self.shadow_window.setColor(QColor(47, 54, 100, 40))
        self.frame_central.setGraphicsEffect(self.shadow_window)

        # ////////////////////////////////////////////////////////////////
        self.cap = cv2.VideoCapture(0)  # 'http://192.168.0.120:8080/video'
        # self.countAvailableCameras()

        # Create a QTimer to update the image every 100ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.continuousImageUpdate)
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

        self.btn_setting.clicked.connect(lambda: self.btn_nav_setting.click())

        self.btn_foto_back.clicked.connect(self.backToMainPage)

        self.btn_show_categoria.clicked.connect(self.showPopupCategoria)
        self.btn_show_unidade.clicked.connect(self.showPopupUnidade)
        self.btn_show_ipwebcam.clicked.connect(self.showPopupIpwebcam)
        self.combo_box_categoria.currentTextChanged.connect(self.itemCategoriaSelected)
        self.combo_box_unidade.currentTextChanged.connect(self.itemUnidadeSelected)
        self.combo_box_ipwebcam.currentTextChanged.connect(self.itemIpwebcamSelected)

        self.checkBox.clicked.connect(self.showExep)

        self.btn_buscar_caminho.clicked.connect(self.setPhotoPath)
        self.lbl_url_diretory.mousePressEvent = lambda a: self.setPhotoPath()

    # VALIDAÇÃO E CÓDIGO DO PAINEL
    # /////////////////////////////////////////////////////
    ################### NAO TERMINDAS #############
    def showPopupCategoria(self):
        self.combo_box_categoria.showPopup()

    def itemCategoriaSelected(self, item):
        self.lineEdit_categoria.setText(item)

    def showPopupUnidade(self):
        self.combo_box_unidade.showPopup()

    def itemUnidadeSelected(self, item):
        self.lineEdit_unidade.setText(item)

    def showPopupIpwebcam(self):
        self.combo_box_ipwebcam.showPopup()

    ################### TERMINDAS #############

    def showExep(self):
        if self.checkBox.isChecked():
            self.icon_img.hide()
            self.show_exem = False
        else:
            self.icon_img.show()
            self.show_exem = True

        json_file = JsonSetting().getPathJson()
        with open(json_file, 'r') as file:
            dados = json.load(file)

        dados['registration_panel']['show_exem'] = self.show_exem
        with open(json_file, "w") as file:
            json.dump(dados, file)

    def reduceUrl(self, url: str):
        if len(url) > 24:
            url = os.path.normpath(url).split('\\')
            url = (*url[:4], '....', url[-1])
            url = '\\'.join(url)
            return url
        return url

    def setPhotoPath(self):
        photo_path = QFileDialog().getExistingDirectory()
        if photo_path:
            self.lbl_url_diretory.setText(self.reduceUrl(photo_path))
            self.image_path = photo_path

            json_file = JsonSetting().getPathJson()
            with open(json_file, 'r') as file:
                dados = json.load(file)

            dados['registration_panel']['image_path'] = photo_path
            with open(json_file, "w") as file:
                json.dump(dados, file)

    def getSettings(self):
        json_file = JsonSetting().getPathJson()
        with open(json_file, 'r') as file:
            dados = json.load(file)

        self.image_path = dados['registration_panel']['image_path']
        self.show_exem = dados['registration_panel']['show_exem']

        self.lbl_url_diretory.setText(self.reduceUrl(self.image_path))

        if self.show_exem:
            self.icon_img.show()
            self.checkBox.setChecked(False)
        else:
            self.icon_img.hide()
            self.checkBox.setChecked(True)

    def itemIpwebcamSelected(self, item):
        self.lineEdit_ipwebcam.setText(item)

    def countAvailableCameras(self):
        # Inicializa a contagem de câmeras disponíveis
        contador = 0
        for i in range(1000):
            if cv2.VideoCapture(i).read()[0]:
                contador += 1
                cv2.VideoCapture(i).release()
            else:
                self.combo_box_categoria.addItem(f"{contador - 2}")
                break

    def addImage(self):

        path = ''
        if not self.image_path:
            path = pathlib.Path().home()
            self.image_path = path
        else:
            path = self.image_path

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
        # self.combo_box_unidade.setValidator(regex_nu)
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
            i2 = 0
        elif btn.objectName() == 'btn_nav_key':
            i1 = 1
            i2 = 0
        elif btn.objectName() == 'btn_nav_edit':
            i1 = 1
            i2 = 1
        elif btn.objectName() == 'btn_nav_setting':
            i1 = 1
            i2 = 2

        self.stackedWidget.slideInIdx(i1)
        self.stackedWidget_2.slideInIdx(i2)

    def removeBackgroundImage(self):

        if not 'icon_gallery' in self.file_path:

            self.render_file = cv2.imread(self.file_path)
            try:
                self.render_file = remove(self.render_file)
                cv2.imwrite(self.file_path, self.render_file)
            except:
                pass
            else:
                self.updateProductImage()

    def rotateImage(self):

        if not 'icon_gallery' in self.file_path:
            try:
                imagem = cv2.imread(self.file_path)

                height, width = imagem.shape[:2]
                center = (height / 2, width / 2)

                rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
                rotated_image = cv2.warpAffine(imagem, rotation_matrix, (width, height))

                cv2.imwrite(self.file_path, rotated_image)
            except:
                pass
            else:
                self.updateProductImage()

    def updateProductImage(self):

        icon = QIcon(self.file_path)

        self.image.setIconSize(QSize(250, 250))
        self.icon_img.setIconSize(QSize(30, 30))

        self.image.setIcon(icon)
        self.icon_img.setIcon(icon)

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
        if not self.cap.isOpened():
            QTimer().singleShot(400, lambda: self.startRecording())  # 'http://192.168.0.120:8080/video'
        QTimer().singleShot(400, lambda: self.timer.start())

    def startRecording(self):
        self.cap = cv2.VideoCapture(0)

    def continuousImageUpdate(self):
        # Read the frame from the video capture object
        ret, frame = self.cap.read()

        # Convert the frame to QImage
        try:
            height, width, channels = frame.shape
            bytes_per_line = channels * width
            qimg = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

            rest = 0
            if width > self.lbl_camera.width():
                rest = (width - self.lbl_camera.width()) / 2
                width = width - rest

            # Convert the QImage to QPixmap
            pixmap = QPixmap.fromImage(qimg.copy(rest, 0, width - rest, height))

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

        rest = 0
        if width > self.lbl_camera.width():
            rest = (width - self.lbl_camera.width()) / 2
            width = width - rest

        # Convert the QImage to QPixmap
        qimg = QPixmap.fromImage(qimg.copy(rest, 0, width - rest, height))

        # Convert the QImage to a bytes object
        self.file_path = self.image_path + "\photo.JPEG"
        self.file_path = os.path.abspath(self.file_path)
        if os.path.exists(self.file_path):
            for i in range(1, 100_000_000):
                if not os.path.exists(self.file_path.replace('.', f'{i}.')):
                    self.file_path = self.file_path.replace('.', f'{i}.')
                    break

        qimg.save(self.file_path)

        if self.file_path:
            icon = QIcon()
            icon.addFile(self.file_path)

            self.image.setIconSize(QSize(250, 250))
            self.icon_img.setIconSize(QSize(30, 30))

            self.image.setIcon(icon)
            self.icon_img.setIcon(icon)

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
            self.menu.rotate.clicked.connect(self.rotateImage)
            self.menu.deletar.clicked.connect(self.closeImage)
            self.menu.rembg.clicked.connect(lambda: QTimer().singleShot(700, lambda: self.removeBackgroundImage()))
            self.menu.showMethod()

    # MONTAGEM DO WIDGET
    # /////////////////////////////////////////////////////
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(296, 462)
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_style = QFrame(Form)
        self.frame_style.setObjectName(u"frame_style")
        self.frame_style.setStyleSheet(u"#frame_style{\n"
                                       "	border-radius: 10px;\n"
                                       "	background-color: rgba(19, 20, 22, 25);}\n"
                                       "\n"
                                       "\n"
                                       "QStackedWidget, \n"
                                       "#btn_calendario, \n"
                                       "#icon_tag, \n"
                                       "#image{background-color: transparent;}\n"
                                       "\n"
                                       "\n"
                                       "#frame_chave_qrcode, \n"
                                       "#frame_continer_prima_info,\n"
                                       "#frame_continer_setting,\n"
                                       "#frame_show_btn_image,\n"
                                       "#frame_folder_img,\n"
                                       " #frame_quantidade,\n"
                                       "#frame_continer_preco,\n"
                                       " #frame_continer_information_adicionais{\n"
                                       "	background-color: rgb(23, 24, 26);\n"
                                       "	border-radius: 7px;}\n"
                                       "\n"
                                       "\n"
                                       "#frame_central{\n"
                                       "	background-color: rgb(19, 20, 22);\n"
                                       "	border-radius: 7px;}\n"
                                       "\n"
                                       "\n"
                                       "#btn_show_unidade,\n"
                                       "#btn_show_categoria,\n"
                                       "#btn_chave_qrcode,\n"
                                       "#btn_show_ipwebcam,\n"
                                       "#btn_buscar_caminho,\n"
                                       "#btn_count_cam{\n"
                                       "	background-color: rgb(32, 33, 37);\n"
                                       "	border-radius:7px;\n"
                                       "	border: 1px solid rgb(47, 54, 100)}\n"
                                       "\n"
                                       "#btn_show_unidade:hover,\n"
                                       "#btn_show_categoria:hover,\n"
                                       "#btn_chave_qrcode:hover,\n"
                                       "#btn_buscar_caminho:hover,\n"
                                       "#btn_count_cam:hover{background-color: rgb(39, 40, 45);}\n"
                                       "\n"
                                       ""
                                       "#btn_show_unidade:pressed,\n"
                                       "#btn_show_categoria:pressed,\n"
                                       "#btn_chave_qrcode:pressed,\n"
                                       "#btn_buscar_caminho:pressed,\n"
                                       "#btn_count_cam:pressed{background-color: rgb(35, 36, 41);}\n"
                                       "\n"
                                       "\n"
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
                                       "\n"
                                       "\n"
                                       "#frame_nav_bar{background-color: rgb(47, 54, 100); border-radius: 7px}\n"
                                       "\n"
                                       "#frame_nav_bar>QPushButton{\n"
                                       "background-color: rgb(19, 20, 22);\n"
                                       "color: rgb(233, 234, 236);}\n"
                                       "\n"
                                       "#frame_nav_bar>QPushButton:hover{background-color: rgb(39, 40, 45);}\n"
                                       "\n"
                                       "#frame_nav_bar>QPushButton:pressed{background-color: rgb(35, 36, 41);}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "QPushButton{\n"
                                       "	background-color:  rgb(19, 20, 22);\n"
                                       "	border-radius:7px;\n"
                                       "	color: #ffffff}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "	background-color: rgb(28, 29, 32)}\n"
                                       "\n"
                                       "QPus"
                                       "hButton:pressed{\n"
                                       "	background-color: rgb(19, 20, 22)}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "QLineEdit{\n"
                                       "border: 1px solid rgb(47, 54, 100);\n"
                                       "border-radius: 5px;\n"
                                       "background-color: rgb(32, 33, 36);\n"
                                       "color: white;padding-left:5px;}\n"
                                       "\n"
                                       "QLineEdit:hover{background-color: rgb(30, 31, 34);}\n"
                                       "\n"
                                       "QLineEdit:focus{background-color: rgb(37, 39, 42);}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "#btn_foto_back{\n"
                                       "background-color: rgba(19, 20, 22, 0);\n"
                                       "color: rgb(233, 234, 236);}\n"
                                       "\n"
                                       "#btn_foto_back:hover{background-color: rgba(39, 40, 45, 150);}\n"
                                       "\n"
                                       "#btn_foto_back:pressed{background-color: rgba(35, 36, 41, 120);}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "#btn_add_data, #btn_add_preco{\n"
                                       "	background-color: rgb(24, 25, 27);\n"
                                       "	border-radius:17px;\n"
                                       "	color: rgb(233, 234, 236);}\n"
                                       "\n"
                                       "#btn_add_data:hover, #btn_add_preco:hover{background-color: rgb(39, 40, 45);}\n"
                                       "\n"
                                       "#btn_add_data:pressed, #btn_add_preco:pressed{background-color: rgb(35, 36, 41);}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "QComboBox{\n"
                                       "    border: 1px solid rgb(47, 54, 100);\n"
                                       "    border-radius: "
                                       "5px;\n"
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
                                       "	selection-background-color: rgb(195, 155, 255);\n"
                                       "	border: 2px solid  rgb(47, 54, 100);\n"
                                       "	borde"
                                       "r-radius:5px;}\n"
                                       "\n"
                                       "QCheckBox{color: rgb(255, 255, 255);}\n"
                                       "QCheckBox::indicator {\n"
                                       "    border: 3px solid rgb(47, 54, 100);\n"
                                       "	width: 15px;\n"
                                       "	height: 15px;\n"
                                       "	border-radius: 10px;\n"
                                       "    background: rgb(44, 49, 60);\n"
                                       "}\n"
                                       "QCheckBox::indicator:hover {\n"
                                       "    border: 3px solid rgb(49, 57, 105);\n"
                                       "}\n"
                                       "QCheckBox::indicator:checked {\n"
                                       "    background: 3px solid rgb(47, 54, 100);\n"
                                       "	border: 3px solid rgb(44, 49, 60);\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "QLabel{color:#ffffff}\n"
                                       "")
        self.frame_style.setFrameShape(QFrame.StyledPanel)
        self.frame_style.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_style)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_central = QFrame(self.frame_style)
        self.frame_central.setObjectName(u"frame_central")
        self.frame_central.setMinimumSize(QSize(296, 462))
        self.frame_central.setMaximumSize(QSize(296, 462))
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
        self.image.setGeometry(QRect(40, 40, 220, 390))
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
        self.frame_segmented_nav.setStyleSheet(u"QFrame{background-color: rgb(19, 20, 22);}\n"
                                               "QPushButton{\n"
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
                                        "color: rgb(233, 234, 236);}\n"
                                        "\n"
                                        "QPushButton:hover{background-color: rgb(50, 57, 106);}\n"
                                        "\n"
                                        "QPushButton:pressed{background-color: rgb(48, 55, 102);}\n"
                                        "")
        self.btn_activate.setIcon(icon1)
        self.btn_activate.setIconSize(QSize(27, 27))
        self.stackedWidget.addWidget(self.page_foto)
        self.page_dados = QWidget()
        self.page_dados.setObjectName(u"page_dados")
        self.frame_nav_bar = QFrame(self.page_dados)
        self.frame_nav_bar.setObjectName(u"frame_nav_bar")
        self.frame_nav_bar.setGeometry(QRect(10, 10, 278, 45))
        self.frame_nav_bar.setMinimumSize(QSize(0, 33))
        self.frame_nav_bar.setMaximumSize(QSize(1234578, 16777215))
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
        self.btn_setting.setIcon(icon4)
        self.btn_setting.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.btn_setting)

        self.btn_del = QPushButton(self.frame_nav_bar)
        self.btn_del.setObjectName(u"btn_del")
        self.btn_del.setMinimumSize(QSize(10, 33))
        self.btn_del.setFont(font)
        icon7 = QIcon()
        icon7.addFile(ImagePath().set_svg_icon("icon_delete.svg"))
        self.btn_del.setIcon(icon7)
        self.btn_del.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.btn_del)

        self.stackedWidget_2 = PySlidingStackedWidget(self.page_dados)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(0, 70, 300, 371))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame_quantidade = QFrame(self.page)
        self.frame_quantidade.setObjectName(u"frame_quantidade")
        self.frame_quantidade.setGeometry(QRect(14, 270, 272, 55))
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
        self.frame_chave_qrcode.setGeometry(QRect(14, 10, 272, 55))
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
        self.frame_continer_prima_info.setGeometry(QRect(14, 90, 271, 161))
        self.frame_continer_prima_info.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_prima_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_continer_prima_info)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.combo_box_unidade = QComboBox(self.frame_continer_prima_info)
        self.combo_box_unidade.addItem("")
        self.combo_box_unidade.addItem("")
        self.combo_box_unidade.addItem("")
        self.combo_box_unidade.setObjectName(u"combo_box_unidade")
        self.combo_box_unidade.setMinimumSize(QSize(0, 37))
        self.combo_box_unidade.setFont(font)
        self.combo_box_unidade.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo_box_unidade.setEditable(False)
        self.combo_box_unidade.setMinimumContentsLength(0)
        self.combo_box_unidade.setDuplicatesEnabled(False)

        self.verticalLayout_4.addWidget(self.combo_box_unidade)

        self.combo_box_categoria = QComboBox(self.frame_continer_prima_info)
        self.combo_box_categoria.addItem("")
        self.combo_box_categoria.addItem("")
        self.combo_box_categoria.addItem("")
        self.combo_box_categoria.setObjectName(u"combo_box_categoria")
        self.combo_box_categoria.setMinimumSize(QSize(0, 37))
        self.combo_box_categoria.setFont(font)
        self.combo_box_categoria.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo_box_categoria.setEditable(False)
        self.combo_box_categoria.setMinimumContentsLength(0)
        self.combo_box_categoria.setDuplicatesEnabled(False)

        self.verticalLayout_4.addWidget(self.combo_box_categoria)

        self.lineEdit_nome_produto = QLineEdit(self.frame_continer_prima_info)
        self.lineEdit_nome_produto.setObjectName(u"lineEdit_nome_produto")
        self.lineEdit_nome_produto.setMinimumSize(QSize(0, 37))
        self.lineEdit_nome_produto.setFont(font)

        self.verticalLayout_4.addWidget(self.lineEdit_nome_produto)

        self.frame_custom_categoria = QFrame(self.page)
        self.frame_custom_categoria.setObjectName(u"frame_custom_categoria")
        self.frame_custom_categoria.setGeometry(QRect(22, 150, 255, 41))
        self.frame_custom_categoria.setStyleSheet(
            u"QPushButton{border-top-left-radius:0px;border-bottom-left-radius:0px;}\n"
            "QLineEdit{border-top-right-radius:0px;border-bottom-right-radius:0px;}")
        self.frame_custom_categoria.setFrameShape(QFrame.StyledPanel)
        self.frame_custom_categoria.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_custom_categoria)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_categoria = QLineEdit(self.frame_custom_categoria)
        self.lineEdit_categoria.setObjectName(u"lineEdit_categoria")
        self.lineEdit_categoria.setMinimumSize(QSize(0, 37))
        self.lineEdit_categoria.setFont(font)
        self.lineEdit_categoria.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.lineEdit_categoria)

        self.btn_show_categoria = QPushButton(self.frame_custom_categoria)
        self.btn_show_categoria.setObjectName(u"btn_show_categoria")
        self.btn_show_categoria.setMinimumSize(QSize(37, 37))
        self.btn_show_categoria.setMaximumSize(QSize(37, 37))
        self.btn_show_categoria.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(ImagePath().set_svg_icon("icon_down_arrow.svg"))
        self.btn_show_categoria.setIcon(icon8)
        self.btn_show_categoria.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_show_categoria)

        self.frame_custom_unidade = QFrame(self.page)
        self.frame_custom_unidade.setObjectName(u"frame_custom_unidade")
        self.frame_custom_unidade.setGeometry(QRect(22, 102, 255, 41))
        self.frame_custom_unidade.setStyleSheet(
            u"QPushButton{border-top-left-radius:0px;border-bottom-left-radius:0px;}\n"
            "QLineEdit{border-top-right-radius:0px;border-bottom-right-radius:0px;}")
        self.frame_custom_unidade.setFrameShape(QFrame.StyledPanel)
        self.frame_custom_unidade.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_custom_unidade)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_unidade = QLineEdit(self.frame_custom_unidade)
        self.lineEdit_unidade.setObjectName(u"lineEdit_unidade")
        self.lineEdit_unidade.setMinimumSize(QSize(0, 37))
        self.lineEdit_unidade.setFont(font)

        self.horizontalLayout_4.addWidget(self.lineEdit_unidade)

        self.btn_show_unidade = QPushButton(self.frame_custom_unidade)
        self.btn_show_unidade.setObjectName(u"btn_show_unidade")
        self.btn_show_unidade.setMinimumSize(QSize(37, 37))
        self.btn_show_unidade.setMaximumSize(QSize(37, 37))
        self.btn_show_unidade.setIcon(icon8)
        self.btn_show_unidade.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.btn_show_unidade)

        self.stackedWidget_2.addWidget(self.page)
        self.page_edit = QWidget()
        self.page_edit.setObjectName(u"page_edit")
        self.frame_continer_preco = QFrame(self.page_edit)
        self.frame_continer_preco.setObjectName(u"frame_continer_preco")
        self.frame_continer_preco.setGeometry(QRect(14, 10, 272, 55))
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

        self.frame_continer_information_adicionais = QFrame(self.page_edit)
        self.frame_continer_information_adicionais.setObjectName(u"frame_continer_information_adicionais")
        self.frame_continer_information_adicionais.setGeometry(QRect(14, 90, 273, 241))
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
        icon9 = QIcon()
        icon9.addFile(ImagePath().set_svg_icon("icon_add.svg"))
        self.btn_add_preco.setIcon(icon9)
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
        self.btn_add_data.setIcon(icon9)
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

        self.stackedWidget_2.addWidget(self.page_edit)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.frame_show_btn_image = QFrame(self.page_setting)
        self.frame_show_btn_image.setObjectName(u"frame_show_btn_image")
        self.frame_show_btn_image.setGeometry(QRect(14, 10, 272, 55))
        self.frame_show_btn_image.setFrameShape(QFrame.StyledPanel)
        self.frame_show_btn_image.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_show_btn_image)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, -1, -1, -1)
        self.checkBox = QCheckBox(self.frame_show_btn_image)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.checkBox)

        self.frame_folder_img = QFrame(self.page_setting)
        self.frame_folder_img.setObjectName(u"frame_folder_img")
        self.frame_folder_img.setGeometry(QRect(14, 90, 272, 55))
        self.frame_folder_img.setFrameShape(QFrame.StyledPanel)
        self.frame_folder_img.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_folder_img)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lbl_url_diretory = QLabel(self.frame_folder_img)
        self.lbl_url_diretory.setObjectName(u"lbl_url_diretory")
        font1 = QFont()
        font1.setBold(True)
        self.lbl_url_diretory.setFont(font1)
        self.lbl_url_diretory.setLayoutDirection(Qt.LeftToRight)
        self.lbl_url_diretory.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.lbl_url_diretory)

        self.btn_buscar_caminho = QPushButton(self.frame_folder_img)
        self.btn_buscar_caminho.setObjectName(u"btn_buscar_caminho")
        self.btn_buscar_caminho.setMinimumSize(QSize(37, 37))
        self.btn_buscar_caminho.setMaximumSize(QSize(37, 37))
        icon12 = QIcon()
        icon12.addFile(ImagePath().set_svg_icon("icon_search_folder.svg"))
        self.btn_buscar_caminho.setIcon(icon12)
        self.btn_buscar_caminho.setIconSize(QSize(18, 18))

        self.horizontalLayout_16.addWidget(self.btn_buscar_caminho)

        self.frame_continer_setting = QFrame(self.page_setting)
        self.frame_continer_setting.setObjectName(u"frame_continer_setting")
        self.frame_continer_setting.setGeometry(QRect(14, 160, 271, 61))
        self.frame_continer_setting.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_setting.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_continer_setting)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.combo_box_ipwebcam = QComboBox(self.frame_continer_setting)
        self.combo_box_ipwebcam.addItem("")
        self.combo_box_ipwebcam.addItem("")
        self.combo_box_ipwebcam.addItem("")
        self.combo_box_ipwebcam.setObjectName(u"combo_box_ipwebcam")
        self.combo_box_ipwebcam.setMinimumSize(QSize(0, 41))

        self.verticalLayout_3.addWidget(self.combo_box_ipwebcam)

        self.frame_custom_ipwebcam = QFrame(self.page_setting)
        self.frame_custom_ipwebcam.setObjectName(u"frame_custom_ipwebcam")
        self.frame_custom_ipwebcam.setGeometry(QRect(22, 169, 256, 41))
        self.frame_custom_ipwebcam.setStyleSheet(
            u"QPushButton{border-top-left-radius:0px;border-bottom-left-radius:0px;}\n"
            "QLineEdit{border-top-right-radius:0px;border-bottom-right-radius:0px;}")
        self.frame_custom_ipwebcam.setFrameShape(QFrame.StyledPanel)
        self.frame_custom_ipwebcam.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_custom_ipwebcam)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_ipwebcam = QLineEdit(self.frame_custom_ipwebcam)
        self.lineEdit_ipwebcam.setObjectName(u"lineEdit_ipwebcam")
        self.lineEdit_ipwebcam.setMinimumSize(QSize(0, 41))
        self.lineEdit_ipwebcam.setFont(font)
        self.lineEdit_ipwebcam.setStyleSheet(u"")
        self.lineEdit_ipwebcam.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lineEdit_ipwebcam)

        self.btn_show_ipwebcam = QPushButton(self.frame_custom_ipwebcam)
        self.btn_show_ipwebcam.setObjectName(u"btn_show_ipwebcam")
        self.btn_show_ipwebcam.setMinimumSize(QSize(37, 41))
        self.btn_show_ipwebcam.setMaximumSize(QSize(37, 41))
        self.btn_show_ipwebcam.setIcon(icon8)
        self.btn_show_ipwebcam.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.btn_show_ipwebcam)

        self.stackedWidget_2.addWidget(self.page_setting)
        self.stackedWidget.addWidget(self.page_dados)
        self.page_camera = QWidget()
        self.page_camera.setObjectName(u"page_camera")
        self.lbl_camera = QLabel(self.page_camera)
        self.lbl_camera.setObjectName(u"lbl_camera")
        self.lbl_camera.setGeometry(QRect(5, 5, 286, 454))
        self.btn_foto_back = QPushButton(self.page_camera)
        self.btn_foto_back.setObjectName(u"btn_foto_back")
        self.btn_foto_back.setGeometry(QRect(5, 5, 37, 37))
        self.btn_foto_back.setMinimumSize(QSize(37, 37))
        self.btn_foto_back.setMaximumSize(QSize(37, 37))
        icon13 = QIcon()
        icon13.addFile(ImagePath().set_svg_icon("icon_back.svg"))
        self.btn_foto_back.setIcon(icon13)
        self.btn_foto_back.setIconSize(QSize(18, 18))
        self.stackedWidget.addWidget(self.page_camera)

        self.verticalLayout_6.addWidget(self.stackedWidget)

        self.verticalLayout_2.addWidget(self.frame_central, 0, Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.frame_style)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.combo_box_unidade.setCurrentIndex(-1)
        self.combo_box_categoria.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit_quantidade.setPlaceholderText(QCoreApplication.translate("Form", u"Quantidade", None))
        self.lineEdit_quantidade_reserva.setPlaceholderText(
            QCoreApplication.translate("Form", u"Quantidade Reserva", None))
        self.lineEdit_chave.setPlaceholderText(QCoreApplication.translate("Form", u"Chave", None))

        self.combo_box_unidade.setItemText(0, QCoreApplication.translate("Form", u"New Item 0", None))
        self.combo_box_unidade.setItemText(1, QCoreApplication.translate("Form", u"New Item 1", None))
        self.combo_box_unidade.setItemText(2, QCoreApplication.translate("Form", u"New Item 2", None))

        self.combo_box_unidade.setPlaceholderText(QCoreApplication.translate("Form", u"Unidade", None))
        self.combo_box_categoria.setItemText(0, QCoreApplication.translate("Form", u"New Item 1", None))
        self.combo_box_categoria.setItemText(1, QCoreApplication.translate("Form", u"New Item 2", None))
        self.combo_box_categoria.setItemText(2, QCoreApplication.translate("Form", u"New Item 3", None))

        self.combo_box_categoria.setPlaceholderText(QCoreApplication.translate("Form", u"Categoria", None))
        self.lineEdit_nome_produto.setPlaceholderText(QCoreApplication.translate("Form", u"Nome do produto", None))
        self.lineEdit_categoria.setPlaceholderText(QCoreApplication.translate("Form", u"categoria", None))

        self.lineEdit_unidade.setPlaceholderText(QCoreApplication.translate("Form", u"unidade", None))

        self.lineEdit_preco_compra.setPlaceholderText(
            QCoreApplication.translate("Form", u"Pre\u00e7o de compra", None))
        self.lineEdit_preco_venda.setPlaceholderText(
            QCoreApplication.translate("Form", u"Pre\u00e7o de venda", None))
        self.lbl_tag.setText(QCoreApplication.translate("Form", u"Pre\u00e7os adicional de venda(opcional)", None))
        self.lbl_calendario.setText(
            QCoreApplication.translate("Form", u"Data de expira\u00e7\u00e3o do produto(opcional)", None))
        self.informacoes_adicionais.setPlaceholderText(
            QCoreApplication.translate("Form", u"Informa\u00e7\u00f5es adicionais sobre o produto (opcional)",
                                       None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Mostrar exemplo da imagem minimizada", None))
        self.lbl_url_diretory.setText(QCoreApplication.translate("Form", u"C:\\Users\\Daniel\\Videos\\.....\\Music", None))

        self.combo_box_ipwebcam.setItemText(0, QCoreApplication.translate("Form", u"New Item 0", None))
        self.combo_box_ipwebcam.setItemText(1, QCoreApplication.translate("Form", u"New Item 1", None))
        self.combo_box_ipwebcam.setItemText(2, QCoreApplication.translate("Form", u"New Item 2", None))

        self.combo_box_ipwebcam.setPlaceholderText(QCoreApplication.translate("Form", u"ipwebcam", None))
        self.lineEdit_ipwebcam.setPlaceholderText(QCoreApplication.translate("Form", u"Ipwebcam", None))
    # retranslateUi


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


if __name__ == '__main__':
    import sys

    app = QApplication([])
    window = PyProductRegistration()
    window.show()
    sys.exit(app.exec())
