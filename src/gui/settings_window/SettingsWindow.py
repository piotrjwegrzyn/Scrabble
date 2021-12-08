import json

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


def save_app_data(settings):
    try:
        with open('data/settings.json', 'w') as f:
            json.dump(settings, f)
    except:
        print('error occurred, cannot save')


class SettingsWindow(QMainWindow):

    def __init__(self):
        super(SettingsWindow, self).__init__()
        loadUi("src/gui/settings_window/settings_window.ui", self)

        self.settings = None
        self.load_data()

        self.buttonTilesOne.clicked.connect(self.action_tiles_one)
        self.buttonTilesTwo.clicked.connect(self.action_tiles_two)

        self.buttonBoardOne.clicked.connect(self.action_board_one)
        self.buttonBoardTwo.clicked.connect(self.action_board_two)

        self.buttonConfirm.clicked.connect(self.action_change_parameters)
        self.buttonBack.clicked.connect(self.close)

    def load_data(self):
        try:
            with open('data/settings.json', 'r') as f:
                self.settings = json.load(f)
        except:
            self.settings = {"tileAppearance": "Set_1", "boardAppearance": "Board_1", "sortingOrder": "Alfabetycznie"}
            print('error occurred, cannot load data, restoring default values')
        self.dropdownListSortTiles.setCurrentText(self.settings["sortingOrder"])

    def action_tiles_one(self):
        self.settings["tileAppearance"] = 'Set_1'

    def action_tiles_two(self):
        self.settings["tileAppearance"] = 'Set_2'

    def action_board_one(self):
        self.settings["boardAppearance"] = 'Board_1'

    def action_board_two(self):
        self.settings["boardAppearance"] = 'Board_2'

    def action_change_parameters(self):
        self.settings["sortingOrder"] = self.dropdownListSortTiles.currentText()
        save_app_data(self.settings)
