import os
import pymysql
from dotenv import load_dotenv
from PyQt6.QtWidgets import *
from PyQt6 import QtGui, QtCore
load_dotenv()

class Base():
    def __init__(self):
        conn = pymysql.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            db=os.getenv('DB_NAME')
        )

        self.cursor = conn.cursor()

    def show_meters(self):
        self.cursor.execute("select * from techic")
        meters = self.cursor.fetchall()
        return meters



class Main(QMainWindow):
    def __init__(self, db):
        self.db = db
        super().__init__()
        self.setWindowTitle("Ремонт")
        self.resize(800, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_vertical = QVBoxLayout(central_widget)

        scrollarea = QScrollArea()
        scrollarea.setWidgetResizable(True)
        central_vertical.addWidget(scrollarea)
        self.botton_next = QPushButton("Дальше")
        self.botton_back = QPushButton("Назад")
        self.botton_next.clicked.connect(self.go_next)

        central_vertical.addWidget(self.botton_next)
        central_vertical.addWidget(self.botton_back)

        self.stacked = QStackedLayout()
        self.stacked.addWidget()


        content_widget = QWidget()
        scrollarea.setWidget(content_widget)

        vertical_content = QVBoxLayout(content_widget)
        for i in self.db.show_meters():
            frame = QFrame()
            frame.setFrameShape(QFrame.Shape.Box)
            frame.setLineWidth(1)
            vertical_content.addWidget(frame)
            horizontal_content = QHBoxLayout(frame)

            content_pictures = QLabel()
            content_pictures.setPixmap(QtGui.QPixmap(f"resourse/icon1.png").scaled(100, 100))

            horizontal_content.addWidget(content_pictures)

            print(i)

        vertical_content.addStretch()

    def go_next(self):
        self.stacked.




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Main(Base())
    window.show()
    sys.exit(app.exec())
