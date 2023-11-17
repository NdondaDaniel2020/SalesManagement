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
    while '\gui' not in str(app_path)[-4::]:
        app_path = app_path.parent

    # SET SVG ICON
    # ///////////////////////////////////////////////////////////////
    def set_svg_icon(cls, icon_name):
        folder = "images/svg_icons/"
        path = os.path.join(cls.app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET SVG IMAGE
    # ///////////////////////////////////////////////////////////////
    def set_svg_image(cls, icon_name):
        folder = "images/svg_images/"
        path = os.path.join(cls.app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET IMAGE
    # ///////////////////////////////////////////////////////////////
    def set_image(cls, image_name):
        folder = "images/images/"
        path = os.path.join(cls.app_path, folder)
        image = os.path.normpath(os.path.join(path, image_name))
        return image



