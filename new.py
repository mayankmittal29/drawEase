import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QPoint

class DrawingEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drawing Editor")
        self.setGeometry(100, 100, 800, 600)
        
        self.canvas = Canvas()
        self.setCentralWidget(self.canvas)
        
        self.line_button = QPushButton("Line", self)
        self.line_button.clicked.connect(self.canvas.draw_line)
        self.line_button.setGeometry(10, 10, 80, 30)
        
class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600, 400)
        self.path = []

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)
        for p1, p2 in self.path:
            painter.drawLine(p1, p2)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.path.append((event.pos(), event.pos()))

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.path[-1] = (self.path[-1][0], event.pos())
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.path[-1] = (self.path[-1][0], event.pos())
            self.update()

    def draw_line(self):
        self.path = []

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrawingEditor()
    window.show()
    sys.exit(app.exec_())
