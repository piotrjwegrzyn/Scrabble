import sqlite3

from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.uic import loadUi


class RegisterWindow(QMainWindow):

    def __init__(self):
        super(RegisterWindow, self).__init__()
        loadUi("Screen/Accounts_Statistics/Register/registerWindow.ui", self)

        self.enterPassword.setEchoMode(QLineEdit.Password)
        self.repeatPassword.setEchoMode(QLineEdit.Password)
        self.buttonRegister.clicked.connect(self.action_register)
        self.buttonBack.clicked.connect(self.action_go_back)

    def clear_data(self):
        self.enterUsername.setText("")
        self.enterPassword.setText("")
        self.repeatPassword.setText("")

    def action_register(self):
        username = self.enterUsername.text()
        password = self.enterPassword.text()
        repassword = self.repeatPassword.text()

        # Todo

        self.clear_data()

    def action_go_back(self):
        self.clear_data()
        self.close()
