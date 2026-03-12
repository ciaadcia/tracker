import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget

from login_screen import LoginScreen
from input_screen import InputScreen
from result_screen import ResultScreen


class MainWindow(QStackedWidget):

    def __init__(self):
        super().__init__()

        self.total_inputs = 0

        self.login = LoginScreen(self)
        self.input = InputScreen(self)
        self.result = ResultScreen(self)

        self.addWidget(self.login)
        self.addWidget(self.input)
        self.addWidget(self.result)

        self.setFixedSize(900,600)
        self.setWindowTitle("Good Deeds Tracker")


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())