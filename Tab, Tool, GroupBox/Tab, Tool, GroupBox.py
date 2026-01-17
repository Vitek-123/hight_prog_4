import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Управление умным домом")
        self.resize(535, 550)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)

        #manadge_page

        manadge_page = QToolBox()

        tab1 = QWidget()
        climat = QVBoxLayout(tab1)
        climat.addWidget(QLabel("Температура(°С):"))
        climat.addWidget(QSpinBox())
        climat.addWidget(QLabel("Влажность(%):"))
        slider = QSlider(Qt.Orientation.Horizontal)
        climat.addWidget(slider)

        tab2 = QWidget()
        light = QVBoxLayout(tab2)
        button_light_on = QRadioButton("Включить")
        button_light_off = QRadioButton("Выключить")
        light.addWidget(button_light_on)
        light.addWidget(button_light_off)

        tab3 = QWidget()
        safety = QVBoxLayout(tab3)
        check_open = QCheckBox("Открыть дверь")
        check_close= QCheckBox("Закрыть дверь")
        safety.addWidget(check_open)
        safety.addWidget(check_close)

        manadge_page.addItem(tab1, "Климат")
        manadge_page.addItem(tab2, "Освещение")
        manadge_page.addItem(tab3, "Безопасность")

        # mode page

        mode_page = QWidget()
        vertical_mode = QVBoxLayout(mode_page)

        group_box_1 = QGroupBox()
        group_box_1.setTitle("Режим работы системы")
        vertical_box_1 =QVBoxLayout(group_box_1)
        vertical_box_1.addWidget(QRadioButton("Экономный"))
        vertical_box_1.addWidget(QRadioButton("Комфортный"))
        vertical_box_1.addWidget(QRadioButton("Автоматически"))
        vertical_box_1.addWidget(QRadioButton("Ручной"))

        group_box_2 = QGroupBox()
        group_box_2.setTitle("Способ оповещения")
        vertical_box_2 = QVBoxLayout(group_box_2)
        vertical_box_2.addWidget(QRadioButton("Через приложение"))
        vertical_box_2.addWidget(QRadioButton("SMS"))
        vertical_box_2.addWidget(QRadioButton("Звонок"))
        vertical_box_2.addWidget(QRadioButton("Email"))

        vertical_mode.addWidget(group_box_1)
        vertical_mode.addWidget(group_box_2)

        # page device

        device_page = QWidget()

        vertical_device = QVBoxLayout(device_page)

        group_box_device = QGroupBox("Управляемые устройства")
        vertical_device.addWidget(group_box_device)
        vertical_device_1 = QVBoxLayout(group_box_device)
        vertical_device_1.addWidget(QCheckBox("Кондиционер"))
        vertical_device_1.addWidget(QCheckBox("Отопление"))
        vertical_device_1.addWidget(QCheckBox("Освещение"))
        vertical_device_1.addWidget(QCheckBox("Жалюзи/шторы"))
        vertical_device_1.addWidget(QCheckBox("Камеры"))
        vertical_device_1.addWidget(QCheckBox("Сигнализация"))

        group_box_shedule = QGroupBox("Расписание")
        vertical_device.addWidget(group_box_shedule)
        vertical_device_2 = QVBoxLayout(group_box_shedule)
        vertical_device_2.addWidget(QCheckBox("Утренний режим"))
        vertical_device_2.addWidget(QCheckBox("Дневной режим"))
        vertical_device_2.addWidget(QCheckBox("Вечерний режим"))
        vertical_device_2.addWidget(QCheckBox("Ночной режим"))
        vertical_device_2.addWidget(QCheckBox("Режим отпуска"))



        table = QTabWidget()
        table.addTab(manadge_page, "Управление")
        table.addTab(mode_page, "Режимы")
        table.addTab(device_page, "Утсройства")


        main_layout.addWidget(table)






if __name__ == "__main__":
    import sys
    app =QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())