from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication,QWidget,
    QPushButton,QLabel,
    QVBoxLayout, QHBoxLayout)

from second_win import TestWin
from instr import *


class MainWin(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.set_appear()
        self.connects()
        self.show()

    def initUI(self):
        self.text1 = QLabel(txt_hello)
        self.text2 = QLabel(txt_instruction)

        self.bn = QPushButton(txt_next)

        self.v_line = QVBoxLayout()
        
        self.v_line.addWidget(self.text1, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.text2, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.bn, alignment=Qt.AlignCenter)

        self.setLayout(self.v_line)

    def next_click(self):
        self.tw = TestWin()
        self.hide()
        
    def connects(self):
        self.bn.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw = MainWin()
app.exec_()
