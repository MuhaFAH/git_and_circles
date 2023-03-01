import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from interface import Ui_MainWindow
from PyQt5 import uic
import random


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.draw = False
        self.spawn_btn.clicked.connect(self.trueDraw)
        self.pos1, self.pos2, self.pos3, self.pos4 = 0, 0, 0, 0
        self.x1, self.x2, self.x3, self.x4 = 0, 0, 0, 0
        self.y1, self.y2, self.y3, self.y4 = 0, 0, 0, 0
        self.size1, self.size2, self.size3, self.size4 = 0, 0, 0, 0
        self.color1, self.color2, self.color3, self.color4 = 0, 0, 0, 0

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircle(qp)
        self.update()
        qp.end()

    def drawCircle(self, qp):
        if self.draw:
            qp.setBrush(self.color1)
            qp.setPen(self.color1)
            qp.drawEllipse(self.x1, self.y1, self.size1, self.size1)
            qp.setBrush(self.color2)
            qp.setPen(self.color2)
            qp.drawEllipse(self.x2, self.y2, self.size2, self.size2)
            qp.setBrush(self.color3)
            qp.setPen(self.color3)
            qp.drawEllipse(self.x3, self.y3, self.size3, self.size3)
            qp.setBrush(self.color4)
            qp.setPen(self.color4)
            qp.drawEllipse(self.x4, self.y4, self.size4, self.size4)

    def trueDraw(self):
        self.draw = True
        self.x1, self.x2, self.x3, self.x4 = random.randrange(0, self.width()), \
                                             random.randrange(0, self.width()), \
                                             random.randrange(0, self.width()), \
                                             random.randrange(0, self.width())
        self.y1, self.y2, self.y3, self.y4 = random.randrange(0, self.width()), \
                                             random.randrange(0, self.width()), \
                                             random.randrange(0, self.width()), \
                                             random.randrange(0, self.width())
        self.size1, self.size2, self.size3, self.size4 = random.randrange(200), \
                                                         random.randrange(200), \
                                                         random.randrange(200), \
                                                         random.randrange(200)
        self.color1, self.color2, self.color3, self.color4 = QColor(random.randrange(255),
                                                                     random.randrange(255), random.randrange(255)), \
                                                             QColor(random.randrange(255),
                                                                     random.randrange(255), random.randrange(255)), \
                                                             QColor(random.randrange(255),
                                                                     random.randrange(255), random.randrange(255)), \
                                                             QColor(random.randrange(255),
                                                                     random.randrange(255), random.randrange(255))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
