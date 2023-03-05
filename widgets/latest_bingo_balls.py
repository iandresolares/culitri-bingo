from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout
)
from PySide6.QtGui import QPixmap


class LatestBallsWidget(QWidget):
    def __init__(self):
        super().__init__()
        ball_layout = QVBoxLayout()
        ball_layout.addWidget(LatestBall())
        ball_layout.addWidget(LatestBingoBalls())
        self.setLayout(ball_layout)


class LatestBingoBalls(QWidget):
    def __init__(self):
        super().__init__()
        balls_layout = QHBoxLayout()

        for ball in range(5):
            image_label = QLabel()
            # TODO add all bingo balls images
            pixmap = QPixmap("resources/balls/bingo_ball.png")
            pixmap = pixmap.scaled(50, 50)
            image_label.setPixmap(pixmap)
            balls_layout.addWidget(image_label)
        self.setLayout(balls_layout)


class LatestBall(QWidget):
    def __init__(self):
        super().__init__()
        ball_layout = QHBoxLayout()
        image_label = QLabel()
        # TODO add all bingo balls images
        pixmap = QPixmap("resources/balls/bingo_ball.png")
        pixmap = pixmap.scaled(100, 100)
        image_label.setPixmap(pixmap)
        ball_layout.addWidget(image_label)
        self.setLayout(ball_layout)
