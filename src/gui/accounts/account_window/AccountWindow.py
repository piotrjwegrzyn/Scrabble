from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class AccountWindow(QMainWindow):

    def __init__(self):
        super(AccountWindow, self).__init__()
        loadUi("src/gui/accounts/account_window/account_window.ui", self)

        self.buttonChangePassword.clicked.connect(self.close)
        self.buttonDeleteAccount.clicked.connect(self.close)
        self.buttonStatistics.clicked.connect(self.close)
        self.buttonBack.clicked.connect(self.close)
