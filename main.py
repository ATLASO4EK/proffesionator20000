import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
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
        

        self.setCentralWidget(widget)
    

    
        boxis = QCheckBox()# тут 
        boxis.setCheckState(Qt.CheckState.Checked)
        boxis.stateChanged.connect(self.show_state)
    
        
        self.setCentralWidget(boxis)
        

    def show_state(self, s):
        print(s == Qt.CheckState.Checked)
        print(s)
    

app = QApplication(sys.argv)

boxis = MainWindow()
boxis.show()

window = MainWindow()
window.show()
app.exec()