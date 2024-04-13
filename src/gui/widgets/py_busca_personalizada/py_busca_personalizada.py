# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'busca_personalizadaTJzSMh.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from src.qt_core import *
from src.gui.core.database import DataBase
from src.gui.core.absolute_path import AbsolutePath


class PyBuscaPersonalizada(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMaximumHeight(149)
        self.__setupUi(self)
        self.__autoInsert()
        self.__validator()
        self.btn_busca.clicked.connect(self.__filtragemDeDados)

    def __validator(self) -> None:
        """
        Responsavel por validar apenas caracteres desejado
        :return:
        """
        regex_id = QRegularExpressionValidator(QRegularExpression("^[0-9]*$"), self)
        regex_valor = QRegularExpressionValidator(QRegularExpression("^[0-9,.]*$"), self)

        self.let_id_valor.setValidator(regex_id)
        self.let_total_valor.setValidator(regex_valor)

    def __autoInsert(self) -> None:
        """
        responsavel pela auto inserção dos dados na GUi
        :return:
        """
        db: DataBase = DataBase(AbsolutePath().getPathDatabase())
        db.connectDataBase()
        query_categoria: list[any] = db.executarFetchall(f"SELECT DISTINCT nome FROM categoria")
        query_unidade: list[any] = db.executarFetchall(f"SELECT DISTINCT nome FROM unidade")
        query_cliente: list[any] = db.executarFetchall(f"SELECT DISTINCT nome FROM cliente")
        query_usuario: list[any] = db.executarFetchall(f"SELECT DISTINCT nome FROM usuario")
        db.disconnectDataBase()

        for i in query_categoria:
            self.com_categoria.addItem(i[0].title())

        for i in query_unidade:
            self.com_unidade.addItem(i[0].title())

        for i in query_cliente:
            self.com_cliente.addItem(i[0].title())

        for i in query_usuario:
            self.com_vendedor.addItem(i[0])

    def __filtragemDeDados(self):
        """
        responsavel pela filtragem dis dados para busca
        :return:
        """
        dados = {}

        ini = self.date_time_edit_inicio.dateTime().toString("dd/MM/yyyy HH:mm:ss")
        fim = self.date_time_edit_fim.dateTime().toString("d/MM/yyyy HH:mm:ss")

        if self.let_id_valor.text():
            dados['id'] = f"id={self.let_id_valor.text()}"

        if self.let_nome_produto.text():
            dados['nome'] = f"nome='{self.let_nome_produto.text().lower()}'"

        if self.com_categoria.currentText():
            dados['categoria'] = f"categoria='{self.com_categoria.currentText().lower()}'"

        if self.com_unidade.currentText():
            dados['unidade'] = f"unidade='{self.com_unidade.currentText().lower()}'"

        if self.com_cliente.currentText():
            dados['cliente'] = f"cliente='{self.com_cliente.currentText().lower()}'"

        if self.com_vendedor.currentText():
            dados['vendedor'] = f"vendedor='{self.com_vendedor.currentText()}'"

        if self.com_total_operador.currentText() and self.let_total_valor.text():
            dados['total_operador'] = f"total{self.com_total_operador.currentText()}{self.let_total_valor.text()}"

        if ini == fim and ini != '1/1/2000 00:00:00':
            dados['data'] = f"data='{ini}'"
        elif not fim in ini:
            dados['data'] = f"data BETWEEN '{ini}' AND '{fim}'"

        return dados

    def criarDoSelect(self):
        """
        responsavel criar por select que fara a busca dos dados
        :return:
        """
        dados = self.__filtragemDeDados()
        select = 'SELECT * FROM vw_historico_de_venda'

        if dados.keys():
            select += f" WHERE"
            for i, value in enumerate(dados.values()):
                select += f" {value}"
                if i != len(dados.values())-1:
                    select += " AND"

        return select

    def __setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(586, 146)
        Form.setMaximumSize(QSize(16777215, 149))
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_borda_esterior = QFrame(Form)
        self.frame_borda_esterior.setObjectName(u"frame_borda_esterior")
        self.frame_borda_esterior.setMaximumSize(QSize(16777215, 149))
        self.frame_borda_esterior.setStyleSheet(u"*{color: rgb(255, 255, 255)}\n"
                                                "\n"
                                                "#frame_continer_bottom,"
                                                "#frame_continer_top_center{background-color: transparent}"
                                                "\n"
                                                "QLabel{background-color: transparent}\n"
                                                "\n"
                                                "\n#frame_continer_total,"
                                                "#frame_continer_data{background-color: transparent}\n"
                                                "\n"
                                                "#frame_borda_esterior{\n"
                                                "	border-radius: 12px;\n"
                                                "	background-color: rgb(28, 29, 32);}\n"
                                                "\n"
                                                "#frame_border_continer{	\n"
                                                "	background-color: rgb(19, 20, 22);\n"
                                                "	border-radius: 10px;}\n"
                                                "\n"
                                                "#frame_continer_center_2 > *{\n"
                                                "   background-color: transparent;}\n" 
                                                "#frame_continer_center > *{\n"
                                                "    background-color: transparent;}\n"
                                                "#frame_border_continer > QFrame{\n"
                                                "	background-color: rgb(28, 29, 32);\n"
                                                "	border-radius: 10px;}\n"
                                                "\n"
                                                "#frame_central_1 QFrame{background-color: rgb(28, 29, 32);}\n"
                                                "\n"
                                                "QPushButton {\n"
                                                "  color: rgb(233, 234, 236);\n"
                                                "  background-color: rgb(38, 38, 42);\n"
                                                "  border: none;\n"
                                                "  border-radius: 6px;\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "  background-color: rgb(41, 41, 45)\n"
                                                "}\n"
                                                "QPushButton:pressed {\n"
                                                "  background-color: rgb(38, 39, 43);\n"
                                                "}\n"
                                                "\n"
                                                "QDateTimeEdit{\n"
                                                "    bor"
                                                "der-bottom: 1px solid rgb(240, 240, 240);\n"
                                                "	border-radius: 0px;\n"
                                                "	color: rgb(133, 133, 136);\n"
                                                "    background-color: rgb(28, 29, 32);\n"
                                                "    text-align: left;\n"
                                                "}\n"
                                                "\n"
                                                "QDateTimeEdit:hover {\n"
                                                "	background-color: rgb(30, 31, 34);\n"
                                                "}\n"
                                                "\n"
                                                "QDateTimeEdit:focus{\n"
                                                "    background-color: rgb(35, 36, 40);\n"
                                                "	color: rgb(240, 240, 240);\n"
                                                "}\n"
                                                "\n"
                                                "\n"
                                                "QLineEdit{\n"
                                                "    border-bottom: 1px solid rgb(240, 240, 240);\n"
                                                "	border-radius: 0px;\n"
                                                "	color: rgb(133, 133, 136);\n"
                                                "    background-color: rgb(28, 29, 32);\n"
                                                "    text-align: left;\n"
                                                "}\n"
                                                "\n"
                                                "QLineEdit:hover {\n"
                                                "	background-color: rgb(30, 31, 34);\n"
                                                "}\n"
                                                "\n"
                                                " QLineEdit:focus{\n"
                                                "    background-color: rgb(35, 36, 40);\n"
                                                "	color: rgb(240, 240, 240);\n"
                                                "}\n"
                                                "\n"
                                                "\n"
                                                "QComboBox{\n"
                                                "    border-bottom: 1px solid rgb(240, 240, 240);\n"
                                                "	border-radius: 0px;\n"
                                                "	color: rgb(133, 133, 136);\n"
                                                "    background-color: rgb(28, 29, 32);\n"
                                                "    text-align: left;\n"
                                                "}\n"
                                                "\n"
                                                "QComboBox:hover {\n"
                                                "	background-color: rgb(30, 31, "
                                                "34);\n"
                                                "}\n"
                                                "\n"
                                                "QComboBox:pressed , QComboBox:focus{\n"
                                                "    background-color: rgb(35, 36, 40);\n"
                                                "	color: rgb(240, 240, 240);\n"
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
                                                "	border: 1px solid  rgb(240, 240, 240);\n"
                                                "	border-radius:5px;}\n"
                                                "\n"
                                                "")
        self.frame_borda_esterior.setFrameShape(QFrame.StyledPanel)
        self.frame_borda_esterior.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_borda_esterior)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_continer_top_center = QFrame(self.frame_borda_esterior)
        self.frame_continer_top_center.setObjectName(u"frame_continer_top_center")
        self.frame_continer_top_center.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_top_center.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_continer_top_center)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 2)
        self.frame_border_continer = QFrame(self.frame_continer_top_center)
        self.frame_border_continer.setObjectName(u"frame_border_continer")
        self.frame_border_continer.setFrameShape(QFrame.StyledPanel)
        self.frame_border_continer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_border_continer)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.frame_continer_center = QFrame(self.frame_border_continer)
        self.frame_continer_center.setObjectName(u"frame_continer_center")
        self.frame_continer_center.setStyleSheet(u"")
        self.frame_continer_center.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_continer_center)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(8, 0, 8, 0)
        self.frame_id = QFrame(self.frame_continer_center)
        self.frame_id.setObjectName(u"frame_id")
        self.frame_id.setMinimumSize(QSize(0, 0))
        self.frame_id.setMaximumSize(QSize(12345678, 16777215))
        self.frame_id.setFrameShape(QFrame.StyledPanel)
        self.frame_id.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_id)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.lbl_id = QLabel(self.frame_id)
        self.lbl_id.setObjectName(u"lbl_id")
        self.lbl_id.setMaximumSize(QSize(16777215, 13))
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        self.lbl_id.setFont(font)
        self.lbl_id.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lbl_id)

        self.let_id_valor = QLineEdit(self.frame_id)
        self.let_id_valor.setObjectName(u"let_id_valor")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.let_id_valor.sizePolicy().hasHeightForWidth())
        self.let_id_valor.setSizePolicy(sizePolicy)
        self.let_id_valor.setMinimumSize(QSize(0, 17))
        self.let_id_valor.setMaximumSize(QSize(16777215, 20))
        self.let_id_valor.setMaxLength(1000000767)
        self.let_id_valor.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.let_id_valor)

        self.horizontalLayout_2.addWidget(self.frame_id)

        self.frame_nome_produto = QFrame(self.frame_continer_center)
        self.frame_nome_produto.setObjectName(u"frame_nome_produto")
        self.frame_nome_produto.setMinimumSize(QSize(0, 0))
        self.frame_nome_produto.setMaximumSize(QSize(12345678, 16777215))
        self.frame_nome_produto.setFrameShape(QFrame.StyledPanel)
        self.frame_nome_produto.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_nome_produto)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.lbl_nome_produto = QLabel(self.frame_nome_produto)
        self.lbl_nome_produto.setObjectName(u"lbl_nome_produto")
        self.lbl_nome_produto.setMaximumSize(QSize(16777215, 17))
        self.lbl_nome_produto.setFont(font)
        self.lbl_nome_produto.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lbl_nome_produto)

        self.let_nome_produto = QLineEdit(self.frame_nome_produto)
        self.let_nome_produto.setObjectName(u"let_nome_produto")

        self.verticalLayout_7.addWidget(self.let_nome_produto)

        self.horizontalLayout_2.addWidget(self.frame_nome_produto, 0, Qt.AlignLeft)

        self.frame_categoria = QFrame(self.frame_continer_center)
        self.frame_categoria.setObjectName(u"frame_categoria")
        self.frame_categoria.setMinimumSize(QSize(0, 0))
        self.frame_categoria.setMaximumSize(QSize(12345678, 16777215))
        self.frame_categoria.setFrameShape(QFrame.StyledPanel)
        self.frame_categoria.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_categoria)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.lbl_categoria = QLabel(self.frame_categoria)
        self.lbl_categoria.setObjectName(u"lbl_categoria")
        self.lbl_categoria.setMaximumSize(QSize(16777215, 17))
        self.lbl_categoria.setFont(font)
        self.lbl_categoria.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.lbl_categoria)

        self.com_categoria = QComboBox(self.frame_categoria)
        self.com_categoria.setObjectName(u"com_categoria")
        self.com_categoria.setMinimumSize(QSize(0, 20))
        self.com_categoria.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Zilla Slab Medium"])
        font1.setPointSize(9)
        self.com_categoria.setFont(font1)

        self.verticalLayout_8.addWidget(self.com_categoria)

        self.horizontalLayout_2.addWidget(self.frame_categoria)

        self.frame_unidade = QFrame(self.frame_continer_center)
        self.frame_unidade.setObjectName(u"frame_unidade")
        self.frame_unidade.setMinimumSize(QSize(0, 0))
        self.frame_unidade.setMaximumSize(QSize(12345678, 16777215))
        self.frame_unidade.setFrameShape(QFrame.StyledPanel)
        self.frame_unidade.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_unidade)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(3, 3, 3, 3)
        self.lbl_unidade = QLabel(self.frame_unidade)
        self.lbl_unidade.setObjectName(u"lbl_unidade")
        self.lbl_unidade.setMaximumSize(QSize(16777215, 17))
        self.lbl_unidade.setFont(font)
        self.lbl_unidade.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.lbl_unidade)

        self.com_unidade = QComboBox(self.frame_unidade)
        self.com_unidade.setObjectName(u"com_unidade")
        self.com_unidade.setMinimumSize(QSize(0, 20))
        self.com_unidade.setMaximumSize(QSize(16777215, 20))
        self.com_unidade.setFont(font1)

        self.verticalLayout_9.addWidget(self.com_unidade)

        self.horizontalLayout_2.addWidget(self.frame_unidade)

        self.frame_cliente = QFrame(self.frame_continer_center)
        self.frame_cliente.setObjectName(u"frame_cliente")
        self.frame_cliente.setMinimumSize(QSize(0, 0))
        self.frame_cliente.setMaximumSize(QSize(12345678, 16777215))
        self.frame_cliente.setFrameShape(QFrame.StyledPanel)
        self.frame_cliente.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_cliente)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 3, 3, 3)
        self.lbl_cliente = QLabel(self.frame_cliente)
        self.lbl_cliente.setObjectName(u"lbl_cliente")
        self.lbl_cliente.setMaximumSize(QSize(16777215, 17))
        self.lbl_cliente.setFont(font)
        self.lbl_cliente.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.lbl_cliente)

        self.com_cliente = QComboBox(self.frame_cliente)
        self.com_cliente.setObjectName(u"com_cliente")
        self.com_cliente.setMinimumSize(QSize(0, 20))
        self.com_cliente.setMaximumSize(QSize(16777215, 20))
        self.com_cliente.setFont(font1)

        self.verticalLayout_10.addWidget(self.com_cliente)

        self.horizontalLayout_2.addWidget(self.frame_cliente)

        self.frame_vendedor = QFrame(self.frame_continer_center)
        self.frame_vendedor.setObjectName(u"frame_vendedor")
        self.frame_vendedor.setMinimumSize(QSize(0, 0))
        self.frame_vendedor.setMaximumSize(QSize(12345678, 16777215))
        self.frame_vendedor.setFrameShape(QFrame.StyledPanel)
        self.frame_vendedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_vendedor)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.lbl_vendedor = QLabel(self.frame_vendedor)
        self.lbl_vendedor.setObjectName(u"lbl_vendedor")
        self.lbl_vendedor.setMaximumSize(QSize(16777215, 17))
        self.lbl_vendedor.setFont(font)
        self.lbl_vendedor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.lbl_vendedor)

        self.com_vendedor = QComboBox(self.frame_vendedor)
        self.com_vendedor.setObjectName(u"com_vendedor")
        self.com_vendedor.setMinimumSize(QSize(0, 20))
        self.com_vendedor.setMaximumSize(QSize(16777215, 20))
        self.com_vendedor.setFont(font1)

        self.verticalLayout_11.addWidget(self.com_vendedor)

        self.horizontalLayout_2.addWidget(self.frame_vendedor)

        self.verticalLayout_4.addWidget(self.frame_continer_center)

        self.frame_continer_center_2 = QFrame(self.frame_border_continer)
        self.frame_continer_center_2.setObjectName(u"frame_continer_center_2")
        self.frame_continer_center_2.setStyleSheet(u"")
        self.frame_continer_center_2.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_center_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_continer_center_2)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(8, 0, 8, 0)
        self.frame_data = QFrame(self.frame_continer_center_2)
        self.frame_data.setObjectName(u"frame_data")
        self.frame_data.setMinimumSize(QSize(0, 0))
        self.frame_data.setMaximumSize(QSize(12345678, 12345676))
        self.frame_data.setFrameShape(QFrame.StyledPanel)
        self.frame_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_data)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(3, 3, 3, 0)
        self.lbl_data = QLabel(self.frame_data)
        self.lbl_data.setObjectName(u"lbl_data")
        self.lbl_data.setMaximumSize(QSize(16777215, 13))
        self.lbl_data.setFont(font)
        self.lbl_data.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.lbl_data)

        self.frame_continer_data = QFrame(self.frame_data)
        self.frame_continer_data.setObjectName(u"frame_continer_data")
        self.frame_continer_data.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_data.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_continer_data)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.date_time_edit_inicio = QDateTimeEdit(self.frame_continer_data)
        self.date_time_edit_inicio.setObjectName(u"date_time_edit_inicio")

        self.horizontalLayout_4.addWidget(self.date_time_edit_inicio)

        self.date_time_edit_fim = QDateTimeEdit(self.frame_continer_data)
        self.date_time_edit_fim.setObjectName(u"date_time_edit_fim")

        self.horizontalLayout_4.addWidget(self.date_time_edit_fim)

        self.verticalLayout_12.addWidget(self.frame_continer_data)

        self.horizontalLayout_3.addWidget(self.frame_data)

        self.frame_total = QFrame(self.frame_continer_center_2)
        self.frame_total.setObjectName(u"frame_total")
        self.frame_total.setMinimumSize(QSize(0, 0))
        self.frame_total.setMaximumSize(QSize(12345678, 12345676))
        self.frame_total.setFrameShape(QFrame.StyledPanel)
        self.frame_total.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_total)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(3, 3, 3, 3)
        self.lbl_total = QLabel(self.frame_total)
        self.lbl_total.setObjectName(u"lbl_total")
        self.lbl_total.setMaximumSize(QSize(16777215, 17))
        self.lbl_total.setFont(font)
        self.lbl_total.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout_13.addWidget(self.lbl_total)

        self.frame_continer_total = QFrame(self.frame_total)
        self.frame_continer_total.setObjectName(u"frame_continer_total")
        self.frame_continer_total.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_total.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_continer_total)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.com_total_operador = QComboBox(self.frame_continer_total)
        self.com_total_operador.addItem("")
        self.com_total_operador.addItem("")
        self.com_total_operador.addItem("")
        self.com_total_operador.addItem("")
        self.com_total_operador.addItem("")
        self.com_total_operador.setObjectName(u"com_total_operador")
        self.com_total_operador.setMinimumSize(QSize(0, 20))
        self.com_total_operador.setMaximumSize(QSize(77, 20))
        self.com_total_operador.setFont(font1)

        self.horizontalLayout_6.addWidget(self.com_total_operador)

        self.let_total_valor = QLineEdit(self.frame_continer_total)
        self.let_total_valor.setObjectName(u"let_total_valor")
        sizePolicy.setHeightForWidth(self.let_total_valor.sizePolicy().hasHeightForWidth())
        self.let_total_valor.setSizePolicy(sizePolicy)
        self.let_total_valor.setMinimumSize(QSize(0, 17))
        self.let_total_valor.setMaximumSize(QSize(16777215, 20))
        self.let_total_valor.setMaxLength(1000000767)
        self.let_total_valor.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.let_total_valor)

        self.verticalLayout_13.addWidget(self.frame_continer_total)

        self.horizontalLayout_3.addWidget(self.frame_total)

        self.verticalLayout_4.addWidget(self.frame_continer_center_2)

        self.verticalLayout_3.addWidget(self.frame_border_continer)

        self.verticalLayout_2.addWidget(self.frame_continer_top_center)

        self.frame_continer_bottom = QFrame(self.frame_borda_esterior)
        self.frame_continer_bottom.setObjectName(u"frame_continer_bottom")
        self.frame_continer_bottom.setMaximumSize(QSize(16777215, 30))
        self.frame_continer_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_continer_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_continer_bottom)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 5, 2)
        self.horizontalSpacer = QSpacerItem(583, 15, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_busca = QPushButton(self.frame_continer_bottom)
        self.btn_busca.setObjectName(u"btn_busca")
        self.btn_busca.setMinimumSize(QSize(75, 24))

        self.horizontalLayout.addWidget(self.btn_busca)

        self.verticalLayout_2.addWidget(self.frame_continer_bottom)

        self.verticalLayout.addWidget(self.frame_borda_esterior)

        self.__retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def __retranslateUi(self, Form):
            Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
            self.lbl_id.setText(QCoreApplication.translate("Form", u"Id", None))
            self.let_id_valor.setText("")
            self.lbl_nome_produto.setText(QCoreApplication.translate("Form", u"Nome do produto", None))
            self.lbl_categoria.setText(QCoreApplication.translate("Form", u"Categoria", None))
            self.com_categoria.setPlaceholderText(QCoreApplication.translate("Form", u"Selecione", None))
            self.lbl_unidade.setText(QCoreApplication.translate("Form", u"Unidade", None))
            self.com_unidade.setPlaceholderText(QCoreApplication.translate("Form", u"Selecione", None))
            self.lbl_cliente.setText(QCoreApplication.translate("Form", u"Cliente", None))
            self.com_cliente.setPlaceholderText(QCoreApplication.translate("Form", u"Selecione", None))
            self.lbl_vendedor.setText(QCoreApplication.translate("Form", u"Vendedor", None))
            self.com_vendedor.setPlaceholderText(QCoreApplication.translate("Form", u"Selecione", None))
            self.lbl_data.setText(QCoreApplication.translate("Form", u"Data", None))
            self.lbl_total.setText(QCoreApplication.translate("Form", u"Total", None))
            self.com_total_operador.setItemText(0, QCoreApplication.translate("Form", u"=", None))
            self.com_total_operador.setItemText(1, QCoreApplication.translate("Form", u">", None))
            self.com_total_operador.setItemText(2, QCoreApplication.translate("Form", u"<", None))
            self.com_total_operador.setItemText(3, QCoreApplication.translate("Form", u">=", None))
            self.com_total_operador.setItemText(4, QCoreApplication.translate("Form", u"<=", None))

            self.com_total_operador.setPlaceholderText(QCoreApplication.translate("Form", u"Selecione", None))
            self.let_total_valor.setText("")
            self.btn_busca.setText(QCoreApplication.translate("Form", u"Buscar", None))
        # retranslateUi


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = PyBuscaPersonalizada()
    win.show()
    sys.exit(app.exec())
