from editor.dialogs.new_fragment_project_dialog import NewFragmentProjectDialog
from PySide6 import QtWidgets
from assets.loader import ICONS_BACKGROUND, ICONS_FOREGROUND


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
        self.new_project_button.setIcon(ICONS_BACKGROUND['plus'])
        self.new_project_button.setText('New')
        self.new_project_button.setDefault(True)
        self.new_project_button.clicked.connect(self.spawn_new_project_dialog)

        self.open_project_button = QtWidgets.QPushButton()
        self.project_button_group_layout.addWidget(self.open_project_button)
        self.open_project_button.setIcon(ICONS_FOREGROUND['folder-open'])
        self.open_project_button.setText('Open')

    def spawn_new_project_dialog(self):
        dialog = NewFragmentProjectDialog(self)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            # Please implement after getting a path datatype for the base folder datatype
            raise NotImplementedError('OH NO, it doesn\'t seem like there\'s anything here :(')
