import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget

import gui


class WindowManager(QMainWindow):
    def __init__(self):
        super(WindowManager, self).__init__()

        self.mainWindow = gui.main_window.MainWindow()
        self.gameSettingWindow = None
        self.accountsStatsWindow = None
        self.settingsWindow = None
        self.set_menu_buttons()

    def set_menu_buttons(self):
        self.mainWindow.buttonGameSetting.clicked.connect(self.goto_game_setting)
        self.mainWindow.buttonAccounts.clicked.connect(self.goto_accounts)
        self.mainWindow.buttonSettings.clicked.connect(self.goto_settings)
        self.mainWindow.buttonExit.clicked.connect(widget.close)

    def goto_game_setting(self):
        print('a')

    def goto_accounts(self):
        self.mainWindow.hide()
        if self.accountsStatsWindow is None:
            self.accountsStatsWindow = gui.accounts_window.AccountsWindow()
            self.accountsStatsWindow.loginWindow = None
            self.accountsStatsWindow.registerWindow = None
            self.accountsStatsWindow.deleteWindow = None
            self.accountsStatsWindow.statisticsWindow = None
        self.set_accounts_stats_buttons()
        widget.addWidget(self.accountsStatsWindow)
        self.accountsStatsWindow.show()

    def set_accounts_stats_buttons(self):
        self.accountsStatsWindow.buttonLogin.clicked.connect(self.goto_login)
        self.accountsStatsWindow.buttonRegister.clicked.connect(self.goto_register)
        self.accountsStatsWindow.buttonDeleteAccount.clicked.connect(self.goto_delete)
        self.accountsStatsWindow.buttonStatistics.clicked.connect(self.goto_statistics)
        self.accountsStatsWindow.buttonBack.clicked.connect(self.mainWindow.show)

    def goto_login(self):
        self.accountsStatsWindow.hide()
        if self.accountsStatsWindow.loginWindow is None:
            self.accountsStatsWindow.loginWindow = gui.login_window.LoginWindow()
        self.accountsStatsWindow.loginWindow.buttonBack.clicked.connect(self.accountsStatsWindow.show)
        widget.addWidget(self.accountsStatsWindow.loginWindow)
        self.accountsStatsWindow.loginWindow.show()

    def goto_register(self):
        self.accountsStatsWindow.hide()
        if self.accountsStatsWindow.registerWindow is None:
            self.accountsStatsWindow.registerWindow = gui.register_window.RegisterWindow()
        self.accountsStatsWindow.registerWindow.buttonBack.clicked.connect(self.accountsStatsWindow.show)
        widget.addWidget(self.accountsStatsWindow.registerWindow)
        self.accountsStatsWindow.registerWindow.show()

    def goto_delete(self):
        self.accountsStatsWindow.hide()
        if self.accountsStatsWindow.deleteWindow is None:
            self.accountsStatsWindow.deleteWindow = gui.delete_window.DeleteWindow()
        self.accountsStatsWindow.deleteWindow.buttonBack.clicked.connect(self.accountsStatsWindow.show)
        widget.addWidget(self.accountsStatsWindow.deleteWindow)
        self.accountsStatsWindow.deleteWindow.show()

    def goto_statistics(self):
        print('stats')

    def goto_settings(self):
        self.mainWindow.hide()
        if self.settingsWindow is None:
            self.settingsWindow = gui.settings_window.SettingsWindow()
        self.settingsWindow.buttonConfirm.clicked.connect(self.mainWindow.show)
        self.settingsWindow.buttonCancel.clicked.connect(self.mainWindow.show)
        widget.addWidget(self.settingsWindow)
        self.settingsWindow.show()


application = QApplication(sys.argv)
widget = QStackedWidget()
window = WindowManager()
widget.addWidget(window.mainWindow)
widget.setMinimumWidth(800)
widget.setMinimumHeight(600)

widget.show()

sys.exit(application.exec())
