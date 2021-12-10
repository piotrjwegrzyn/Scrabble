import hashlib
import sqlite3
from time import sleep

from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.uic import loadUi

from src.gui.accounts.LoggedUser import LoggedUser


class DeleteAccountWindow(QMainWindow):

    def __init__(self):
        super(DeleteAccountWindow, self).__init__()
        loadUi("src/gui/accounts/delete_account_window/delete_account_window.ui", self)

        self.enterPassword.setEchoMode(QLineEdit.Password)
        self.enterPassword_2.setEchoMode(QLineEdit.Password)
        self.buttonDelete.clicked.connect(self.action_delete_account)
        self.buttonBack.clicked.connect(self.action_go_back)

    def clear_data(self):
        self.enterPassword.setText("")
        self.enterPassword_2.setText("")

    def action_delete_account(self):
        password = self.enterPassword.text()
        password_2 = self.enterPassword_2.text()

        if len(password) != 0 and len(password_2) != 0:
            if password == password_2:
                hashedPassword = hashlib.sha512(password.encode('utf-8')).hexdigest()
                id = LoggedUser.getInstance().uid

                connection = sqlite3.connect('data/Accounts_Statistics.db')
                cursor = connection.cursor()

                query_check_password = "SELECT EXISTS (SELECT 1 FROM users WHERE ID='{}' AND password='{}')"\
                    .format(id, hashedPassword)
                if cursor.execute(query_check_password).fetchone()[0] == 1:
                    query_delete_user_stats = "DELETE FROM statistics WHERE ID='{}'"\
                        .format(id)
                    cursor.execute(query_delete_user_stats)
                    query_delete_user = "DELETE FROM users WHERE ID='{}'"\
                        .format(id)
                    cursor.execute(query_delete_user)
                    connection.commit()
                    LoggedUser.getInstance().uid = None
                    self.errorMessage.setText("Konto zostało usunięte. Kliknij 'powrot', aby wrocic do menu startowego")
                else:
                    self.errorMessage.setStyleSheet("background-color: rgb(0,0,0,0); color: red")
                    self.errorMessage.setText('Nieprawidłowe hasło')
                cursor.close()
                connection.close()
            else:
                self.errorMessage.setStyleSheet("background-color: rgb(0,0,0,0); color: red")
                self.errorMessage.setText('Hasła się różnią')
        else:
            self.errorMessage.setStyleSheet("background-color: rgb(0,0,0,0); color: red")
            self.errorMessage.setText('Przynajmniej jedno z pól jest puste')
        self.clear_data()

    def action_go_back(self):
        self.clear_data()
        self.close()
