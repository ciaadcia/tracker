from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QLineEdit,QPushButton


class InputScreen(QWidget):

    def __init__(self,stack):
        super().__init__()

        self.stack = stack

        self.layout = QVBoxLayout()

        self.title = QLabel()

        self.layout.addWidget(self.title)

        self.inputs = []

        self.next_btn = QPushButton("Next")
        self.next_btn.clicked.connect(self.next_screen)

        self.setLayout(self.layout)


    def setup(self,name,level,screen):

        self.name = name
        self.level = level
        self.screen = screen

        self.title.setText(f"Screen {screen}")

        for widget in self.inputs:
            widget.deleteLater()

        self.inputs = []

        for i in range(level):

            inp = QLineEdit()
            inp.setPlaceholderText(f"Input {i+1}")

            self.layout.addWidget(inp)

            self.inputs.append(inp)

        self.layout.addWidget(self.next_btn)


    def next_screen(self):

        filled = 0

        for i in self.inputs:
            if i.text():
                filled += 1

        self.stack.total_inputs += filled

        if self.screen < 4:

            self.setup(
                self.name,
                self.level,
                self.screen + 1
            )

        else:

            points = self.stack.total_inputs * 10

            self.stack.result.show_result(
                self.name,
                points
            )

            self.stack.setCurrentWidget(
                self.stack.result
            )