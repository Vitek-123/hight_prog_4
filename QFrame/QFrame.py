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



        # middle left

        frame_middle_left = QtWidgets.QFrame()
        frame_middle_left.setLineWidth(5)
        frame_middle_left.setFrameShape(QtWidgets.QFrame.Shape.Box)

        frame_middle_right = QtWidgets.QFrame()
        frame_middle_right.setLineWidth(1)
        frame_middle_right.setFrameShape(QtWidgets.QFrame.Shape.Box)

        middle_left = QtWidgets.QVBoxLayout(frame_middle)
        middle_left.addWidget(frame_middle_left)

        middle_right = QtWidgets.QVBoxLayout(frame_middle)
        middle_right.addWidget(frame_middle_right)



        #middle right






        #bottom
        main_verticall.addWidget(frame_bottom)









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
