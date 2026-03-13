from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class LoginScreen(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout()

        title = QLabel("JUDUL")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")

        subtitle = QLabel("TEXT TEXT TEXT")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("font-size: 12px; color: #34495e;")

        input_layout = QHBoxLayout()
        username_label = QLabel("Name:")
        username_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #2c3e50; padding: 10px;")
        
        self.name = QLineEdit()
        self.name.setPlaceholderText("Masukkan username...")
        self.name.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                font-size: 14px;
                border: 2px solid #bdc3c7;
                border-radius: 10px;
                background-color: #ecf0f1;
            }
            QLineEdit:focus {
                border-color: #3498db;
                background-color: white;
            }
        """)
        
        input_layout.addWidget(username_label)
        input_layout.addWidget(self.name)

        button_layout = QHBoxLayout()
        btn1 = QPushButton("1")
        btn3 = QPushButton("3")
        btn5 = QPushButton("5")

        btn_style = """
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 12px 24px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 20px;
                margin: 20 20px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1f618d;
            }
        """
        btn1.setStyleSheet(btn_style)
        btn3.setStyleSheet(btn_style)
        btn5.setStyleSheet(btn_style)

        btn1.clicked.connect(lambda: self.start_input(1))
        btn3.clicked.connect(lambda: self.start_input(3))
        btn5.clicked.connect(lambda: self.start_input(5))

        button_layout.addWidget(btn1)
        button_layout.addWidget(btn3)
        button_layout.addWidget(btn5)


        layout.addStretch(1)
        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(subtitle)
        layout.addSpacing(40)
        layout.addLayout(input_layout)
        layout.setAlignment(input_layout, Qt.AlignCenter)
        layout.addSpacing(30)
        layout.addLayout(button_layout)
        layout.setAlignment(button_layout, Qt.AlignCenter)  
        layout.addSpacing(40)
        layout.addStretch(1)

        self.setLayout(layout)

    def start_input(self, level):
        name = self.name.text()
        if name == "":
            return
        self.stack.total_inputs = 0
        self.stack.input.setup(name, level, 3)
        self.stack.setCurrentWidget(self.stack.input)

    def go_next(self):
        self.start_input(3)
