from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from src.gui.accounts.LoggedUser import LoggedUser


class MenuWindow(QMainWindow):

    def __init__(self):
        super(MenuWindow, self).__init__()
        loadUi("src/gui/menu_window/menu_window.ui", self)

        self.buttonGameSetting.clicked.connect(self.close)
        self.buttonAccountStatistics.clicked.connect(self.close)
        self.buttonSettings.clicked.connect(self.close)
        self.buttonLogout.clicked.connect(self.logout)

    def logout(self):
        LoggedUser.getInstance().uid = None
        self.close()
