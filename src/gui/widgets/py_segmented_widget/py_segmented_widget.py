from src.qt_core import *
from src.gui.core.absolute_path import AbsolutePath

class PySegmentedWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        self.btn_active = QPushButton(self)
        self.btn_active.setObjectName(u"btn_nav_key")
        self.btn_active.setGeometry(
            self.btn_nav_camera.x() + self.frame_nave_bar.x() + 3,
            self.btn_nav_camera.y() + self.frame_nave_bar.y() + 3,
            40, 40
        )
        self.btn_active.setMinimumSize(QSize(40, 40))
        self.btn_active.setMaximumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(AbsolutePath().getPathIcon("icon_key.svg"))
        self.btn_active.setIcon(icon)
        self.btn_active.setStyleSheet("""QPushButton{
background-color: rgb(47, 54, 100);
color: rgb(233, 234, 236);}
QPushButton:hover{background-color: rgb(50, 57, 106);}
QPushButton:pressed{background-color: rgb(48, 55, 102);}
""")
        self.btn_active.setIconSize(QSize(27, 27))

        self.btn_nav_key.clicked.connect(self.changePosition)
        self.btn_nav_info.clicked.connect(self.changePosition)
        self.btn_nav_camera.clicked.connect(self.changePosition)
        self.btn_nav_edit.clicked.connect(self.changePosition)

    def changePosition(self):
        btn = self.sender()

        self.posAnimation = QPropertyAnimation(self.btn_active, b'pos')
        self.posAnimation.setStartValue(QPoint(self.btn_active.x(), self.btn_active.y()))
        self.posAnimation.setDuration(400)
        self.posAnimation.setEndValue(QPoint(btn.x() + self.frame_nave_bar.x(), btn.y() + self.frame_nave_bar.y()))
        self.posAnimation.setEasingCurve(QEasingCurve.Type.InOutExpo)
        self.posAnimation.finished.connect(self.btn_active.setIcon(btn.icon()))
        self.posAnimation.start()

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(182, 47)
        Form.setStyleSheet(u"border-radius: 10px;")
        self.frame_nave_bar = QFrame(Form)
        self.frame_nave_bar.setObjectName(u"frame_nave_bar")
        self.frame_nave_bar.setGeometry(QRect(0, 0, 182, 47))
        self.frame_nave_bar.setMinimumSize(QSize(182, 47))
        self.frame_nave_bar.setMaximumSize(QSize(182, 47))
        self.frame_nave_bar.setStyleSheet(u"QFrame{background-color: rgb(19, 20, 22);}\n"
"QPushButton{\n"
"background-color: rgb(19, 20, 22);\n"
"color: rgb(233, 234, 236);}\n"
"\n"
"QPushButton:hover{background-color: rgb(39, 40, 45);}\n"
"\n"
"QPushButton:pressed{background-color: rgb(35, 36, 41);}")
        self.frame_nave_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_nave_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_nave_bar)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 0, 5, 0)
        self.btn_nav_camera = QPushButton(self.frame_nave_bar)
        self.btn_nav_camera.setObjectName(u"btn_nav_camera")
        self.btn_nav_camera.setMinimumSize(QSize(40, 40))
        self.btn_nav_camera.setMaximumSize(QSize(40, 40))
        self.btn_nav_camera.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(AbsolutePath().getPathIcon("icon_camera.svg"))
        self.btn_nav_camera.setIcon(icon3)
        self.btn_nav_camera.setIconSize(QSize(27, 27))

        self.horizontalLayout_2.addWidget(self.btn_nav_camera)

        self.btn_nav_key = QPushButton(self.frame_nave_bar)
        self.btn_nav_key.setObjectName(u"btn_nav_key")
        self.btn_nav_key.setMinimumSize(QSize(40, 40))
        self.btn_nav_key.setMaximumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(AbsolutePath().getPathIcon("icon_key.svg"))
        self.btn_nav_key.setIcon(icon)
        self.btn_nav_key.setIconSize(QSize(27, 27))

        self.horizontalLayout_2.addWidget(self.btn_nav_key)

        self.btn_nav_edit = QPushButton(self.frame_nave_bar)
        self.btn_nav_edit.setObjectName(u"btn_nav_edit")
        self.btn_nav_edit.setMinimumSize(QSize(40, 40))
        self.btn_nav_edit.setMaximumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(AbsolutePath().getPathIcon("icon_edit_text.svg"))
        self.btn_nav_edit.setIcon(icon1)
        self.btn_nav_edit.setIconSize(QSize(27, 27))

        self.horizontalLayout_2.addWidget(self.btn_nav_edit)

        self.btn_nav_info = QPushButton(self.frame_nave_bar)
        self.btn_nav_info.setObjectName(u"btn_nav_info")
        self.btn_nav_info.setMinimumSize(QSize(40, 40))
        self.btn_nav_info.setMaximumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(AbsolutePath().getPathIcon("icon_info_2.svg"))
        self.btn_nav_info.setIcon(icon2)
        self.btn_nav_info.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.btn_nav_info)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_nav_key.setText("")
        self.btn_nav_edit.setText("")
        self.btn_nav_info.setText("")
        self.btn_nav_camera.setText("")
    # retranslateUi

if __name__ == '__main__':
    import sys
    app = QApplication([])
    window = PySegmentedWidget()
    window.show()
    sys.exit(app.exec())