from src.qt_core import *
from src.gui.uis.windows.main_window.ui_main_window import Ui_MainWindow
from src.gui.widgets.py_dynamic_chart.py_dynamic_chart import PyDynamicChart

class ChartFunctions:

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def addInventoryChart(self):

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

        self.axis_x = self.chart.axes(Qt.Horizontal)[0]
        self.axis_y = self.chart.axes(Qt.Vertical)[0]
        # self.axis_y.setRange(0, 20)

        self.axis_x.setLabelsColor(QColor(255, 255, 255))
        self.axis_y.setLabelsColor(QColor(255, 255, 255))

        self.chart.setContentsMargins(-7, -7, -7, -7)
        self.chart.setMargins(QMargins(5, 5, 5, 5))

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.ui.vertical_layout_chart_inevntario.insertWidget(0, self._chart_view)


    def addBarChartOnHomepage(self):
        grid_color = QColor(54, 63, 118)

        # CRIAR AS BARRAS
        self.set_0 = QBarSet("Saida")
        self.set_1 = QBarSet("Entrada")

        # COR DAS BARRAS
        self.set_0.setColor(QColor(241, 2, 121))
        self.set_1.setColor(QColor(233, 234, 236))

        # ADICIONAR DADOS DAS BARRAS
        self.set_0.append((5, 3, 4, 7, 2))
        self.set_1.append((9, 8, 7, 6, 5))

        # MUDAR COR DA LABEL DOS BAR
        self.set_0.setLabelColor(QColor(255, 255, 255))
        self.set_1.setLabelColor(QColor(255, 255, 255))

        # CRIAR A SERIES X DAS BARRAS
        self.series = QBarSeries()
        self.series.append(self.set_0)
        self.series.append(self.set_1)

        # CRIAR O GRAFICO
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setBackgroundBrush(QColor(32, 33, 37))
        # self.chart.setAnimationOptions(QChart.AllAnimations)
        self.chart.setContentsMargins(-7, -7, -7, -7)
        self.chart.setMargins(QMargins(-2, 3, 10, 0))

        # ADICIONAR O NOME DAS CATEGORIA
        self.categories = (1, 2, 3, 4, 5)

        # CRIAR GREAD AUTOMATICA
        self.chart.createDefaultAxes()

        # PEGAR OS DADOS DAS GRID
        self.axis_x = self.chart.axes(Qt.Horizontal)[0]
        self.axis_y = self.chart.axes(Qt.Vertical)[0]
        self.axis_y.setRange(0, 20)

        # MUDAR A COR DA LABEL
        self.axis_x.setLabelsColor(QColor(255, 255, 255))
        self.axis_y.setLabelsColor(QColor(255, 255, 255))

        # MUDAR A COR DA GRID Y
        pen = self.axis_y.linePen()
        pen.setColor(grid_color)
        self.axis_y.setLinePen(pen)

        self.grid_pen_y = self.axis_y.gridLinePen()
        self.grid_pen_y.setColor(grid_color)
        self.axis_y.setGridLinePen(self.grid_pen_y)

        # MUDAR A COR DA GRID X
        pen = self.axis_x.linePen()
        pen.setColor(grid_color)
        self.axis_x.setLinePen(pen)

        self.grid_pen_x = self.axis_x.gridLinePen()
        self.grid_pen_x.setColor(grid_color)
        self.axis_x.setGridLinePen(self.grid_pen_x)

        # CRIA O OBJETO QUE MOSTRA O GRÁFIOCO
        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        # APAGAR A LEGENDA
        self._chart_view.chart().legend().hide()

        self.ui.vertical_layout_char_bar.addWidget(self._chart_view)


    def addDynamicLineChart(self):
        self.dynamic_chart = PyDynamicChart()
        self.dynamic_chart.legend().hide()
        self.dynamic_chart.setAnimationOptions(QChart.AllAnimations)

        self.dynamic_chart.setBackgroundBrush(QColor(32, 33, 37))
        self.dynamic_chart.setContentsMargins(-7, -7, -7, -7)
        self.dynamic_chart.setMargins(QMargins(-2, 3, 10, 0))

        self.axis_x = self.dynamic_chart.axes(Qt.Horizontal)[0]
        self.axis_y = self.dynamic_chart.axes(Qt.Vertical)[0]

        self.axis_x.setLabelsColor(QColor(255, 255, 255))
        self.axis_y.setLabelsColor(QColor(255, 255, 255))


        pen = self.axis_y.linePen()
        pen.setColor(QColor(54, 63, 118))
        self.axis_y.setLinePen(pen)

        self.grid_pen_y = self.axis_y.gridLinePen()
        self.grid_pen_y.setColor(QColor(54, 63, 118))
        self.axis_y.setGridLinePen(self.grid_pen_y)

        # MUDAR A COR DA GRID X
        pen = self.axis_x.linePen()
        pen.setColor(QColor(54, 63, 118))
        self.axis_x.setLinePen(pen)

        self.grid_pen_x = self.axis_x.gridLinePen()
        self.grid_pen_x.setColor(QColor(54, 63, 118))
        self.axis_x.setGridLinePen(self.grid_pen_x)

        self.dynamic_chart_view = QChartView(self.dynamic_chart)
        self.dynamic_chart_view.setRenderHint(QPainter.Antialiasing)

        self.ui.vertical_layout_dynamic_chart.addWidget(self.dynamic_chart_view)

