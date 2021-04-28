from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

from Board import Board


class Tetris(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Экземпляр класса Board создается и
        # устанавливается центральным виджетом приложения
        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        # Строка состояния - для отображения сообщений, как то - сколько линий
        # выиграно, поставлена на паузу, игра окончена.

        # msgStatusbar – это пользовательский сигнал,
        # который реализуется в классе Board.
        self.statusbar = self.statusBar()
        # showMessage() – это встроенный метод, который отображает
        # сообщение в строке состояния.
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)

        # Инициируем игру
        self.tboard.start()

        # Параметры
        self.resize(250, 500)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
                (screen.height()-size.height())/2)
