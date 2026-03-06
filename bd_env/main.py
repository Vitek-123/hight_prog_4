import math
import os
import re
import pymysql
from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import QDir
from PyQt6.QtWidgets import *
from dotenv import load_dotenv
import sys

load_dotenv()

class Base():
    def __init__(self):
        conn = pymysql.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            db=os.getenv('DB_NAME'),
            autocommit=True
        )

        self.cursor = conn.cursor()

    def technic(self):
        self.cursor.execute("select * from techic")
        meters = self.cursor.fetchall()
        return meters

    def curent_technic(self, id):
        self.cursor.execute("select * from techic where id_technic =%s", (id, ))
        meters = self.cursor.fetchall()
        return meters

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
        self.cursor.execute("select name, surname, phone, email, photo from client where id_client = %s", (id,))
        self.name_user = self.cursor.fetchall()
        return self.name_user

    def changepassword(self, new_password, id_client):
        self.cursor.execute("UPDATE client SET `password` = %s where id_client = %s;", (new_password, id_client))

    def update_client(self, name, surname, email, phone, id_client):
        self.cursor.execute("UPDATE client SET name = %s, surname = %s, email = %s, phone = %s where id_client = %s;", (name, surname, email, phone, id_client))
        return

    def create_client(self, name, surname, email, phone, login, password, photo):
        self.cursor.execute("CALL create_client(%s, %s, %s, %s, %s, %s, %s);",(name, surname, email, phone, login, password, photo))
        return
    def login_exist(self, login):
        self.cursor.execute("select id_client from client where login = %s", (login, ))
        self.data = self.cursor.fetchall()
        return self.data

    def insert_basket(self, id_technic, id_client):
        self.cursor.execute(
            "SELECT quantity FROM basket WHERE id_technic = %s AND id_client = %s",
            (id_technic, id_client)
        )
        result = self.cursor.fetchone()

        if result:
            new_quantity = result[0] + 1
            self.cursor.execute(
                "UPDATE basket SET quantity = %s WHERE id_technic = %s AND id_client = %s",
                (new_quantity, id_technic, id_client)
            )
            return new_quantity
        else:
            self.cursor.execute(
                "INSERT INTO basket(id_technic, id_client, quantity) VALUES (%s, %s, 1)",
                (id_technic, id_client)
            )
            return 1

    def pruduct_auth(self, id):
        self.cursor.execute("SELECT id_technic, quantity FROM basket WHERE id_client = %s", (id,))
        return self.cursor.fetchall()

    def quantity(self, id_t, id_c):
        self.cursor.execute("SELECT quantity FROM basket WHERE id_technic = %s AND id_client = %s;", (id_t, id_c))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return 0

    def update_quantity_direct(self, id_technic, id_client, new_quantity):
        if new_quantity <= 0:
            self.cursor.execute(
                "DELETE FROM basket WHERE id_technic = %s AND id_client = %s",
                (id_technic, id_client)
            )
        else:
            self.cursor.execute(
                "UPDATE basket SET quantity = %s WHERE id_technic = %s AND id_client = %s",
                (new_quantity, id_technic, id_client)
            )

    def price_technic(self, id_t, quantity):
        self.cursor.execute("select brend, price, id_technic from techic where id_technic = %s", (id_t, ))
        data = self.cursor.fetchall()
        summa = 0
        for sale in data:
            if sale[0] == "Lenovo":
                summa = (sale[1]*0.85)*quantity
            else:
                summa += sale[1]*quantity
        return summa

    def create_order(self, id_c):
        basket_items = self.pruduct_auth(id_c)
        if not basket_items:
            return False
        price = 0
        for items in basket_items:
            price_tichnic = self.price_technic(items[0], items[1])
            price += price_tichnic

        self.cursor.execute("INSERT INTO orders (date_time, id_client, price, id_typeOrder) VALUES (now(), %s, %s, 1);",
                            (id_c, price))
        id_order = self.cursor.lastrowid
        for items in basket_items:
            self.cursor.execute("INSERT INTO chek (id_technic, id_orders, quantity) VALUES(%s, %s, %s);",
                                (items[0], id_order, items[1]))
        self.cursor.execute("delete from basket where id_client = %s", (id_c,))


class Main(QMainWindow):
    def __init__(self, db):
        self.db = db
        self.current_user_id = None
        self.current_user_login = None
        self.current_user_password = None
        super().__init__()
        self.setWindowTitle("Ремонт")
        self.resize(800, 300)
        self.next_enable = True
        self.back_enable = False
        self.bascket_state = False
        self.previous_order_page = 3
        self.product = {}
        icon = QtGui.QIcon("resourse/icon.png")
        self.setWindowIcon(icon)

        self.order_detail_widget = OrderDetailWidget(self.db, self)

        self.logIn_button = QPushButton("log_in")
        self.logIn_button.clicked.connect(self.log_in)

        self.main_basket_button = QPushButton("Корзина")
        self.main_basket_button.clicked.connect(self.open_basket)

        self.central_vidget = QWidget()
        self.setCentralWidget(self.central_vidget)
        self.stacked_widget = QStackedWidget(self)

        self.group_box = QGroupBox("Каталог")

        self.vertical_group = QVBoxLayout(self.group_box)

        # menubar info start
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
        # menubar info end

        # menubar order start

        self.order_menuBar = QMenuBar()
        self.order = self.order_menuBar.addMenu("Заказы")

        self.active_order = QtGui.QAction("Активные заказы")
        self.history_order = QtGui.QAction("История заказов")

        self.active_order.triggered.connect(self.open_active_order)
        self.history_order.triggered.connect(self.open_history_order)

        self.order.addAction(self.active_order)
        self.order.addAction(self.history_order)

        self.order_menuBar.hide()

        # menubar order start

        self.vertical_center = QVBoxLayout(self.central_vidget)

        # start H Layout for menu
        self.horizontal_for_menu = QHBoxLayout()

        self.horizontal_for_menu.addWidget(self.menu_bar)
        self.horizontal_for_menu.addWidget(self.order_menuBar)
        self.horizontal_for_menu.addStretch()
        self.horizontal_for_menu.addWidget(self.main_basket_button)
        self.horizontal_for_menu.addWidget(self.logIn_button)

        # end H Layout for menu

        self.stacked = QStackedLayout(self.vertical_group)
        self.central_button_next = QPushButton("Next")

        self.central_button_back = QPushButton("Back")
        self.central_button_back.setEnabled(self.back_enable)

        self.central_button_next.clicked.connect(self.go_next)
        self.central_button_back.clicked.connect(self.go_back)

        # bd

        self.technic = Base().technic()
        self.count_product = len(self.technic)
        self.count_page = math.ceil(self.count_product/5)

        for i in range(self.count_page):
            self.content_widget = QWidget()
            self.vertical_for_scroll = QVBoxLayout(self.content_widget)

            self.scrollarea = QScrollArea(self)
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
                self.content_scroll_pictures.setPixmap(
                    QtGui.QPixmap(self.resource_path(f"resourse/icon{i[0]}.png")).scaled(100, 100)
                )

                self.content_scroll_info = QLabel("Подробнее")
                self.content_scroll_info.setFrameShape(QFrame.Shape.Box)

                self.content_scroll_info.mousePressEvent = lambda event, id = i[0]: self.show_more_info(id)

                self.content_scroll_sale_vertical = QVBoxLayout()
                self.content_scroll_sale_vertical.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)

                self.content_scroll_sale = QLabel()
                if i[2] == "Lenovo":
                    self.content_scroll_sale.setText("Скидка - 15%")
                else:
                    self.content_scroll_sale.setText("Скидка - 0%")

                self.content_scroll_bascket = QPushButton()
                self.content_scroll_bascket.clicked.connect(lambda _, id = i[0]: self.add_product_in_bascket(id))
                self.content_scroll_bascket.setIcon(
                    QtGui.QIcon(self.resource_path("resourse/basket.png"))
                )
                self.content_scroll_bascket.setFixedSize(55, 50)
                self.content_scroll_bascket.setIconSize(QtCore.QSize(32, 32))

                self.content_scroll_vertical_horizontal.addWidget(self.content_scroll_pictures)
                self.content_scroll_vertical_horizontal.addWidget(self.content_scroll_info, stretch=5)
                self.content_scroll_vertical_horizontal.addLayout(self.content_scroll_sale_vertical, stretch=2)
                self.content_scroll_sale_vertical.addWidget(self.content_scroll_sale)
                self.content_scroll_sale_vertical.addWidget(self.content_scroll_bascket)

                if (i[0]) % 5 == 0:
                    self.technic = self.technic[5:]
                    break

        # GROUP BOX 2

        self.group_box_user = QGroupBox("О пользоватете")
        self.vertical_group_vertical = QVBoxLayout(self.group_box_user)

        self.label_photo_user = QLabel("Фото")

        self.pictures_photo_user = QLabel()

        self.name_user_label = QLabel("Имя")
        self.name_user_lineEdit = QLineEdit()
        self.name_user_lineEdit.setEnabled(False)

        self.surname_user_label = QLabel("Фамилия")
        self.surname_user_lineEdit = QLineEdit()
        self.surname_user_lineEdit.setEnabled(False)

        self.email_user_label = QLabel("Почта")
        self.email_user_lineEdit = QLineEdit()
        self.email_user_lineEdit.setEnabled(False)

        self.phone_user_label = QLabel("Телефон")
        self.phone_user_lineEdit = QLineEdit()
        self.phone_user_lineEdit.setEnabled(False)

        self.edit_pass_user_button = QPushButton("Изменить пароль")
        self.red_pass_user_button = QPushButton("Редактировать")
        self.red_pass_user_button.clicked.connect(self.red_info)

        self.save_pass_user_button = QPushButton("Сохранить")
        self.save_pass_user_button.clicked.connect(self.update_client)
        self.save_pass_user_button.hide()

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
        self.vertical_group_vertical.addWidget(self.red_pass_user_button)
        self.vertical_group_vertical.addWidget(self.save_pass_user_button)

        # GROUP BOX 3 Basket

        self.group_box_basket = QGroupBox("Корзина")

        self.create_order = QPushButton("Оформить заказ")
        self.create_order.clicked.connect(self.create_orders)

        self.basket_main_layout = QVBoxLayout(self.group_box_basket)

        self.basket_scroll = QScrollArea()
        self.basket_scroll.setWidgetResizable(True)

        self.basket_content_widget = QWidget()

        self.basket_content_layout = QVBoxLayout(self.basket_content_widget)

        self.basket_scroll.setWidget(self.basket_content_widget)

        self.basket_main_layout.addWidget(self.basket_scroll)
        self.basket_main_layout.addWidget(self.create_order)

        # GROUP BOX 4 ORDERS

        self.grop_active_order = QGroupBox("Активные заказы")

        self.active_order_vertical = QVBoxLayout(self.grop_active_order)

        self.grop_history_order = QGroupBox("История заказов")
        self.history_order_vertical = QVBoxLayout(self.grop_history_order)
        self.history_order_vertical.addWidget(QLabel("История заказов"))

        # Добавление

        self.vertical_group.addWidget(self.central_button_next)
        self.vertical_group.addWidget(self.central_button_back)

        self.vertical_center.addLayout(self.horizontal_for_menu)
        self.stacked_widget.addWidget(self.group_box)  # 0
        self.stacked_widget.addWidget(self.group_box_user)  # 1
        self.stacked_widget.addWidget(self.group_box_basket)  # 2
        self.stacked_widget.addWidget(self.grop_active_order)  # 3
        self.stacked_widget.addWidget(self.grop_history_order)  # 4
        self.stacked_widget.addWidget(self.order_detail_widget)  # 5
        self.vertical_center.addWidget(self.stacked_widget)

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    sub_layout = item.layout()
                    if sub_layout:
                        self.clear_layout(sub_layout)

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
        self.window = LogIn(self.db, self.menu_bar, self, self.logIn_button, self.product, self.stacked_widget, self.main_basket_button, self.order_menuBar)
        self.window.show()

    def exit(self):
        self.menu_bar.hide()
        self.logIn_button.setEnabled(True)
        self.stacked_widget.setCurrentIndex(0)
        self.phone_user_lineEdit.setEnabled(False)
        self.email_user_lineEdit.setEnabled(False)
        self.surname_user_lineEdit.setEnabled(False)
        self.name_user_lineEdit.setEnabled(False)

        self.product.clear()

        self.clear_layout(self.basket_content_layout)

        self.main_basket_button.setText("Корзина")
        self.bascket_state = False
        print(self.bascket_state)

        self.save_pass_user_button.hide()
        self.red_pass_user_button.show()

    def user(self):
        self.stacked_widget.setCurrentIndex(1)

        self.info_user = Base().info_user(self.current_user_id)[0]

        self.name_user_lineEdit.setText(self.info_user[0])
        self.surname_user_lineEdit.setText(self.info_user[1])
        self.email_user_lineEdit.setText(self.info_user[3])
        self.phone_user_lineEdit.setText(self.info_user[2])
        self.pictures_photo_user.setPixmap(
            QtGui.QPixmap(self.resource_path(f"face/{self.info_user[4]}")).scaled(150, 150)
        )

    def open_basket(self):
        if self.stacked_widget.currentIndex() != 2:
            self.stacked_widget.setCurrentIndex(2)
            self.main_basket_button.setText("Закрыть корзину")
            self.bascket_state = True
            self.update_basket_content()
        else:
            self.stacked_widget.setCurrentIndex(0)
            self.main_basket_button.setText("Корзина")
            self.bascket_state = False

    def update_basket_content(self):
        self.clear_layout(self.basket_content_layout)

        if self.current_user_id:
            basket_items = Base().pruduct_auth(self.current_user_id)
            for item in basket_items:
                product_id = item[0]
                quantity = item[1]
                try:
                    tech_info = Base().curent_technic(product_id)
                    if tech_info and tech_info[0]:
                        self.add_basket_item_widget(tech_info[0], quantity)
                except Exception as e:
                    print(f"Ошибка при загрузке товара {product_id}: {e}")
        else:
            for product_id, quantity in self.product.items():
                try:
                    tech_info = Base().curent_technic(product_id)
                    if tech_info and tech_info[0]:
                        self.add_basket_item_widget(tech_info[0], quantity)
                except Exception as e:
                    print(f"Ошибка при загрузке товара {product_id}: {e}")

        if not self.basket_content_layout.count():
            empty_label = QLabel("Корзина пуста")
            empty_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.basket_content_layout.addWidget(empty_label)
            self.create_order.setEnabled(False)
        else:
            self.create_order.setEnabled(True)

    def add_basket_item_widget(self, tech_info, quantity=1):
        content_scroll_vertical_horizonta = QHBoxLayout()
        self.basket_content_layout.addLayout(content_scroll_vertical_horizonta)

        content_scroll_picture = QLabel()
        content_scroll_picture.setPixmap(
            QtGui.QPixmap(self.resource_path(f"resourse/icon{tech_info[0]}.png")).scaled(100, 100)
        )

        info_layout = QVBoxLayout()
        name_label = QLabel(f"{tech_info[2]}")
        info_layout.addWidget(name_label)

        more_info_btn = QPushButton("Подробнее")
        more_info_btn.clicked.connect(lambda: self.show_more_info(tech_info[0]))

        quantity_layout = QHBoxLayout()

        minus_btn = QPushButton("-")
        minus_btn.setMaximumWidth(30)
        minus_btn.clicked.connect(lambda: self.decrease_quantity(tech_info[0]))

        quantity_label = QLabel(str(quantity))
        quantity_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        quantity_label.setMinimumWidth(30)

        plus_btn = QPushButton("+")
        plus_btn.setMaximumWidth(30)
        plus_btn.clicked.connect(lambda: self.increase_quantity(tech_info[0]))

        quantity_layout.addWidget(minus_btn)
        quantity_layout.addWidget(quantity_label)
        quantity_layout.addWidget(plus_btn)

        delete_btn = QPushButton("Удалить")
        delete_btn.clicked.connect(lambda: self.remove_from_basket(tech_info[0]))

        sale_label = QLabel()
        if tech_info[2] == "Lenovo":
            sale_label.setText("Скидка - 15%")
        else:
            sale_label.setText("Скидка - 0%")

        content_scroll_vertical_horizonta.addWidget(content_scroll_picture)
        content_scroll_vertical_horizonta.addLayout(info_layout, stretch=3)
        content_scroll_vertical_horizonta.addWidget(more_info_btn)
        content_scroll_vertical_horizonta.addLayout(quantity_layout)
        content_scroll_vertical_horizonta.addWidget(delete_btn)
        content_scroll_vertical_horizonta.addWidget(sale_label)

    def increase_quantity(self, product_id):
        if self.current_user_id:
            try:
                current_quantity = Base().quantity(product_id, self.current_user_id)
                new_quantity = current_quantity + 1

                Base().update_quantity_direct(product_id, self.current_user_id, new_quantity)

                if self.bascket_state:
                    self.update_basket_content()
            except Exception as e:
                print(f"Ошибка при увеличении количества: {e}")
        else:
            if product_id in self.product:
                self.product[product_id] += 1
                if self.bascket_state:
                    self.update_basket_content()

    def decrease_quantity(self, product_id):
        if self.current_user_id:
            try:
                current_quantity = Base().quantity(product_id, self.current_user_id)

                if current_quantity > 1:
                    new_quantity = current_quantity - 1
                    Base().update_quantity_direct(product_id, self.current_user_id, new_quantity)
                else:
                    reply = QMessageBox.question(
                        self,
                        'Подтверждение',
                        'Удалить товар из корзины?',
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                    )
                    if reply == QMessageBox.StandardButton.Yes:
                        Base().update_quantity_direct(product_id, self.current_user_id, 0)  # 0 = удалить

                if self.bascket_state:
                    self.update_basket_content()
            except Exception as e:
                print(f"Ошибка при уменьшении количества: {e}")
        else:
            if product_id in self.product:
                if self.product[product_id] > 1:
                    self.product[product_id] -= 1
                else:
                    reply = QMessageBox.question(
                        self,
                        'Подтверждение',
                        'Удалить товар из корзины?',
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                    )
                    if reply == QMessageBox.StandardButton.Yes:
                        del self.product[product_id]

                if self.bascket_state:
                    self.update_basket_content()

    def remove_from_basket(self, product_id):
        reply = QMessageBox.question(
            self,
            'Подтверждение',
            'Удалить товар из корзины?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            if self.current_user_id:
                try:
                    Base().update_quantity_direct(product_id, self.current_user_id, 0)
                except Exception as e:
                    print(f"Ошибка при удалении из корзины: {e}")
            else:
                if product_id in self.product:
                    del self.product[product_id]

            if self.bascket_state:
                self.update_basket_content()

    def add_product_in_bascket(self, id):
        if not self.current_user_id:
            if id in self.product:
                self.product[id] += 1
            else:
                self.product[id] = 1

            if self.bascket_state:
                self.update_basket_content()
        else:
            try:
                if self.bascket_state:
                    self.update_basket_content()
            except Exception as e:
                print(f"Ошибка при добавлении в корзину: {e}")
                QMessageBox.warning(self, "Ошибка", "Не удалось добавить товар в корзину")

    def catalog(self):
        self.stacked_widget.setCurrentIndex(0)

    def changepass(self):
        self.window = ChangePassword(self.current_user_login, self.current_user_password)
        self.window.show()

    def red_info(self):
        self.save_pass_user_button.show()
        self.red_pass_user_button.hide()
        self.phone_user_lineEdit.setEnabled(True)
        self.email_user_lineEdit.setEnabled(True)
        self.surname_user_lineEdit.setEnabled(True)
        self.name_user_lineEdit.setEnabled(True)

    def update_client(self):
        new_name = self.name_user_lineEdit.text().strip()
        new_surname = self.surname_user_lineEdit.text().strip()
        new_email = self.email_user_lineEdit.text().strip()
        new_phone = self.phone_user_lineEdit.text().strip()

        if new_name or new_surname or new_email or new_phone:
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', new_email):
                if re.match(r'^\+7 \(\d{3}\) \d{3}-\d{4}$', new_phone):
                    Base().update_client(new_name, new_surname, new_email, new_phone, self.current_user_id)
                    QMessageBox.information(self, "info", "ДАнные изменены")
                    self.phone_user_lineEdit.setEnabled(False)
                    self.email_user_lineEdit.setEnabled(False)
                    self.surname_user_lineEdit.setEnabled(False)
                    self.name_user_lineEdit.setEnabled(False)
                else:
                    QMessageBox.warning(self, "Ошибка", "Введите корректный номер телефона")
                    return
            else:
                QMessageBox.warning(self, "Ошибка", "Введите корректный email адрес")
                return
        else:
            QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены")
            return

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def open_active_order(self):
        self.load_active_orders()
        self.previous_order_page = 3
        self.stacked_widget.setCurrentIndex(3)

    def open_history_order(self):
        self.load_history_orders()
        self.previous_order_page = 4
        self.stacked_widget.setCurrentIndex(4)

    def show_order_details(self, order_id, order_price):
        self.order_detail_widget.load_order_details(order_id, order_price)
        self.stacked_widget.setCurrentIndex(5)

    def create_orders(self):
        try:
            scroll_widget = self.basket_scroll.widget()
            if self.current_user_id:
                if QMessageBox.question(self, "Подтверждение заказа", "Вы уверены что хотите оформить заказ?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No) == QMessageBox.StandardButton.Yes:
                    Base().create_order(self.current_user_id)
                    if scroll_widget and scroll_widget.layout():
                        self.clear_layout(scroll_widget.layout())
                    go_activ_orders = QMessageBox.question(self, "Заказ оформлен", "Пернйти в активные заказы?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                    self.update_basket_content()
                    if go_activ_orders == QMessageBox.StandardButton.Yes:
                        self.open_active_order()
            else:
                QMessageBox.information(self, "info", "Чтобы сделать заказ авторизируйтесь")
        except Exception as e:
            print(e)

    def load_active_orders(self):
        try:
            active_layout = self.grop_active_order.layout()
            self.clear_layout(active_layout)

            title_label = QLabel("Активные заказы")
            active_layout.addWidget(title_label)

            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)

            content_widget = QWidget()
            content_layout = QVBoxLayout(content_widget)

            self.db.cursor.execute("""
                SELECT orders.id_order, orders.price, orders.date_time, type_order.type
                FROM orders
                JOIN type_order ON type_order.id_typeOrder = orders.id_typeOrder
                WHERE orders.id_client = %s AND orders.id_typeOrder IN (1, 2, 3)
                ORDER BY orders.date_time DESC
            """, (self.current_user_id,))

            orders = self.db.cursor.fetchall()

            if not orders:
                empty_label = QLabel("Нет активных заказов")
                empty_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                empty_label.setStyleSheet("padding: 20px;")
                content_layout.addWidget(empty_label)
            else:
                for order in orders:
                    order_widget = OrderWidget(
                        self.db,
                        order[0],  # id_order
                        order[1],  # price
                        order[2].strftime("%d.%m.%Y %H:%M"),  # date_time
                        order[3]  # type
                    )
                    content_layout.addWidget(order_widget)

            scroll_area.setWidget(content_widget)
            active_layout.addWidget(scroll_area)

        except Exception as e:
            print(f"Ошибка при загрузке активных заказов: {e}")
            QMessageBox.warning(self, "Ошибка", "Не удалось загрузить активные заказы")

    def load_history_orders(self):
        try:
            history_layout = self.grop_history_order.layout()
            self.clear_layout(history_layout)

            title_label = QLabel("История заказов")
            history_layout.addWidget(title_label)

            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)

            content_widget = QWidget()
            content_layout = QVBoxLayout(content_widget)

            self.db.cursor.execute("""
                SELECT orders.id_order, orders.price, orders.date_time, type_order.type
                FROM orders
                JOIN type_order ON type_order.id_typeOrder = orders.id_typeOrder
                WHERE orders.id_client = %s AND orders.id_typeOrder IN (4, 5, 6)
                ORDER BY orders.date_time DESC
            """, (self.current_user_id,))

            orders = self.db.cursor.fetchall()

            if not orders:
                empty_label = QLabel("Нет истории заказов")
                empty_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                empty_label.setStyleSheet("padding: 20px;")
                content_layout.addWidget(empty_label)
            else:
                for order in orders:
                    order_widget = OrderWidget(
                        self.db,
                        order[0],  # id_order
                        order[1],  # price
                        order[2].strftime("%d.%m.%Y %H:%M"),  # date_time
                        order[3]  # type
                    )
                    content_layout.addWidget(order_widget)

            scroll_area.setWidget(content_widget)
            history_layout.addWidget(scroll_area)

        except Exception as e:
            print(f"Ошибка при загрузке истории заказов: {e}")
            QMessageBox.warning(self, "Ошибка", "Не удалось загрузить историю заказов")


class Registration(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регистрация")
        self.resize(400, 400)

        self.main_layou = QGridLayout(self)

        self.name_label = QLabel("Введите имя")
        self.name_line = QLineEdit()
        self.name_line.setPlaceholderText("Введите имя")

        self.surname_label = QLabel("Введите фамилию")
        self.surname_line = QLineEdit()
        self.surname_line.setPlaceholderText("Введите фамилию")

        self.email_label = QLabel("Введите почту")
        self.email_line = QLineEdit()
        self.email_line.setPlaceholderText("Введите почту")

        self.phone_label = QLabel("Введите номер")
        self.phone_line = QLineEdit()
        self.phone_line.setPlaceholderText("+7 (___) ___-____")
        self.phone_line.setInputMask("+7 (000) 000-0000")

        self.login_label = QLabel("Введите логин")
        self.login_line = QLineEdit()
        self.login_line.setPlaceholderText("Введите логин")

        self.password_label = QLabel("Введите пароль.")
        self.password_line = QLineEdit()
        self.password_line.setPlaceholderText("Введите пароль")

        self.add_photo_button = QPushButton("выбрать фото")
        self.add_photo_button.clicked.connect(self.add_photo)

        self.add_photo_label = QLabel("Выбрано фото")
        self.add_photo_label.hide()
        self.add_photo_line = QLineEdit()
        self.add_photo_line.hide()

        self.button_red = QPushButton("Регистрация")
        self.button_red.clicked.connect(self.registration)
        self.button_auth = QPushButton("Войти")

        # Добавление
        self.main_layou.addWidget(self.name_label, 0, 0)
        self.main_layou.addWidget(self.name_line, 0, 1)
        self.main_layou.addWidget(self.surname_label, 1, 0)
        self.main_layou.addWidget(self.surname_line, 1, 1)
        self.main_layou.addWidget(self.email_label, 2, 0)
        self.main_layou.addWidget(self.email_line, 2, 1)
        self.main_layou.addWidget(self.phone_label, 3, 0)
        self.main_layou.addWidget(self.phone_line, 3, 1)
        self.main_layou.addWidget(self.login_label, 4, 0)
        self.main_layou.addWidget(self.login_line, 4, 1)
        self.main_layou.addWidget(self.password_label, 5, 0)
        self.main_layou.addWidget(self.password_line, 5, 1)
        self.main_layou.addWidget(self.add_photo_button, 6, 0, 1, 2)
        self.main_layou.addWidget(self.add_photo_label, 7, 0)
        self.main_layou.addWidget(self.add_photo_line, 7, 1)
        self.main_layou.addWidget(self.button_auth, 8, 0)
        self.main_layou.addWidget(self.button_red, 8, 1)

    def registration(self):
        try:
            name = self.name_line.text()
            surname = self.surname_line.text()
            email = self.email_line.text()
            phone = self.phone_line.text()
            login = self.login_line.text()
            password = self.password_line.text()
            photo = self.add_photo_line.text()

            if name and surname and email and phone and login and password and photo:
                if not Base().login_exist(login):
                    if len(password) > 7 and re.search(r'[A-ZА-Яa-zа-я\d!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', password):
                        Base().create_client(name, surname, email, phone, login, password, photo)
                        QMessageBox.information(self, "info", "Регистрация успешна")
                        self.hide()
                        self.name_line.clear()
                        self.surname_line.clear()
                        self.email_line.clear()
                        self.phone_line.clear()
                        self.login_line.clear()
                        self.password_line.clear()
                        self.add_photo_line.clear()
                    else:
                        QMessageBox.warning(self, "Eror", "Пароль не соответствует требованиям")
                else:
                    QMessageBox.warning(self, "Eror", "Пользователь с таким логином уже существуеь")
            else:
                QMessageBox.warning(self, "Eror", "Заполните все поля")
        except Exception as e:
            print(e)

    def add_photo(self):
        filters = {
            "Изображения (*.png *.jpg *.jpeg *.bmp *.gif)",
        }
        file_name, selected_filter = QFileDialog.getOpenFileName(
            self,
            "Выберите файл",
            QDir.homePath(),
            ";;".join(filters)
        )

        if file_name:
            self.add_photo_label.show()
            self.add_photo_line.show()
            name = file_name.split("/")
            self.add_photo_line.setText(f"{name[-1]}")
            self.add_photo_line.setEnabled(False)

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)


class ChangePassword(QWidget):
    def __init__(self, login, password):
        self.current_login = login
        self.current_password = password
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
        self.current_user = Base().go_in(self.current_login, self.old_pass)

        if self.old_pass and self.first_pass and self.second_pass:
            if self.current_user:
                if self.first_pass == self.second_pass:
                   if self.old_pass != self.first_pass:
                       if len(self.first_pass) > 7 and re.search(r'[A-ZА-Яa-zа-я\d!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', self.first_pass):
                           QMessageBox.information(self, "info", "Пароль обновлен")
                           Base().changepassword(self.first_pass, self.current_user)
                       else:
                         QMessageBox.warning(self, "Eror", "Новый пароль не соответствует требованиям")
                   else:
                        QMessageBox.warning(self, "Eror", "Новый пароль должен отличаться от старого")
                else:
                    QMessageBox.warning(self, "Eror", "Пароли не совпадают")
            else:
                QMessageBox.warning(self, "Eror", "Пользователя с таким паролем не существует")
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


class OrderWidget(QFrame):

    def __init__(self, db, order_id, order_price, order_date, order_type, parent=None):
        super().__init__(parent)
        self.db = db
        self.order_id = order_id
        self.order_price = order_price
        self.order_date = order_date
        self.order_type = order_type

        self.setFrameShape(QFrame.Shape.Box)

        layout = QHBoxLayout(self)

        info_layout = QVBoxLayout()
        info_layout.addWidget(QLabel(f"<b>Заказ №{order_id}</b>"))
        info_layout.addWidget(QLabel(f"Дата: {order_date}"))
        info_layout.addWidget(QLabel(f"Статус: {order_type}"))
        info_layout.addWidget(QLabel(f"Сумма: {order_price} руб."))

        detail_btn = QPushButton("Подробнее")
        detail_btn.setFixedSize(100, 30)
        detail_btn.clicked.connect(self.show_details)

        layout.addLayout(info_layout, stretch=1)
        layout.addWidget(detail_btn)

    def show_details(self):
        main_window = self.get_main_window()
        if main_window:
            main_window.show_order_details(self.order_id, self.order_price)

    def get_main_window(self):
        parent = self.parent()
        while parent:
            if isinstance(parent, Main):
                return parent
            parent = parent.parent()
        return None


class OrderDetailWidget(QWidget):
    def __init__(self, db, main_window):
        super().__init__()
        self.db = db
        self.main_window = main_window
        self.current_order_id = None
        self.current_order_price = None

        self.main_layout = QVBoxLayout(self)

        self.title_label = QLabel("Детали заказа")
        self.main_layout.addWidget(self.title_label)

        self.back_button = QPushButton("← Назад к заказам")
        self.back_button.clicked.connect(self.go_back)
        self.main_layout.addWidget(self.back_button)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)

        self.scroll_area.setWidget(self.content_widget)
        self.main_layout.addWidget(self.scroll_area)

    def load_order_details(self, order_id, order_price):
        self.current_order_id = order_id
        self.current_order_price = order_price

        self.title_label.setText(f"Заказ №{order_id} - Сумма: {order_price} руб.")

        self.clear_layout(self.content_layout)

        try:
            self.db.cursor.execute("""
                SELECT techic.photo, techic.model, techic.brend, 
                       techic.price, chek.quantity
                FROM techic
                JOIN chek ON chek.id_technic = techic.id_technic
                WHERE chek.id_orders = %s
            """, (order_id,))

            items = self.db.cursor.fetchall()

            if not items:
                empty_label = QLabel("Нет товаров в заказе")
                empty_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.content_layout.addWidget(empty_label)
                return

            for item in items:
                self.add_order_item_widget(item)

        except Exception as e:
            print(f"Ошибка при загрузке товаров заказа: {e}")
            error_label = QLabel("Ошибка загрузки данных")
            error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.content_layout.addWidget(error_label)

    def add_order_item_widget(self, item_data):
        photo, model, brend, price, quantity = item_data

        item_widget = QFrame()
        item_widget.setFrameShape(QFrame.Shape.Box)

        item_layout = QHBoxLayout(item_widget)

        photo_label = QLabel()
        try:
            import re
            match = re.search(r'\d+', photo)
            if match:
                tech_id = match.group()
                photo_path = self.main_window.resource_path(f"resourse/icon{tech_id}.png")
                print(f"Пробуем путь с ID {tech_id}: {photo_path}")

                if os.path.exists(photo_path):
                    pixmap = QtGui.QPixmap(photo_path)
                    if not pixmap.isNull():
                        photo_label.setPixmap(pixmap.scaled(80, 80, QtCore.Qt.AspectRatioMode.KeepAspectRatio))
                    else:
                        photo_label.setText("📷")
                        photo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        photo_label.setFixedSize(80, 80)
                else:
                    photo_label.setText("📷")
                    photo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    photo_label.setFixedSize(80, 80)
            else:
                photo_path = self.main_window.resource_path(f"resourse/{photo}")
                print(f"Пробуем оригинальный путь: {photo_path}")

                if os.path.exists(photo_path):
                    pixmap = QtGui.QPixmap(photo_path)
                    if not pixmap.isNull():
                        photo_label.setPixmap(pixmap.scaled(80, 80, QtCore.Qt.AspectRatioMode.KeepAspectRatio))
                    else:
                        photo_label.setText("📷")
                        photo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        photo_label.setFixedSize(80, 80)
                else:
                    photo_label.setText("📷")
                    photo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    photo_label.setFixedSize(80, 80)

        except Exception as e:
            print(f"Ошибка при загрузке фото: {e}")
            photo_label.setText("📷")
            photo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            photo_label.setFixedSize(80, 80)

        info_layout = QVBoxLayout()
        info_layout.addWidget(QLabel(f"<b>{brend} {model}</b>"))
        info_layout.addWidget(QLabel(f"Цена: {price} руб."))
        info_layout.addWidget(QLabel(f"Количество: {quantity}"))
        info_layout.addWidget(QLabel(f"Сумма: {price * quantity} руб."))

        item_layout.addWidget(photo_label)
        item_layout.addLayout(info_layout, stretch=1)

        self.content_layout.addWidget(item_widget)

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    sub_layout = item.layout()
                    if sub_layout:
                        self.clear_layout(sub_layout)

    def go_back(self):
        self.main_window.stacked_widget.setCurrentIndex(self.main_window.previous_order_page)


class LogIn(QWidget):
    def __init__(self, db, bar, main, logIn_button, product, stacked_widget, main_basket_button, order_menuBar ):
        super().__init__()
        self.db = db
        self.menu_bar = bar
        self.order_menuBar = order_menuBar
        self.main_window = main
        self.logIn_button = logIn_button
        self.product = product
        self.main_basket_button = main_basket_button
        self.stacked_widget = stacked_widget
        self.setWindowTitle("Login")
        self.resize(370, 370)

        self.lineEdit_login = QLineEdit("petrov_p")
        self.lineEdit_pass = QLineEdit("password123")
        self.button_go = QPushButton("Войти")
        self.button_reg = QPushButton("Регистрация")
        self.button_go.clicked.connect(lambda :self.go_in(self.product))
        self.button_reg.clicked.connect(self.registration)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.main_layout.addWidget(self.lineEdit_login)
        self.main_layout.addWidget(self.lineEdit_pass)
        self.main_layout.addWidget(self.button_go)
        self.main_layout.addWidget(self.button_reg)

    def go_in(self, product):
        self.login = self.lineEdit_login.text()
        self.password = self.lineEdit_pass.text()

        if self.login == "" or self.password == "":
            QMessageBox.warning(self, "Eror", "Заполните все поля")
        else:
            self.id_client = Base().go_in(self.login, self.password)
            if self.id_client:
                self.hide()
                self.menu_bar.show()
                self.order_menuBar.show()

                if product:
                    for tovar_id, quantity in product.items():
                        for _ in range(quantity):
                            Base().insert_basket(tovar_id, self.id_client)

                if self.main_window:
                    self.main_window.current_user_id = self.id_client
                    self.main_window.current_user_login = self.login
                    self.main_window.current_user_password = self.password

                    self.main_window.product.clear()

                    if self.main_window.bascket_state:
                        self.main_window.update_basket_content()

                self.logIn_button.setEnabled(False)
                self.stacked_widget.setCurrentIndex(0)
                self.main_basket_button.setText("Корзина")
                QMessageBox.information(self, "", "Авторизация успешна")
            else:
                QMessageBox.warning(self, "Eror", "Неверный логин или пароль")

    def registration(self):
        self.window = Registration()
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Main(Base())
    window.show()
    sys.exit(app.exec())
