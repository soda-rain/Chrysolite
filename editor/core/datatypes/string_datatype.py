from .base_datatype import BaseDatatype


class StringDatatype(BaseDatatype):
    def __init__(self):
        super().__init__()
        self.value = str()
    
    def update_value(self, value: str):
        self.value = value
        self.value_changed.emit()

    def is_blank(self) -> bool:
        return not bool(self.value)

    def to_json_data(self) -> list:
        return [
            'editor.datatype.string_datatype',
            self.value
        ]
    
    def load_json_data(self, data: list):
        self.update_value(data[1])
