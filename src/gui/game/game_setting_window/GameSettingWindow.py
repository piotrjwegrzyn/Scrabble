from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from src.game_classes.PlayerHuman import PlayerHuman
from src.game_classes.Data import Data
from ...accounts.LoggedUser import LoggedUser
from ...accounts.login.mini_login_window.MiniLoginWindow import MiniLoginWindow
from src.game_classes.GamePlayers import GamePlayers


class GameSettingWindow(QMainWindow):

    def __init__(self):
        super(GameSettingWindow, self).__init__()
        loadUi("src/gui/game/game_setting_window/game_setting_window.ui", self)

        self.buttonBack.clicked.connect(self.close)
        self.buttonGame.clicked.connect(self.go_to_game)

        self.miniLogin = None
        self.player1 = None
        self.player2 = None
        self.player3 = None
        self.player4 = None
        self.logged = ""

        self.hide_everything()
        self.set_buttons_actions()
        self.show_p1()
        self.show_p2()
        self.comboBoxPlayerCount.currentIndexChanged.connect(self.show_players)

    def hide_everything(self):
        self.buttonGameP1.setVisible(False)
        self.buttonLoginP1.setVisible(False)
        self.buttonLogoutP1.setVisible(False)
        self.comboBoxAiDifficulty1.setVisible(False)
        self.enterNameP1.setVisible(False)

        self.buttonGameP2.setVisible(False)
        self.buttonLoginP2.setVisible(False)
        self.buttonLogoutP2.setVisible(False)
        self.comboBoxAiDifficulty2.setVisible(False)
        self.enterNameP2.setVisible(False)

        self.buttonGameP3.setVisible(False)
        self.buttonLoginP3.setVisible(False)
        self.buttonLogoutP3.setVisible(False)
        self.comboBoxAiDifficulty3.setVisible(False)
        self.enterNameP3.setVisible(False)

        self.buttonGameP4.setVisible(False)
        self.buttonLoginP4.setVisible(False)
        self.buttonLogoutP4.setVisible(False)
        self.comboBoxAiDifficulty4.setVisible(False)
        self.enterNameP4.setVisible(False)

    def show_players(self):
        index = self.comboBoxPlayerCount.currentIndex()
        self.show_p1()
        self.show_p2()
        if index == 0:
            self.hide_p3()
            self.hide_p4()
        if index == 1:
            self.show_p3()
            self.hide_p4()
        if index == 2:
            self.show_p3()
            self.show_p4()

    def set_buttons_actions(self):
        self.set_p1_buttons()
        self.set_p2_buttons()
        self.set_p3_buttons()
        self.set_p4_buttons()

    # General function to call p1 elements
    def set_p1_buttons(self):
        self.buttonGameP1.clicked.connect(self.change_p1)
        self.buttonLoginP1.clicked.connect(self.login_p1)
        self.buttonLogoutP1.clicked.connect(self.logout_p1)
        self.comboBoxAiDifficulty1.currentIndexChanged.connect(self.change_ai_1)

    # 4 functions actually doing sth
    def change_p1(self):
        if isinstance(self.player1, PlayerHuman):
            GamePlayers.delete_instance(self.player1)
            GamePlayers("Komputer 1", "AI")
            self.player1 = GamePlayers.get_instance("AI Komputer 1")
        else:
            GamePlayers.delete_instance(self.player1)
            GamePlayers("Gracz 1", "Human")
            self.player1 = GamePlayers.get_instance("Gracz 1")
        self.show_p1()

    def login_p1(self):
        if self.logged == "":
            self.player1.id = LoggedUser.get_instance().uid
            self.player1.name = LoggedUser.get_instance().uname
            self.logged = "loggedSlot1"
        else:
            self.miniLogin = MiniLoginWindow(self.player1)
            self.miniLogin.show()
            self.miniLogin.buttonLogin.clicked.connect(self.show_p1)
        self.show_p1()

    def logout_p1(self):
        if self.logged == "loggedSlot1":
            self.logged = ""
        self.player1.id = None
        self.show_p1()

    def change_ai_1(self):
        index = self.comboBoxAiDifficulty1.currentIndex()
        if index == 0:
            self.player1.level = "Easy"
            self.player1.id = 1
        elif index == 1:
            self.player1.level = "Medium"
            self.player1.id = 2
        else:
            self.player1.level = "Hard"
            self.player1.id = 3
        self.show_p1()

    # General function to call p2 elements
    def set_p2_buttons(self):
        self.buttonGameP2.clicked.connect(self.change_p2)
        self.buttonLoginP2.clicked.connect(self.login_p2)
        self.buttonLogoutP2.clicked.connect(self.logout_p2)
        self.comboBoxAiDifficulty2.currentIndexChanged.connect(self.change_ai_2)

    # 4 functions actually doing sth
    def change_p2(self):
        if isinstance(self.player2, PlayerHuman):
            GamePlayers.delete_instance(self.player2)
            GamePlayers("Komputer 2", "AI")
            self.player2 = GamePlayers.get_instance("AI Komputer 2")
        else:
            GamePlayers.delete_instance(self.player2)
            GamePlayers("Gracz 2", "Human")
            self.player2 = GamePlayers.get_instance("Gracz 2")
        self.show_p2()

    def login_p2(self):
        if self.logged == "":
            self.player2.id = LoggedUser.get_instance().uid
            self.player2.name = LoggedUser.get_instance().uname
            self.logged = "loggedSlot2"
        else:
            self.miniLogin = MiniLoginWindow(self.player2)
            self.miniLogin.show()
            self.miniLogin.buttonLogin.clicked.connect(self.show_p2)
        self.show_p2()

    def logout_p2(self):
        if self.logged == "loggedSlot2":
            self.logged = ""
        self.player2.id = None
        self.show_p2()

    def change_ai_2(self):
        index = self.comboBoxAiDifficulty2.currentIndex()
        if index == 0:
            self.player2.level = "Easy"
            self.player2.id = 1
        elif index == 1:
            self.player2.level = "Medium"
            self.player2.id = 2
        else:
            self.player2.level = "Hard"
            self.player2.id = 3
        self.show_p2()

    # General function to call p3 elements
    def set_p3_buttons(self):
        self.buttonGameP3.clicked.connect(self.change_p3)
        self.buttonLoginP3.clicked.connect(self.login_p3)
        self.buttonLogoutP3.clicked.connect(self.logout_p3)
        self.comboBoxAiDifficulty3.currentIndexChanged.connect(self.change_ai_3)

    # 4 functions actually doing sth
    def change_p3(self):
        if isinstance(self.player3, PlayerHuman):
            GamePlayers.delete_instance(self.player3)
            GamePlayers("Komputer 3", "AI")
            self.player3 = GamePlayers.get_instance("AI Komputer 3")
        else:
            GamePlayers.delete_instance(self.player3)
            GamePlayers("Gracz 3", "Human")
            self.player3 = GamePlayers.get_instance("Gracz 3")
        self.show_p3()

    def login_p3(self):
        if self.logged == "":
            self.player3.id = LoggedUser.get_instance().uid
            self.player3.name = LoggedUser.get_instance().uname
            self.logged = "loggedSlot3"
        else:
            self.miniLogin = MiniLoginWindow(self.player3)
            self.miniLogin.show()
            self.miniLogin.buttonLogin.clicked.connect(self.show_p3)
        self.show_p3()

    def logout_p3(self):
        if self.logged == "loggedSlot3":
            self.logged = ""
        self.player3.id = None
        self.show_p3()

    def change_ai_3(self):
        index = self.comboBoxAiDifficulty3.currentIndex()
        if index == 0:
            self.player3.level = "Easy"
            self.player3.id = 1
        elif index == 1:
            self.player3.level = "Medium"
            self.player3.id = 2
        else:
            self.player3.level = "Hard"
            self.player3.id = 3
        self.show_p3()

    # General function to call p4 elements
    def set_p4_buttons(self):
        self.buttonGameP4.clicked.connect(self.change_p4)
        self.buttonLoginP4.clicked.connect(self.login_p4)
        self.buttonLogoutP4.clicked.connect(self.logout_p4)
        self.comboBoxAiDifficulty4.currentIndexChanged.connect(self.change_ai_4)

    # 4 functions actually doing sth
    def change_p4(self):
        if isinstance(self.player4, PlayerHuman):
            GamePlayers.delete_instance(self.player4)
            GamePlayers("Komputer 4", "AI")
            self.player4 = GamePlayers.get_instance("AI Komputer 4")
        else:
            GamePlayers.delete_instance(self.player4)
            GamePlayers("Gracz 4", "Human")
            self.player4 = GamePlayers.get_instance("Gracz 4")
        self.show_p4()

    def login_p4(self):
        if self.logged == "":
            self.player4.id = LoggedUser.get_instance().uid
            self.player4.name = LoggedUser.get_instance().uname
            self.logged = "loggedSlot4"
        else:
            self.miniLogin = MiniLoginWindow(self.player4)
            self.miniLogin.show()
            self.miniLogin.buttonLogin.clicked.connect(self.show_p4)
        self.show_p4()

    def logout_p4(self):
        if self.logged == "loggedSlot4":
            self.logged = ""
        self.player4.id = None
        self.show_p4()

    def change_ai_4(self):
        index = self.comboBoxAiDifficulty4.currentIndex()
        if index == 0:
            self.player4.level = "Easy"
            self.player4.id = 1
        elif index == 1:
            self.player4.level = "Medium"
            self.player4.id = 2
        else:
            self.player4.level = "Hard"
            self.player4.id = 3
        self.show_p4()

    # Functions to show/hide game players
    def show_p1(self):
        if self.player1 is None:
            GamePlayers("Gracz 1", "Human")
            self.player1 = GamePlayers.get_instance("Gracz 1")
        if isinstance(self.player1, PlayerHuman):
            self.buttonGameP1.setText("Gracz")
            if self.player1.id is None:
                self.buttonGameP1.setEnabled(True)
                self.buttonLoginP1.setVisible(True)
                self.buttonLogoutP1.setVisible(False)
                self.enterNameP1.setEnabled(True)
            else:
                self.buttonGameP1.setEnabled(False)
                self.buttonLoginP1.setVisible(False)
                self.buttonLogoutP1.setVisible(True)
                self.enterNameP1.setEnabled(False)
            self.comboBoxAiDifficulty1.setVisible(False)
        else:
            self.buttonGameP1.setText("Komputer")
            self.buttonLoginP1.setVisible(False)
            self.buttonLogoutP1.setVisible(False)
            if self.player1.level == "Easy":
                self.comboBoxAiDifficulty1.setCurrentIndex(0)
            elif self.player1.level == "Medium":
                self.comboBoxAiDifficulty1.setCurrentIndex(1)
            elif self.player1.level == "Hard":
                self.comboBoxAiDifficulty1.setCurrentIndex(2)
            self.comboBoxAiDifficulty1.setVisible(True)
            self.enterNameP1.setEnabled(True)
        self.buttonGameP1.setVisible(True)
        self.enterNameP1.setVisible(True)
        self.enterNameP1.setText(self.player1.name)

    def show_p2(self):
        if self.player2 is None:
            GamePlayers("Gracz 2", "Human")
            self.player2 = GamePlayers.get_instance("Gracz 2")
        if isinstance(self.player2, PlayerHuman):
            self.buttonGameP2.setText("Gracz")
            if self.player2.id is None:
                self.buttonGameP2.setEnabled(True)
                self.buttonLoginP2.setVisible(True)
                self.buttonLogoutP2.setVisible(False)
                self.enterNameP2.setEnabled(True)
            else:
                self.buttonGameP2.setEnabled(False)
                self.buttonLoginP2.setVisible(False)
                self.buttonLogoutP2.setVisible(True)
                self.enterNameP2.setEnabled(False)
            self.comboBoxAiDifficulty2.setVisible(False)
        else:
            self.buttonGameP2.setText("Komputer")
            self.buttonLoginP2.setVisible(False)
            self.buttonLogoutP2.setVisible(False)
            if self.player2.level == "Easy":
                self.comboBoxAiDifficulty1.setCurrentIndex(0)
            elif self.player2.level == "Medium":
                self.comboBoxAiDifficulty1.setCurrentIndex(1)
            elif self.player2.level == "Hard":
                self.comboBoxAiDifficulty1.setCurrentIndex(2)
            self.comboBoxAiDifficulty2.setVisible(True)
            self.enterNameP2.setEnabled(True)
        self.buttonGameP2.setVisible(True)
        self.enterNameP2.setVisible(True)
        self.enterNameP2.setText(self.player2.name)

    def show_p3(self):
        if self.player3 is None:
            GamePlayers("Gracz 3", "Human")
            self.player3 = GamePlayers.get_instance("Gracz 3")
        if isinstance(self.player3, PlayerHuman):
            self.buttonGameP3.setText("Gracz")
            if self.player3.id is None:
                self.buttonGameP3.setEnabled(True)
                self.buttonLoginP3.setVisible(True)
                self.buttonLogoutP3.setVisible(False)
                self.enterNameP3.setEnabled(True)
            else:
                self.buttonGameP3.setEnabled(False)
                self.buttonLoginP3.setVisible(False)
                self.buttonLogoutP3.setVisible(True)
                self.enterNameP3.setEnabled(False)
            self.comboBoxAiDifficulty3.setVisible(False)
        else:
            self.buttonGameP3.setText("Komputer")
            self.buttonLoginP3.setVisible(False)
            self.buttonLogoutP3.setVisible(False)
            if self.player3.level == "Easy":
                self.comboBoxAiDifficulty1.setCurrentIndex(0)
            elif self.player3.level == "Medium":
                self.comboBoxAiDifficulty1.setCurrentIndex(1)
            elif self.player3.level == "Hard":
                self.comboBoxAiDifficulty1.setCurrentIndex(2)
            self.comboBoxAiDifficulty3.setVisible(True)
            self.enterNameP3.setEnabled(True)
        self.buttonGameP3.setVisible(True)
        self.enterNameP3.setVisible(True)
        self.enterNameP3.setText(self.player3.name)

    def show_p4(self):
        if self.player4 is None:
            GamePlayers("Gracz 4", "Human")
            self.player4 = GamePlayers.get_instance("Gracz 4")
        if isinstance(self.player4, PlayerHuman):
            self.buttonGameP4.setText("Gracz")
            if self.player4.id is None:
                self.buttonGameP4.setEnabled(True)
                self.buttonLoginP4.setVisible(True)
                self.buttonLogoutP4.setVisible(False)
                self.enterNameP4.setEnabled(True)
            else:
                self.buttonGameP4.setEnabled(False)
                self.buttonLoginP4.setVisible(False)
                self.buttonLogoutP4.setVisible(True)
                self.enterNameP4.setEnabled(False)
            self.comboBoxAiDifficulty4.setVisible(False)
        else:
            self.buttonGameP4.setText("Komputer")
            self.buttonLoginP4.setVisible(False)
            self.buttonLogoutP4.setVisible(False)
            if self.player4.level == "Easy":
                self.comboBoxAiDifficulty1.setCurrentIndex(0)
            elif self.player4.level == "Medium":
                self.comboBoxAiDifficulty1.setCurrentIndex(1)
            elif self.player4.level == "Hard":
                self.comboBoxAiDifficulty1.setCurrentIndex(2)
            self.comboBoxAiDifficulty4.setVisible(True)
            self.enterNameP4.setEnabled(True)
        self.buttonGameP4.setVisible(True)
        self.enterNameP4.setVisible(True)
        self.enterNameP4.setText(self.player4.name)

    def hide_p3(self):
        if self.player3 is not None:
            GamePlayers.delete_instance(self.player3)
            self.player3 = None
        self.buttonGameP3.setVisible(False)
        self.buttonLoginP3.setVisible(False)
        self.buttonLogoutP3.setVisible(False)
        self.comboBoxAiDifficulty3.setVisible(False)
        self.enterNameP3.setVisible(False)

    def hide_p4(self):
        if self.player4 is not None:
            GamePlayers.delete_instance(self.player4)
            self.player4 = None
        self.buttonGameP4.setVisible(False)
        self.buttonLoginP4.setVisible(False)
        self.buttonLogoutP4.setVisible(False)
        self.comboBoxAiDifficulty4.setVisible(False)
        self.enterNameP4.setVisible(False)

    def go_to_game(self):
        index = self.comboBoxPlayerCount.currentIndex()
        self.player1.name = self.enterNameP1.text()
        self.player2.name = self.enterNameP2.text()
        if index >= 1:
            self.player3.name = self.enterNameP3.text()
        if index == 2:
            self.player4.name = self.enterNameP4.text()
        Data.players = GamePlayers.get_instances()
        self.close()
