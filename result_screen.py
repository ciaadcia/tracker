from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QProgressBar, QPushButton, QHBoxLayout)
from PyQt5.QtCore import Qt
from data_manager import add_points

class ResultScreen(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout()

        title = QLabel("RESULT")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 36px; font-weight: bold; color: #2c3e50;")

        self.progress = QProgressBar()
        self.progress.setMaximum(500)
        self.progress.setStyleSheet("""
            QProgressBar {
                border: 2px solid #bdc3c7;
                border-radius: 10px;
                text-align: center;
                background-color: #ecf0f1;
                height: 25px;
                font-weight: bold;
                color: #2c3e50;
            }
            QProgressBar::chunk {
                background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                                  stop: 0 #27ae60, stop: 1 #2ecc71);
                border-radius: 8px;
            }
        """)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            font-size: 20px; 
            font-weight: bold; 
            color: #27ae60;
            padding: 20px;
            background-color: #ecf0f1;
            border-radius: 15px;
            border: 2px solid #d5dbdb;
        """)

        back_layout = QHBoxLayout()
        back_layout.addStretch(1)
        back_btn = QPushButton("BACK")
        back_btn.clicked.connect(self.back)
        back_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 999px;
                min-height: 50px;
                min-width: 130px;
            }
            QPushButton:hover {
                background-color: #c0392b;
                box-shadow: 0 4px 15px rgba(231, 76, 60, 0.4);
            }
            QPushButton:pressed {
                background-color: #a93226;
            }
        """)
        back_layout.addWidget(back_btn)

        layout.addStretch(1)
        layout.addWidget(title)
        layout.addSpacing(30)
        layout.addWidget(self.progress)
        layout.addSpacing(20)
        layout.addWidget(self.label)
        layout.addSpacing(40)
        layout.addLayout(back_layout)
        layout.addStretch(1)

        self.setLayout(layout)

    def show_result(self, name, points):
        total = add_points(name, points)
        self.progress.setValue(total)

        if total >= 200:
            self.label.setText(f"Total Point: {total}\n🎉 Great job! You're getting close to the maximum points!")
            self.label.setStyleSheet("""
                font-size: 22px; 
                font-weight: bold; 
                color: #27ae60;
                padding: 25px;
            """)
        elif total >= 100:
            self.label.setText(f"Total Point: {total}\n🏆 Congratulations! You have reached the maximum points!")
            self.label.setStyleSheet("""
                font-size: 22px; 
                font-weight: bold; 
                color: #f39c12;
                padding: 25px;
            """)
        else:
            self.label.setText(f"Total Point: {total}\nKeep going! 💪")
            self.label.setStyleSheet("""
                font-size: 20px; 
                font-weight: bold; 
                color: #3498db;
                padding: 20px;
            """)

    def back(self):
        self.stack.setCurrentWidget(self.stack.login)
