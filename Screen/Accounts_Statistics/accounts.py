from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class AccountsWindow(QMainWindow):

    def __init__(self):
        super(AccountsWindow, self).__init__()
        loadUi("Screen/Accounts_Statistics/accountsWindow.ui", self)

        self.buttonBack.clicked.connect(self.close)


