__all__ = ['ICONS_BACKGROUND', 'ICONS_FOREGROUND']

from editor.theme.theme_builder import theme
from pathlib import Path
from PySide6 import QtCore, QtGui, QtSvg


class SvgIconEngine(QtGui.QIconEngine):
    def __init__(self, normal: QtSvg.QSvgRenderer, disabled: QtSvg.QSvgRenderer | None = None):
        super().__init__()
        self.renderers = {
            QtGui.QIcon.Mode.Normal: normal,
            QtGui.QIcon.Mode.Disabled: disabled or normal,
        }

    def _renderer_for(self, mode):
        return self.renderers.get(mode, self.renderers[QtGui.QIcon.Mode.Normal])

    def pixmap(self, size, mode, state):
        image = QtGui.QImage(size, QtGui.QImage.Format.Format_ARGB32_Premultiplied)
        image.fill(QtCore.Qt.GlobalColor.transparent)
        painter = QtGui.QPainter(image)
        self._renderer_for(mode).render(painter, QtCore.QRectF(0, 0, size.width(), size.height()))
        painter.end()
        return QtGui.QPixmap.fromImage(image)

    def paint(self, painter, rect, mode, state):
        self._renderer_for(mode).render(painter, QtCore.QRectF(rect))

    def clone(self):
        return SvgIconEngine(self.renderers[QtGui.QIcon.Mode.Normal], self.renderers[QtGui.QIcon.Mode.Disabled])


def make_vector_icon(path: Path, normal_color: str, disabled_color: str) -> QtGui.QIcon:
    raw = path.read_bytes()
    normal_data = raw.replace(b'currentColor', normal_color.encode('ascii'), 1)
    disabled_data = raw.replace(b'currentColor', disabled_color.encode('ascii'), 1)
    normal = QtSvg.QSvgRenderer(QtCore.QByteArray(normal_data))
    disabled = QtSvg.QSvgRenderer(QtCore.QByteArray(disabled_data))
    return QtGui.QIcon(SvgIconEngine(normal, disabled))


ICONS_BACKGROUND: dict[str, QtGui.QIcon] = {}
ICONS_FOREGROUND: dict[str, QtGui.QIcon] = {}

background_icon_color = theme['background']
foreground_icon_color = theme['foreground']
foreground_disabled_icon_color = theme['foreground_disabled']

def init():
    for path in Path('assets/icons').iterdir():
        if path.suffix != '.svg':
            continue
        ICONS_BACKGROUND[path.stem] = make_vector_icon(path, background_icon_color, background_icon_color)
        ICONS_FOREGROUND[path.stem] = make_vector_icon(path, foreground_icon_color, foreground_disabled_icon_color)

