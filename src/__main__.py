import sqlite3
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget

import gui


class WindowManager(QMainWindow):
    def __init__(self):
        super(WindowManager, self).__init__()
        self.initialize_database_tables()
        self.game = None
        self.game_window = None
        self.blackscreen_window = None
        self.show_welcome_window()

    def show_welcome_window(self):
        welcomeWindow = gui.welcome_window.WelcomeWindow()
        welcomeWindow.buttonLogin.clicked.connect(self.show_login_window)
        welcomeWindow.buttonRegister.clicked.connect(self.show_register_window)
        welcomeWindow.buttonExit.clicked.connect(widget.close)
        widget.addWidget(welcomeWindow)
        welcomeWindow.setFixedSize(widget.width(), widget.height())
        welcomeWindow.show()

    def show_register_window(self):
        registerWindow = gui.register_window.RegisterWindow()
        registerWindow.buttonBack.clicked.connect(self.show_welcome_window)
        widget.addWidget(registerWindow)
        registerWindow.setFixedSize(widget.width(), widget.height())
        registerWindow.show()

    def show_login_window(self):
        loginWindow = gui.login_window.LoginWindow()
        loginWindow.buttonLogin.clicked.connect(self.show_menu_window)
        loginWindow.buttonBack.clicked.connect(self.show_welcome_window)
        widget.addWidget(loginWindow)
        loginWindow.setFixedSize(widget.width(), widget.height())
        loginWindow.show()

    def show_menu_window(self):
        if gui.LoggedUser.get_instance() is not None:
            menuWindow = gui.menu_window.MenuWindow()
            menuWindow.buttonGameSetting.clicked.connect(self.show_game_setting_window)
            menuWindow.buttonAccountStatistics.clicked.connect(self.show_account_window)
            menuWindow.buttonSettings.clicked.connect(self.show_settings_window)
            menuWindow.buttonLogout.clicked.connect(self.show_login_window)
            menuWindow.buttonExit.clicked.connect(widget.close)
            widget.addWidget(menuWindow)
            menuWindow.setFixedSize(widget.width(), widget.height())
            menuWindow.show()

    def show_game_setting_window(self):
        gameSettingWindow = gui.game_setting_window.GameSettingWindow()
        gameSettingWindow.buttonGame.clicked.connect(self.start_game)
        gameSettingWindow.buttonBack.clicked.connect(self.show_menu_window)
        widget.addWidget(gameSettingWindow)
        gameSettingWindow.setFixedSize(widget.width(), widget.height())
        gameSettingWindow.show()

    def show_game_window(self):
        if self.blackscreen_window is not None:
            self.blackscreen_window.hide()
        if self.game_window is None:
            self.game_window = gui.game_window.GameWindow()
            self.game_window.display_data()
            self.game_window.buttonResign.clicked.connect(self.show_menu_window)
            self.game_window.buttonExchange.clicked.connect(self.game.exchange_clicked)
            self.game_window.buttonEndTurn.clicked.connect(self.game.make_move)
            widget.addWidget(self.game_window)
            self.game_window.setFixedSize(widget.width(), widget.height())
        self.game_window.show()

    def show_blackscreen_window(self):
        self.game_window.hide()
        if self.blackscreen_window is None:
            self.blackscreen_window = gui.blackscreen_window.BlackscreenWindow()
            self.blackscreen_window.buttonContinue.clicked.connect(self.show_game_window)
            widget.addWidget(self.blackscreen_window)
            self.blackscreen_window.setFixedSize(widget.width(), widget.height())
        self.blackscreen_window.show()

    def show_account_window(self):
        if gui.LoggedUser.get_instance() is not None:
            accountWindow = gui.account_window.AccountWindow()
            accountWindow.buttonChangePassword.clicked.connect(self.show_change_password_window)
            accountWindow.buttonDeleteAccount.clicked.connect(self.show_delete_account_window)
            accountWindow.buttonStatistics.clicked.connect(self.show_statistics_window)
            accountWindow.buttonBack.clicked.connect(self.show_menu_window)
            widget.addWidget(accountWindow)
            accountWindow.setFixedSize(widget.width(), widget.height())
            accountWindow.show()
        else:
            self.show_welcome_window()

    def show_change_password_window(self):
        changePasswordWindow = gui.change_password_window.ChangePasswordWindow()
        changePasswordWindow.buttonBack.clicked.connect(self.show_account_window)
        widget.addWidget(changePasswordWindow)
        changePasswordWindow.setFixedSize(widget.width(), widget.height())
        changePasswordWindow.show()

    def show_delete_account_window(self):
        deleteAccountWindow = gui.delete_account_window.DeleteAccountWindow()
        deleteAccountWindow.buttonBack.clicked.connect(self.show_account_window)
        widget.addWidget(deleteAccountWindow)
        deleteAccountWindow.setFixedSize(widget.width(), widget.height())
        deleteAccountWindow.show()

    def show_statistics_window(self):
        statisticsWindow = gui.statistics_window.StatisticsWindow()
        statisticsWindow.buttonBack.clicked.connect(self.show_account_window)
        widget.addWidget(statisticsWindow)
        statisticsWindow.setFixedSize(widget.width(), widget.height())
        statisticsWindow.show()

    def show_settings_window(self):
        settingsWindow = gui.settings_window.SettingsWindow()
        settingsWindow.buttonBack.clicked.connect(self.show_menu_window)
        widget.addWidget(settingsWindow)
        settingsWindow.setFixedSize(widget.width(), widget.height())
        settingsWindow.show()

    def initialize_database_tables(self):
        connection = sqlite3.connect('data/Accounts_Statistics.db')
        cursor = connection.cursor()

        query_table_exists = "SELECT EXISTS (SELECT 1 FROM users)"
        try:
            cursor.execute(query_table_exists)
        except:
            query_table_create = "CREATE TABLE users (ID INTEGER PRIMARY KEY AUTOINCREMENT, username varchar(30), " \
                                 "password varchar(128))"
            cursor.execute(query_table_create)
            query_add_ai_easy = "INSERT INTO users (username) VALUES ('AI Komputer Easy')"
            cursor.execute(query_add_ai_easy)
            connection.commit()
            query_add_ai_medium = "INSERT INTO users (username) VALUES ('AI Komputer Medium')"
            cursor.execute(query_add_ai_medium)
            connection.commit()
            query_add_ai_hard = "INSERT INTO users (username) VALUES ('AI Komputer Hard')"
            cursor.execute(query_add_ai_hard)
            connection.commit()

        query_statistics_exists = "SELECT EXISTS (SELECT 1 FROM statistics)"
        try:
            cursor.execute(query_statistics_exists)
        except:
            query_statistics_create = "CREATE TABLE statistics (ID INTEGER PRIMARY KEY AUTOINCREMENT, matches int4, " \
                                      "wins int4, points int4, max_points int4)"
            cursor.execute(query_statistics_create)
            query_add_ai_easy_stats = "INSERT INTO statistics (matches, wins, points, max_points) VALUES (0, 0, 0, 0)"
            cursor.execute(query_add_ai_easy_stats)
            connection.commit()
            query_add_ai_medium_stats = "INSERT INTO statistics (matches, wins, points, max_points) VALUES (0, 0, 0, 0)"
            cursor.execute(query_add_ai_medium_stats)
            connection.commit()
            query_add_ai_hard_stats = "INSERT INTO statistics (matches, wins, points, max_points) VALUES (0, 0, 0, 0)"
            cursor.execute(query_add_ai_hard_stats)
            connection.commit()

        cursor.close()
        connection.close()

    def start_game(self):
        from src.game_classes.Game import Game
        self.game = Game(self)  # mamy użytkowników i ekrany, więc git
        self.show_game_window()  # tutaj też tworzymy gameWindow
        self.game.start_game()  # start
        self.game_window.draw_letters()

        """# WERSJA 2 <- gameWindow
        self.game = Game(self.game_window)
        self.game.start_game()"""


application = QApplication(sys.argv)
widget = QStackedWidget()
widget.showFullScreen()
window = WindowManager()
widget.show()

sys.exit(application.exec())
