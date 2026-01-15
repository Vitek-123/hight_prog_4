from PyQt6 import QtWidgets

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Форма реистрации")
        self.resize(700, 500)

        window = QtWidgets.QWidget()
        self.setCentralWidget(window)

        self.label_new_reg = QtWidgets.QLabel("Регистрация нового пользователя")
        self.label_name = QtWidgets.QLabel("Имя:")
        self.label_surname = QtWidgets.QLabel("Фамилия:")
        self.label_age = QtWidgets.QLabel("Возраст:")

        self.lineEdit_name = QtWidgets.QLineEdit()
        self.lineEdit_surname = QtWidgets.QLineEdit()
        self.lineEdit_agename = QtWidgets.QLineEdit()

        self.label_phone = QtWidgets.QLabel("Телефон:")
        self.label_email = QtWidgets.QLabel("Email:")
        self.label_city = QtWidgets.QLabel("Город:")

        self.label_phone = QtWidgets.QLineEdit()
        self.label_email = QtWidgets.QLineEdit()
        self.label_city = QtWidgets.QLineEdit()

        self.button_phone = QtWidgets.QPushButton("Проверить")
        self.button_email = QtWidgets.QPushButton("Проверить")
        self.button_city = QtWidgets.QPushButton("Проверить")

        self.button_send = QtWidgets.QPushButton("Отправить")
        self.button_clear = QtWidgets.QPushButton("Очистить")
        self.button_cancel = QtWidgets.QPushButton("Отмена")

        main_frame = QtWidgets.QFrame()
        main_frame.setLineWidth(1)
        main_frame.setFrameStyle(QtWidgets.QFrame.Shape.Box)

        main_vertical = QtWidgets.QVBoxLayout(main_frame)
        window.setLayout(main_vertical)

        horiz = QtWidgets.QHBoxLayout(main_frame)
        horiz.addWidget(self.button_send)


























if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
