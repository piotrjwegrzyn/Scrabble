from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class AccountsWindow(QMainWindow):

    def __init__(self):
        super(AccountsWindow, self).__init__()
        loadUi("src/gui/accounts/accounts_window/accounts_window.ui", self)

        self.buttonBack.clicked.connect(self.close)


