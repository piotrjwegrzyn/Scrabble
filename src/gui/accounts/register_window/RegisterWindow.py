import sqlite3

from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.uic import loadUi


class RegisterWindow(QMainWindow):

    def __init__(self):
        super(RegisterWindow, self).__init__()
        loadUi("src/gui/accounts/register_window/register_window.ui", self)

        self.connection = sqlite3.connect('data/Accounts_Statistics.db')
        self.createTables()    # TODO przeniesc, gdzies na poczatek? <--

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

        cursor = self.connection.cursor()

        if len(username) != 0 and len(password) != 0 and len(repassword) != 0:
            if password == repassword:
                usernameUsed = self.isUsernameUsed(cursor, username)
                if not usernameUsed:
                    query_add_user = "INSERT INTO users(username, password) VALUES('{0}','{1}')".format(username, password)
                    cursor.execute(query_add_user)

                    query_add_user_stats = "INSERT INTO statistics(matches, points) VALUES('0','0')"
                    cursor.execute(query_add_user_stats)
                    self.errorMessage.setText("")
                else:
                    self.errorMessage.setText("Podana nazwa użytkownika jest zajęta")
            else:
                self.errorMessage.setText("Hasła nie są takie same")
        else:
            self.errorMessage.setText("Przynajmniej jedno z pol jest puste")

        cursor.close()
        self.connection.commit()
        self.clear_data()

    def isUsernameUsed(self, cur, name):
        query_check = "SELECT EXISTS (SELECT 1 FROM users WHERE username='{}')".format(name)
        cur.execute(query_check)
        if cur.fetchone()[0]:
            return True
        else:
            return False

    def action_go_back(self):
        self.connection.close()
        self.clear_data()
        self.close()

    def createTables(self):

        query_table_exists = "SELECT EXISTS (SELECT 1 FROM '{}')".format('users')
        cursor = self.connection.cursor()
        try:
            cursor.execute(query_table_exists)
        except:
            # TODO password <- nie bedzie przechowywane plain text'em
            query_table_create = 'CREATE TABLE users (ID INTEGER PRIMARY KEY AUTOINCREMENT, username varchar(30), password varchar(20))'
            cursor.execute(query_table_create)

        query_statistics_exists = "SELECT EXISTS (SELECT 1 FROM '{}')".format('statistics')
        try:
            cursor.execute(query_statistics_exists)
        except:
            query_statistics_create = "CREATE TABLE statistics (ID INTEGER PRIMARY KEY AUTOINCREMENT, matches int4, points int4)"
            cursor.execute(query_statistics_create)
