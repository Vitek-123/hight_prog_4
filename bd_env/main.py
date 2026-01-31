import os
import pymysql
from dotenv import load_dotenv
from PyQt6.QtWidgets import *
from PyQt6 import QtGui, QtCore
import math
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

    def technic(self):
        self.cursor.execute("select * from techic")
        meters = self.cursor.fetchall()
        return meters



class Main(QMainWindow):
    def __init__(self, db):
        self.db = db
        super().__init__()
        self.setWindowTitle("Ремонт")
        self.resize(800, 300)

        self.central_vidget = QWidget()
        self.setCentralWidget(self.central_vidget)

        self.vertical_center = QVBoxLayout(self.central_vidget)

        self.stacked = QStackedLayout(self.vertical_center)
        self.central_button_next = QPushButton("Next")
        self.central_button_back = QPushButton("Back")

        self.central_button_next.clicked.connect(self.go_next)
        self.central_button_back.clicked.connect(self.go_back)

        self.technic = self.db.technic()
        self.count_product = len(self.technic)
        self.count_page = math.ceil(self.count_product/5)

        for i in range(self.count_page):
            self.content_widget = QWidget()
            self.vertical_for_scroll = QVBoxLayout(self.content_widget)

            self.scrollarea = QScrollArea()
            self.scrollarea.setWidgetResizable(True)

            self.vertical_scroll = QVBoxLayout()
            self.scrollarea.setLayout(self.vertical_scroll)

            self.content_scroll_widget = QWidget()
            self.content_scroll_vertical = QVBoxLayout(self.content_scroll_widget)


            self.vertical_for_scroll.addWidget(self.scrollarea)
            self.scrollarea.setWidget(self.content_scroll_widget)
            self.stacked.addWidget(self.content_widget)
            self.stop_product = 0
            i = self.stop_product
            for i in self.technic:
                if i[0] % 6 == 0:
                    break
                else:
                    self.content_scroll_vertical.addWidget(QLabel(f"{i[0]}"))


        # Добавление

        self.vertical_center.addWidget(self.central_button_next)
        self.vertical_center.addWidget(self.central_button_back)

    def go_next(self):
        self.stacked.setCurrentIndex(self.stacked.currentIndex()+1)

    def go_back(self):
        self.stacked.setCurrentIndex(self.stacked.currentIndex()-1)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Main(Base())
    window.show()
    sys.exit(app.exec())
