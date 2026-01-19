from PyQt6.QtWidgets import *


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("THIS IS MY WINDOW")
        self.resize(700, 600)
        main_layout = QWidget()
        self.setCentralWidget(main_layout)
        main_widget = QVBoxLayout(main_layout)
        self.stacked = QStackedLayout()
        main_widget.addLayout(self.stacked)
        self.main_list = []

        # stack 1
        stacked1 = QWidget()
        stack1_vertical = QVBoxLayout(stacked1)

        # stacked 1 question 1

        stacked1_group1 = QGroupBox()
        vertical_stacked1_group1 = QHBoxLayout(stacked1_group1)
        stacked1_group1.setTitle("Что говорит Cristiano Ronaldo во время празднования гола?")
        self.stacked1_group1_check1 = QCheckBox("ГОООООЛЛЛ")
        self.stacked1_group1_check2 = QCheckBox("УРАА")
        self.stacked1_group1_check3 = QCheckBox("ДАААА")
        self.stacked1_group1_check4 = QCheckBox("SSSUUUUUUUUII") # +

        stack1_vertical.addWidget(stacked1_group1)
        vertical_stacked1_group1.addWidget(self.stacked1_group1_check1)
        vertical_stacked1_group1.addWidget(self.stacked1_group1_check2)
        vertical_stacked1_group1.addWidget(self.stacked1_group1_check3)
        vertical_stacked1_group1.addWidget(self.stacked1_group1_check4)

        # stacked 1 question 2

        stacked1_group2 = QGroupBox()
        vertical_stacked1_group2 = QHBoxLayout(stacked1_group2)
        stacked1_group2.setTitle("Какие компании принадлежат Илону Маску?")
        self.stacked1_group2_check1 = QCheckBox("SpaceX") # +
        self.stacked1_group2_check2 = QCheckBox("Tesla")  # +
        self.stacked1_group2_check3 = QCheckBox("Neuralink") # +
        self.stacked1_group2_check4 = QCheckBox("X") # +

        stack1_vertical.addWidget(stacked1_group2)

        vertical_stacked1_group2.addWidget(self.stacked1_group2_check1)
        vertical_stacked1_group2.addWidget(self.stacked1_group2_check2)
        vertical_stacked1_group2.addWidget(self.stacked1_group2_check3)
        vertical_stacked1_group2.addWidget(self.stacked1_group2_check4)

        # stacked 1 question 3

        stacked1_group3 = QGroupBox()
        vertical_stacked1_group3 = QVBoxLayout(stacked1_group3)
        stacked1_group3.setTitle("Выберите все строчки MACANа")
        self.stacked1_group3_check1 = QCheckBox("Подо мной M5, Asphalt 8")  # +
        self.stacked1_group3_check2 = QCheckBox("Джеб, ушёл, джеб, ушёл — джет")  # +
        self.stacked1_group3_check3 = QCheckBox("В моём ДНК славяне, в моём паспорте Россия")  # +
        self.stacked1_group3_check4 = QCheckBox("Знакомься, это брат, брат это тоже брат, брат")  # +

        stack1_vertical.addWidget(stacked1_group3)

        vertical_stacked1_group3.addWidget(self.stacked1_group3_check1)
        vertical_stacked1_group3.addWidget(self.stacked1_group3_check2)
        vertical_stacked1_group3.addWidget(self.stacked1_group3_check3)
        vertical_stacked1_group3.addWidget(self.stacked1_group3_check4)

        # stacked 1 question 4

        stacked1_group4 = QGroupBox()
        vertical_stacked1_group4 = QVBoxLayout(stacked1_group4)
        stacked1_group4.setTitle("Кого из представленных президентов похищали?")
        self.stacked1_group4_check1 = QCheckBox("Муамар Кадафи")
        self.stacked1_group4_check2 = QCheckBox("Садам Хусейн")
        self.stacked1_group4_check3 = QCheckBox("Мадуро")  # +
        self.stacked1_group4_check4 = QCheckBox("Мбашар Аль-Асад")

        stack1_vertical.addWidget(stacked1_group4)

        vertical_stacked1_group4.addWidget(self.stacked1_group4_check1)
        vertical_stacked1_group4.addWidget(self.stacked1_group4_check2)
        vertical_stacked1_group4.addWidget(self.stacked1_group4_check3)
        vertical_stacked1_group4.addWidget(self.stacked1_group4_check4)

        # stacked 1 question 5

        stacked1_group5 = QGroupBox()
        vertical_stacked1_group5 = QVBoxLayout(stacked1_group5)
        stacked1_group5.setTitle("Выберите преподователей КМПО РАНХиГС")
        self.stacked1_group5_check1 = QCheckBox("Бабаева Назият Агабеговна") # +
        self.stacked1_group5_check2 = QCheckBox("Васильев Сергей Валентинович") # +
        self.stacked1_group5_check3 = QCheckBox("Калашникова Ольга Алексеевна")  # +
        self.stacked1_group5_check4 = QCheckBox("Юров Иван Сергеевич") # +

        stack1_vertical.addWidget(stacked1_group5)

        vertical_stacked1_group5.addWidget(self.stacked1_group5_check1)
        vertical_stacked1_group5.addWidget(self.stacked1_group5_check2)
        vertical_stacked1_group5.addWidget(self.stacked1_group5_check3)
        vertical_stacked1_group5.addWidget(self.stacked1_group5_check4)

        self.stacked1_button = QPushButton("Далее")
        stack1_vertical.addWidget(self.stacked1_button)
        self.stacked1_button.clicked.connect(self.go_stacked2)

        # stack 2

        stacked2 = QWidget()
        stacked2_vertical = QVBoxLayout(stacked2)
        self.stacked2_button = QPushButton("Далее")




        # stacked 2 question 1

        stacked2_group1 = QGroupBox()
        vertical_stacked2_group1 = QHBoxLayout(stacked2_group1)
        stacked2_group1.setTitle("Расшифруйте аббревиатуру ГЕИ")
        self.stacked2_group1_radio1 = QRadioButton("Государственная единая инспекция")
        self.stacked2_group1_radio2 = QRadioButton("Геодезические Единицы Измерений")

        stacked2_vertical.addWidget(stacked2_group1)
        vertical_stacked2_group1.addWidget(self.stacked2_group1_radio1)
        vertical_stacked2_group1.addWidget(self.stacked2_group1_radio2)


        # stacked 2 question 2

        stacked2_group2 = QGroupBox()
        vertical_stacked2_group2 = QHBoxLayout(stacked2_group2)
        stacked2_group2.setTitle("Что чаще всего теряют люди?")
        self.stacked2_group2_radio1 = QRadioButton("Рассудок")
        self.stacked2_group2_radio2 = QRadioButton("Пульт от телевизора")

        stacked2_vertical.addWidget(stacked2_group2)
        vertical_stacked2_group2.addWidget(self.stacked2_group2_radio1)
        vertical_stacked2_group2.addWidget(self.stacked2_group2_radio2)

        # stacked 2 question 3

        stacked2_group3 = QGroupBox()
        vertical_stacked2_group3 = QHBoxLayout(stacked2_group3)
        stacked2_group3.setTitle("Что делать, если звонит неизвестный номер?")
        self.stacked2_group3_radio1 = QRadioButton("Сделать вид, что вы — автоответчик")
        self.stacked2_group3_radio2 = QRadioButton("Сказать: «Пиццерия „У Антонио“, вы уже заказывали?»")

        stacked2_vertical.addWidget(stacked2_group3)
        vertical_stacked2_group3.addWidget(self.stacked2_group3_radio1)
        vertical_stacked2_group3.addWidget(self.stacked2_group3_radio2)

        # stacked 2 question 4

        stacked2_group4 = QGroupBox()
        vertical_stacked2_group4 = QHBoxLayout(stacked2_group4)
        stacked2_group4.setTitle("Как объяснить коту, что 5 утра — это не время для завтрака?")
        self.stacked2_group4_radio1 = QRadioButton("Надеть ему наручные часы")
        self.stacked2_group4_radio2 = QRadioButton("Самому начать мяукать под дверью в 3 ночи")

        stacked2_vertical.addWidget(stacked2_group4)
        vertical_stacked2_group4.addWidget(self.stacked2_group4_radio1)
        vertical_stacked2_group4.addWidget(self.stacked2_group4_radio2)

        # stacked 2 question 5

        stacked2_group5 = QGroupBox()
        vertical_stacked2_group5 = QHBoxLayout(stacked2_group5)
        stacked2_group5.setTitle("Почему носки всегда теряются?")
        self.stacked2_group5_radio1 = QRadioButton("Они уходят в параллельную вселенную стирки")
        self.stacked2_group5_radio2 = QRadioButton("Это заговор сушилки")

        stacked2_vertical.addWidget(stacked2_group5)
        vertical_stacked2_group5.addWidget(self.stacked2_group5_radio1)
        vertical_stacked2_group5.addWidget(self.stacked2_group5_radio2)

        stacked2_vertical.addWidget(self.stacked2_button)
        self.stacked2_button.clicked.connect(self.go_stacked3)

        # stack 3
        stacked3 = QWidget()
        stacked3_vertical = QVBoxLayout(stacked3)
        self.stacked3_button = QPushButton("Завершить")
        self.stacked3_button.clicked.connect(self.go_stacked2)

        # stacked 3 question 1

        stacked3_group1 = QGroupBox()
        stacked3_group1.setTitle("Решить уравнение")
        vertical_stacked3_group1 = QVBoxLayout(stacked3_group1)
        self.stacked3_group1_label1 = QLabel("(2x²-x+1)²+x²(2x²-x+1)-6x⁴=0")  # 1
        self.stacked3_group1_lineEdit1 = QLineEdit()

        stacked3_vertical.addWidget(stacked3_group1)
        vertical_stacked3_group1.addWidget(self.stacked3_group1_label1)
        vertical_stacked3_group1.addWidget(self.stacked3_group1_lineEdit1)

        # stacked 3 question 2

        stacked3_group2 = QGroupBox()
        stacked3_group2.setTitle("Сколько мне лет")
        vertical_stacked3_group2 = QVBoxLayout(stacked3_group2)
        self.stacked3_group2_lineEdit2 = QLineEdit()  # 19

        stacked3_vertical.addWidget(stacked3_group2)
        vertical_stacked3_group2.addWidget(self.stacked3_group2_lineEdit2)

        # stacked 3 question 3

        stacked3_group3 = QGroupBox()
        stacked3_group3.setTitle("В каких месяцах 28 дней")
        vertical_stacked3_group3 = QVBoxLayout(stacked3_group3)
        self.stacked3_group3_label3 = QLabel("Напишите число")
        self.stacked3_group3_lineEdit3 = QLineEdit()  # 12

        stacked3_vertical.addWidget(stacked3_group3)
        vertical_stacked3_group3.addWidget(self.stacked3_group3_label3)
        vertical_stacked3_group3.addWidget(self.stacked3_group3_lineEdit3)

        # stacked 3 question 4

        stacked3_group4 = QGroupBox()
        stacked3_group4.setTitle("Как меня зовут?")
        vertical_stacked3_group4 = QVBoxLayout(stacked3_group4)
        self.stacked3_group4_lineEdit4 = QLineEdit()  # Виктор

        stacked3_vertical.addWidget(stacked3_group4)
        vertical_stacked3_group4.addWidget(self.stacked3_group4_lineEdit4)

        # stacked 3 question 5

        stacked3_group5 = QGroupBox()
        stacked3_group5.setTitle("Напишите любую цифру")
        vertical_stacked3_group5 = QVBoxLayout(stacked3_group5)
        self.stacked3_group5_lineEdit5 = QLineEdit()  # 2

        stacked3_vertical.addWidget(stacked3_group5)
        vertical_stacked3_group5.addWidget(self.stacked3_group5_lineEdit5)

        stacked3_vertical.addWidget(self.stacked3_button)

        # stack 4
        stacked4 = QWidget()
        stacked4_vertical = QVBoxLayout(stacked4)
        self.stacked4_button = QPushButton("Далее")
        self.stacked4_button.clicked.connect(self.go_stacked2)
        stacked4_vertical.addWidget(QLabel("52"))



        self.stacked.addWidget(stacked1)
        self.stacked.addWidget(stacked2)
        self.stacked.addWidget(stacked3)
        self.stacked.addWidget(stacked4)

    def go_stacked2(self):
        if self.stacked1_group1_check4.isChecked():
            self.main_list.append(1)
        else:
            self.main_list.append(0)

        if self.stacked1_group2_check1.isChecked() and self.stacked1_group2_check2.isChecked() and self.stacked1_group2_check3.isChecked() and self.stacked1_group2_check4.isChecked():
            self.main_list.append(1)
        else:
            self.main_list.append(0)

        if self.stacked1_group3_check1.isChecked() and self.stacked1_group3_check2.isChecked() and self.stacked1_group3_check3.isChecked() and self.stacked1_group3_check4.isChecked():
            self.main_list.append(1)
        else:
            self.main_list.append(0)

        if self.stacked1_group4_check3.isChecked():
            self.main_list.append(1)
        else:
            self.main_list.append(0)

        if self.stacked1_group5_check1.isChecked() and self.stacked1_group5_check2.isChecked() and self.stacked1_group5_check3.isChecked() and self.stacked1_group5_check4.isChecked():
            self.main_list.append(1)
        else:
            self.main_list.append(0)
        self.stacked.setCurrentIndex(self.stacked.currentIndex() + 1)
        print(self.main_list)

    def go_stacked3(self):
        #1
        if self.stacked2_group1_radio1.isChecked():
            self.main_list.append(1)
        else:
            self.main_list.append(0)

        #2
        if self.stacked2_group2_radio1.isChecked():
            self.main_list.append(1)
        else:
            self.main_list.append(0)

        #3
        if self.stacked2_group3_radio1.isChecked():
            self.main_list.append(1)
        else:
            self.main_list.append(0)

        #4
        if self.stacked2_group4_radio1.isChecked():
            self.main_list.append(1)
        else:
            self.main_list.append(0)

        #5
        if self.stacked2_group4_radio1.isChecked():
            self.main_list.append(1)
        else:
            self.main_list.append(0)

        print(self.main_list)
        self.stacked.setCurrentIndex(self.stacked.currentIndex()+1)












if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
