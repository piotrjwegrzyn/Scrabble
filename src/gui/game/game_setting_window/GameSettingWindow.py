from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class GameSettingWindow(QMainWindow):

    def __init__(self):
        super(GameSettingWindow, self).__init__()
        loadUi("src/gui/game/game_setting_window/game_setting_window.ui", self)
