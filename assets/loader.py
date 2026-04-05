__all__ = ['ICONS_DARK', 'ICONS_LIGHT']

from PySide6 import QtGui
from pathlib import Path

ICONS_DARK: dict[str, QtGui.QIcon] = {}
ICONS_LIGHT: dict[str, QtGui.QIcon] = {}

for path in Path('assets/icons/dark').iterdir():
    if path.is_file() and path.suffix == '.svg':
        icon_dark = QtGui.QIcon(path.as_posix())
        ICONS_DARK[path.stem] = icon_dark

for path in Path('assets/icons/light').iterdir():
    if path.is_file() and path.suffix == '.svg':
        icon_light = QtGui.QIcon(path.as_posix())
        ICONS_LIGHT[path.stem] = icon_light

for path in Path('assets/icons/dark').iterdir():
    if path.is_file() and path.suffix == '.svg':
        ICONS_DARK[path.stem].addFile(path.as_posix(), mode=QtGui.QIcon.Mode.Disabled)

for path in Path('assets/icons/disabled_light').iterdir():
    if path.is_file() and path.suffix == '.svg':
        ICONS_LIGHT[path.stem].addFile(path.as_posix(), mode=QtGui.QIcon.Mode.Disabled)
