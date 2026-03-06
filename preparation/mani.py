from PyQt6.QtWidgets import *
from untitled1 import *

class Auth(QWidget, Auth):
    def __init__(self):
        super().__init__()
        self.auth(self)
        self.pushButton.clicked.connect(self.open_file)
    def open_file(self):
        filecmp = QFileDialog.getOpenFileName(self, "Выбери фото")

        if filecmp:
            pass
        else:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = Auth()
    win.show()
    sys.exit(app.exec())