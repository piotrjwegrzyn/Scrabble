import sqlite3

from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.uic import loadUi


class DeleteWindow(QMainWindow):

    def __init__(self):
        super(DeleteWindow, self).__init__()
        loadUi("Screen/Accounts_Statistics/Delete/deleteWindow.ui", self)

        self.connection = sqlite3.connect('AppData/Accounts_Statistics.db')

        self.enterPassword.setEchoMode(QLineEdit.Password)
        self.buttonDelete.clicked.connect(self.action_login)
        self.buttonBack.clicked.connect(self.action_go_back)

    def clear_data(self):
        self.enterUsername.setText("")
        self.enterPassword.setText("")

    def action_login(self):
        username = self.enterUsername.text()
        password = self.enterPassword.text()

        cursor = self.connection.cursor()

        if len(username) != 0 and len(password) != 0:
            # hash_password = cos(password)
            passCheckOK = None
            query_check_password = "SELECT EXISTS (SELECT 1 FROM users WHERE password='{}')".format(password)
            # TODO ^hashed_pass
            cursor.execute(query_check_password)
            if cursor.fetchone()[0]:
                query_delete_user_stats = "DELETE FROM statistics WHERE ID=(SELECT ID FROM users WHERE username='{}')".format(username)
                cursor.execute(query_delete_user_stats)
                query_delete_user = "DELETE FROM users WHERE username='{}'".format(username)
                cursor.execute(query_delete_user)
            else:
                self.errorMessage('Cos poszlo nie tak')
        else:
            self.errorMessage.setText('Przynajmniej jedno z pol jest puste')

        cursor.close()
        self.connection.commit()
        self.clear_data()

    def action_go_back(self):
        self.clear_data()
        self.close()
