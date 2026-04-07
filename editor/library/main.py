from PySide6 import QtWidgets
from assets.loader import ICONS_LIGHT, ICONS_DARK


class Library(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.project_panel = QtWidgets.QWidget()
        self.setCentralWidget(self.project_panel)

        self.project_panel_layout = QtWidgets.QVBoxLayout(self.project_panel)

        self.project_button_group = QtWidgets.QWidget()
        self.project_button_group.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.project_button_group_layout = QtWidgets.QHBoxLayout(self.project_button_group)
        self.project_panel_layout.addWidget(self.project_button_group)

        self.new_project_button = QtWidgets.QPushButton()
        self.project_button_group_layout.addWidget(self.new_project_button)
        self.new_project_button.setIcon(ICONS_DARK['plus'])
        self.new_project_button.setText('New')
        self.new_project_button.setDefault(True)

        self.open_project_button = QtWidgets.QPushButton()
        self.project_button_group_layout.addWidget(self.open_project_button)
        self.open_project_button.setIcon(ICONS_LIGHT['folder-open'])
        self.open_project_button.setText('Open')
