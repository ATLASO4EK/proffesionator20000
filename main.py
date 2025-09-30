import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QListWidget, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() 
        
        self.setWindowTitle("Тест НКЭиВТ") # тут название сайта

        widget = QLabel("Тест: Твоя будущая профессия") # тут главный текст
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        
        podzagalovok = QLabel("Маленький текст")
        podzagalovok_font = podzagalovok.font()
        podzagalovok_font.setPointSize(23)
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

        spisok = QComboBox("На сколько вы готовы")
        spisok.addItems(["1", "2", "3"])
        spisok.currentIndexChanged.connect(self.index_xhanged)
        spisok.editTextChanged.connect(self.text_xhanged)

        neskolko = QListWidget("дада выбирай скока хочешь")
        neskolko.addItems(["One", "Two", "Three"])
        neskolko.currentItemChanged.connect(self.index_changed)
        neskolko.currentTextChanged.connect(self.text_changed)

        texito = QLineEdit("Введите текс")
        texito.setMaxLength(10)
        texito.setPlaceholderText("Enter your text")
        texito.returnPressed.connect(self.return_pressed)
        texito.selectionChanged.connect(self.selection_changed)
        texito.textChanged.connect(self.text_changed)
        texito.textEdited.connect(self.text_edited)
    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s) 

        layout.addWidget(widget)

    
        
        

    def show_state(self, s):
        print(s == Qt.CheckState.Checked)
        print(s)
    

app = QApplication(sys.argv)

boxis = MainWindow()
boxis.show()

window = MainWindow()
window.show()
app.exec()