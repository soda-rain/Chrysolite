__all__ = ['ICONS_DARK', 'ICONS_LIGHT']

from editor.theme.theme_builder import theme
from pathlib import Path
from PySide6 import QtCore, QtGui, QtSvg

def get_colored_svg_icon(svg_path: Path, hex_color: str, size: int = 512) -> QtGui.QPixmap:
    """
    Loads an SVG, tints it to a specific hex color using masking, 
    and returns a QIcon.
    """
    renderer = QtSvg.QSvgRenderer(svg_path.as_posix())
    if not renderer.isValid():
        raise Exception('Renderer is not valid')

    pixmap = QtGui.QPixmap(QtCore.QSize(size, size))
    pixmap.fill(QtCore.Qt.GlobalColor.transparent)

    painter = QtGui.QPainter(pixmap)
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
    renderer.render(painter)

    painter.setCompositionMode(QtGui.QPainter.CompositionMode.CompositionMode_SourceIn)
    painter.fillRect(pixmap.rect(), QtGui.QColor(hex_color))
    painter.end()

    return pixmap

ICONS_DARK: dict[str, QtGui.QIcon] = {}
ICONS_LIGHT: dict[str, QtGui.QIcon] = {}

dark_icon_color = theme['background']
light_icon_color = theme['foreground']
light_disabled_icon_color = theme['foreground_disabled']

def init():
    for path in Path('assets/icons').iterdir():
        if path.is_file() and path.suffix == '.svg':
            ICONS_DARK[path.stem] = QtGui.QIcon(get_colored_svg_icon(path, dark_icon_color))
            ICONS_DARK[path.stem].addPixmap(get_colored_svg_icon(path, dark_icon_color), mode=QtGui.QIcon.Mode.Disabled)
            ICONS_LIGHT[path.stem] = QtGui.QIcon(get_colored_svg_icon(path, light_icon_color))
            ICONS_LIGHT[path.stem].addPixmap(get_colored_svg_icon(path, light_disabled_icon_color), mode=QtGui.QIcon.Mode.Disabled)
