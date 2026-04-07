from editor.core.file_factory.fragment_config import create_fragment_config
from editor.theme import build_custom_colors
from assets.loader import init
from editor.library import Library
from PySide6 import QtWidgets
from pathlib import Path
import qdarktheme
import sys

if not Path('.fragment').exists():
    create_fragment_config(Path(''))

def start():
    app = QtWidgets.QApplication()
    init() # Init the assets after QApplication
    qdarktheme.setup_theme(theme='dark', custom_colors=build_custom_colors())
    library = Library()
    library.show()
    sys.exit(app.exec())
