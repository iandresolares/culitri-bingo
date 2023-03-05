import random


class GameLogic:
    def __init__(self):
        pass

    def start(self, bingo_balls):
        number = random.randint(1, 90)
        bingo_balls.update_ball(number)

    def stop(self):
        print("STOPPED")

    def reset(self):
        pass
