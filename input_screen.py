from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class InputScreen(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(30,10,30,10)
        self.layout.setSpacing(0)

        label_layout = QVBoxLayout()

        self.title = QLabel()
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFixedHeight(40)
        self.title.setStyleSheet("font-size:36px; font-weight:bold; color:#2c3e50; padding:0; margin:0;")

        self.subtitle1 = QLabel()
        self.subtitle1.setAlignment(Qt.AlignCenter)
        self.subtitle1.setFixedHeight(20)
        self.subtitle1.setStyleSheet("font-size:16px; color:#34495e; padding:0; margin:0;")

        self.subtitle2 = QLabel()
        self.subtitle2.setAlignment(Qt.AlignCenter)
        self.subtitle2.setFixedHeight(20)
        self.subtitle2.setStyleSheet("font-size:16px; color:#34495e; padding:0; margin:0;")

        label_layout.addWidget(self.title)
        label_layout.addWidget(self.subtitle1)
        label_layout.addWidget(self.subtitle2)

        self.layout.addLayout(label_layout)

        self.inputs = []

        next_layout = QHBoxLayout()
        next_layout.addStretch()

        self.next = QPushButton("NEXT")
        self.next.clicked.connect(self.next_screen)
        self.next.setStyleSheet("""
            QPushButton{
                background:#3498db;
                color:white;
                border:none;
                padding:15px 30px;
                font-size:18px;
                font-weight:bold;
                border-radius:25px;
            }
            QPushButton:hover{
                background:#2980b9;
            }
            QPushButton:pressed{
                background:#1f618d;
            }
        """)

        next_layout.addWidget(self.next)

        self.layout.addLayout(next_layout)
        self.setLayout(self.layout)

    def setup(self, name, level, screen):
        self.name = name
        self.level = level
        self.screen = screen

        self.title.setText(f"SCREEN {screen}")
        self.subtitle1.setText(f"Halo {name}!")
        self.subtitle2.setText(f"Isi {level} input untuk screen ini")

        for i in self.inputs:
            self.layout.removeWidget(i)
            i.deleteLater()

        self.inputs = []

        for i in range(level):
            inp = QLineEdit()
            inp.setPlaceholderText(f"Input {i+1}")
            inp.setStyleSheet("""
                QLineEdit{
                    padding:12px;
                    font-size:14px;
                    border:2px solid #bdc3c7;
                    border-radius:10px;
                    background:#ecf0f1;
                    margin:2px 0;
                }
                QLineEdit:focus{
                    border-color:#3498db;
                    background:white;
                }
            """)

            self.layout.insertWidget(self.layout.count()-1, inp)
            self.inputs.append(inp)

    def next_screen(self):
        filled = 0
        for i in self.inputs:
            if i.text() != "":
                filled += 1

        self.stack.total_inputs += filled

        if self.screen < 5:
            self.setup(self.name, self.level, self.screen + 1)
        else:
            points = self.stack.total_inputs * 10
            self.stack.result.show_result(self.name, points)
            self.stack.setCurrentWidget(self.stack.result)