# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
import pathlib


# APP FUNCTIONS
# ///////////////////////////////////////////////////////////////
class Functions:

    ## PATH IMAGES
    # ///////////////////////////////////////////////////////////////
    app_path = pathlib.Path().absolute()

    if '\gui' in str(app_path):
        while '\gui' not in str(app_path)[-4::]:
            app_path = app_path.parent
    else:
        app_path = os.path.abspath(os.getcwd())

    app_path = str(app_path)
    # SET SVG ICON
    # ///////////////////////////////////////////////////////////////
    def set_svg_icon(cls, icon_name):
        folder = 'images/svg_icons/' if 'gui' in cls.app_path else 'gui/images/svg_icons/'
        path = os.path.join(cls.app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET SVG IMAGE
    # ///////////////////////////////////////////////////////////////
    def set_svg_image(cls, icon_name):
        folder = 'images/svg_images/' if 'gui' in cls.app_path else 'gui/images/svg_images/'
        path = os.path.join(cls.app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET IMAGE
    # ///////////////////////////////////////////////////////////////
    def set_image(cls, image_name):
        folder = 'images/images/' if 'gui' in cls.app_path else 'gui/images/images/'
        path = os.path.join(cls.app_path, folder)
        image = os.path.normpath(os.path.join(path, image_name))
        return image
