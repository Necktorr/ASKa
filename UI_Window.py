from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
    QPushButton, QApplication)
from PyQt6.QtGui import QFont

import sys, datetime, Voice
import stt
import weather

class ASKA_UI(QWidget):
    def __init__(self, voice_model = Voice.Voice_Module()):
        super().__init__()
        self.accept_micro = True

        self.voice_model = voice_model
        
        self.initUI()
        
    def initUI(self):
        now = datetime.datetime.now()
        self.lablel_1 = QLabel(f'Время сейчас: {now.strftime("%H:%M:%S")}', self)
        self.lablel_1.setGeometry(10, 0, 200, 15)

        # self.lablel_2 = QLabel(f'Погода: = {weather.f1, weather.f2}', self)
        # self.lablel_2.setGeometry(10, 20, 200, 15)

        self.lablel_3 = QLabel(f'Дата: {now.strftime("%d-%m-%Y")}', self)
        self.lablel_3.setGeometry(10, 40, 200, 15)

        self.lablel_4 = QLabel(f'Микрофон: {self.accept_micro}', self)
        self.lablel_4.setGeometry(10, 60, 200, 15)

        self.btn = QPushButton('Выключить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.switch_micro)
        self.btn.move(10, 80)

        self.input_secret_key = QLineEdit(self)
        self.input_secret_key.setGeometry(10, 110, 150, 20)

        self.btn_save = QPushButton('Выключить', self)
        self.btn_save.resize(self.btn.sizeHint())
        # self.btn_save.clicked.connect(self.switch_micro)
        self.btn_save.move(10, 130)

        self.setGeometry(500, 500, 300, 160)
        self.setWindowTitle('Настройки')
        
    def switch_micro(self):
        if self.accept_micro:
            self.accept_micro = False
            self.btn.setText("Включить")
            self.lablel_4.setText(f'Микрофон: {self.accept_micro}')
            
            self.voice_model.stop()
            
        else:
            self.accept_micro = True
            self.btn.setText("Выключить")
            self.lablel_4.setText(f'Микрофон: {self.accept_micro}')
            self.voice_model.start()

def start_ui():
    app = QApplication(sys.argv)
    window = ASKA_UI()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    start_ui()