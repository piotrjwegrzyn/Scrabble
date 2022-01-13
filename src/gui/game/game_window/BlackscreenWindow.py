from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class BlackscreenWindow(QMainWindow):

    def __init__(self):
        super(BlackscreenWindow, self).__init__()
        loadUi("src/gui/game/game_window/black_window.ui", self)
