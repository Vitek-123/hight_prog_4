from PyQt6 import QtWidgets

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Форма реистрации")
        self.resize(700, 500)



        self.label_new_reg = QtWidgets.QLabel("Регистрация нового пользователя")
        self.label_name = QtWidgets.QLabel("Имя:")
        self.label_surname = QtWidgets.QLabel("Фамилия:")
        self.label_age = QtWidgets.QLabel("Возраст:")

        self.lineEdit_name = QtWidgets.QLineEdit()
        self.lineEdit_surname = QtWidgets.QLineEdit()
        self.lineEdit_age = QtWidgets.QLineEdit()

        self.label_phone = QtWidgets.QLabel("Телефон:")
        self.label_email = QtWidgets.QLabel("Email:")
        self.label_city = QtWidgets.QLabel("Город:")

        self.lineEdit_phone = QtWidgets.QLineEdit()
        self.lineEdit_email = QtWidgets.QLineEdit()
        self.lineEdit_city = QtWidgets.QLineEdit()

        self.button_phone = QtWidgets.QPushButton("Проверить")
        self.button_email = QtWidgets.QPushButton("Проверить")
        self.button_city = QtWidgets.QPushButton("Проверить")

        self.button_send = QtWidgets.QPushButton("Отправить")
        self.button_clear = QtWidgets.QPushButton("Очистить")
        self.button_cancel = QtWidgets.QPushButton("Отмена")

        window = QtWidgets.QWidget()
        self.setCentralWidget(window)


        main_frame = QtWidgets.QFrame()
        main_frame.setLineWidth(1)
        main_frame.setFrameStyle(QtWidgets.QFrame.Shape.Box)

        main_vertical = QtWidgets.QVBoxLayout(window)
        main_vertical.addWidget(main_frame)

        frame_top = QtWidgets.QFrame()
        frame_top.setLineWidth(1)
        frame_top.setFrameStyle(QtWidgets.QFrame.Shape.Box)

        frame_middle = QtWidgets.QFrame()
        frame_middle.setLineWidth(1)
        frame_middle.setFrameStyle(QtWidgets.QFrame.Shape.Box)

        frame_bottom = QtWidgets.QFrame()
        frame_bottom.setLineWidth(1)
        frame_bottom.setFrameStyle(QtWidgets.QFrame.Shape.Box)

        main_verticall = QtWidgets.QVBoxLayout(main_frame)
        main_verticall.addWidget(frame_top)
        lay = QtWidgets.QHBoxLayout(frame_top)
        lay.addWidget(self.label_new_reg)

        #middle

        main_verticall.addWidget(frame_middle)





        frame_middle_left = QtWidgets.QFrame()
        frame_middle_left.setLineWidth(1)
        frame_middle_left.setFrameShape(QtWidgets.QFrame.Shape.Box)

        frame_middle_right = QtWidgets.QFrame()
        frame_middle_right.setLineWidth(1)
        frame_middle_right.setFrameShape(QtWidgets.QFrame.Shape.Box)

        middle_left = QtWidgets.QHBoxLayout(frame_middle)

        # middle left

        middle_left.addWidget(frame_middle_left)

        middle_leftt = QtWidgets.QVBoxLayout(frame_middle_left)

        # middle left 1

        frame_middle_left_1 = QtWidgets.QFrame()
        frame_middle_left_1.setLineWidth(1)
        frame_middle_left_1.setFrameShape(QtWidgets.QFrame.Shape.Box)

        middle_leftt.addWidget(frame_middle_left_1)

        middle_left_1 = QtWidgets.QHBoxLayout(frame_middle_left_1)
        middle_left_1.addWidget(self.label_name)
        middle_left_1.addWidget(self.lineEdit_name)

        # middle left 2

        frame_middle_left_2 = QtWidgets.QFrame()
        frame_middle_left_2.setLineWidth(1)
        frame_middle_left_2.setFrameShape(QtWidgets.QFrame.Shape.Box)

        middle_leftt.addWidget(frame_middle_left_2)

        middle_left_2 = QtWidgets.QHBoxLayout(frame_middle_left_2)
        middle_left_2.addWidget(self.label_surname)
        middle_left_2.addWidget(self.lineEdit_surname)


        # middle left 3

        frame_middle_left_3 = QtWidgets.QFrame()
        frame_middle_left_3.setLineWidth(1)
        frame_middle_left_3.setFrameShape(QtWidgets.QFrame.Shape.Box)

        middle_leftt.addWidget(frame_middle_left_3)

        middle_left_3 = QtWidgets.QHBoxLayout(frame_middle_left_3)
        middle_left_3.addWidget(self.label_age)
        middle_left_3.addWidget(self.lineEdit_age)

        #middle right

        middle_left.addWidget(frame_middle_right)

        middle_rightt = QtWidgets.QVBoxLayout(frame_middle_right)

        # middle right 1

        frame_middle_right_1 = QtWidgets.QFrame()
        frame_middle_right_1.setLineWidth(1)
        frame_middle_right_1.setFrameShape(QtWidgets.QFrame.Shape.Box)

        middle_rightt.addWidget(frame_middle_right_1)

        middle_right_1 = QtWidgets.QHBoxLayout(frame_middle_right_1)
        middle_right_1.addWidget(self.label_phone)
        middle_right_1.addWidget(self.lineEdit_phone)
        middle_right_1.addWidget(self.button_phone)

        # middle right 2

        frame_middle_right_2 = QtWidgets.QFrame()
        frame_middle_right_2.setLineWidth(1)
        frame_middle_right_2.setFrameShape(QtWidgets.QFrame.Shape.Box)

        middle_rightt.addWidget(frame_middle_right_2)

        middle_right_2 = QtWidgets.QHBoxLayout(frame_middle_right_2)
        middle_right_2.addWidget(self.label_email)
        middle_right_2.addWidget(self.lineEdit_email)
        middle_right_2.addWidget(self.button_email)

        # middle right 3

        frame_middle_right_3 = QtWidgets.QFrame()
        frame_middle_right_3.setLineWidth(1)
        frame_middle_right_3.setFrameShape(QtWidgets.QFrame.Shape.Box)

        middle_rightt.addWidget(frame_middle_right_3)

        middle_right_3 = QtWidgets.QHBoxLayout(frame_middle_right_3)
        middle_right_3.addWidget(self.label_city)
        middle_right_3.addWidget(self.lineEdit_city)
        middle_right_3.addWidget(self.button_city)


        #bottom
        main_verticall.addWidget(frame_bottom)

        bottom = QtWidgets.QHBoxLayout(frame_bottom)
        bottom.addWidget(self.button_send)
        bottom.addWidget(self.button_clear)
        bottom.addWidget(self.button_cancel)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())