import hashlib
import sqlite3

from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.uic import loadUi

from ....accounts.LoggedUser import LoggedUser


class LoginWindow(QMainWindow):

    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("src/gui/accounts/login/login_window/login_window.ui", self)

        self.errorMessage.setText("")
        self.enterPassword.setEchoMode(QLineEdit.Password)
        self.buttonLogin.clicked.connect(self.action_login)
        self.buttonBack.clicked.connect(self.close)

    def clear_data(self):
        self.enterUsername.setText("")
        self.enterPassword.setText("")

    def action_login(self):
        username = self.enterUsername.text()
        password = self.enterPassword.text()
        if len(username) == 0 or len(password) == 0:
            self.errorMessage.setStyleSheet("background-color: rgb(0,0,0,0); color: red")
            self.errorMessage.setText('Przynajmniej jedno pole jest puste, wypełnij wszystkie pola')
        else:
            connection = sqlite3.connect("data/Accounts_Statistics.db")
            cursor = connection.cursor()
            hashedPass = hashlib.sha512(password.encode('utf-8')).hexdigest()

            try:
                queryGetUserID = "SELECT ID FROM 'users' WHERE username = '{0}' AND password = '{1}'"\
                    .format(username, hashedPass)
                id = cursor.execute(queryGetUserID).fetchone()[0]

                try:
                    LoggedUser(username, id)
                    self.errorMessage.setText("Passed")
                    connection.close()
                    self.close()
                except:
                    self.errorMessage.setStyleSheet("background-color: rgb(0,0,0,0); color: red")
                    self.errorMessage.setText("Coś poszło nie tak (LoggedUser assignment)")
            except:
                self.errorMessage.setStyleSheet("background-color: rgb(0,0,0,0); color: red")
                self.errorMessage.setText("Przynajmniej jedno pole jest nieprawidłowe")
                connection.close()
        self.clear_data()
