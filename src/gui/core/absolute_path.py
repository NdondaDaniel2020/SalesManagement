# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
import pathlib


# APP FUNCTIONS
# ///////////////////////////////////////////////////////////////
class AbsolutePath:
    
    def __init__(self):
        super().__init__()
        ## PATH IMAGES
        # ///////////////////////////////////////////////////////////////
        self.obs_path = pathlib.Path().absolute()
        while os.path.normpath('/gui') in str(self.obs_path):
            self.obs_path = self.obs_path.parent

        self.obs_path = str(self.obs_path)

    # SET SVG ICON
    # ///////////////////////////////////////////////////////////////
    def getPathIcon(self, icon_name):
        folder = 'gui/images/svg_icons/'
        path = os.path.join(self.obs_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET SVG IMAGE
    # ///////////////////////////////////////////////////////////////
    def getPathImage(self, icon_name):
        folder = 'gui/images/svg_images/'
        path = os.path.join(self.obs_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    def getThemeDarkQss(self, file_name):
        folder = 'theme/dark/qss' if 'gui' in self.obs_path else 'gui/theme/dark/qss'
        path = os.path.join(self.obs_path, folder)
        qss_path = os.path.normpath(os.path.join(path, file_name))

        with open(qss_path, encoding='utf-8') as file:
            return file.read()

    # SET QSS THEME LIGHT
    # ///////////////////////////////////////////////////////////////
    def getThemeLightQss(self, file_name):
        folder = 'theme/light/qss' if 'gui' in self.obs_path else 'gui/theme/light/qss'
        path = os.path.join(self.obs_path, folder)
        qss_path = os.path.normpath(os.path.join(path, file_name))
        with open(qss_path, encoding='utf-8') as file:
            return file.read()

    # SET QSS THEMES
    # ///////////////////////////////////////////////////////////////
    def getThemeQss(self, file_name='', theme='dark'):

        if theme == 'dark':
            return self.getThemeDarkQss(file_name)
        else:
            return self.getThemeLightQss(file_name)

    # get SETTING JSON
    # ///////////////////////////////////////////////////////////////
    def getPathSetting(self):
        path = self.obs_path + r'/gui/settings/settings.json'
        json = os.path.normpath(path)
        return json

    def getPathSettingSize(self):
        path = self.obs_path + r'/gui/settings/settings_size.json'
        json = os.path.normpath(path)
        return json

    def getPathSettingIp(self):
        path = self.obs_path + r'/gui/settings/settings_ip.json'
        json = os.path.normpath(path)
        return json

    def getPathDatabase(self):
        path = self.obs_path + r'/SalesManagement.db'
        json = os.path.normpath(path)
        return json


if __name__ == '__main__':
    # import json
    # import os
    # path = '/gui'
    # json_file = AbsolutePath().getPathSettingIp()
    # print(json_file)

    ...
