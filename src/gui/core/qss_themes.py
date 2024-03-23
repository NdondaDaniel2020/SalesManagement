# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
import pathlib


# APP QSSTHEMS
# ///////////////////////////////////////////////////////////////
class QssThemes:

    ## PATH QSS
    # ///////////////////////////////////////////////////////////////
    app_path = pathlib.Path().absolute()

    if '\guis' in str(app_path):
        while '\guis' not in str(app_path)[-4::]:
            app_path = app_path.parent
    else:
        app_path = os.path.abspath(os.getcwd())

    app_path = str(app_path)
    # SET QSS THEME DARK
    # ///////////////////////////////////////////////////////////////
    def set_dark_qss(cls, file_name):
        folder = 'theme/dark/qss' if 'gui' in cls.app_path else 'gui/theme/dark/qss'
        path = os.path.join(cls.app_path, folder)
        qss_path = os.path.normpath(os.path.join(path, file_name))

        with open(qss_path, encoding='utf-8') as file:
            return file.read()

    # SET QSS THEME LIGHT
    # ///////////////////////////////////////////////////////////////
    def set_light_qss(cls, file_name):
        folder = 'theme/light/qss' if 'gui' in cls.app_path else 'gui/theme/light/qss'
        path = os.path.join(cls.app_path, folder)
        qss_path = os.path.normpath(os.path.join(path, file_name))



        with open(qss_path, encoding='utf-8') as file:
            return file.read()

    # SET QSS THEMES
    # ///////////////////////////////////////////////////////////////
    def set_qss(cls, file_name='', theme='dark'):

        if theme == 'dark':
            return cls.set_dark_qss(file_name)
        else:
            return cls.set_light_qss(file_name)

