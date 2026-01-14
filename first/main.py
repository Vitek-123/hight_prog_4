from PyQt6 import QtWidgets

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setuui()

    def setuui(self):
        self.setWindowTitle("Мониторинг Системы")
        self.resize(500, 350)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QtWidgets.QHBoxLayout(central_widget)

        self.label_proc = QtWidgets.QLabel("Процессор:")
        self.lineEdit_proc = QtWidgets.QLineEdit("45%")
        self.button_det = QtWidgets.QPushButton("Детали")
        self.label_memory = QtWidgets.QLabel("Память")
        self.lineEdit_memory = QtWidgets.QLineEdit("32/8 Гб")
        self.button_clear = QtWidgets.QPushButton("Очистить")

        vertical_left = QtWidgets.QVBoxLayout()
        vertical_left.addWidget(self.label_proc)
        vertical_left.addWidget(self.lineEdit_proc)
        vertical_left.addWidget(self.button_det)
        vertical_left.addWidget(self.label_memory)
        vertical_left.addWidget(self.lineEdit_memory)
        vertical_left.addWidget(self.button_clear)
        main_layout.addLayout(vertical_left)

        self.button_restart = QtWidgets.QPushButton("Перезапуск")
        self.button_copy = QtWidgets.QPushButton("Рез. копия")
        self.button_logi = QtWidgets.QPushButton("Логи")
        self.label_cmd = QtWidgets.QLabel("CMD")
        self.lineEdit_cmd = QtWidgets.QLineEdit("systemctl status")
        self.button_do = QtWidgets.QPushButton("выполнить")



        vertical_right = QtWidgets.QVBoxLayout()
        vertical_button = QtWidgets.QVBoxLayout()
        vertical_button.addWidget(self.button_restart)
        vertical_button.addWidget(self.button_copy)
        vertical_button.addWidget(self.button_logi)
        vertical_right.addLayout(vertical_button)


        horizontal_cmd = QtWidgets.QHBoxLayout()
        horizontal_cmd.addWidget(self.label_cmd)
        horizontal_cmd.addWidget(self.lineEdit_cmd)
        horizontal_cmd.addWidget(self.button_do)
        vertical_right.addLayout(horizontal_cmd)
        main_layout.addLayout(vertical_right)

















if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
