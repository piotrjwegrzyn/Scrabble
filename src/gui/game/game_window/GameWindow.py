from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


# TODO
class GameWindow(QMainWindow):

    def __init__(self):
        super(GameWindow, self).__init__()
        loadUi("src/gui/game/game_window/game_window.ui", self)
