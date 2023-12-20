import random
import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        canvas = QtGui.QPixmap(600, 550)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.label.setText("OK")
        canvas = QtGui.QPixmap(600, 550)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)

        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor(255, 255, 0))
        painter.setPen(pen)
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor(255, 255, 0))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        painter.setBrush(brush)
        painter.begin(self)
        sec = random.randrange(10, 300)
        painter.drawEllipse(random.randrange(0, 450), random.randrange(0, 450), sec, sec)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
