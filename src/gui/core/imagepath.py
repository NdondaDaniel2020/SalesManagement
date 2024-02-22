# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
import pathlib


# APP FUNCTIONS
# ///////////////////////////////////////////////////////////////
class ImagePath:
    
    def __init__(self):
        super().__init__()
        ## PATH IMAGES
        # ///////////////////////////////////////////////////////////////
        self.app_path = pathlib.Path().absolute()

        if '\gui' in str(self.app_path):
            while '\gui' not in str(self.app_path)[-4::]:
                self.app_path = self.app_path.parent
        else:
            self.app_path = os.path.abspath(os.getcwd())

        self.app_path = str(self.app_path)

    # SET SVG ICON
    # ///////////////////////////////////////////////////////////////
    def set_svg_icon(self, icon_name):
        folder = 'images/svg_icons/' if 'gui' in self.app_path else 'gui/images/svg_icons/'
        path = os.path.join(self.app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET SVG IMAGE
    # ///////////////////////////////////////////////////////////////
    def set_svg_image(self, icon_name):
        folder = 'images/svg_images/' if 'gui' in self.app_path else 'gui/images/svg_images/'
        path = os.path.join(self.app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET IMAGE
    # ///////////////////////////////////////////////////////////////
    def set_image(self, image_name):
        folder = 'images/images/' if 'gui' in self.app_path else 'gui/images/images/'
        path = os.path.join(self.app_path, folder)
        image = os.path.normpath(os.path.join(path, image_name))
        return image
