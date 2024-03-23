# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
import pathlib


# APP FUNCTIONS
# ///////////////////////////////////////////////////////////////
class JsonSetting:

    def __init__(self):
        super().__init__()
        ## PATH IMAGES
        # ///////////////////////////////////////////////////////////////
        self.app_path = pathlib.Path().absolute()

        if '\guis' in str(self.app_path):
            while '\guis' not in str(self.app_path)[-4::]:
                self.app_path = self.app_path.parent
        else:
            self.app_path = os.path.abspath(os.getcwd())

        self.app_path = str(self.app_path)

    # SET SVG ICON
    # ///////////////////////////////////////////////////////////////
    def getPathJson(self):
        path = '\settings\settings.json' if '\guis' in self.app_path else '\guis\settings\settings.json'
        path = self.app_path + path
        json = os.path.normpath(path)
        return json