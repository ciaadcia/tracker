from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QProgressBar,QPushButton

from data_manager import add_points


class ResultScreen(QWidget):

    def __init__(self,stack):
        super().__init__()

        self.stack = stack

        layout = QVBoxLayout()

        title = QLabel("RESULT")

        self.progress = QProgressBar()
        self.progress.setMaximum(500)

        self.label = QLabel()

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.back)

        layout.addWidget(title)
        layout.addWidget(self.progress)
        layout.addWidget(self.label)
        layout.addWidget(back_btn)

        self.setLayout(layout)


    def show_result(self,name,points):

        total = add_points(name,points)

        self.progress.setValue(total)

        self.label.setText(f"Total Point: {total}")


    def back(self):

        self.stack.setCurrentWidget(self.stack.login)