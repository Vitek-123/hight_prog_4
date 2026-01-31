from PyQt6.QtWidgets import *
from PyQt6 import QtGui, QtCore

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scroll")
        self.resize(800, 200)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        content_widget = QWidget()
        vertical_content_widget = QVBoxLayout(content_widget)
        for i in range(4):
            pic_label = QLabel()
            pic_label.setPixmap(QtGui.QPixmap(f"resources/icons/ico{i+1}.png").scaled(200, 200))

            text_label = QLabel(f"Товар{i+1}")
            text_label.setFrameStyle(QFrame.Shape.Box)
            frame = QFrame()
            frame.setLineWidth(1)
            frame.setFrameShape(QFrame.Shape.Box)

            sale_label = QLabel(f"Скидка {10*(i+1)}")
            sale_label.setFrameStyle(QFrame.Shape.Box)

            vertical_content = QHBoxLayout(frame)
            vertical_content.addWidget(pic_label)
            vertical_content.addWidget(text_label, stretch=5)
            vertical_content.addWidget(sale_label)

            text_label.mousePressEvent = lambda event, idx=i: self.show_next_window(idx)

            vertical_content_widget.addWidget(frame)

        scrollarea = QScrollArea()
        scrollarea.setWidgetResizable(True)
        scrollarea.setWidget(content_widget)
        main_layout.addWidget(scrollarea)

    def show_next_window(self, idx):
        self.next_win = NextWin(idx)
        self.next_win.show()


class NextWin(QWidget):
    def __init__(self, idx):
        super().__init__()
        self.resize(200, 150)
        self.setWindowTitle(f"Просмотр деталей товара {idx + 1}")

        layout = QVBoxLayout(self)
        label = QLabel(f"Детали товара {idx + 1}")
        layout.addWidget(label)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())

