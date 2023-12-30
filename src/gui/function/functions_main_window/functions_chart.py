from src.qt_core import *
from src.gui.uis.windows.main_window.ui_main_window import Ui_MainWindow

class ChartFunctions:

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def inventoryChart(self):

        self.series = QSplineSeries()
        self.series.append(0, 6)
        self.series.append(2, 4)
        self.series.append(3, 8)
        self.series.append(7, 4)
        self.series.append(10, 5)
        self.series.append(QPointF(11, 1))
        self.series.append(QPointF(13, 3))
        self.series.append(QPointF(17, 6))
        self.series.append(QPointF(18, 3))
        self.series.append(QPointF(20, 2))
        self.series.setColor(QColor(233, 234, 236))

        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.GridAxisAnimations)

        self.chart.setBackgroundBrush(QColor(47, 54, 100))
        self.chart.setBackgroundPen(QColor(47, 54, 100))

        self.chart.createDefaultAxes()

        self.chart.setContentsMargins(-7, -7, -7, -7)
        self.chart.setMargins(QMargins(10, 10, 10, 10))



        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.ui.vertical_layout_chart_inevntario.insertWidget(0, self._chart_view)
