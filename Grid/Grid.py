from PyQt6 import QtWidgets

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Центр поддержки клиентов")
        self.resize(700, 500)

        center = QtWidgets.QWidget()
        self.setCentralWidget(center)

        main_layout = QtWidgets.QGridLayout(center)


        self.label_support_center = QtWidgets.QLabel("Центр поддержки клиентов")

        self.label_new_application = QtWidgets.QLabel("Новая заявка")
        self.label_topic = QtWidgets.QLabel("Тема:")
        self.lineEdit_topic = QtWidgets.QLineEdit("Проблемы с доступом")

        self.label_priority = QtWidgets.QLabel("Приоритет:")
        self.lineEdit_priority = QtWidgets.QLineEdit("Средний")

        self.label_desc = QtWidgets.QLabel("Описание:")
        self.lineEdit_desc = QtWidgets.QLineEdit("Не могу войти в систему")

        self.label_categor = QtWidgets.QLabel("Катеория:")
        self.lineEdit_categor = QtWidgets.QLineEdit("Техническая")

        self.lineEdit_time = QtWidgets.QLineEdit("с 10:00")

        main_layout.addWidget(self.label_support_center, 0, 0, 1, 2)
        main_layout.addWidget(self.label_new_application, 1, 0)
        main_layout.addWidget(self.label_topic, 2, 0)
        main_layout.addWidget(self.lineEdit_topic, 2, 1, 1, 3)
        main_layout.addWidget(self.label_priority, 3, 0)
        main_layout.addWidget(self.lineEdit_priority, 3, 1)
        main_layout.addWidget(self.label_categor, 3, 2)
        main_layout.addWidget(self.lineEdit_categor, 3, 3)
        main_layout.addWidget(self.label_desc, 4, 0)
        main_layout.addWidget(self.lineEdit_desc, 4, 1)
        main_layout.addWidget(self.lineEdit_time, 5, 1)

        self.label_active_application = QtWidgets.QLabel("Активные заявки")

        self.label_01 = QtWidgets.QLabel("#001")
        self.label_02 = QtWidgets.QLabel("#002")
        self.label_03 = QtWidgets.QLabel("#003")
        self.label_04 = QtWidgets.QLabel("#004")

        self.lineEdit_nomber_001 = QtWidgets.QLineEdit("Ошибка оплаты")
        self.lineEdit_nomber_002 = QtWidgets.QLineEdit("Обновление данных")
        self.lineEdit_nomber_003 = QtWidgets.QLineEdit("Консультация")
        self.lineEdit_nomber_004 = QtWidgets.QLineEdit("Баги в интерфейсе")

        self.label_priority_001 = QtWidgets.QLabel("Приор:")
        self.label_priority_002 = QtWidgets.QLabel("Приор:")
        self.label_priority_003 = QtWidgets.QLabel("Приор:")
        self.label_priority_004 = QtWidgets.QLabel("Приор:")

        self.lineEdit_priority_001 = QtWidgets.QLineEdit("Высокий")
        self.lineEdit_priority_002 = QtWidgets.QLineEdit("Средний")
        self.lineEdit_priority_003 = QtWidgets.QLineEdit("Низкий")
        self.lineEdit_priority_004 = QtWidgets.QLineEdit("Высокий")

        main_layout.addWidget(self.label_active_application, 6, 0, 1, 2)
        main_layout.addWidget(self.label_01, 7, 0)
        main_layout.addWidget(self.lineEdit_nomber_001, 7, 1)
        main_layout.addWidget(self.label_priority_001, 7, 2)
        main_layout.addWidget(self.lineEdit_priority_001, 7, 3)

        main_layout.addWidget(self.label_02, 8, 0)
        main_layout.addWidget(self.lineEdit_nomber_002, 8, 1)
        main_layout.addWidget(self.label_priority_002, 8, 2)
        main_layout.addWidget(self.lineEdit_priority_002, 8, 3)

        main_layout.addWidget(self.label_03, 9, 0)
        main_layout.addWidget(self.lineEdit_nomber_003, 9, 1)
        main_layout.addWidget(self.label_priority_003, 9, 2)
        main_layout.addWidget(self.lineEdit_priority_003, 9, 3)

        main_layout.addWidget(self.label_04, 10, 0)
        main_layout.addWidget(self.lineEdit_nomber_004, 10, 1)
        main_layout.addWidget(self.label_priority_004, 10, 2)
        main_layout.addWidget(self.lineEdit_priority_004, 10, 3)

        self.label_statistic = QtWidgets.QLabel("Статистика")

        self.label_total_application = QtWidgets.QLabel("Всего заявок:")
        self.label_open = QtWidgets.QLabel("Открыто:")
        self.label_decided = QtWidgets.QLabel("Решено:")

        self.lineEdit_total_application = QtWidgets.QLineEdit("24")
        self.lineEdit_open = QtWidgets.QLineEdit("8")
        self.lineEdit_decided = QtWidgets.QLineEdit("16")

        self.button_create = QtWidgets.QLineEdit("Создать")
        self.button_appoint = QtWidgets.QLineEdit("Назначить")

        self.button_update = QtWidgets.QLineEdit("Обновить")
        self.button_close = QtWidgets.QLineEdit("Закрыть")

        main_layout.addWidget(self.label_statistic, 11, 0)
        main_layout.addWidget(self.label_total_application, 12, 0)
        main_layout.addWidget(self.lineEdit_total_application, 12, 1)
        main_layout.addWidget(self.button_create, 12, 2)
        main_layout.addWidget(self.button_update, 12, 3)

        main_layout.addWidget(self.label_open, 13, 0)
        main_layout.addWidget(self.lineEdit_open, 13, 1)
        main_layout.addWidget(self.button_appoint, 13, 2)
        main_layout.addWidget(self.button_close, 13, 3)

        main_layout.addWidget(self.label_decided, 14, 0)
        main_layout.addWidget(self.lineEdit_decided, 14, 1)



















if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
