import sys
import json

from PyQt5.QtWidgets import QApplication, QStackedWidget, QMainWindow
from PyQt5.uic import loadUi


def saveAppData(settings):
    try:
        with open('AppData/settings.json', 'w') as f:
            json.dump(settings, f)
    except:
        print('error occurred, cannot save')


def goBack():
    print('back')


class SettingsScreen(QMainWindow):
    settings = ''

    def __init__(self):
        super(SettingsScreen, self).__init__()
        loadUi("Screen/Settings/windowSettings.ui", self)
        self.loadData()

        self.buttonTilesOne.clicked.connect(self.changeTilesOne)
        self.buttonTilesTwo.clicked.connect(self.changeTilesTwo)

        self.buttonBoardOne.clicked.connect(self.changeBoardOne)
        self.buttonBoardTwo.clicked.connect(self.changeBoardTwo)

        self.buttonConfirm.clicked.connect(self.changeParameters)
        self.buttonCancel.clicked.connect(goBack)

    def loadData(self):
        try:
            with open('AppData/settings.json', 'r') as f:
                self.settings = json.load(f)
        except:
            self.settings = {"tileAppearance": "Set_1", "boardAppearance": "Board_1", "sortingOrder": "Alfabetycznie"}
            print('error occurred, cannot load data, restoring default values')
        self.dropdownListSortTiles.setCurrentText(self.settings["sortingOrder"])

    def changeTilesOne(self):
        self.settings["tileAppearance"] = 'Set_1'

    def changeTilesTwo(self):
        self.settings["tileAppearance"] = 'Set_2'

    def changeBoardOne(self):
        self.settings["boardAppearance"] = 'Board_1'

    def changeBoardTwo(self):
        self.settings["boardAppearance"] = 'Board_2'

    def changeParameters(self):
        self.settings["sortingOrder"] = self.dropdownListSortTiles.currentText()
        saveAppData(self.settings)
        goBack()


app = QApplication(sys.argv)
settings = SettingsScreen()
widget = QStackedWidget()
widget.addWidget(settings)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("X")

