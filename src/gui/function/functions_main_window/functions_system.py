from src.qt_core import *
from src.gui.uis.windows.main_window.ui_main_window import Ui_MainWindow

class FunctionsSystem:

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @Slot(None)
    def resizeLeftColumn(self) -> None:
        width = self.ui.left_column.width()

        width_init = 0
        width_end = 200

        width_qr_init = 0
        width_qr_end = 200

        if width != 0:
            width_init = 200
            width_end = 0

            width_qr_init = 200
            width_qr_end = 0

        self.animation_left_column = QPropertyAnimation(self.ui.left_column, b'minimumWidth')

        self.animation_left_column.setStartValue(width_init)
        self.animation_left_column.setDuration(500)
        self.animation_left_column.setEndValue(width_end)
        self.animation_left_column.setEasingCurve(QEasingCurve.Type.InOutCubic)

        self.animation_qrcode = QPropertyAnimation(self.ui.frame_qrcode, b'minimumWidth')

        self.animation_qrcode.setStartValue(width_qr_init)
        self.animation_qrcode.setDuration(500)
        self.animation_qrcode.setEndValue(width_qr_end)
        self.animation_qrcode.setEasingCurve(QEasingCurve.Type.InOutCubic)

        self.left_column_parallel_animation_group = QParallelAnimationGroup()
        self.left_column_parallel_animation_group.stop()
        self.left_column_parallel_animation_group.addAnimation(self.animation_left_column)
        self.left_column_parallel_animation_group.addAnimation(self.animation_qrcode)
        self.left_column_parallel_animation_group.start()








