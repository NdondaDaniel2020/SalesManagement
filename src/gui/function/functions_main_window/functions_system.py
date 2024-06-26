from src.qt_core import *
from src.gui.ui.windows.main_window.ui_main_window import Ui_MainWindow
from src.gui.widgets.py_registration_list.py_registration_list import PyRegistrationList
from src.gui.widgets.py_lista_registro_perda.py_lista_registro_perda import PyListaDePerda
from src.gui.widgets.py_lista_de_relatorio_categoria.py_lista_de_relatorio_categoria import PyListaRelatorioDeCategoria

from src.gui.function.functions_main_window.static_functions import meses_do_ano, cores_contraste_do_grafico
from src.gui.core.database import DataBase
from src.gui.core.absolute_path import AbsolutePath

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

    @Slot(None)
    def searchPerda(self):
        nome = self.ui.line_edit_pesquisa_produto_perda.text()

        objs = self.ui.scroll_area_widget_contents_perda.findChildren(PyListaDePerda)

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
            self.ui.frame_chart_bar.setMaximumWidth(height)
            self.ui.frame_chart_bar.setMinimumWidth(height)

    def autoInsertRelatorioCategoria(self):
        db = DataBase(AbsolutePath().getPathDatabase())

        db.connectDataBase()
        for i in range(1, 13):
            query = db.executarFetchall(f"""SELECT categoria, count(categoria) AS quantidade FROM vw_historico_de_venda
                                            WHERE data like '%-{i:02}-%' GROUP by categoria""")
            query_total = db.executarFetchone(f"""SELECT count(categoria) AS quantidade FROM vw_historico_de_venda
                                                  WHERE data like '%-{i:02}-%'""")
            if query:
                for item, color in zip(query, cores_contraste_do_grafico):
                    lista = PyListaRelatorioDeCategoria()
                    lista.setCategoria(item[0])
                    lista.setQuantidade(item[1], query_total[0])
                    lista.setColoProgressbar(color)
                    lista.setMes(meses_do_ano[i])
                    lista.mes_n = i
                    self.ui.vertical_layout_listas_relatorio_categoria.insertWidget(0, lista)

        db.disconnectDataBase()

    def serachRelatorioCategoria(self, mes_n):

        objs = self.ui.scroll_area_widget_contents_inventario_5.findChildren(PyListaRelatorioDeCategoria)

        if mes_n == 13:
            for obj in objs:
                obj.show()

        if objs and mes_n <= 12:
            for obj in objs:
                if mes_n != obj.mes_n:
                    obj.hide()
                else:
                    obj.show()







