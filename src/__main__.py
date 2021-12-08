import sys
import sqlite3

from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget

import gui


class WindowManager(QMainWindow):
    def __init__(self):
        super(WindowManager, self).__init__()
        self.initialize_database_tables()

        self.welcomeWindow = gui.welcome_window.WelcomeWindow()
        self.menuWindow = None

        self.welcomeWindow.loginWindow = None
        self.welcomeWindow.buttonLogin.clicked.connect(self.goto_login)
        self.welcomeWindow.buttonRegister.clicked.connect(self.goto_register)
        self.welcomeWindow.buttonExit.clicked.connect(widget.close)

    def goto_login(self):
        self.welcomeWindow.hide()
        if self.welcomeWindow.loginWindow is None:
            self.welcomeWindow.loginWindow = gui.login_window.LoginWindow()
            self.welcomeWindow.loginWindow.buttonBack.clicked.connect(self.welcomeWindow.show)
            self.welcomeWindow.loginWindow.buttonLogin.clicked.connect(self.goto_menu)
        widget.addWidget(self.welcomeWindow.loginWindow)
        self.welcomeWindow.loginWindow.show()

    def goto_register(self):
        self.welcomeWindow.hide()
        registerWindow = gui.register_window.RegisterWindow()
        registerWindow.buttonBack.clicked.connect(self.welcomeWindow.show)
        widget.addWidget(registerWindow)
        registerWindow.show()

    def goto_menu(self):
        if self.welcomeWindow.loginWindow.errorMessage.text() == "Passed":
            self.welcomeWindow.loginWindow.hide()
            if self.menuWindow is None:
                self.menuWindow = gui.menu_window.MenuWindow()
                self.menuWindow.gameSettingWindow = None
                self.menuWindow.accountWindow = None
                self.menuWindow.buttonGameSetting.clicked.connect(self.goto_game_setting)
                self.menuWindow.buttonAccountStatistics.clicked.connect(self.goto_account_statistics)
                self.menuWindow.buttonSettings.clicked.connect(self.goto_settings)
                self.menuWindow.buttonLogoutExit.clicked.connect(self.logout)
            widget.addWidget(self.menuWindow)
            self.menuWindow.show()

    def goto_game_setting(self):
        self.menuWindow.hide()
        if self.menuWindow.gameSettingWindow is None:
            self.menuWindow.gameSettingWindow = gui.game_setting_window.GameSettingWindow()
        widget.addWidget(self.menuWindow.gameSettingWindow)
        self.menuWindow.gameSettingWindow.show()

    def goto_account_statistics(self):
        self.menuWindow.hide()
        if self.menuWindow.accountWindow is None:
            self.menuWindow.accountWindow = gui.account_window.AccountWindow()
            self.menuWindow.accountWindow.buttonChangePassword.clicked.connect(self.goto_change_password)
            self.menuWindow.accountWindow.buttonDeleteAccount.clicked.connect(self.goto_delete_account)
            self.menuWindow.accountWindow.buttonStatistics.clicked.connect(self.goto_statistics)
            self.menuWindow.accountWindow.buttonBack.clicked.connect(self.menuWindow.show)
        widget.addWidget(self.menuWindow.accountWindow)
        self.menuWindow.accountWindow.show()

    def goto_change_password(self):
        self.menuWindow.accountWindow.hide()
        changePasswordWindow = gui.change_password_window.ChangePasswordWindow()
        changePasswordWindow.buttonBack.clicked.connect(self.menuWindow.accountWindow.show)
        widget.addWidget(changePasswordWindow)
        changePasswordWindow.show()

    def goto_delete_account(self):
        self.menuWindow.accountWindow.hide()
        deleteAccountWindow = gui.delete_account_window.DeleteAccountWindow()
        deleteAccountWindow.buttonBack.clicked.connect(self.menuWindow.accountWindow.show)
        widget.addWidget(deleteAccountWindow)
        deleteAccountWindow.show()

    def goto_statistics(self):
        self.menuWindow.accountWindow.hide()
        statisticsWindow = gui.statistics_window.StatisticsWindow()
        statisticsWindow.buttonBack.clicked.connect(self.menuWindow.accountWindow.show)
        widget.addWidget(statisticsWindow)
        statisticsWindow.show()

    def goto_settings(self):
        self.menuWindow.hide()
        settingsWindow = gui.settings_window.SettingsWindow()
        settingsWindow.buttonBack.clicked.connect(self.menuWindow.show)
        widget.addWidget(settingsWindow)
        settingsWindow.show()

    def logout(self):
        # TODO singleton delete
        widget.close()

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


application = QApplication(sys.argv)
widget = QStackedWidget()
window = WindowManager()
widget.addWidget(window.welcomeWindow)
widget.setMinimumWidth(800)
widget.setMinimumHeight(600)

widget.show()

sys.exit(application.exec())
