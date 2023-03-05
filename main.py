import sys
from PySide6.QtWidgets import QApplication

from culitri_bingo import CulitriBingo


def main():
    app = QApplication(sys.argv)
    window = CulitriBingo()
    window.initialize_buttons()
    window.show()
    app.exec()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print("Exiting Culitri Bingo...")
