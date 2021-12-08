import hashlib
import sqlite3

from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.uic import loadUi


class ChangePasswordWindow(QMainWindow):

    def __init__(self):
        super(ChangePasswordWindow, self).__init__()
        loadUi("src/gui/accounts/change_password_window/change_password_window.ui", self)

        self.enterOldPassword.setEchoMode(QLineEdit.Password)
        self.enterNewPassword.setEchoMode(QLineEdit.Password)
        self.enterNewPassword_2.setEchoMode(QLineEdit.Password)
        self.buttonChangePassword.clicked.connect(self.action_change_pass)
        self.buttonBack.clicked.connect(self.close)

    def clear_data(self):
        self.enterOldPassword.setText("")
        self.enterNewPassword.setText("")
        self.enterNewPassword_2.setText("")

    def action_change_pass(self):
        password = self.enterOldPassword.text()
        newPass = self.enterNewPassword.text()
        newPass2 = self.enterNewPassword_2.text()

        if len(password) != 0 or len(newPass) != 0 or len(newPass2) != 0:
            if newPass == newPass2:
                connection = sqlite3.connect('data/Accounts_Statistics.db')
                cursor = connection.cursor()

                hashedPass = hashlib.sha512(password.encode('utf-8')).hexdigest()
                query_check_password = "SELECT EXISTS (SELECT 1 FROM users WHERE ID='{}' AND password='{}')".format(
                    singleton.id, hashedPass)
                cursor.execute(query_check_password)
                if cursor.fetchone()[0]:
                    newHashedPass = hashlib.sha512(newPass.encode('utf-8')).hexdigest()
                    query_change_password = "UPDATE users SET password='{1}' WHERE ID='{0}'".format(singleton.id, newHashedPass)
                    cursor.execute(query_change_password)
                else:
                    self.errorMessage.setStyleSheet("background-color: rgb(0,0,0,0); color: red")
                    self.errorMessage('Nieprawidłowe hasło')
                cursor.close()
                connection.commit()
                connection.close()
            else:
                self.errorMessage.setStyleSheet("background: rgb(0,0,0,0); color: red")
                self.errorMessage.setText('Hasła się różnią')
        else:
            self.errorMessage.setStyleSheet("background: rgb(0,0,0,0); color: red")
            self.errorMessage.setText('Przynajmniej jedno z pól jest puste')


        cursor.close()
        connection.commit()
        connection.close()
        self.clear_data()
