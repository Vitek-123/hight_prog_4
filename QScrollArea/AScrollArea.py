from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 170)
        self.setWindowTitle("Список товаров")
        icon = QtGui.QIcon("resources/icons/ico1.png")
        self.setWindowIcon(icon)

        lbl_pixmap = QLabel()
        lbl_pixmap.setFrameStyle(QFrame.Shape.Box)
        lbl_pixmap.setPixmap(QtGui.QPixmap("resources/icons/ico1.png").scaled(60, 60))

        lbl_desc_tovar = QLabel("Товар 1")
        lbl_desc_tovar.setFrameStyle(QFrame.Shape.Box)
        lbl_desc_tovar.setWordWrap(True)

        lbl_desc_tovar.mousePressEvent = lambda event, pix_img = lbl_pixmap.pixmap(): self.show_next_window(pix_img)

        lbl_discount = QLabel("10%")
        lbl_discount.setFrameStyle(QFrame.Shape.Box)

        frame = QFrame()
        frame.setLineWidth(1)
        frame.setFrameStyle(QFrame.Shape.Box)

        layout_for_labels = QHBoxLayout(frame)
        layout_for_labels.addWidget(lbl_pixmap)
        layout_for_labels.addWidget(lbl_desc_tovar, 5)
        layout_for_labels.addWidget(lbl_discount)

        layout_for_frame = QVBoxLayout()
        layout_for_frame.addWidget(frame)

        scrollarea = QScrollArea()
        scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scrollarea.setLayout(layout_for_frame)

    
        main_layout = QVBoxLayout()
        main_layout.addWidget(scrollarea)
        self.setLayout(main_layout)

    def show_next_window(self, value):
        self.next_win = NextWin(value)
        self.next_win.show()

class NextWin(QWidget):
    def __init__(self, pix_img):
        super().__init__()
        self.resize(200, 150)
        self.setWindowTitle("Просмотр деталей")
        icon = QtGui.QIcon("resources/icons/ico4.png")
        self.setWindowIcon(icon)
        pix = pix_img
        lbl_pix = QLabel(self)
        lbl_pix.setPixmap(QtGui.QPixmap(pix))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
