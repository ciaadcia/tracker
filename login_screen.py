from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QLineEdit,QPushButton,QComboBox


class LoginScreen(QWidget):

    def __init__(self,stack):
        super().__init__()

        self.stack = stack

        layout = QVBoxLayout()

        title = QLabel("JUDUL PROJECT")

        desc = QLabel("Masukkan nama dan jumlah target")

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nama")

        self.dropdown = QComboBox()
        self.dropdown.addItems(["1","2","3","4","5"])

        start_btn = QPushButton("Start")
        start_btn.clicked.connect(self.start)

        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addWidget(self.name_input)
        layout.addWidget(self.dropdown)
        layout.addWidget(start_btn)

        self.setLayout(layout)


    def start(self):

        name = self.name_input.text()
        level = int(self.dropdown.currentText())

        self.stack.total_inputs = 0

        self.stack.input.setup(name,level,screen=2)

        self.stack.setCurrentWidget(self.stack.input)