from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
import pymysql


class Base():
    def __init__(self):
        self.son = pymysql.connect(host="localhost", user="root", password="", db="test", autocommit=True)
        self.cur = self.son.cursor()

    def all_quest(self):
        self.cur.execute("select * from quest")
        self.data = self.cur.fetchall()
        return self.data

    def all_ques(self, id):
        self.cur.execute("select * from answer_options where id_quest = %s", (id,))
        self.data = self.cur.fetchall()
        return self.data

    def add_anketa(self, surname, name, triname, phone, birthday):
        self.cur.execute("insert into anketa (surname, name, triname, phone, birthday) VALUES (%s, %s, %s, %s, %s);",
                         (surname, name, triname, phone, birthday))
        self.cur.execute("SELECT LAST_INSERT_ID()")
        return self.cur.fetchone()[0]

    def add_response(self, id_answerOptions, id_anketa):
        self.cur.execute("insert into questionnaire_responses (id_answerOptions, id_anketa) VALUES (%s, %s);",
                         (id_answerOptions, id_anketa))
        return


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 600)

        main_layout = QVBoxLayout(self)

        self.widget_titl = []

        self.main_label = QLabel("АНКЕТА ПУТЕШЕСТВЕННИКА")
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.info_user = QLabel("Личные данные")

        self.surname_label = QLabel("Фамилия")
        self.surname_lineEdit = QLineEdit()
        self.surname_lineEdit.setPlaceholderText("Иванов")

        self.name_label = QLabel("Имя")
        self.name_lineEdit = QLineEdit()
        self.name_lineEdit.setPlaceholderText("Иван")

        self.triname_label = QLabel("Отчество")
        self.triname_lineEdit = QLineEdit()
        self.triname_lineEdit.setPlaceholderText("Иванов")

        self.phone_label = QLabel("Телефон")
        self.phone_lineEdit = QLineEdit()
        self.phone_lineEdit.setPlaceholderText("")
        self.phone_lineEdit.setInputMask("+7 (000) 000-00-00")

        self.birthday_label = QLabel("Дата рождения")
        self.birthday_dataEdit = QDateEdit()
        self.birthday_dataEdit.setCalendarPopup(True)

        self.push_anketa_button = QPushButton("Отправить анкету")
        self.push_anketa_button.clicked.connect(self.send_anketa)

        self.clear_button = QPushButton("Очистить")
        self.clear_button.clicked.connect(self.clear_form)

        self.widget_for_scroll = QWidget()
        self.vertical_for_scroll = QVBoxLayout(self.widget_for_scroll)

        self.first_frame = QFrame()
        self.first_frame.setLineWidth(1)
        self.first_frame.setFrameShape(QFrame.Shape.Box)

        self.first_grid = QGridLayout(self.first_frame)
        self.first_grid.addWidget(self.info_user, 0, 0)
        self.first_grid.addWidget(self.surname_label, 1, 0)
        self.first_grid.addWidget(self.surname_lineEdit, 1, 1)
        self.first_grid.addWidget(self.name_label, 2, 0)
        self.first_grid.addWidget(self.name_lineEdit, 2, 1)
        self.first_grid.addWidget(self.triname_label, 3, 0)
        self.first_grid.addWidget(self.triname_lineEdit, 3, 1)
        self.first_grid.addWidget(self.phone_label, 4, 0)
        self.first_grid.addWidget(self.phone_lineEdit, 4, 1)
        self.first_grid.addWidget(self.birthday_label, 5, 0)
        self.first_grid.addWidget(self.birthday_dataEdit, 5, 1)

        self.main_scroll = QScrollArea()
        self.main_scroll.setWidgetResizable(True)
        self.main_scroll.setWidget(self.widget_for_scroll)
        self.vertical_for_scroll.addWidget(self.main_label)
        self.vertical_for_scroll.addWidget(self.first_frame)

        main_layout.addWidget(self.main_scroll)

        self.db = Base()
        self.all_quest = self.db.all_quest()
        self.len_quest = len(self.all_quest)

        for i in self.all_quest:
            type_quest = i[2]
            self.someone_frame = QFrame()
            self.someone_frame.setLineWidth(1)
            self.someone_frame.setFrameShape(QFrame.Shape.Box)

            vertical_for_quest = QVBoxLayout(self.someone_frame)

            quest_label = QLabel(f"{i[0]}. {i[1]}")
            vertical_for_quest.addWidget(quest_label)

            answers = self.db.all_ques(i[0])

            widget_answer = {
                "id": i[0],
                "text": i[1],
                "type": i[2],
                "widget": [],
                "answer_ids": []
            }

            if type_quest == 1:
                for answer in answers:
                    answer_text = answer[2]
                    answer_id = answer[0]
                    check_box = QCheckBox(answer_text)
                    vertical_for_quest.addWidget(check_box)
                    widget_answer["widget"].append(check_box)
                    widget_answer["answer_ids"].append(answer_id)

            elif type_quest == 2:
                group_button = QButtonGroup(self)
                group_button.setExclusive(True)
                for answer in answers:
                    answer_text = answer[2]
                    answer_id = answer[0]
                    radio_button = QRadioButton(answer_text)
                    group_button.addButton(radio_button, answer_id)
                    vertical_for_quest.addWidget(radio_button)
                    widget_answer["widget"].append(radio_button)
                    widget_answer["answer_ids"].append(answer_id)
                widget_answer["group"] = group_button

            else:
                combobox = QComboBox()
                for answer in answers:
                    answer_text = answer[2]
                    answer_id = answer[0]
                    combobox.addItem(answer_text, answer_id)
                vertical_for_quest.addWidget(combobox)
                widget_answer["widget"].append(combobox)

            self.widget_titl.append(widget_answer)

            self.vertical_for_scroll.addWidget(self.someone_frame)


        self.vertical_for_scroll.addWidget(self.push_anketa_button)
        self.vertical_for_scroll.addWidget(self.clear_button)

    def send_anketa(self):
        surname = self.surname_lineEdit.text()
        name = self.name_lineEdit.text()
        triname = self.triname_lineEdit.text()
        phone = self.phone_lineEdit.text()
        data = self.birthday_dataEdit.date().toString('yyyy-MM-dd')

        if surname and name and triname and phone and data:
            Base().add_anketa(surname, name, triname, phone, data)
        else:
            QMessageBox.warning(self, "Eror", "Заплните контактную информацию")

        anketa_id = self.db.add_anketa(surname, name, triname, phone, data)

        responses_saved = False
        all_questions_answered = True

        for question in self.widget_titl:
            question_id = question["id"]
            question_type = question["type"]

            if question_type == 1:
                selected_answers = []
                for i, check_box in enumerate(question["widget"]):
                    if check_box.isChecked():
                        answer_id = question["answer_ids"][i]
                        selected_answers.append(answer_id)
                        self.db.add_response(answer_id, anketa_id)
                        responses_saved = True

                if not selected_answers:
                    all_questions_answered = False
                    QMessageBox.warning(self, "Ошибка", f"Ответьте на вопрос {question_id}")
                    break

            elif question_type == 2:
                selected_answer = None
                group = question.get("group")
                if group:
                    selected_id = group.checkedId()
                    if selected_id != -1:
                        selected_answer = selected_id
                        self.db.add_response(selected_answer, anketa_id)
                        responses_saved = True

                if not selected_answer:
                    all_questions_answered = False
                    QMessageBox.warning(self, "Ошибка", f"Ответьте на вопрос {question_id}")
                    break

            else:
                combobox = question["widget"][0]
                if combobox.currentIndex() >= 0:
                    answer_id = combobox.currentData()
                    self.db.add_response(answer_id, anketa_id)
                    responses_saved = True
                else:
                    all_questions_answered = False
                    QMessageBox.warning(self, "Ошибка", f"Ответьте на вопрос {question_id}")
                    break

        if all_questions_answered and responses_saved:
            QMessageBox.information(self, "Успех", "Анкета успешно сохранена!")
            self.clear_form()

    def clear_form(self):
        self.surname_lineEdit.clear()
        self.name_lineEdit.clear()
        self.triname_lineEdit.clear()
        self.phone_lineEdit.clear()
        self.birthday_dataEdit.setDate(self.birthday_dataEdit.date())

        for question in self.widget_titl:
            question_type = question["type"]

            if question_type == 1:
                for widget in question["widget"]:
                    if isinstance(widget, QCheckBox):
                        widget.setChecked(False)

            elif question_type == 2:
                group = question.get("group")
                if group:
                    group.setExclusive(False)
                    for widget in question["widget"]:
                        if isinstance(widget, QRadioButton):
                            widget.setChecked(False)
                    group.setExclusive(True)

            else:
                combobox = question["widget"][0]
                if isinstance(combobox, QComboBox):
                    combobox.setCurrentIndex(-1)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())