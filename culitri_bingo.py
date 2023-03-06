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
from functools import partial

from widgets.bingo_balls import BingoBalls
from widgets.control_buttons import ControlButtons
from widgets.latest_bingo_balls import LatestBallsWidget

from bingo.game_logic import GameLogic


class CulitriBingo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Culitri bingo")

        # * Window layout
        central_widget = QWidget()
        window_layout = QGridLayout()

        self.control_buttons = ControlButtons()
        self.latest_balls_widget = LatestBallsWidget()
        self.bingo_balls = BingoBalls()

        self.game_logic = GameLogic(self.bingo_balls)

        window_layout.addWidget(self.control_buttons, 0, 0)
        window_layout.addWidget(self.latest_balls_widget, 0, 1)
        window_layout.addWidget(self.bingo_balls, 1, 0)

        central_widget.setLayout(window_layout)
        self.setCentralWidget(central_widget)

        self.control_buttons.start_button.clicked.connect(self.game_logic.start)
        self.control_buttons.stop_button.clicked.connect(self.game_logic.stop)
        self.control_buttons.reset_button.clicked.connect(self.game_logic.reset)


# def checkable_button_clicked(data):
#     print("Button clicked!", data)


# def normal_button_clicked():
#     print("Button clicked!")


# class CulitriBingo(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Culitri bingo!!")

#         self.checkable_button = QPushButton()
#         self.checkable_button.setText("Click me! (checkeable)")
#         self.checkable_button.setCheckable(True)
#         self.setCentralWidget(self.checkable_button)

#         self.normal_button = QPushButton()
#         self.normal_button.setText("Click me (normal)!")

#         self.setCentralWidget(self.normal_button)


#     def initialize_buttons(self):
#         self.checkable_button.clicked.connect(checkable_button_clicked)
#         self.normal_button.clicked.connect(normal_button_clicked)
