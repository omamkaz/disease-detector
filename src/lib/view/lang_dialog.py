#!/usr/bin/python3

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QRadioButton
from ..utils.base_dir import Assets
from glob import glob
import os.path


class LangDialog(QWidget):
    on_changed = Signal()

    def __init__(self, parent: object = None) -> None:
        super().__init__(parent)

        self.selected_langauge = None

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setStyleSheet("background-color: black;")

        self.grid_layout = QGridLayout(self)

        self.title = QLabel(self)
        self.title.setText("Select Langauge")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.grid_layout.addWidget(self.title)

        self.set_langs_list()

        self.setLayout(self.grid_layout)

    def changed_language(self, toggled: bool):
        self.selected_langauge = self.sender().objectName()
        self.close()
        self.on_changed.emit()

    def set_langs_list(self):
        row = 1
        for index, lang in enumerate(glob(Assets.data("locals", "*.json"))):
            name = os.path.basename(lang).split(".")[0]
            
            lang_btn = QRadioButton()
            lang_btn.setText(name.title())
            lang_btn.setObjectName(name)
            lang_btn.setChecked(False)
            lang_btn.setUpdatesEnabled(True)
            lang_btn.toggled.connect(self.changed_language)

            if not index % 3:
                row += 1

            self.grid_layout.addWidget(lang_btn, row, index)