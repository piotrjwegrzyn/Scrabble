import sqlite3

from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.uic import loadUi


class LoginWindow(QMainWindow):

    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("src/gui/accounts/login_window/login_window.ui", self)

        self.enterPassword.setEchoMode(QLineEdit.Password)
        self.buttonLogin.clicked.connect(self.action_login)
        self.buttonBack.clicked.connect(self.action_go_back)

    def clear_data(self):
        self.enterUsername.setText("")
        self.enterPassword.setText("")

    def action_login(self):
        username = self.enterUsername.text()
        password = self.enterPassword.text()

        if len(username) == 0 or len(password) == 0:
            self.errorMessage.setText('Input is missing. Please fill both boxes')
        else:
            connection = sqlite3.connect("AppData/Accounts_Statistics.db")
            cursor = connection.cursor()
            # TODO

        self.clear_data()

    def action_go_back(self):
        self.clear_data()
        self.close()
