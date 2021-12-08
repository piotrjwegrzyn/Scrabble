import hashlib
import sqlite3

from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.uic import loadUi


class RegisterWindow(QMainWindow):

    def __init__(self):
        super(RegisterWindow, self).__init__()
        loadUi("src/gui/accounts/register_window/register_window.ui", self)

        self.enterPassword.setEchoMode(QLineEdit.Password)
        self.repeatPassword.setEchoMode(QLineEdit.Password)
        self.buttonRegister.clicked.connect(self.action_register)
        self.buttonBack.clicked.connect(self.close)

    def clear_data(self):
        self.enterUsername.setText("")
        self.enterPassword.setText("")
        self.repeatPassword.setText("")

    def action_register(self):
        username = self.enterUsername.text()
        password = self.enterPassword.text()
        repassword = self.repeatPassword.text()

        connection = sqlite3.connect('data/Accounts_Statistics.db')
        cursor = connection.cursor()

        if len(username) != 0 and len(password) != 0 and len(repassword) != 0:
            if password == repassword:
                if self.isUsernameAvailable(cursor, username):
                    hashedPass = hashlib.sha512(password.encode('utf-8')).hexdigest()
                    query_add_user = "INSERT INTO users(username, password) VALUES('{0}','{1}')".format(username, hashedPass)
                    cursor.execute(query_add_user)

                    query_add_user_stats = "INSERT INTO statistics(matches, wins, points, max_points) VALUES('0','0','0','0')"
                    cursor.execute(query_add_user_stats)
                    self.errorMessage.setStyleSheet("background-color: rgb(0,0,0,0); color: green")
                    self.errorMessage.setText("Konto założone pomyślnie. \nPrzejdź do menu logowania, aby się zalogować")
                else:
                    self.errorMessage.setStyleSheet("background-color: rgb(0,0,0,0); color: red")
                    self.errorMessage.setText("Podana nazwa użytkownika jest zajęta")
            else:
                self.errorMessage.setStyleSheet("background-color: rgb(0,0,0,0); color: red")
                self.errorMessage.setText("Hasła nie są takie same")
        else:
            self.errorMessage.setStyleSheet("background-color: rgb(0,0,0,0); color: red")
            self.errorMessage.setText("Przynajmniej jedno z pol jest puste")

        cursor.close()
        connection.commit()
        connection.close()
        self.clear_data()

    def isUsernameAvailable(self, cur, name):
        query_check = "SELECT EXISTS (SELECT 1 FROM users WHERE username='{}')".format(name)
        cur.execute(query_check)
        if cur.fetchone()[0]:
            return False
        else:
            return True
