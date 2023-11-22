import io
from pprint import pprint

code = ""
with open("ui_main_window.py", 'r', encoding="utf-8") as file:
    for line in file.readlines():

        if "from src.gui.widgets.py_push_button" in line:
            line += """from src.gui.core.functions import Functions\n"""
            code += line



        elif "self.btn_close = PyPushButton" in line:
            line = """        self.btn_close = PyPushButton(self.frame_control_window,
                                       btn_hover="#313237",
                                       btn_pressed="#e10000",
                                       btn_radius=4, text_padding=5)\n"""
            code += line

        elif """icon2.addFile""" in line:
            line = '        icon2.addFile(Functions().set_svg_icon("icon_close.svg"), QSize(), QIcon.Normal, QIcon.Off)\n'
            code += line


        elif "self.btn_minimize = PyPushButton" in line:
            line = """        self.btn_minimize = PyPushButton(self.frame_control_window,
                                       btn_hover="#313237",
                                       btn_pressed="#26272b",
                                       btn_radius=4, text_padding=4.5)\n"""
            code += line

        elif """icon.addFile""" in line:
            line = '        icon.addFile(Functions().set_svg_icon("icon_minimize.svg"), QSize(), QIcon.Normal, QIcon.Off)\n'
            code += line


        elif "self.btn_maximize = PyPushButton" in line:
            line = """        self.btn_maximize = PyPushButton(self.frame_control_window,
                                       btn_hover="#313237",
                                       btn_pressed="#26272b",
                                       btn_radius=4, text_padding=4)\n"""
            code += line

        elif """icon2.addFile""" in line:
            line = '        icon2.addFile(Functions().set_svg_icon("icon_maximize.svg"), QSize(), QIcon.Normal, QIcon.Off)\n'
            code += line


        else:
            code += line


with open("ui_main_window.py", 'w', encoding="utf-8") as file:
    file.write(code)
