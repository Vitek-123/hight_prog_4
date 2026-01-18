from PyQt6.QtWidgets import *
from PyQt6 import QtCore


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stack = None
        self.setupui()

    def setupui(self):
        self.setWindowTitle("Натсройка игрового режима")
        self.resize(330, 350)

        center = QWidget()
        self.setCentralWidget(center)

        button_forward = QPushButton("Вперед→")
        button_back = QPushButton("←Назад")

        main_vertical = QVBoxLayout(center)

        self.stack = QStackedLayout()

        button_layout = QHBoxLayout()
        button_layout.addWidget(button_back)
        button_layout.addWidget(button_forward)

        main_vertical.addLayout(self.stack)
        main_vertical.addLayout(button_layout)

        # stack 1

        stack_1 = QWidget()

        vertical_stack_1 = QVBoxLayout(stack_1)
        vertical_stack_1.addWidget(QLabel("Шаг 1: Натройки игрового режима"))

        stack_1_groupBox_1 = QGroupBox("Режим игры")
        stack_1_groupBox_1_vertical = QVBoxLayout(stack_1_groupBox_1)
        stack_1_groupBox_1_vertical.addWidget(QRadioButton("Казуальный (для отдыха)"))
        stack_1_groupBox_1_vertical.addWidget(QRadioButton("Соревноватьльный (PvP)"))
        stack_1_groupBox_1_vertical.addWidget(QRadioButton("Хардков (макс. слжность)"))

        vertical_stack_1.addWidget(stack_1_groupBox_1)

        stack_1_groupBox_2 = QGroupBox("Игровые функции")
        stack_1_groupBox_2_vertical = QVBoxLayout(stack_1_groupBox_2)
        stack_1_groupBox_2_vertical.addWidget(QCheckBox("Показать обучение"))
        stack_1_groupBox_2_vertical.addWidget(QCheckBox("Включить подсказки"))
        stack_1_groupBox_2_vertical.addWidget(QCheckBox("Автосохраниение"))
        stack_1_groupBox_2_vertical.addWidget(QCheckBox("Мкльтиплеер"))

        vertical_stack_1.addWidget(stack_1_groupBox_2)

        # stack 2

        stack_2 = QWidget()
        vertical_stack_2 = QVBoxLayout(stack_2)
        vertical_stack_2.addWidget(QLabel("Шаг 2: Описание игрового режима"))
        vertical_stack_2.addWidget(QTextEdit("Выбран казуальный режим игрыю.\n Включены подсказки и автосохранение.\n "
                                             "Доступен мультиплеер."))

        # stack 3

        stack_3 = QWidget()
        main_vertical_stack_3 = QVBoxLayout(stack_3)
        table = QTabWidget()
        main_vertical_stack_3.addWidget(table)

        # tab 1

        tab1 = QWidget()

        vertical_tab_1 = QVBoxLayout(tab1)

        # splitter 1

        splitter_tab_1 = QSplitter(QtCore.Qt.Orientation.Horizontal)

        # splitter 1 left

        frame_hight_left_tab_1 = QFrame()
        frame_hight_left_tab_1.setLineWidth(1)
        frame_hight_left_tab_1.setFrameShape(QFrame.Shape.Box)

        vertical_hight_left_tab_1 = QVBoxLayout(frame_hight_left_tab_1)

        vertical_2_hight_left_tab_1 = QVBoxLayout()
        vertical_1_hight_left_tab_1 = QVBoxLayout()

        vertical_2_hight_left_tab_1.addWidget(QLabel("Время игры: 45"))
        vertical_2_hight_left_tab_1.addWidget(QLabel("Уровень: 25"))
        vertical_2_hight_left_tab_1.addWidget(QLabel("Достижения 12/50"))

        vertical_1_hight_left_tab_1.addWidget(QLabel("Статистика:"))

        vertical_hight_left_tab_1.addLayout(vertical_1_hight_left_tab_1)
        vertical_hight_left_tab_1.addLayout(vertical_2_hight_left_tab_1)

        # splitter 1 right

        frame_hight_right_tab_1 = QFrame()
        frame_hight_right_tab_1.setLineWidth(1)
        frame_hight_right_tab_1.setFrameShape(QFrame.Shape.Box)

        splitter_tab_1.addWidget(frame_hight_left_tab_1)
        splitter_tab_1.addWidget(frame_hight_right_tab_1)

        vertical_tab_1.addWidget(splitter_tab_1)

        # splitter 2

        splitter_tab_2 = QSplitter(QtCore.Qt.Orientation.Horizontal)

        frame_bottom_left_tab_1 = QFrame()
        frame_bottom_left_tab_1.setFrameShape(QFrame.Shape.Box)
        frame_bottom_left_tab_1.setLineWidth(1)

        frame_bottom_right_tab_1 = QFrame()
        frame_bottom_right_tab_1.setFrameShape(QFrame.Shape.Box)
        frame_bottom_right_tab_1.setLineWidth(1)

        splitter_tab_2.addWidget(frame_bottom_left_tab_1)
        splitter_tab_2.addWidget(frame_bottom_right_tab_1)

        vertical_tab_1.addWidget(splitter_tab_2)

        # tab 2

        tab2 = QWidget()

        table.addTab(tab1, "Характеристики")
        table.addTab(tab2, "Прогресс")

        self.stack.addWidget(stack_1)
        self.stack.addWidget(stack_2)
        self.stack.addWidget(stack_3)

        button_forward.clicked.connect(self.go_forward)
        button_back.clicked.connect(self.go_back)

    def go_forward(self):
        self.stack.setCurrentIndex(self.stack.currentIndex() + 1)

    def go_back(self):
        self.stack.setCurrentIndex(self.stack.currentIndex()-1)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
