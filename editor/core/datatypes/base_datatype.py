from PySide6 import QtCore
from abc import abstractmethod


class BaseDatatype(QtCore.QObject):
    value_changed = QtCore.Signal()
    def __init__(self):
        super().__init__()

    @abstractmethod
    def is_blank(self) -> bool:
        """Returns if datatype is falsy"""
        return True
    
    @abstractmethod
    def to_json_data(self) -> list:
        return ['editor.datatype.base_datatype', None]
    
    @abstractmethod
    def load_json_data(self, data: list):
        pass
