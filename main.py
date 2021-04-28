import sys
from PyQt5.QtWidgets import QApplication

from Tetris import Tetris


if __name__ == '__main__':
    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())
