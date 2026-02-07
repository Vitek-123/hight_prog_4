import math
import os

import pymysql
from PyQt6 import QtGui
from PyQt6.QtWidgets import *
from dotenv import load_dotenv

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

    def go_in(self, login, password):
        self.cursor.execute("SELECT id_client from client where client.login = %s and client.password = %s;", (login, password))
        self.client = self.cursor.fetchall()
        if self.client:
            return self.client[0][0]
        else:
            return

    def info_user(self, id):
        self.cursor.execute("select name, surname, phone, email, photo from client where id_client = %s", id)
        self.name_user = self.cursor.fetchall()
        return self.name_user
    
    # НАЙТИ id по паролю



class Main(QMainWindow):
    def __init__(self, db):
        self.db = db
        self.current_user_id = None
        super().__init__()
        self.setWindowTitle("Ремонт")
        self.resize(800, 300)
        self.next_enable = True
        self.back_enable = False

        self.logIn_button = QPushButton("log_in")
        self.logIn_button.clicked.connect(self.log_in)

        self.central_vidget = QWidget()
        self.setCentralWidget(self.central_vidget)
        self.stacked_widget = QStackedWidget()

        self.group_box = QGroupBox()

        self.vertical_group = QVBoxLayout(self.group_box)

        # menubar start
        self.menu_bar = QMenuBar(parent=None)
        self.file = self.menu_bar.addMenu("Личный кабинет")

        self.action_info = QtGui.QAction("Каталог", self)
        self.action_exit = QtGui.QAction("Выход", self)
        self.action_user = QtGui.QAction("О пользователе", self)

        self.file.addAction(self.action_info)
        self.file.addAction(self.action_user)
        self.file.addAction(self.action_exit)

        self.action_exit.triggered.connect(self.exit)
        self.action_user.triggered.connect(self.user)
        self.action_info.triggered.connect(self.catalog)

        self.menu_bar.hide()
        # menubar end

        self.vertical_center = QVBoxLayout(self.central_vidget)

        # start H Layout for menu
        self.horizontal_for_menu = QHBoxLayout()

        self.horizontal_for_menu.addWidget(self.menu_bar)
        self.horizontal_for_menu.addStretch()
        self.horizontal_for_menu.addWidget(self.logIn_button)

        # end H Layout for menu

        self.stacked = QStackedLayout(self.vertical_group)
        self.central_button_next = QPushButton("Next")

        self.central_button_back = QPushButton("Back")
        self.central_button_back.setEnabled(self.back_enable)

        self.central_button_next.clicked.connect(self.go_next)
        self.central_button_back.clicked.connect(self.go_back)

        # bd

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

        # GROUP BOX 2


        self.group_box_user = QGroupBox("О пользоватете")
        self.vertical_group_vertical = QVBoxLayout(self.group_box_user)

        self.label_photo_user = QLabel("Фото")

        self.pictures_photo_user = QLabel()
        self.pictures_photo_user.setPixmap(QtGui.QPixmap("resourse/icon1.png").scaled(150, 150))

        self.name_user_label = QLabel("Имя")
        self.name_user_lineEdit = QLineEdit()

        self.surname_user_label = QLabel("Фамилия")
        self.surname_user_lineEdit = QLineEdit()

        self.email_user_label = QLabel("Почта")
        self.email_user_lineEdit = QLineEdit()

        self.phone_user_label = QLabel("Телефон")
        self.phone_user_lineEdit = QLineEdit()

        self.edit_pass_user_button = QPushButton("Изменить пароль")
        self.save_pass_user_button = QPushButton("Сохранить")

        self.edit_pass_user_button.clicked.connect(self.changepass)

        self.vertical_group_vertical.addWidget(self.label_photo_user)
        self.vertical_group_vertical.addWidget(self.pictures_photo_user)
        self.vertical_group_vertical.addWidget(self.name_user_label)
        self.vertical_group_vertical.addWidget(self.name_user_lineEdit)
        self.vertical_group_vertical.addWidget(self.surname_user_label)
        self.vertical_group_vertical.addWidget(self.surname_user_lineEdit)
        self.vertical_group_vertical.addWidget(self.email_user_label)
        self.vertical_group_vertical.addWidget(self.email_user_lineEdit)
        self.vertical_group_vertical.addWidget(self.phone_user_label)
        self.vertical_group_vertical.addWidget(self.phone_user_lineEdit)
        self.vertical_group_vertical.addWidget(self.edit_pass_user_button)
        self.vertical_group_vertical.addWidget(self.save_pass_user_button)

        # Добавление

        self.vertical_group.addWidget(self.central_button_next)
        self.vertical_group.addWidget(self.central_button_back)

        self.vertical_center.addLayout(self.horizontal_for_menu)
        self.stacked_widget.addWidget(self.group_box)
        self.stacked_widget.addWidget(self.group_box_user)
        self.vertical_center.addWidget(self.stacked_widget)
        self.group_box_user.hide()



    def go_next(self):
        if self.stacked.currentIndex() != -1:
            self.back_enable = True
            self.central_button_back.setEnabled(self.back_enable)
        if self.stacked.currentIndex() == self.count_page - 2:
            self.next_enable = False
            self.central_button_next.setEnabled(self.next_enable)
        self.stacked.setCurrentIndex(self.stacked.currentIndex()+1)

    def go_back(self):
        self.stacked.setCurrentIndex(self.stacked.currentIndex()-1)
        if self.stacked.currentIndex() == 0:
            self.back_enable = False
            self.central_button_back.setEnabled(self.back_enable)
        if self.stacked.currentIndex() != self.count_page:
            self.next_enable = True
            self.central_button_next.setEnabled(self.next_enable)

    def show_more_info(self, id):
        self.more_info = MoreInfo(self.db, id)
        self.more_info.show()

    def log_in(self):
        self.window = LogIn(self.db, self.menu_bar, self, self.logIn_button)
        self.window.show()

    def exit(self):
        self.menu_bar.hide()
        self.logIn_button.setEnabled(True)
        self.stacked_widget.setCurrentIndex(0)

    def user(self):
        self.stacked_widget.setCurrentIndex(1)

        self.info_user = Base().info_user(self.current_user_id)[0]

        self.name_user_lineEdit.setText(self.info_user[0])
        self.surname_user_lineEdit.setText(self.info_user[1])
        self.email_user_lineEdit.setText(self.info_user[3])
        self.phone_user_lineEdit.setText(self.info_user[2])
        self.pictures_photo_user.setPixmap(QtGui.QPixmap(f"face/{self.info_user[4]}").scaled(150, 150))  # ДОБАВИТЬ ФОТО В РЕСУРСЫ

    def catalog(self):
        self.stacked_widget.setCurrentIndex(0)

    def changepass(self):
        self.window = ChangePassword()
        self.window.show()


class ChangePassword(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(100, 200)
        self.setWindowTitle("Смена пароля")

        self.main_layout = QGridLayout(self)

        self.info_password_label = QLabel("Пароль минимум 8 символов среди которых заглавные\строчный буквы, цифры, символы.")

        self.old_password_label = QLabel("Старый пароль")
        self.old_password_lineEdit = QLineEdit()

        self.new_password_first_label = QLabel("Новый пароль")
        self.new_password_first_lineEdit = QLineEdit()

        self.new_password_second_label = QLabel("Повторите пароль")
        self.new_password_second_lineEdit = QLineEdit()

        self.button_saved = QPushButton("Сохранить")
        self.button_saved.clicked.connect(self.update_password)

        self.main_layout.addWidget(self.info_password_label, 0, 0, 1, 2)
        self.main_layout.addWidget(self.old_password_label, 1, 0)
        self.main_layout.addWidget(self.old_password_lineEdit, 1, 1)

        self.main_layout.addWidget(self.new_password_first_label, 2, 0)
        self.main_layout.addWidget(self.new_password_first_lineEdit, 2, 1)

        self.main_layout.addWidget(self.new_password_second_label, 3, 0)
        self.main_layout.addWidget(self.new_password_second_lineEdit, 3, 1)

        self.main_layout.addWidget(self.button_saved, 4, 0, 1, 2)

    def update_password(self):
        self.old_pass = self.old_password_lineEdit.text()
        self.first_pass = self.new_password_first_lineEdit.text()
        self.second_pass = self.new_password_second_lineEdit.text()

        if self.old_pass and self.first_pass and self.second_pass:
            if self.first_pass == self.second_pass:
               if self.old_pass != self.first_pass:
                   print("Вход")
               else:
                    QMessageBox.warning(self, "Eror", "Новый пароль должен отличаться от старого")
            else:
                QMessageBox.warning(self, "Eror", "Пароли не совпадают")

        else:
            QMessageBox.warning(self, "Eror", "Заполните все поля")
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


class LogIn(QWidget):
    def __init__(self, db, bar, main, logIn_button):
        super().__init__()
        self.db = db
        self.menu_bar = bar
        self.main_window = main
        self.logIn_button = logIn_button
        self.setWindowTitle("Login")
        self.resize(370, 370)

        self.lineEdit_login = QLineEdit("ivanov_i")
        self.lineEdit_pass = QLineEdit("password123")
        self.button_go = QPushButton("Войти")
        self.button_reg = QPushButton("Регистрация")
        self.button_go.clicked.connect(self.go_in)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.main_layout.addWidget(self.lineEdit_login)
        self.main_layout.addWidget(self.lineEdit_pass)
        self.main_layout.addWidget(self.button_go)
        self.main_layout.addWidget(self.button_reg)

    def go_in(self):
        self.login = self.lineEdit_login.text()
        self.password = self.lineEdit_pass.text()

        if self.login == "" or self.password == "":
            QMessageBox.warning(self, "Eror", "Заполните все поля")

        self.id_client = Base().go_in(self.login, self.password)
        if self.id_client:
            self.hide()
            self.menu_bar.show()
            if self.main_window:
                self.main_window.current_user_id = self.id_client
            self.logIn_button.setEnabled(False)
            QMessageBox.information(self, "", "Авторизация успешна")


        else:
            QMessageBox.warning(self,"Eror", "Неверный логин или пароль")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Main(Base())
    window.show()
    sys.exit(app.exec())
