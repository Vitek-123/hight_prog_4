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

    def repair(self):
        self.cursor.execute("select * from repair")
        repair = self.cursor.fetchall()
        return repair

    def more_info(self, id):
        self.cursor.execute(f"call More_info({id});")
        more_info = self.cursor.fetchall()
        return more_info



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

        #bd

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

            for i in self.technic:
                self.content_scroll_vertical_horizontal = QHBoxLayout()
                self.content_scroll_vertical.addLayout(self.content_scroll_vertical_horizontal)

                self.content_scroll_pictures = QLabel()
                self.content_scroll_pictures.setPixmap(QtGui.QPixmap(f"resourse/icon{i[0]}.png").scaled(100, 100))

                self.content_scroll_info = QLabel("Подробнее")
                self.content_scroll_info.setFrameShape(QFrame.Shape.Box)

                self.content_scroll_info.mousePressEvent = lambda event, id = i[0]: self.show_more_info(id)

                self.content_scroll_sale = QLabel()
                self.content_scroll_sale.setFrameShape(QFrame.Shape.Box)
                if i[2] == "Lenovo":
                    self.content_scroll_sale.setText("Скидка - 15%")
                else:
                    self.content_scroll_sale.setText("Скидка - 0%")



                self.content_scroll_vertical_horizontal.addWidget(self.content_scroll_pictures)
                self.content_scroll_vertical_horizontal.addWidget(self.content_scroll_info, stretch=5)
                self.content_scroll_vertical_horizontal.addWidget(self.content_scroll_sale, stretch=1)
                if (i[0]) % 5 == 0:
                    self.technic = self.technic[5:]
                    break





        # Добавление

        self.vertical_center.addWidget(self.central_button_next)
        self.vertical_center.addWidget(self.central_button_back)

    def go_next(self):
        self.stacked.setCurrentIndex(self.stacked.currentIndex()+1)

    def go_back(self):
        self.stacked.setCurrentIndex(self.stacked.currentIndex()-1)

    def show_more_info(self, id):
        self.more_info = MoreInfo(self.db, id)
        self.more_info.show()

class MoreInfo(QWidget):
    def __init__(self, db, id):
        self.db = db
        self.id = id
        super().__init__()
        self.setWindowTitle("Подробрее")
        self.resize(400, 400)

        self.main_layout = QVBoxLayout(self)

        self.more_info = self.db.more_info(self.id)

        self.type_technic = self.more_info[0][0]
        self.brend = self.more_info[0][1]
        self.model = self.more_info[0][2]
        self.work = self.more_info[0][3]
        self.price = self.more_info[0][4]

        self.main_layout.addWidget(QLabel(f"Тип: {self.type_technic}"))
        self.main_layout.addWidget(QLabel(f"Бренд: {self.brend}"))
        self.main_layout.addWidget(QLabel(f"Модель: {self.model}"))
        self.main_layout.addWidget(QLabel(f"Перечень работ: {self.work}"))
        self.main_layout.addWidget(QLabel(f"Цена: {str(self.price)}"))






if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Main(Base())
    window.show()
    sys.exit(app.exec())
