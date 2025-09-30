import sys
import json
import os
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QLineEdit,
    QListWidget, QVBoxLayout, QWidget, QPushButton,
    QFileDialog, QMessageBox)
from AI_agent import AIagent
from PIL import Image

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ai = AIagent()
        self.setWindowTitle("Тест НКЭиВТ")
        self.setFixedSize(800, 600)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Заголовок
        widget = QLabel("Тест: Твоя будущая профессия")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        podzagalovok = QLabel("Маленький текст")
        podzagalovok_font = podzagalovok.font()
        podzagalovok_font.setPointSize(23)
        podzagalovok.setFont(podzagalovok_font)
        podzagalovok.setAlignment(Qt.AlignmentFlag.AlignLeft)

        vopros_1_label = QLabel("1. Тебе нравится бла-бла-бла")
        vopros_1_font = vopros_1_label.font()
        vopros_1_font.setPointSize(16)
        vopros_1_label.setFont(vopros_1_font)

        # Чекбоксы
        self.vopros_1_1 = QCheckBox("котяки")
        self.vopros_1_2 = QCheckBox("рыбики")

        vopros_2_label = QLabel("2. Твоя специальность чтобы тебя отчислить")
        vopros_2_font = vopros_1_label.font()
        vopros_2_font.setPointSize(16)
        vopros_2_label.setFont(vopros_1_font)

        # Комбо-бокс
        self.spisok = QComboBox()
        self.spisok.addItems(["Информационные системы и программирование",
                              "Оператор информационных систем и ресурсов",
                              "Сетевое и системное администрирование",
                              "Компьютерные системы и комплексы",
                              "Монтаж, техническое обслуживание и ремонт электронных приборов и устройств",])

        vopros_3_label = QLabel("3. Какащке?")
        vopros_3_font = vopros_1_label.font()
        vopros_3_font.setPointSize(16)
        vopros_3_label.setFont(vopros_1_font)

        # Листбокс
        self.neskolko = QListWidget()
        self.neskolko.addItems(["yes", "da", "Ещё как!","да без б"])

        vopros_4_label = QLabel("4. Последние слова")
        vopros_4_font = vopros_1_label.font()
        vopros_4_font.setPointSize(16)
        vopros_4_label.setFont(vopros_1_font)

        # Поле ввода
        self.texito = QLineEdit()
        self.texito.setMaxLength(10)
        self.texito.setPlaceholderText("Введите текст")

        # Загрузка фото
        self.photo_label = QLabel("Фото не выбрано")
        self.photo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.photo_button = QPushButton("Загрузить фото")
        self.photo_button.clicked.connect(self.load_photo)

        layout.addWidget(widget)
        layout.addWidget(podzagalovok)
        layout.addWidget(vopros_1_label)
        layout.addWidget(self.vopros_1_1)
        layout.addWidget(self.vopros_1_2)
        layout.addWidget(vopros_2_label)
        layout.addWidget(self.spisok)
        layout.addWidget(vopros_3_label)
        layout.addWidget(self.neskolko)
        layout.addWidget(vopros_4_label)
        layout.addWidget(self.texito)
        layout.addWidget(self.photo_button)
        layout.addWidget(self.photo_label)

        # Кнопка сохранения JSON
        self.save_button = QPushButton("Сохранить в JSON")
        self.save_button.setStyleSheet("background-color: blue; color: white; font-size: 16px; padding: 8px;")
        self.save_button.clicked.connect(self.save_to_json)
        #self.save_button.clicked.connect(lambda: self.show_image_from_json("data.json"))
        layout.addWidget(self.save_button)

    # Метод загрузки фотоs
    def load_photo(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Выбрать фото",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if file_name:
            pixmap = QPixmap(file_name).scaledToWidth(200)
            self.photo_label.setPixmap(pixmap)
            self.photo_label.setText("")
            self.selected_photo = file_name

    # Метод сохранения JSON
    def save_to_json(self):
        if not (self.vopros_1_1.isChecked() or self.vopros_1_2.isChecked()):
            QMessageBox.warning(self, "Ошибка", "Ответь на вопрос 1!")
            return
        if self.spisok.currentText().strip() == "":
            QMessageBox.warning(self, "Ошибка", "Выбери вариант из списка!")
            return
        if not self.neskolko.currentItem():
            QMessageBox.warning(self, "Ошибка", "Выбери элемент из списка!")
            return
        if self.texito.text().strip() == "":
            QMessageBox.warning(self, "Ошибка", "Поле ввода текста не должно быть пустым!")
            return
        if not hasattr(self, "selected_photo"):
            QMessageBox.warning(self, "Ошибка", "Загрузите фото!")
            return

        data = {
            "q_one": {
                "ans_one": self.vopros_1_1.isChecked(),
                "ans_two": self.vopros_1_2.isChecked(),
            },
            "q_two": self.spisok.currentText(),
            "q_three": self.neskolko.currentItem().text(), #забей на ошибку, так надо
            "text": self.texito.text(),
            "path": self.selected_photo
        }

        predicted_img = self.ai.getimg(prof=self.spisok.currentText(),
                                       prof_disc='интересная профессия, связанная с айти технологиями',
                                       image=open(self.selected_photo, 'rb').read())

        predicted_img.show()
        predicted_img.save('123.png')

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        QMessageBox.information(self, "Успех", "✅ Данные сохранены в data.json")
        self.show_image_from_json("data.json")

    # Метод показа фото из JSON
    def show_image_from_json(self, json_path):
        if not os.path.exists(json_path):
            QMessageBox.warning(self, "Ошибка", "JSON файл не найден!")
            return

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        photo_path = data.get("path")
        if photo_path and os.path.exists(photo_path):
            msg = QMessageBox(self)
            msg.setWindowTitle("Ваше фото")
            pixmap = QPixmap(photo_path).scaled(800, 600, Qt.AspectRatioMode.KeepAspectRatio)
            msg.setIconPixmap(pixmap)
            msg.exec()
        else:
            QMessageBox.warning(self, "Ошибка", "Фото не найдено!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
