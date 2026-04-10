from .selection_dialog import SelectionDialog
from editor.core.datatypes import StringDatatype
from editor.widgets.datatype_views import StringDatatypeView
from PySide6 import QtWidgets
from pathlib import Path
import re

# Reserved names on Windows that cannot be used as directory names
_RESERVED_NAMES = re.compile(
    r'^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])$',
    re.IGNORECASE
)

def validate_dirname(name: str) -> bool:
    if not name or len(name) > 255:
        return False
    if _RESERVED_NAMES.match(name):
        return False

    pattern = r'^(?![.\s])[\w\s\-]{1,255}(?<![.\s])$'
    return bool(re.match(pattern, name))



class NewFragmentProjectDialog(SelectionDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.main_content_layout = QtWidgets.QFormLayout(self.central_widget)

        self.project_name = StringDatatype()
        self.project_base_folder = StringDatatype() # TODO: Change this to a path datatype

        self.project_name_view = StringDatatypeView(self.project_name)
        self.project_base_folder_view = StringDatatypeView(self.project_base_folder)

        self.project_name.value_changed.connect(lambda: self.set_can_continue(self.is_valid_project()))
        self.project_base_folder.value_changed.connect(lambda: self.set_can_continue(self.is_valid_project()))

        self.main_content_layout.addRow('Project Name', self.project_name_view)
        self.main_content_layout.addRow('Project Base Folder', self.project_base_folder_view)

        self.set_can_continue(self.is_valid_project())

    def is_valid_project(self) -> bool:
        if self.project_name.is_blank():
            return False
        if not validate_dirname(self.project_name.value):
            return False
        
        if not Path(self.project_base_folder.value).is_absolute():
            return False
        if not Path(self.project_base_folder.value).exists():
            return False
        if (Path(self.project_base_folder.value) / self.project_name.value).exists():
            return False

        return True
