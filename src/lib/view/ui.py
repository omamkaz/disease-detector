from .window_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt, QPoint, QSize
from PySide6.QtGui import QIcon
from ..utils.base_dir import Assets


class WindowUI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: object = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.is_maximize = False
        self.is_dark = True
        self.oldPos = self.pos()

        self.setWindowTitle("تشخيص الامراض")
        self.setWindowIcon(QIcon(Assets.icons("logo.png")))

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.setUpdatesEnabled(True)
        self.setDocumentMode(True)
        self.setAnimated(True)

        self.setAttribute(Qt.WA_Hover, True)
        self.setAttribute(Qt.WA_AcceptTouchEvents, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.list_symptoms.setUpdatesEnabled(True)
        self.list_symptoms.setAutoFillBackground(True)
        self.list_symptoms.setAutoScroll(False)
        self.list_symptoms.setSortingEnabled(False)
        self.list_symptoms.setSelectionRectVisible(False)
        self.list_symptoms.setAlternatingRowColors(False)

        self.list_symptoms.setAttribute(
            Qt.WidgetAttribute.WA_TouchPadAcceptSingleTouchEvents, True
        )
        self.list_symptoms.setAttribute(Qt.WidgetAttribute.WA_AcceptTouchEvents, True)

        self.list_symptoms.executeDelayedItemsLayout()
        self.list_symptoms.scheduleDelayedItemsLayout()

        self.list_symptoms_all.setUpdatesEnabled(True)
        self.list_symptoms_all.setAutoFillBackground(True)
        self.list_symptoms_all.setAutoScroll(False)
        self.list_symptoms_all.setSortingEnabled(False)
        self.list_symptoms_all.setSelectionRectVisible(False)
        self.list_symptoms_all.setAlternatingRowColors(False)

        self.list_symptoms_all.setAttribute(
            Qt.WidgetAttribute.WA_TouchPadAcceptSingleTouchEvents, True
        )
        self.list_symptoms_all.setAttribute(
            Qt.WidgetAttribute.WA_AcceptTouchEvents, True
        )

        self.list_symptoms_all.executeDelayedItemsLayout()
        self.list_symptoms_all.scheduleDelayedItemsLayout()

        self.close_btn.clicked.connect(self.close)
        self.max_btn.clicked.connect(self.on_maximize)
        self.min_btn.clicked.connect(self.showMinimized)
        self.theme_btn.clicked.connect(self.toggle_style_sheet)

        self.close_btn.setIconSize(QSize(22, 22))
        self.max_btn.setIconSize(QSize(22, 22))
        self.min_btn.setIconSize(QSize(22, 22))
        self.theme_btn.setIconSize(QSize(22, 22))
        self.go_btn.setIconSize(QSize(22, 22))

        self.close_btn.setIcon(QIcon(Assets.icons("close.svg")))
        self.max_btn.setIcon(QIcon(Assets.icons("maximize.svg")))
        self.min_btn.setIcon(QIcon(Assets.icons("minimize.svg")))
        self.theme_btn.setIcon(QIcon(Assets.icons("light.png")))
        self.go_btn.setIcon(QIcon(Assets.icons("search.png")))

        self.app_title.setText(self.windowTitle())
        self.app_icon.setPixmap(self.windowIcon().pixmap(32, 32))

        self.list_result.setSpacing(3)
        self.list_symptoms.setSpacing(3)
        self.list_symptoms_all.setSpacing(3)

        self.set_style_sheet("dark")

    def mousePressEvent(self, event):
        if self.is_maximize:
            self.on_maximize()

        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def on_maximize(self):
        if self.is_maximize:
            # set max_btn -> max icon
            self.max_btn.setIcon(QIcon(Assets.icons("maximize.svg")))
            self.showNormal()
        else:
            # set max_btn -> restore icon
            self.max_btn.setIcon(QIcon(Assets.icons("restore.svg")))
            self.showMaximized()

        self.is_maximize = not self.is_maximize

    def set_style_sheet(self, name: str):
        with open(Assets.themes(name + ".qss"), "r") as fr:
            self.setStyleSheet(fr.read())

    def toggle_style_sheet(self):
        self.theme_btn.setIcon(
            QIcon(Assets.icons("dark.png" if self.is_dark else "light.png"))
        )
        self.set_style_sheet("light" if self.is_dark else "dark")
        self.is_dark = not self.is_dark
