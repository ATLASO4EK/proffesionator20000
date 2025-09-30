import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QListWidget, QVBoxLayout, QHBoxLayout, QWidget
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() 
        
        self.setWindowTitle("Тест НКЭиВТ") # тут название сайта

        # Создаем центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        widget = QLabel("Тест: Твоя будущая профессия") # тут главный текст
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
    
        vopros_1_1 = QCheckBox("10/10")
        vopros_1_1.stateChanged.connect(self.vopros_1_chaged_1)
        vopros_1_2 = QCheckBox("9/10")
        vopros_1_2.stateChanged.connect(self.vopros_1_chaged_2)
        vopros_1_3 = QCheckBox("8/10")
        vopros_1_3.stateChanged.connect(self.vopros_1_chaged_3)

        spisok = QComboBox()
        spisok.addItems(["1", "2", "3"])
        spisok.currentIndexChanged.connect(self.index_xhanged)
        spisok.currentTextChanged.connect(self.text_xhanged)

        neskolko = QListWidget()
        neskolko.addItems(["One", "Two", "Three"])
        neskolko.currentItemChanged.connect(self.index_changed)
        neskolko.currentTextChanged.connect(self.text_changed)

        texito = QLineEdit()
        texito.setMaxLength(10)
        texito.setPlaceholderText("Введите текс")
        texito.returnPressed.connect(self.return_pressed)
        texito.selectionChanged.connect(self.selection_changed)
        texito.textChanged.connect(self.text_changed_line)
        texito.textEdited.connect(self.text_edited)

        # Добавляем все виджеты в layout
        layout.addWidget(widget)
        layout.addWidget(podzagalovok)
        layout.addWidget(vopros_1_label)
        layout.addWidget(vopros_1_1)
        layout.addWidget(vopros_1_2)
        layout.addWidget(vopros_1_3)
        layout.addWidget(spisok)
        layout.addWidget(neskolko)
        layout.addWidget(texito)

    def vopros_1_chaged_1(self, state):
        self.show_state(state)

    def vopros_1_chaged_2(self, state):
        self.show_state(state)

    def vopros_1_chaged_3(self, state):
        self.show_state(state)

    def index_xhanged(self, i):
        print(i)

    def text_xhanged(self, s):
        print(s)

    def index_changed(self, current, previous):
        print(current.text())

    def text_changed(self, s):
        print(s)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().findChild(QLineEdit).setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().findChild(QLineEdit).selectedText())

    def text_changed_line(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s) 

    def show_state(self, s):
        print(s == Qt.CheckState.Checked.value)
        print(s)
    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()