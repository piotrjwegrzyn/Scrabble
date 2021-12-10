from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


# TODO
class GameSettingWindow(QMainWindow):

    def __init__(self):
        super(GameSettingWindow, self).__init__()
        loadUi("src/gui/game/game_setting_window/game_setting_window.ui", self)

        self.set_default_buttons()

        self.buttonPlayer1.clicked.connect(self.show_p1)
        # self.buttonPlayer2.clicked.connect(self.player_2_clicked)
        # self.buttonPlayer3.clicked.connect(self.player_3_clicked)
        # self.buttonPlayer4.clicked.connect(self.player_4_clicked)
        self.buttonComputer1.clicked.connect(self.computer1_clicked)
        # self.buttonComputer2.clicked.connect(self.computer2_clicked)
        # self.buttonComputer3.clicked.connect(self.computer3_clicked)
        # self.buttonComputer4.clicked.connect(self.computer4_clicked)
        self.show_p1()

    def set_default_buttons(self):
        self.buttonPlayer1.setStyleSheet('color: rgb(0,0,0,80)')
        self.buttonPlayer2.setStyleSheet('color: rgb(0,0,0,80)')
        self.buttonPlayer3.setStyleSheet('color: rgb(0,0,0,80)')
        self.buttonPlayer4.setStyleSheet('color: rgb(0,0,0,80)')
        self.buttonKomputer1.setStyleSheet('color: rgb(0,0,0,80)')
        self.buttonKomputer2.setStyleSheet('color: rgb(0,0,0,80)')
        self.buttonKomputer3.setStyleSheet('color: rgb(0,0,0,80)')
        self.buttonKomputer4.setStyleSheet('color: rgb(0,0,0,80)')

    def show_p1(self):
        self.buttonPlayer1.setStyleSheet('color: rgb(0,0,0,255)')
        self.buttonKomputer1.setStyleSheet('color: rgb(0,0,0,80)')

        self.buttonPlayer1.clicked.connect(self.player_1_clicked)

    def printt(self):
        print('a')
