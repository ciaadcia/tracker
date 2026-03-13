import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

from login_screen import LoginScreen
from input_screen import InputScreen
from result_screen import ResultScreen

class MainMenu(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout()

        title = QLabel("JUDUL TRACKER")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 36px; font-weight: bold; color: #2c3e50;")

        subtitle1 = QLabel("TEXT TEXT")
        subtitle1.setAlignment(Qt.AlignCenter)
        subtitle1.setStyleSheet("font-size: 18px; color: #34495e;")

        subtitle2 = QLabel("TEXT TEXT")
        subtitle2.setAlignment(Qt.AlignCenter)
        subtitle2.setStyleSheet("font-size: 18px; color: #34495e;")
        
        start_btn = QPushButton("START")
        start_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 18px;
                font-weight: bold;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1f618d;
            }
        """)
        start_btn.clicked.connect(self.start)
        layout.addStretch(1)
        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(subtitle1)
        layout.addSpacing(10)
        layout.addWidget(subtitle2)
        layout.addSpacing(40)
        layout.addWidget(start_btn, alignment=Qt.AlignCenter)
        layout.addStretch(1)
        self.setLayout(layout)
    def start(self):
        self.stack.setCurrentWidget(self.stack.login)

class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.total_inputs = 0
        self.menu = MainMenu(self)
        self.login = LoginScreen(self)
        self.input = InputScreen(self)
        self.result = ResultScreen(self)
        self.addWidget(self.menu)
        self.addWidget(self.login)
        self.addWidget(self.input)
        self.addWidget(self.result)
        self.setFixedSize(900, 600)
        self.setWindowTitle("Good Deeds Tracker")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
