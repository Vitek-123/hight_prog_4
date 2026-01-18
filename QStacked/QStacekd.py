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

        vertical_hight_right_tab_1 = QVBoxLayout(frame_hight_right_tab_1)
        vertical_2_hight_right_tab_1 = QVBoxLayout()

        vertical_hight_right_tab_1.addWidget(QLabel("Ресурсы"))
        vertical_2_hight_right_tab_1.addWidget(QLabel("Золото: 12500"))
        vertical_2_hight_right_tab_1.addWidget(QLabel("Кристалы: 450"))
        vertical_2_hight_right_tab_1.addWidget(QLabel("Энергия 85/100"))

        vertical_hight_right_tab_1.addLayout(vertical_2_hight_right_tab_1)

        splitter_tab_1.addWidget(frame_hight_left_tab_1)
        splitter_tab_1.addWidget(frame_hight_right_tab_1)

        vertical_tab_1.addWidget(splitter_tab_1)

        # splitter 2

        splitter_tab_2 = QSplitter(QtCore.Qt.Orientation.Horizontal)

        # splitter 2 left

        frame_bottom_left_tab_1 = QFrame()
        frame_bottom_left_tab_1.setFrameShape(QFrame.Shape.Box)
        frame_bottom_left_tab_1.setLineWidth(1)

        vertical_bottom_left_tab_1 = QVBoxLayout(frame_bottom_left_tab_1)
        vertical_2_bottom_left_tab_1 = QVBoxLayout()
        vertical_bottom_left_tab_1.addWidget(QLabel("Инвентарь"))
        vertical_bottom_left_tab_1.addLayout(vertical_2_bottom_left_tab_1)
        vertical_2_bottom_left_tab_1.addWidget(QLabel("Оружие: 8"))
        vertical_2_bottom_left_tab_1.addWidget(QLabel("Броня: 5"))
        vertical_2_bottom_left_tab_1.addWidget(QLabel("Зелья: 12"))

        # splitter 2 right

        frame_bottom_right_tab_1 = QFrame()
        frame_bottom_right_tab_1.setFrameShape(QFrame.Shape.Box)
        frame_bottom_right_tab_1.setLineWidth(1)

        vertical_bottom_right_tab_1 = QVBoxLayout(frame_bottom_right_tab_1)
        vertical_2_bottom_right_tab_1 = QVBoxLayout()
        vertical_bottom_right_tab_1.addWidget(QLabel("Навыки"))
        vertical_bottom_right_tab_1.addLayout(vertical_2_bottom_right_tab_1)
        vertical_2_bottom_right_tab_1.addWidget(QLabel("Атака: 75"))
        vertical_2_bottom_right_tab_1.addWidget(QLabel("Защита: 60"))
        vertical_2_bottom_right_tab_1.addWidget(QLabel("Магия: 45"))

        splitter_tab_2.addWidget(frame_bottom_left_tab_1)
        splitter_tab_2.addWidget(frame_bottom_right_tab_1)

        vertical_tab_1.addWidget(splitter_tab_2)

        # tab 2

        tab2 = QWidget()

        vertical_tab_2 = QVBoxLayout(tab2)

        # tab 2 hight

        frame_hight_tab_2 = QFrame()
        frame_hight_tab_2.setFrameShape(QFrame.Shape.Box)
        frame_hight_tab_2.setLineWidth(1)

        vertical_tab_2_hight = QVBoxLayout(frame_hight_tab_2)

        vertical_tab_2_hight.addWidget(QLabel("Квесты"))

        vertical_tab_2_hight_2 = QVBoxLayout()
        vertical_tab_2_hight_2.addWidget(QLabel("Активныйе: 3"))
        vertical_tab_2_hight_2.addWidget(QLabel("Выполненые: 15"))
        vertical_tab_2_hight_2.addWidget(QLabel("Доступные: 5"))

        vertical_tab_2_hight.addLayout(vertical_tab_2_hight_2)

        # tab 2 middle

        frame_middle_tab_2 = QFrame()
        frame_middle_tab_2.setFrameShape(QFrame.Shape.Box)
        frame_middle_tab_2.setLineWidth(1)

        vertical_tab_2_middle = QVBoxLayout(frame_middle_tab_2)
        vertical_tab_2_middle.addWidget(QLabel("Локации"))

        vertical_tab_2_middle_2 = QVBoxLayout()
        vertical_tab_2_middle.addLayout(vertical_tab_2_middle_2)
        vertical_tab_2_middle_2.addWidget(QLabel("Открыто 8/12"))
        vertical_tab_2_middle_2.addWidget(QLabel("Исследовано: 65%"))

        # tab 2 bottom

        frame_bottom_tab_2 = QFrame()
        frame_bottom_tab_2.setFrameShape(QFrame.Shape.Box)
        frame_bottom_tab_2.setLineWidth(1)

        vertical_tab_2_bottom = QVBoxLayout(frame_bottom_tab_2)
        vertical_tab_2_bottom.addWidget(QLabel("Прогресс навыков"))
        vertical_tab_2_bottom_2 = QVBoxLayout()
        vertical_tab_2_bottom.addLayout(vertical_tab_2_bottom_2)
        vertical_tab_2_bottom_2.addWidget(QLabel("Боевые: 75%"))
        vertical_tab_2_bottom_2.addWidget(QLabel("Магические: 40%"))
        vertical_tab_2_bottom_2.addWidget(QLabel("Ремесло: 55%"))

        vertical_tab_2.addWidget(frame_hight_tab_2)
        vertical_tab_2.addWidget(frame_middle_tab_2)
        vertical_tab_2.addWidget(frame_bottom_tab_2)

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
