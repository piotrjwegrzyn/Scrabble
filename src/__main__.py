import sys
import sqlite3

from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget

import gui


class WindowManager(QMainWindow):
    def __init__(self):
        super(WindowManager, self).__init__()
        self.initialize_database_tables()

        self.show_welcome_window()

    def show_welcome_window(self):
        welcomeWindow = gui.welcome_window.WelcomeWindow()
        welcomeWindow.buttonLogin.clicked.connect(self.show_login_window)
        welcomeWindow.buttonRegister.clicked.connect(self.show_register_window)
        welcomeWindow.buttonExit.clicked.connect(widget.close)
        widget.addWidget(welcomeWindow)
        welcomeWindow.show()

    def show_register_window(self):
        registerWindow = gui.register_window.RegisterWindow()
        registerWindow.buttonBack.clicked.connect(self.show_welcome_window)
        widget.addWidget(registerWindow)
        registerWindow.show()

    def show_login_window(self):
        loginWindow = gui.login_window.LoginWindow()
        loginWindow.buttonLogin.clicked.connect(self.show_menu_window)
        loginWindow.buttonBack.clicked.connect(self.show_welcome_window)
        widget.addWidget(loginWindow)
        loginWindow.show()

    def show_menu_window(self):
        # TODO odkomentowac -> +loginWindow.py x2 TODO
        # if gui.LoggedUser.get_instance() is not None:
            menuWindow = gui.menu_window.MenuWindow()
            menuWindow.buttonGameSetting.clicked.connect(self.show_game_setting_window)
            menuWindow.buttonAccountStatistics.clicked.connect(self.show_account_window)
            menuWindow.buttonSettings.clicked.connect(self.show_settings_window)
            menuWindow.buttonLogout.clicked.connect(self.show_login_window)
            menuWindow.buttonExit.clicked.connect(widget.close)
            widget.addWidget(menuWindow)
            menuWindow.show()

    def show_game_setting_window(self):
        gameSettingWindow = gui.game_setting_window.GameSettingWindow()
        gameSettingWindow.buttonGame.clicked.connect(self.show_game_window)
        gameSettingWindow.buttonBack.clicked.connect(self.show_menu_window)
        widget.addWidget(gameSettingWindow)
        gameSettingWindow.show()

    def show_game_window(self):  # TODO
        gameWindow = gui.game_window.GameWindow()
        gameWindow.buttonResign.clicked.connect(self.show_menu_window)
        widget.addWidget(gameWindow)
        gameWindow.show()

    def show_account_window(self):
        if gui.LoggedUser.get_instance() is not None:
            accountWindow = gui.account_window.AccountWindow()
            accountWindow.buttonChangePassword.clicked.connect(self.show_change_password_window)
            accountWindow.buttonDeleteAccount.clicked.connect(self.show_delete_account_window)
            accountWindow.buttonStatistics.clicked.connect(self.show_statistics_window)
            accountWindow.buttonBack.clicked.connect(self.show_menu_window)
            widget.addWidget(accountWindow)
            accountWindow.show()
        else:
            self.show_welcome_window()

    def show_change_password_window(self):
        changePasswordWindow = gui.change_password_window.ChangePasswordWindow()
        changePasswordWindow.buttonBack.clicked.connect(self.show_account_window)
        widget.addWidget(changePasswordWindow)
        changePasswordWindow.show()

    def show_delete_account_window(self):
        deleteAccountWindow = gui.delete_account_window.DeleteAccountWindow()
        deleteAccountWindow.buttonBack.clicked.connect(self.show_account_window)
        widget.addWidget(deleteAccountWindow)
        deleteAccountWindow.show()

    def show_statistics_window(self):
        statisticsWindow = gui.statistics_window.StatisticsWindow()
        statisticsWindow.buttonBack.clicked.connect(self.show_account_window)
        widget.addWidget(statisticsWindow)
        statisticsWindow.show()

    def show_settings_window(self):
        settingsWindow = gui.settings_window.SettingsWindow()
        settingsWindow.buttonBack.clicked.connect(self.show_menu_window)
        widget.addWidget(settingsWindow)
        settingsWindow.show()

    def initialize_database_tables(self):
        connection = sqlite3.connect('data/Accounts_Statistics.db')
        cursor = connection.cursor()

        query_table_exists = "SELECT EXISTS (SELECT 1 FROM users)"
        try:
            cursor.execute(query_table_exists)
        except:
            query_table_create = "CREATE TABLE users (ID INTEGER PRIMARY KEY AUTOINCREMENT, username varchar(30), password varchar(128))"
            cursor.execute(query_table_create)

        query_statistics_exists = "SELECT EXISTS (SELECT 1 FROM statistics)"
        try:
            cursor.execute(query_statistics_exists)
        except:
            query_statistics_create = "CREATE TABLE statistics (ID INTEGER PRIMARY KEY AUTOINCREMENT, matches int4, wins int4, points int4, max_points int4)"
            cursor.execute(query_statistics_create)
        cursor.close()
        connection.close()


application = QApplication(sys.argv)
widget = QStackedWidget()
window = WindowManager()
widget.setFixedWidth(1440)
widget.setFixedHeight(900)

widget.show()

sys.exit(application.exec())
