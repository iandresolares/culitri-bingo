import random
from enum import StrEnum
from PySide6.QtCore import Signal, QObject, QTimer
import pyttsx3
from playsound import playsound
from gtts import gTTS


class GameState(StrEnum):
    READY = "READY"
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"


class GameLogic(QObject):
    new_ball_signal = Signal()

    def __init__(self, bingo_balls):
        super().__init__()
        self.state = GameState.READY
        self.numbers = [n for n in range(1, 91)]

        self.new_ball_signal.connect(self.new_ball)

        self.new_ball_timer = QTimer()
        self.new_ball_timer.timeout.connect(self.new_ball_signal.emit)

        self.bingo_balls = bingo_balls

        self.audio_engine = pyttsx3.init()

        spanish_voice = None
        voices = self.audio_engine.getProperty("voices")

        for voice in voices:
            print(voice.id)
            if "spanish" in voice.languages:
                spanish_voice = voice.id
                break
        self.audio_engine.setProperty("voice", spanish_voice)

    def start(self):
        if self.state == GameState.RUNNING:
            return
        elif self.state == GameState.STOPPED:
            # * Resume game
            self.state = GameState.RUNNING
            print("Bingo resuming...")
        elif self.state == GameState.READY:
            # * Start game
            self.state = GameState.RUNNING
            print("Bingo starting...")

        self.new_ball_timer.start(1000)
        # * start bingo sequence

    def stop(self):
        if self.state != GameState.RUNNING:
            return
        self.new_ball_timer.stop()
        self.state = GameState.STOPPED
        print("Bingo stopping...")
        self.audio_engine.say("Bingo stopping...")
        self.audio_engine.runAndWait()

    def reset(self):
        self.new_ball_timer.stop()
        self.numbers = [n for n in range(1, 91)]
        self.state = GameState.READY
        self.bingo_balls.reset_balls()

        print("Bingo resetting...")

    def new_ball(self):
        # TODO handle number
        # TODO update bingo balls and latest balls
        number = random.choice(self.numbers)
        self.bingo_balls.update_ball(number)
        self.numbers.remove(number)
        # TODO test gtts and fix this
        tts = gTTS(text=str(number), lang="es").save("audio.mp3")
        playsound("audio.mp3")
        # self.audio_engine.say(str(number))
        # self.audio_engine.runAndWait()
