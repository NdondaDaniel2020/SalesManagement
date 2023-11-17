import io
from pprint import pprint

code = ""
with open("ui_main_window.py", 'r', encoding="utf-8") as file:
    for line in file.readlines():

        if "from src.gui.widgets.py_push_button" in line:
            line += """from src.gui.core.functions import Functions\n"""
            code += line


        elif "self.btn_menu = PyPushButton" in line:
            line = """        self.btn_menu = PyPushButton(self.frame_continer_left_menu_logo,
                                     radius=8, text_padding=0,
                                     btn_hover="#313237",
                                     btn_pressed="#26272b")\n"""
            code += line

        elif """icon.addFile""" in line:
            line = '        icon.addFile(Functions().set_svg_icon("icon_menu.svg"), QSize(), QIcon.Normal, QIcon.Off)\n'
            code += line


        elif "self.btn_home = PyPushButton(self.frame_left_menu_top)" in line:
            line = """        self.btn_home = PyPushButton(self.frame_left_menu_top,
                                     radius=8, text_padding=5,
                                     is_active=True)\n"""
            code += line

        elif """icon1.addFile""" in line:
            line = '        icon1.addFile(Functions().set_svg_icon("icon_home.svg"), QSize(), QIcon.Normal, QIcon.Off)\n'
            code += line


        elif "self.btn_compra = PyPushButton(self.frame_left_menu_top)" in line:
            line = """        self.btn_compra = PyPushButton(self.frame_left_menu_top,
                                       radius=8, text_padding=2)\n"""
            code += line

        elif """icon2.addFile""" in line:
            line = '        icon2.addFile(Functions().set_svg_icon("icon_compra.svg"), QSize(), QIcon.Normal, QIcon.Off)\n'
            code += line


        elif "self.btn_venda = PyPushButton" in line:
            line = """        self.btn_venda = PyPushButton(self.frame_left_menu_top,
                                       radius=8, text_padding=1)\n"""
            code += line

        elif """icon3.addFile""" in line:
            line = '        icon3.addFile(Functions().set_svg_icon("icon_venda.svg"), QSize(), QIcon.Normal, QIcon.Off)\n'
            code += line


        elif "self.btn_close = PyPushButton" in line:
            line = """        self.btn_close = PyPushButton(self.frame_continer_control_window,
                                       btn_hover="#313237",
                                       btn_pressed="#e10000",
                                       radius=4, text_padding=3)\n"""
            code += line

        elif """icon9.addFile""" in line:
            line = '        icon9.addFile(Functions().set_svg_icon("icon_close.svg"), QSize(), QIcon.Normal, QIcon.Off)\n'
            code += line


        elif "self.btn_minimize = PyPushButton" in line:
            line = """        self.btn_minimize = PyPushButton(self.frame_continer_control_window,
                                       btn_hover="#313237",
                                       btn_pressed="#26272b",
                                       radius=4, text_padding=3)\n"""
            code += line

        elif """icon7.addFile""" in line:
            line = '        icon7.addFile(Functions().set_svg_icon("icon_minimize.svg"), QSize(), QIcon.Normal, QIcon.Off)\n'
            code += line


        elif "self.btn_maximize = PyPushButton" in line:
            line = """        self.btn_maximize = PyPushButton(self.frame_continer_control_window,
                                       btn_hover="#313237",
                                       btn_pressed="#26272b",
                                       radius=4, text_padding=3)\n"""
            code += line

        elif """icon8.addFile""" in line:
            line = '        icon8.addFile(Functions().set_svg_icon("icon_maximize.svg"), QSize(), QIcon.Normal, QIcon.Off)\n'
            code += line


        elif "self.btn_setting = PyPushButton" in line:
            line = """        self.btn_setting = PyPushButton(self.frame_left_menu_top,
                                       radius=8, text_padding=6)\n"""
            code += line

        elif """icon11.addFile""" in line:
            line = '        icon11.addFile(Functions().set_svg_icon("icon_setting.svg"), QSize(), QIcon.Normal, QIcon.Off)\n'
            code += line


        elif "self.btn_info = PyPushButton" in line:
            line = """        self.btn_info = PyPushButton(self.frame_left_menu_top,
                                       radius=8, text_padding=6)\n"""
            code += line

        elif """icon12.addFile""" in line:
            line = '        icon12.addFile(Functions().set_svg_icon("icon_information.svg"), QSize(), QIcon.Normal, QIcon.Off)\n'
            code += line


        elif "self.btn_user = PyPushButton" in line:
            line = """        self.btn_user = PyPushButton(self.frame_left_menu_top,
                                       radius=8, text_padding=2)\n"""
            code += line

        elif """icon13.addFile""" in line:
            line = '        icon13.addFile(Functions().set_svg_image("daniel.jpg"), QSize(), QIcon.Normal, QIcon.Off)\n'
            code += line


        elif "self.btn_user = PyPushButton" in line:
            line = """        self.btn_user = PyPushButton(self.frame_left_menu_top,
                                       radius=8, text_padding=2)\n"""
            code += line

        elif """icon13.addFile""" in line:
            line = '        icon13.addFile(Functions().set_svg_image("daniel.jpg"), QSize(), QIcon.Normal, QIcon.Off)\n'
            code += line



        else:
            code += line


with open("ui_main_window.py", 'w', encoding="utf-8") as file:
    file.write(code)
