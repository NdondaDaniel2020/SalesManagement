
# IMPORTS
import os

# IMPORT QT CORE
from src.qt_core import *
from src.gui.core.imagepath import ImagePath

class PyPushButton(QPushButton):
    def __init__(
            self,
            parent=None,
            text="",
            height=40,
            minimum_width=50,
            text_padding=4,
            text_color="#e9eaec",
            tooltip_text="",
            app_parent=None,
            top_margin=40,
            icon_path="",
            icon_color="#e9eaec",
            btn_radius=8,
            btn_color="#202125",
            btn_hover="#4050aa",
            btn_pressed="#596deb",
            is_active=False,
            active_line_tooltip=True
    ):
        super().__init__(parent)

        # Set default parametros
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Custom parameters
        self._minimum_width = minimum_width
        self._text_padding = text_padding
        self._text_color = text_color
        self._tooltip_text = tooltip_text
        self._top_margin = top_margin
        self._icon_path = icon_path
        self._icon_color = icon_color
        self._btn_radius = btn_radius
        self._btn_color = btn_color
        self._btn_hover = btn_hover
        self._btn_pressed = btn_pressed
        self.is_active = is_active

        # Parent
        self._parent = parent
        self._app_parent = app_parent

        # TOOLTIP
        self._adjust_x = 0
        self._adjust_y = 0
        self._pos_tooltip = 'top'
        self.permission_show_tooltip = True

        self._tooltip_text = tooltip_text
        self._tooltip = _ToolTip(
            app_parent,
            tooltip_text,
            self._btn_color,
            self._text_color,
            active_line_tooltip
        )
        self._tooltip.hide()

        # Set style
        self.set_style(
            text_padding=self._text_padding,
            text_color=self._text_color,
            btn_radius=self._btn_radius,
            btn_color=self._btn_color,
            btn_hover=self._btn_hover,
            btn_pressed=self._btn_pressed,
            is_active=self.is_active
        )

    def set_active(self, is_active_menu):
        self.set_style(
            text_padding=self._text_padding,
            text_color=self._text_color,
            btn_radius=self._btn_radius,
            btn_color=self._btn_color,
            btn_hover=self._btn_hover,
            btn_pressed=self._btn_pressed,
            is_active=is_active_menu
        )

    def setMoveTooltipText(self, adjust_x=0, adjust_y=0):
        self._adjust_x = adjust_x
        self._adjust_y = adjust_y

    def setTooltipText(self, tooltip_text, app_parent, pos_tooltip="top", adjust_x=0, adjust_y=0):

        self._tooltip_text = tooltip_text
        self._app_parent = app_parent
        self._pos_tooltip = pos_tooltip.lower()

        self._adjust_x = adjust_x
        self._adjust_y = adjust_y

        self._tooltip = _ToolTip(
            self._app_parent,
            self._tooltip_text,
            self._btn_color,
            self._text_color
        )
        self._tooltip.hide()

    def setPermissionShowTooltip(self, bool):
        self.permission_show_tooltip = bool

    def enterEvent(self, event):
        self.moveTooltip()
        if self.permission_show_tooltip:
            self._tooltip.show()

    def leaveEvent(self, event):
        self.moveTooltip()
        self._tooltip.hide()

    def moveTooltip(self):
        # GET MAIN WINDOW PARENT
        gp = self.mapToGlobal(QPoint(0, 0))

        # SET WIDGET TO GET POSTION
        # Return absolute position of widget inside app
        while "central_widget" != self._parent.objectName():
            self._parent = self._parent.parent()

        pos = self._parent.mapFromGlobal(gp)

        # FORMAT POSITION
        # Adjust tooltip position with offset
        if self._pos_tooltip == "top":
            pos_x = (pos.x() - (self._tooltip.width() // 2)) + (self.width() // 2) + self._adjust_x
            pos_y = pos.y() - self._top_margin + self._adjust_y
        elif self._pos_tooltip == "bottom":
            pos_x = (pos.x() - (self._tooltip.width() // 2)) + (self.width() // 2) + self._adjust_x
            pos_y = pos.y() + self._top_margin + 2 + self._adjust_y
        elif self._pos_tooltip == "left":
            pos_x = (pos.x() - self._tooltip.width() - 23) + (self.width() / 2) + self._adjust_x
            pos_y = pos.y() + 1.5 + self._adjust_y
        elif self._pos_tooltip == "right":
            pos_x = (pos.x() + (self._tooltip.width() // 4)-5) + (self.width() / 2) + self._adjust_x
            pos_y = pos.y() + 1.5 + self._adjust_y
        else:
            pos_x = (pos.x() - (self._tooltip.width() // 2)) + (self.width() // 2) + self._adjust_x
            pos_y = pos.y() - self._top_margin + self._adjust_y

        # SET POSITION TO WIDGET
        # Move tooltip position

        self._tooltip.move(pos_x, pos_y)


    def set_style(
            self,
            text_padding=4,
            text_color="#e9eaec",
            btn_radius=8,
            btn_color="#202125",
            btn_hover="#4050aa",
            btn_pressed="#596deb",
            is_active=True
    ):
        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
            border-radius: {btn_radius}px;
        }}
        QPushButton:hover {{
            background-color: {btn_hover};
        }}
        QPushButton:pressed {{
            background-color: {btn_pressed};
        }}
        """

        active_style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_pressed};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
            border-radius: {btn_radius}px;
        }}
        QPshButton:hover {{
            background-color: {btn_hover};
        }}
        QPushButton:pressed {{
            background-color: {btn_pressed};
        }}
        """

        self.is_active = is_active

        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)

    def paintEvent(self, event):
        # Return default style
        QPushButton.paintEvent(self, event)

        # Painter
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        rect = QRect(0, 0, self._minimum_width, self.height())

        self.draw_icon(qp, self._icon_path, rect, self._icon_color)

        qp.end()

    def draw_icon(self, qp, image, rect, color):

        # Draw icon
        icon = QPixmap(ImagePath().set_svg_icon(image))

        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()



class _ToolTip(QLabel):
    # TOOLTIP / LABEL StyleSheet
    style_tooltip = """ 
    QLabel {{		
        background-color: {_dark_one};	
        color: {_text_foreground};
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 12px;
        border: 0px solid transparent;
        font: 800 10pt "Segoe UI";
    }}
    """
    style_tooltip_active = """
    QLabel {		
        border-left: 2px solid #596deb;
    }
    """
    def __init__(
        self,
        parent,
        tooltip,
        dark_one,
        text_foreground,
        active=True
    ):
        QLabel.__init__(self)

        # LABEL SETUP
        style = self.style_tooltip.format(
            _dark_one=dark_one,
            _text_foreground=text_foreground
        )

        if active:
            style = style+self.style_tooltip_active

        self.setObjectName(u"label_tooltip")
        self.setStyleSheet(style)
        self.setMinimumHeight(25)
        self.setParent(parent)
        self.setText(tooltip)
        self.adjustSize()

        # SET DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(self.shadow)
