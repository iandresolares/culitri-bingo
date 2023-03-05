from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
    QLabel,
)
from PySide6.QtGui import QPixmap


class BingoBalls(QWidget):
    def __init__(self):
        super().__init__()
        self.balls = []
        balls_layout = QGridLayout()
        number = 1
        for row in range(9):
            for col in range(10):
                image_label = QLabel()
                # TODO add all bingo balls images
                pixmap = QPixmap("resources/balls/bingo_ball.png")
                pixmap = pixmap.scaled(75, 75)
                image_label.setPixmap(pixmap)
                balls_layout.addWidget(image_label, row, col)
                self.balls.append(image_label)
                number += 1
        self.setLayout(balls_layout)

    def update_ball(self, ball_number: int):
        self.balls[ball_number - 1]
        self.balls[ball_number - 1].setPixmap(
            QPixmap(f"resources/balls/bingo_ball2.jpg").scaled(75, 75)
        )
