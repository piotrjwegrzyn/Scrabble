import hashlib
import sqlite3

from PyQt5.QtWidgets import QLineEdit, QDialog
from PyQt5.uic import loadUi

from src.game_classes.GamePlayers import GamePlayers


class MiniLoginWindow(QDialog):

    def __init__(self, player):
        super(MiniLoginWindow, self).__init__()
        loadUi("src/gui/accounts/login/mini_login_window/mini_login_window.ui", self)

        self.playerEdit = player

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

                canPass = True
                for player in GamePlayers.get_instances():
                    if player.id == id:
                        canPass = False
                        break
                if canPass:
                    self.playerEdit.name = username
                    self.playerEdit.id = id
                    connection.close()
                    self.close()
                else:
                    self.errorMessage.setStyleSheet("background-color: rgb(0,0,0,0); color: red")
                    self.errorMessage.setText("Użytkownik jest już zalogowany")
                    connection.close()
            except:
                self.errorMessage.setStyleSheet("background-color: rgb(0,0,0,0); color: red")
                self.errorMessage.setText("Przynajmniej jedno pole jest nieprawidłowe")
                connection.close()
        self.clear_data()
