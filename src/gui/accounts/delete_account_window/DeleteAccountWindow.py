import hashlib
import sqlite3

from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.uic import loadUi


class DeleteAccountWindow(QMainWindow):

    def __init__(self):
        super(DeleteAccountWindow, self).__init__()
        loadUi("src/gui/accounts/delete_account_window/delete_account_window.ui", self)

        self.enterPassword.setEchoMode(QLineEdit.Password)
        self.enterPassword_2.setEchoMode(QLineEdit.Password)
        self.buttonDelete.clicked.connect(self.action_login)
        self.buttonBack.clicked.connect(self.action_go_back)

    def clear_data(self):
        self.enterPassword.setText("")
        self.enterPassword_2.setText("")

    def action_login(self):
        password = self.enterUsername.text()
        password_2 = self.enterPassword.text()

        if len(password) != 0 and len(password_2) != 0:
            if password == password_2:
                connection = sqlite3.connect('data/Accounts_Statistics.db')
                cursor = connection.cursor()

                hashedPass = hashlib.sha512(password.encode('utf-8')).hexdigest()
                query_check_password = "SELECT EXISTS (SELECT 1 FROM users WHERE ID='{}'password='{}')".format(
                    singleton.id,hashedPass)
                cursor.execute(query_check_password)
                if cursor.fetchone()[0]:
                    query_delete_user_stats = "DELETE FROM statistics WHERE ID='{}'".format(singleton.id)
                    cursor.execute(query_delete_user_stats)
                    query_delete_user = "DELETE FROM users WHERE ID='{}'".format(singleton.id)
                    cursor.execute(query_delete_user)
                else:
                    self.errorMessage.setStyleSheet("background-color: rgb(0,0,0,0); color: red")
                    self.errorMessage('Nieprawidłowe hasło')
                connection.commit()
                cursor.close()
                connection.close()
            else:
                self.errorMessage.setStyleSheet("background-color: rgb(0,0,0,0); color: red")
                self.errorMessage('Hasła się różnią')
        else:
            self.errorMessage.setStyleSheet("background-color: rgb(0,0,0,0); color: red")
            self.errorMessage.text('Przynajmniej jedno z pól jest puste')
        self.clear_data()

    def action_go_back(self):
        self.clear_data()
        self.close()
