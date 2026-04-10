from editor.core.datatypes.base_datatype import BaseDatatype
from PySide6 import QtWidgets
from abc import abstractmethod


class BaseDatatypeView(QtWidgets.QWidget):
    def __init__(self, datatype: BaseDatatype):
        super().__init__()
        self.datatype = datatype
        self.datatype.value_changed.connect(self.on_datatype_value_change)

    @abstractmethod
    def on_datatype_value_change(self):
        pass
