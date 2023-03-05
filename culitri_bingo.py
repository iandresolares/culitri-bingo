from PySide6.QtWidgets import QMainWindow, QPushButton


def checkable_button_clicked(data):
    print("Button clicked!", data)


def normal_button_clicked():
    print("Button clicked!")


class CulitriBingo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Culitri bingo!!")

        self.checkable_button = QPushButton()
        self.checkable_button.setText("Click me! (checkeable)")
        self.checkable_button.setCheckable(True)
        self.setCentralWidget(self.checkable_button)

        self.normal_button = QPushButton()
        self.normal_button.setText("Click me (normal)!")

        self.setCentralWidget(self.normal_button)
        # self.show()

    def initialize_buttons(self):
        self.checkable_button.clicked.connect(checkable_button_clicked)
        self.normal_button.clicked.connect(normal_button_clicked)
