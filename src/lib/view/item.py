from PySide6.QtWidgets import QWidget, QGridLayout, QLabel
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize
from typing import Callable
from .item_ui import Ui_Form
from ..utils.base_dir import Assets


class ItemUI(QWidget, Ui_Form):
    def __init__(
        self, parent: object = None, title: str = "", remove_callback: Callable = None
    ) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.setObjectName("item_widget")

        self.on_remove = remove_callback
        self.row_index = 0

        self.title.setText(title)
        self.title.setObjectName("item_title")

        self.remove_btn.setIcon(QIcon(Assets.icons("remove.png")))
        self.remove_btn.setObjectName("item_remove_btn")
        self.remove_btn.setIconSize(QSize(32, 32))
        self.remove_btn.clicked.connect(lambda: self.on_remove(self.row_index))


class ResultItemUI(QWidget):
    def __init__(
        self, parent: object = None, title: str = "", subtitle: str = ""
    ) -> None:
        super().__init__(parent)

        self.gridLayout = QGridLayout(self)

        self.title = QLabel(title, self)
        self.subtitle = QLabel(subtitle, self)

        self.title.setObjectName("result_title")
        self.subtitle.setObjectName("result_subtitle")

        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.title)
        self.gridLayout.addWidget(self.subtitle)

        self.adjustSize()
