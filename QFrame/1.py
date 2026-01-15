from PyQt6 import QtWidgets


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Форма регистрации")
        self.resize(700, 500)

        # Создаем виджеты (исправлены имена переменных)
        self.label_new_reg = QtWidgets.QLabel("Регистрация нового пользователя")
        self.label_name = QtWidgets.QLabel("Имя:")
        self.label_surname = QtWidgets.QLabel("Фамилия:")
        self.label_age = QtWidgets.QLabel("Возраст:")

        self.lineEdit_name = QtWidgets.QLineEdit()
        self.lineEdit_surname = QtWidgets.QLineEdit()
        self.lineEdit_age = QtWidgets.QLineEdit()

        # НЕ переопределяем label как QLineEdit!
        self.label_phone_text = QtWidgets.QLabel("Телефон:")
        self.label_email_text = QtWidgets.QLabel("Email:")
        self.label_city_text = QtWidgets.QLabel("Город:")

        self.lineEdit_phone = QtWidgets.QLineEdit()
        self.lineEdit_email = QtWidgets.QLineEdit()
        self.lineEdit_city = QtWidgets.QLineEdit()

        self.button_phone = QtWidgets.QPushButton("Проверить")
        self.button_email = QtWidgets.QPushButton("Проверить")
        self.button_city = QtWidgets.QPushButton("Проверить")

        self.button_send = QtWidgets.QPushButton("Отправить")
        self.button_clear = QtWidgets.QPushButton("Очистить")
        self.button_cancel = QtWidgets.QPushButton("Отмена")

        # Центральный виджет
        window = QtWidgets.QWidget()
        self.setCentralWidget(window)

        # Главный фрейм
        main_frame = QtWidgets.QFrame()
        main_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        main_frame.setLineWidth(2)

        # Главный layout окна
        main_vertical = QtWidgets.QVBoxLayout(window)
        main_vertical.addWidget(main_frame)

        # Layout для главного фрейма
        main_frame_layout = QtWidgets.QVBoxLayout(main_frame)
        main_frame_layout.setSpacing(10)

        # === ВЕРХНИЙ ФРЕЙМ ===
        frame_top = QtWidgets.QFrame()
        frame_top.setFrameShape(QtWidgets.QFrame.Shape.Box)
        frame_top.setLineWidth(1)

        top_layout = QtWidgets.QHBoxLayout(frame_top)
        top_layout.addWidget(self.label_new_reg)

        main_frame_layout.addWidget(frame_top)

        # === СРЕДНИЙ ФРЕЙМ ===
        frame_middle = QtWidgets.QFrame()
        frame_middle.setFrameShape(QtWidgets.QFrame.Shape.Box)
        frame_middle.setLineWidth(1)

        # ОДИН layout для среднего фрейма - горизонтальный
        middle_layout = QtWidgets.QHBoxLayout(frame_middle)
        middle_layout.setSpacing(20)  # Отступ между левой и правой частью

        # ЛЕВАЯ часть среднего фрейма
        frame_middle_left = QtWidgets.QFrame()
        frame_middle_left.setFrameShape(QtWidgets.QFrame.Shape.Box)
        frame_middle_left.setLineWidth(2)


        left_layout = QtWidgets.QHBoxLayout(frame_middle_left)
        left_layout.addWidget(self.label_name)
        left_layout.addWidget(self.label_surname)
        left_layout.addWidget(self.label_age)

        # ПРАВАЯ часть среднего фрейма
        frame_middle_right = QtWidgets.QFrame()
        frame_middle_right.setFrameShape(QtWidgets.QFrame.Shape.Box)
        frame_middle_right.setLineWidth(2)


        right_layout = QtWidgets.QHBoxLayout(frame_middle_right)
        right_layout.addWidget(self.label_name)
        right_layout.addWidget(self.label_name)
        right_layout.addWidget(self.label_name)

        # Добавляем обе части в средний фрейм
        middle_layout.addWidget(frame_middle_left)
        middle_layout.addWidget(frame_middle_right)

        main_frame_layout.addWidget(frame_middle)

        # === НИЖНИЙ ФРЕЙМ ===
        frame_bottom = QtWidgets.QFrame()
        frame_bottom.setFrameShape(QtWidgets.QFrame.Shape.Box)
        frame_bottom.setLineWidth(1)

        bottom_layout = QtWidgets.QHBoxLayout(frame_bottom)
        bottom_layout.addStretch()  # Растяжка слева
        bottom_layout.addWidget(self.button_send)
        bottom_layout.addWidget(self.button_clear)
        bottom_layout.addWidget(self.button_cancel)
        bottom_layout.addStretch()  # Растяжка справа

        main_frame_layout.addWidget(frame_bottom)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())