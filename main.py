import sys
import json
import os
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFontDatabase, QFont
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QLineEdit,
    QListWidget, QVBoxLayout, QWidget, QPushButton,
    QFileDialog, QMessageBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Тест НКЭиВТ")
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: #F0F0F0; color: #101010;")

        fonts_path = os.path.join(os.path.dirname(__file__), "fonts")

        # Подключаем шрифты
        tektur_file = os.path.join(fonts_path, "Tektur-VariableFont_wdth,wght.ttf")
        tttravels_file = os.path.join(fonts_path, "TT Travels Trial Medium.otf")

        tektur_id = QFontDatabase.addApplicationFont(tektur_file)
        if tektur_id == -1:
            print("Не удалось загрузить Tektur")
            tektur_family = "Arial"  # запасной шрифт
        else:
            tektur_family = QFontDatabase.applicationFontFamilies(tektur_id)[0]

        tttravels_id = QFontDatabase.addApplicationFont(tttravels_file)
        if tttravels_id == -1:
            print("Не удалось загрузить TTTravels")
            tttravels_family = "Arial"  # запасной шрифт
        else:
            tttravels_family = QFontDatabase.applicationFontFamilies(tttravels_id)[0]

        print("Шрифты загружены:", tektur_family, tttravels_family)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Заголовок
        widget = QLabel("Тест: Твоя будущая профессия")
        widget.setFont(QFont(tektur_family, 30))
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        widget.setStyleSheet("color: #1F43CD;")

        podzagalovok = QLabel("Маленький текст")
        podzagalovok.setFont(QFont(tttravels_family, 23))
        podzagalovok.setAlignment(Qt.AlignmentFlag.AlignLeft)
        podzagalovok.setStyleSheet("color: #5EC9F5;")

        # Вопрос 1
        vopros_1_label = QLabel("1. Тебе нравится бла-бла-бла")
        vopros_1_label.setFont(QFont(tttravels_family, 16))

        self.vopros_1_1 = QCheckBox("котяки")
        self.vopros_1_2 = QCheckBox("рыбики")
        self.vopros_1_1.setFont(QFont(tttravels_family, 14))
        self.vopros_1_2.setFont(QFont(tttravels_family, 14))

        # Вопрос 2
        vopros_2_label = QLabel("2. Твоя специальность чтобы тебя отчислить")
        vopros_2_label.setFont(QFont(tttravels_family, 16))

        self.spisok = QComboBox()
        self.spisok.addItems([
            "Информационные системы и программирование",
            "Оператор информационных систем и ресурсов",
            "Сетевое и системное администрирование",
            "Компьютерные системы и комплексы",
            "Монтаж, техническое обслуживание и ремонт электронных приборов и устройств",
        ])
        self.spisok.setFont(QFont(tttravels_family, 14))
        self.spisok.setStyleSheet("background-color: #FFFFFF; color: #101010;")

        # Вопрос 3
        vopros_3_label = QLabel("3. Какащке?")
        vopros_3_label.setFont(QFont(tttravels_family, 16))

        self.neskolko = QListWidget()
        self.neskolko.addItems(["yes", "da", "Ещё как!", "да без б"])
        self.neskolko.setFont(QFont(tttravels_family, 14))
        self.neskolko.setStyleSheet("background-color: #FFFFFF; color: #101010;")

        # Вопрос 4
        vopros_4_label = QLabel("4. Последние слова")
        vopros_4_label.setFont(QFont(tttravels_family, 16))

        self.texito = QLineEdit()
        self.texito.setMaxLength(10)
        self.texito.setPlaceholderText("Введите текст")
        self.texito.setFont(QFont(tttravels_family, 14))
        self.texito.setStyleSheet("background-color: #FFFFFF; color: #101010; padding: 4px;")

        # Фото
        self.photo_label = QLabel("Фото не выбрано")
        self.photo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.photo_label.setStyleSheet("border: 2px dashed #5EC9F5; padding: 20px;")

        self.photo_button = QPushButton("Загрузить фото")
        self.photo_button.setFont(QFont(tttravels_family, 14))
        self.photo_button.setStyleSheet("background-color: #1F43CD; color: #FFFFFF; padding: 8px;")
        self.photo_button.clicked.connect(self.load_photo)

        # Кнопка сохранения
        self.save_button = QPushButton("Сохранить в JSON")
        self.save_button.setFont(QFont(tttravels_family, 16))
        self.save_button.setStyleSheet("background-color: #5EC9F5; color: #FFFFFF; padding: 8px;")
        self.save_button.clicked.connect(self.save_to_json)

        # Добавляем виджеты в layout
        for w in [widget, podzagalovok, vopros_1_label, self.vopros_1_1, self.vopros_1_2,
                  vopros_2_label, self.spisok, vopros_3_label, self.neskolko,
                  vopros_4_label, self.texito, self.photo_button, self.photo_label, self.save_button]:
            layout.addWidget(w)

    def load_photo(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Выбрать фото", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if file_name:
            pixmap = QPixmap(file_name).scaledToWidth(200)
            self.photo_label.setPixmap(pixmap)
            self.photo_label.setText("")
            self.selected_photo = file_name

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
            "q_three": self.neskolko.currentItem().text(),
            "text": self.texito.text(),
            "path": self.selected_photo
        }

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        QMessageBox.information(self, "Успех", "✅ Данные сохранены в data.json")
        self.show_image_from_json("data.json")

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
