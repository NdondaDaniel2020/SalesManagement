from src.qt_core import *
from src.gui.uis.windows.main_window.ui_main_window import Ui_MainWindow

class ChartFunctions:

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def inventoryChart(self):

        series_max = QSplineSeries()
        series_max.append(0, 6)
        series_max.append(2, 4)
        series_max.append(3, 8)
        series_max.append(7, 4)
        series_max.append(10, 5)
        series_max.append(QPointF(11, 1))
        series_max.append(QPointF(13, 3))
        series_max.append(QPointF(17, 6))
        series_max.append(QPointF(18, 3))
        series_max.append(QPointF(20, 2))
        series_max.setColor(QColor(233, 234, 236))

        series_min = QSplineSeries()
        series_min.append(QPointF(0, 1))
        series_min.append(QPointF(3, 3))
        series_min.append(QPointF(6, 6))
        series_min.append(QPointF(8, 3))
        series_min.append(QPointF(10, 2))
        series_min.append(QPointF(11, 9))
        series_min.append(QPointF(13, 4))
        series_min.append(QPointF(17, 11))
        series_min.append(QPointF(18, 5))
        series_min.append(QPointF(20, 8))
        series_min.setColor(QColor(233, 0, 0))

        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(series_max)
        self.chart.addSeries(series_min)
        # self.chart.setAnimationOptions(QChart.GridAxisAnimations)

        self.chart.setBackgroundBrush(QColor(47, 54, 100))
        self.chart.setBackgroundPen(QColor(47, 54, 100))

        self.chart.createDefaultAxes()

        self.chart.setContentsMargins(-7, -7, -7, -7)
        self.chart.setMargins(QMargins(10, 10, 10, 10))



        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.ui.vertical_layout_chart_inevntario.insertWidget(0, self._chart_view)
