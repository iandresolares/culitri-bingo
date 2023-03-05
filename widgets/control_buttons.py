from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QPushButton,
    QStatusBar,
    QGridLayout,
    QLayoutItem,
    QLabel,
    QHBoxLayout,
)
from PySide6.QtGui import QPixmap



class ControlButtons(QWidget):
    def __init__(self):
        super().__init__()
        buttons_layout = QHBoxLayout()
        self.start_button = QPushButton("START")
        self.stop_button = QPushButton("STOP")
        self.reset_button = QPushButton("RESET")

        buttons_layout.addWidget(self.start_button)
        buttons_layout.addWidget(self.stop_button)
        buttons_layout.addWidget(self.reset_button)

        self.setLayout(buttons_layout)


