"""
package gui

THIS FILE CREATES ACCESSIBLE PACKAGE

"""

from .welcome_window import WelcomeWindow as welcome_window
from .menu_window import MenuWindow as menu_window
from .game.game_window import GameWindow as game_window
from .game.game_setting_window import GameSettingWindow as game_setting_window
from .settings_window import SettingsWindow as settings_window
from .accounts.account_window import AccountWindow as account_window
from .accounts.login_window import LoginWindow as login_window
from .accounts.register_window import RegisterWindow as register_window
from .accounts.change_password_window import ChangePasswordWindow as change_password_window
from .accounts.delete_account_window import DeleteAccountWindow as delete_account_window
from .accounts.statistics_window import StatisticsWindow as statistics_window
from .accounts.LoggedUser import LoggedUser
