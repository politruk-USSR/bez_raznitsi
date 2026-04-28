from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication,QWidget,
    QPushButton,QLabel,
    QVBoxLayout, QHBoxLayout, QLineEdit)

from instr import *
class TestWin(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.set_appear()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
    
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btntext1 = QPushButton(txt_starttest1, self)
        self.btntext2 = QPushButton(txt_starttest2, self)
        self.btntext3 = QPushButton(txt_starttest3, self)

        self.text_name = QLabel('your name')
        self.text_age =  QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel('время будет тут')

        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)

        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()

        self.r_line.addWidget(self.text_timer, alignment=Qt.AlignRight)
        self.l_line.addWidget(self.line_name, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3, alignment=Qt.AlignLeft)

        self.l_line.addWidget(self.btntext1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btntext2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btntext3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)

        self.setLayout(self.h_line)
    def next_click(self):
        self.tw = FinalWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

