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

    @Slot(None)
    def resizeFrameChart(self) -> None:

        height_start = 190
        height_end = 0

        if self.ui.frame_char.height() != 190:
            self.ui.frame_char.show()
            height_start = 0
            height_end = 190

        self.animation_frame_chart_min = QPropertyAnimation(self.ui.frame_char, b'minimumHeight')
        self.animation_frame_chart_min.setStartValue(height_start)
        self.animation_frame_chart_min.setDuration(500)
        self.animation_frame_chart_min.setEndValue(height_end)
        self.animation_frame_chart_min.setEasingCurve(QEasingCurve.Type.InOutCubic)

        self.animation_frame_chart_max = QPropertyAnimation(self.ui.frame_char, b'maximumHeight')
        self.animation_frame_chart_max.setStartValue(height_start)
        self.animation_frame_chart_max.setDuration(500)
        self.animation_frame_chart_max.setEndValue(height_end)
        self.animation_frame_chart_max.setEasingCurve(QEasingCurve.Type.InOutCubic)

        self.parallel_animation_chart = QParallelAnimationGroup()
        self.parallel_animation_chart.addAnimation(self.animation_frame_chart_min)
        self.parallel_animation_chart.addAnimation(self.animation_frame_chart_max)
        self.parallel_animation_chart.finished.connect(lambda: FunctionsSystem.finishedChart(self))
        self.parallel_animation_chart.start()

    def finishedChart(self):
        if self.ui.frame_char.height() == 0:
            self.ui.frame_char.hide()




# : https://doc.qt.io/qt-6/qt.html#Key-enum


