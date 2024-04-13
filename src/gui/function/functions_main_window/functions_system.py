from src.qt_core import *
from src.gui.ui.windows.main_window.ui_main_window import Ui_MainWindow
from src.gui.widgets.py_registration_list.py_registration_list import PyRegistrationList


class FunctionsSystem:

    def __init__(self) -> None:
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

    def finishedChart(self) -> None:
        if self.ui.frame_char.height() == 0:
            self.ui.frame_char.hide()

    @Slot(None)
    def searchProduct(self):
        nome = self.ui.line_edit_pesquisa_produto.text()

        objs = self.ui.scroll_area_widget_contents_inventario.findChildren(PyRegistrationList)

        if not nome:
            for obj in objs:
                obj.show()
        else:
            for obj in objs:
                obj.hide()
                if nome.lower() in obj.nome_produto.text().lower():
                    obj.show()

    def resizeFrameChartWidth(self):
        height = self.ui.frame_chart_bar.size().height()
        width = self.ui.frame_chart_bar.size().width()

        if height > 154:
            # self.group_animation = QParallelAnimationGroup()
            #
            # self.maximum_animation = QPropertyAnimation(self.ui.frame_chart_bar, b'maximumWidth')
            # self.maximum_animation.setStartValue(width)
            # self.maximum_animation.setDuration(400)
            # self.maximum_animation.setEndValue(height)
            # self.maximum_animation.setEasingCurve(QEasingCurve.Type.InOutCirc)
            #
            # self.group_animation.addAnimation(self.maximum_animation)
            #
            # self.minimum_animation = QPropertyAnimation(self.ui.frame_chart_bar, b'minimumWidth')
            # self.minimum_animation.setStartValue(width)
            # self.minimum_animation.setDuration(400)
            # self.minimum_animation.setEndValue(height)
            # self.minimum_animation.setEasingCurve(QEasingCurve.Type.InOutCirc)
            #
            # self.group_animation.addAnimation(self.minimum_animation)
            #
            # self.group_animation.start()

            self.ui.frame_chart_bar.setMaximumWidth(height)
            self.ui.frame_chart_bar.setMinimumWidth(height)

# : https://doc.qt.io/qt-6/qt.html#Key-enum


