import sys
import json

from PySide6.QtWidgets import QApplication, QListWidgetItem
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon

from .view.ui import WindowUI
from .view.lang_dialog import LangDialog
from .view.item import ItemUI, ResultItemUI
from .utils.ML import DiseasePrediction
from .utils.base_dir import Assets


class DiseaseDetector:
    def __init__(self):
        self.ui = WindowUI()
        self.ml = DiseasePrediction()
        self.lang_dialog = LangDialog()

        self.ui.line_search.textChanged.connect(self.on_search)
        self.ui.go_btn.clicked.connect(self.process_symptoms)

        self.ui.list_symptoms_all.itemDoubleClicked.connect(self.on_item_double_clicked)

        self.symptoms_db = {}

    def load_json_data(self):
        with open(Assets.data("locals", 
                              self.lang_dialog.selected_langauge + ".json"), "r") as fr:
            self.json_data = json.load(fr)

    def on_item_double_clicked(self):
        if item := self.ui.list_symptoms_all.currentItem():
            index, symptom = item.data(-1)
            item.setHidden(True)
            self.add_symptom(index, symptom)

    def on_search(self, text: str):
        for index in range(self.ui.list_symptoms_all.count()):
            item = self.ui.list_symptoms_all.item(index)
            if text.strip().lower() not in item.text().strip().lower():
                item.setHidden(True)
            elif not self.symptoms_db.get(item.data(-1)[0]):
                item.setHidden(False)

    def add_symptom(self, index: int, symptom: str):
        if not self.symptoms_db.get(index):
            self.symptoms_db.update({index: symptom})
            self.load_symptoms()

    def load_symptoms(self):
        self.ui.list_symptoms.clear()
        for index, symptom in self.symptoms_db.items():
            item = QListWidgetItem(self.ui.list_symptoms)
            widget = ItemUI(
                self.ui.list_symptoms,
                symptom,
                self.on_remove_symptom,
            )
            widget.row_index = self.ui.list_symptoms.count()
            item.setData(-1, index)
            item.setSizeHint(QSize(50, widget.height()))
            self.ui.list_symptoms.setItemWidget(item, widget)
            self.ui.list_symptoms.setCurrentRow(0)

    def load_symptoms_all(self):
        symptoms = tuple(self.json_data.get("symptoms").keys())
        for symptom in symptoms:
            item = QListWidgetItem(self.ui.list_symptoms_all)
            item.setText(symptom)
            item.setData(-1, (symptoms.index(symptom), symptom))
            item.setSizeHint(QSize(30, 30))

            self.ui.list_symptoms_all.addItem(item)
            self.ui.list_symptoms_all.setCurrentRow(0)

    def on_remove_symptom(self, row: int):
        item = self.ui.list_symptoms.item(row - 1)
        index = item.data(-1)
        self.symptoms_db.pop(index)
        self.ui.list_symptoms.removeItemWidget(item)
        self.ui.list_symptoms_all.item(index).setHidden(False)
        self.load_symptoms()

    def process_symptoms(self):
        if self.ui.stackedWidget.currentIndex() >= 1:
            # Back to main
            self.ui.go_btn.setIcon(QIcon(Assets.icons("search.png")))
            self.ui.stackedWidget.setCurrentIndex(0)

        elif self.symptoms_db:
            self.ui.go_btn.setIcon(QIcon(Assets.icons("back.png")))
            # Process symptoms
            self.ui.list_result.clear()
            self.ui.stackedWidget.setCurrentIndex(1)
            for key, value in self.ml.predictDisease(
                map(
                    lambda symptom: self.json_data.get("symptoms").get(symptom),
                    self.symptoms_db.values(),
                )
            ).items():
                item = QListWidgetItem(self.ui.list_result)
                widget = ResultItemUI(
                    self.ui.list_result,
                    self.json_data.get("results").get(key.strip().lower()),
                    self.json_data.get("types").get(value.strip().lower()) + " ⮠ ",
                )
                item.setSizeHint(QSize(50, widget.height()))
                item.setFlags(Qt.ItemFlag.ItemIsSelectable)
                self.ui.list_result.setItemWidget(item, widget)

    def load_data(self):
        self.load_json_data()
        self.load_symptoms_all()

        title = self.json_data.get("title", "")
        self.ui.setWindowTitle(title)
        self.ui.app_title.setText(title)
        
        self.ui.show()
        
    def show_ui(self):
        self.lang_dialog.show()
        self.lang_dialog.on_changed.connect(self.load_data)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Disease Detector")

    window = DiseaseDetector()
    window.show_ui()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()