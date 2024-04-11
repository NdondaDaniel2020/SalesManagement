from src.qt_core import *
from src.gui.ui.windows.main_window.ui_main_window import Ui_MainWindow
from src.gui.widgets.py_dynamic_chart.py_dynamic_chart import PyDynamicChart

from src.gui.core.database import DataBase
from src.gui.core.absolute_path import AbsolutePath


class ChartFunctions:
    MES_DO_GRAFICO_DE_VENDA_SELECIONADO: int = 0

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def addInventoryChart(self):
        """
        grafico das vendas (saidas) e entradas (entrada de produto)
        :return:
        """
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

    # historico de venda
    def addHistoricBar(self):
        """
        código que cria o gráfico do historico de venda
        :return:
        """
        valor_total_dos_meses = []
        db = DataBase(AbsolutePath().getPathDatabase())
        for i in range(1, 13):
            db.connectDataBase()
            query = db.executarFetchone(f"SELECT sum(total) FROM vw_venda WHERE data like '%/{i:02}/%'")
            if query[0]:
                valor_total_dos_meses.append(query[0])
            else:
                valor_total_dos_meses.append(0)
            db.disconnectDataBase()

        self.set_0 = QBarSet("Mes")
        self.set_0.append(valor_total_dos_meses)
        self.set_0.setColor(QColor(233, 234, 236))

        self.series_bar = QBarSeries()
        self.series_bar.append(self.set_0)
        self.series_bar.clicked.connect(lambda: ChartFunctions.buscarDadosDoMesSelecionado(self))
        self.series_bar.hovered.connect(ChartFunctions.selecionarMes)

        self.chart_bar = QChart()
        self.chart_bar.addSeries(self.series_bar)
        self.chart_bar.setBackgroundBrush(QColor(255, 255, 255))
        self.chart_bar.legend().hide()

        self.categories = ["Jan", "Feb", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Sem", "Oct", "Nov", "Dez"]
        self.axis_x_bar = QBarCategoryAxis()
        self.axis_x_bar.append(self.categories)
        self.chart_bar.addAxis(self.axis_x_bar, Qt.AlignBottom)

        self.axis_y_bar = QValueAxis()
        self.axis_y_bar.setRange(0, max(valor_total_dos_meses)+1000)
        self.chart_bar.addAxis(self.axis_y_bar, Qt.AlignLeft)
        self.series_bar.attachAxis(self.axis_y_bar)

        # cor da linha x e y
        pen = self.axis_x_bar.linePen()
        pen.setColor(QColor(54, 63, 118))
        self.axis_x_bar.setLinePen(pen)

        pen = self.axis_y_bar.linePen()
        pen.setColor(QColor(54, 63, 118))
        self.axis_y_bar.setLinePen(pen)

        # grid color
        self.grid_pen_y_bar = self.axis_y_bar.gridLinePen()
        self.grid_pen_y_bar.setColor(QColor(54, 63, 118))
        self.axis_y_bar.setGridLinePen(self.grid_pen_y_bar)

        self.grid_pen_x_bar = self.axis_x_bar.gridLinePen()
        self.grid_pen_x_bar.setColor(QColor(54, 63, 118))
        self.axis_x_bar.setGridLinePen(self.grid_pen_x_bar)

        self.axis_x_bar.setLabelsColor(QColor(255, 255, 255))
        self.axis_y_bar.setLabelsColor(QColor(255, 255, 255))

        self.chart_bar.setBackgroundBrush(QColor(32, 33, 37))
        self.chart_bar.setBackgroundPen(QColor(32, 33, 37))

        self.chart_bar.legend().setVisible(False)
        self.chart_bar.legend().setAlignment(Qt.AlignBottom)

        self.chart_bar.setContentsMargins(-9, -7, -7, -7)
        self.chart_bar.setMargins(QMargins(0, 5, 10, 0))

        self._chart_view = QChartView(self.chart_bar)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.ui.vertical_layout_chart_historico_de_venda_bar.insertWidget(0, self._chart_view)

    @staticmethod
    def selecionarMes(_, mes):
        """
        responsavel por armazenar o mes selecionado
        :param _:
        :param mes:
        :return:
        """
        ChartFunctions.MES_DO_GRAFICO_DE_VENDA_SELECIONADO = mes

    def buscarDadosDoMesSelecionado(self):
        """
        responsavel po buscar pelo mes
        :return:
        """
        mes = ChartFunctions.MES_DO_GRAFICO_DE_VENDA_SELECIONADO
        self.ui.tabela_widget_de_historico_de_venda.setRowCount(0)

        select = f"SELECT * FROM vw_historico_de_venda WHERE data like '%/{mes+1:02}/%'"

        ChartFunctions.atribuirDadosNaTabelaDeHistorico(self, select)

    def atribuirDadosNaTabelaDeHistorico(self, select):
        """
        responsavel por adicionar dados na tabela do historico de venda
        :param select:
        :return:
        """
        db = DataBase(AbsolutePath().getPathDatabase())
        db.connectDataBase()
        query = db.executarFetchall(select)
        db.disconnectDataBase()

        self.ui.tabela_widget_de_historico_de_venda.setRowCount(len(query))

        for i, dados in enumerate(query):
            self.ui.tabela_widget_de_historico_de_venda.setItem(i, 0, QTableWidgetItem(str(dados[0])))
            self.ui.tabela_widget_de_historico_de_venda.setItem(i, 1, QTableWidgetItem(str(dados[2])))
            self.ui.tabela_widget_de_historico_de_venda.setItem(i, 2, QTableWidgetItem(str(dados[5])))
            self.ui.tabela_widget_de_historico_de_venda.setItem(i, 3, QTableWidgetItem(str(dados[7]).title()))
            self.ui.tabela_widget_de_historico_de_venda.setItem(i, 4, QTableWidgetItem(str(dados[6]).title()))
            self.ui.tabela_widget_de_historico_de_venda.setItem(i, 5, QTableWidgetItem(str(dados[8])))
            self.ui.tabela_widget_de_historico_de_venda.setItem(i, 6, QTableWidgetItem(str(dados[9]).title()))
            self.ui.tabela_widget_de_historico_de_venda.setItem(i, 7, QTableWidgetItem(str(dados[11])))
            self.ui.tabela_widget_de_historico_de_venda.setItem(i, 8, QTableWidgetItem(str(dados[10])))
            self.ui.tabela_widget_de_historico_de_venda.setItem(i, 9, QTableWidgetItem(str(dados[13])))
            self.ui.tabela_widget_de_historico_de_venda.setItem(i, 10, QTableWidgetItem(str(dados[12])))
            self.ui.tabela_widget_de_historico_de_venda.setItem(i, 11, QTableWidgetItem(str(dados[3])))
            self.ui.tabela_widget_de_historico_de_venda.setItem(i, 12, QTableWidgetItem(
                str(dados[1] if dados[1] else '').title()))

    def criacaoDoSelectPeloAtributo(self):
        """
        responsavel pela criação do select de acordo pelos dados dados no line edit
        no historico de venda
        :return:
        """
        txt = self.ui.line_edit_pesquisa_historico_de_venda.text()

        lista_do_dado: dict = dict()
        atribustos: list = ['id', 'nome', 'unidade', 'categoria', 'metodo_de_pagamento', 'vendedor', 'cliente']
        db: DataBase = DataBase(AbsolutePath().getPathDatabase())

        for atributo in atribustos:
            db.connectDataBase()
            query = db.executarFetchall(f"SELECT DISTINCT {atributo} FROM vw_historico_de_venda")
            lista_do_dado[f'{atributo}'] = query
            db.disconnectDataBase()

        select = 'SELECT * FROM vw_historico_de_venda'
        padrao = QRegularExpression(r"^[0-9]{2}\/[0-9]{2}\/[0-9]{4}")

        if txt:
            if txt in str(lista_do_dado['id']):
                select = f"{select} WHERE id='{txt}';"
            elif padrao.match(txt).hasMatch():
                select = f"{select} WHERE data LIKE '{txt}%';"
            elif txt in str(lista_do_dado['nome']):
                select = f"{select} WHERE nome='{txt}';"
            elif txt in str(lista_do_dado['unidade']):
                select = f"{select} WHERE unidade='{txt}';"
            elif txt in str(lista_do_dado['metodo_de_pagamento']):
                select = f"{select} WHERE metodo_de_pagamento='{txt}';"
            elif txt in str(lista_do_dado['vendedor']):
                select = f"{select} WHERE vendedor='{txt}';"
            elif txt in str(lista_do_dado['cliente']):
                select = f"{select} WHERE cliente='{txt}';"

        return select

    def pesquisarHistorico(self):
        """
        responsavel pela buca do select e inserção dos dados pesquisados
        :return:
        """
        select = ChartFunctions.criacaoDoSelectPeloAtributo(self)
        ChartFunctions.atribuirDadosNaTabelaDeHistorico(self, select.lower())

    def updateHistorico(self):
        """
        responsavel por atualizar o historico de venda
        :return:
        """
        select = "SELECT * FROM vw_historico_de_venda"
        ChartFunctions.atribuirDadosNaTabelaDeHistorico(self, select)

    def connecoesHistoricoDeVenda(self):
        """
        coneções do historico de venda
        :return:
        """
        self.ui.line_edit_pesquisa_historico_de_venda.returnPressed.connect(lambda:
                                                                            ChartFunctions.pesquisarHistorico(self))
        self.ui.btn_pesquisa_historico_de_venda.clicked.connect(lambda: ChartFunctions.pesquisarHistorico(self))
        ChartFunctions.updateHistorico(self)
    # fechamento historico de venda

    def updatCircularProgress(self):
        """
        responsavel por atualizar o o ggraficu circular do inventario
        :return:
        """

        db = DataBase(AbsolutePath().getPathDatabase())
        db.connectDataBase()
        query = db.executarFetchone("SELECT * FROM vw_nivel_atualt_do_inventario")
        db.disconnectDataBase()

        valor = float(f'{(query[0] / query[1]) * 100:.1f}')

        self.ui.circular_progress_bar.width = 150
        self.ui.circular_progress_bar.height = 150
        self.ui.circular_progress_bar.value = valor
        self.ui.circular_progress_bar.setFixedSize(215, 172)
        self.ui.circular_progress_bar.move(30, 10)
        self.ui.circular_progress_bar.font_size = 12
        self.ui.circular_progress_bar.progress_width = 6
        self.ui.circular_progress_bar.ad_shadow(True)
        self.ui.circular_progress_bar.progress_color = 0x596deb
        self.ui.circular_progress_bar.text_color = 0xE9EAEC

    def updateCircularProgress(self):
        db = DataBase(AbsolutePath().getPathDatabase())
        db.connectDataBase()
        query = db.executarFetchone("SELECT * FROM vw_nivel_atualt_do_inventario")
        db.disconnectDataBase()

        valor = float(f'{(query[0] / query[1]) * 100:.1f}')

        self.ui.circular_progress_bar.value = valor

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

        return self.dynamic_chart.timer
