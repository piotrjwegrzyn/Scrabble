from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class GamePlayer:
    def __init__(self, playerName):
        self.real_player = True
        self.id = None
        self.difficulty = None
        self.name = playerName


class GameSettingWindow(QMainWindow):

    def __init__(self):
        super(GameSettingWindow, self).__init__()
        loadUi("src/gui/game/game_setting_window/game_setting_window.ui", self)

        self.buttonBack.clicked.connect(self.close)
        self.buttonGame.clicked.connect(self.close)  # TODO self.gramy()

        self.player1 = None
        self.player2 = None
        self.player3 = None
        self.player4 = None

        self.hide_everything()
        self.show_p1()
        self.show_p2()
        self.comboBoxPlayerCount.currentIndexChanged.connect(self.show_players)
        self.set_buttons_actions()

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
        #self.set_p2_buttons()
        #self.set_p3_buttons()
        #self.set_p4_buttons()

    # General function to call p1 elements
    def set_p1_buttons(self):
        self.buttonGameP1.clicked.connect(self.change_p1)
        self.buttonLoginP1.clicked.connect(self.login_p1)
        self.buttonLogoutP1.clicked.connect(self.logout_p1)
        self.comboBoxAiDifficulty1.currentIndexChanged.connect(self.change_ai_1)

    # 4 functions actually doing sth
    def change_p1(self):
        if self.player1.real_player:
            self.player1.real_player = False
            self.player1.difficulty = 1
            self.player1.id = None
            self.player1.name = "Komputer1"  # TODO - pozmieniac nazwy (jak beda nudy) xD (moze jakies losowe z jakiejs listy)
            # TODO ^ albo po prostu zostawic mozliwosc wpisania uzytkownikowi (show_p1 -> else -> set true)
        else:
            self.player1.real_player = True
            self.player1.difficulty = None
            self.player1.id = None
            self.player1.name = "Gracz1"
        self.show_p1()

    def login_p1(self):
        # TODO -> mini-okno do logowania
        # if login_success
        self.player1.id = 10  # TODO pobrac z mini-okna
        # self.player1.name =  #TODO pobrac z mini-okna
        self.enterNameP1.setEnabled(False)
        # else jakis warning screen <- nieudana operacja czy cosiek
        self.show_p1()

    def logout_p1(self):
        self.player1.id = None
        self.enterNameP1.setEnabled(True)
        self.show_p1()

    def change_ai_1(self):
        index = self.comboBoxAiDifficulty1.currentIndex()
        self.player1.difficulty = index
        self.show_p1()

    # TODO
    # Pozmieniac po finalnym ogarniaciu p1 -> aktualna wersja -> za stara xD, ale chyba bez bledow uniemozliwiajacych odpalenie
    # odkementowujac """ ponizej odkomentuj tez w set_buttons_actions()
    """
    # General function to call p2 elements
    def set_p2_buttons(self):
        self.buttonGameP2.clicked.connect(self.change_p2)
        self.buttonLoginP2.clicked.connect(self.login_p2)
        self.buttonLogoutP2.clicked.connect(self.logout_p2)
        self.comboBoxAiDifficulty2.currentIndexChanged.connect(self.change_ai_2)

    # 4 functions actually doing sth
    def change_p2(self):
        if self.player2.real_player:
            self.player2.real_player = False
            self.player2.difficulty = 1
            self.player2.id = None
            self.player2.name = "Komputer2"  # TODO - pozmieniac nazwy (jak beda nudy) xD
        else:
            self.player2.real_player = True
            self.player2.difficulty = None
            self.player2.id = None
            self.player2.name = "Gracz2"
        self.show_p2()
    def login_p2(self):
        # TODO -> mini-okno do logowania
        # if login_success
        self.player2.id = 10  # TODO pobrac z mini-okna
        # else jakis warning screen <- nieudana operacja czy cos
        self.show_p2()
    def logout_p2(self):
        self.player2.id = None
        self.show_p2()
    def change_ai_2(self):
        index = self.comboBoxAiDifficulty2.currentIndex()
        self.player2.difficulty = index
        self.show_p2()

    # General function to call p3 elements
    def set_p3_buttons(self):
        self.buttonGameP3.clicked.connect(self.change_p3)
        self.buttonLoginP3.clicked.connect(self.login_p3)
        self.buttonLogoutP3.clicked.connect(self.logout_p3)
        self.comboBoxAiDifficulty3.currentIndexChanged.connect(self.change_ai_3)

    # 4 functions actually doing sth
    def change_p3(self):
        if self.player3.real_player:
            self.player3.real_player = False
            self.player3.difficulty = 1
            self.player3.id = None
            self.player3.name = "Komputer3"  # TODO - pozmieniac nazwy (jak beda nudy) xD
        else:
            self.player3.real_player = True
            self.player3.difficulty = None
            self.player3.id = None
            self.player3.name = "Gracz3"
        self.show_p3()
    def login_p3(self):
        # TODO -> mini-okno do logowania
        # if login_success
        self.player3.id = 10  # TODO pobrac z mini-okna
        # else jakis warning screen <- nieudana operacja czy cos
        self.show_p3()
    def logout_p3(self):
        self.player3.id = None
        self.show_p3()
    def change_ai_3(self):
        index = self.comboBoxAiDifficulty3.currentIndex()
        self.player3.difficulty = index
        self.show_p3()

    # General function to call p4 elements
    def set_p4_buttons(self):
        self.buttonGameP4.clicked.connect(self.change_p4)
        self.buttonLoginP4.clicked.connect(self.login_p4)
        self.buttonLogoutP4.clicked.connect(self.logout_p4)
        self.comboBoxAiDifficulty4.currentIndexChanged.connect(self.change_ai_4)

    # 4 functions actually doing sth
    def change_p4(self):
        if self.player4.real_player:
            self.player4.real_player = False
            self.player4.difficulty = 1
            self.player4.id = None
            self.player4.name = "Komputer4"
        else:
            self.player4.real_player = True
            self.player4.difficulty = None
            self.player4.id = None
            self.player4.name = "Gracz4"
        self.show_p4()
    def login_p4(self):
        # if login_success
        self.player4.id = 10  # TODO pobrac z mini-okna
        # else jakis warning screen <- nieudana operacja czy cos
        self.show_p4()
    def logout_p4(self):
        self.player4.id = None
        self.show_p4()
    def change_ai_4(self):
        index = self.comboBoxAiDifficulty4.currentIndex()
        self.player4.difficulty = index
        self.show_p4()
    """

    # Functions to show/hide game players
    def show_p1(self):
        if self.player1 is None:
            self.player1 = GamePlayer("Gracz1")
        if self.player1.real_player:
            self.buttonGameP1.setText("Gracz")
            if self.player1.id is None:
                self.buttonLoginP1.setVisible(True)
                self.buttonLogoutP1.setVisible(False)
            else:
                self.buttonLoginP1.setVisible(False)
                self.buttonLogoutP1.setVisible(True)
            self.comboBoxAiDifficulty1.setVisible(False)
        else:
            self.buttonGameP1.setText("Komputer")
            self.buttonLoginP1.setVisible(False)
            self.buttonLogoutP1.setVisible(False)
            self.comboBoxAiDifficulty1.setCurrentIndex(self.player1.difficulty-1)
            self.comboBoxAiDifficulty1.setVisible(True)
            self.enterNameP1.setEnabled(True)
        self.buttonGameP1.setVisible(True)
        self.enterNameP1.setVisible(True)
        self.enterNameP1.setText(self.player1.name)

    def show_p2(self):
        if self.player2 is None:
            self.player2 = GamePlayer("Gracz2")
        if self.player2.real_player:
            self.buttonGameP2.setText("Gracz")
            if self.player2.id is None:
                self.buttonLoginP2.setVisible(True)
                self.buttonLogoutP2.setVisible(False)
            else:
                self.buttonLoginP2.setVisible(False)
                self.buttonLogoutP2.setVisible(True)
            self.comboBoxAiDifficulty2.setVisible(False)
        else:
            self.buttonGameP2.setText("Komputer")
            self.buttonLoginP2.setVisible(False)
            self.buttonLogoutP2.setVisible(False)
            self.comboBoxAiDifficulty2.setVisible(True)
        self.buttonGameP2.setVisible(True)
        self.enterNameP2.setVisible(True)
        self.enterNameP2.setText(self.player2.name)

    def show_p3(self):
        if self.player3 is None:
            self.player3 = GamePlayer("Gracz3")
        if self.player3.real_player:
            self.buttonGameP3.setText("Gracz")
            if self.player3.id is None:
                self.buttonLoginP3.setVisible(True)
                self.buttonLogoutP3.setVisible(False)
            else:
                self.buttonLoginP3.setVisible(False)
                self.buttonLogoutP3.setVisible(True)
            self.comboBoxAiDifficulty3.setVisible(False)
        else:
            self.buttonGameP3.setText("Komputer")
            self.buttonLoginP3.setVisible(False)
            self.buttonLogoutP3.setVisible(False)
            self.comboBoxAiDifficulty3.setVisible(True)
        self.buttonGameP3.setVisible(True)
        self.enterNameP3.setVisible(True)
        self.enterNameP3.setText(self.player3.name)

    def show_p4(self):
        if self.player4 is None:
            self.player4 = GamePlayer("Gracz3")
        if self.player4.real_player:
            self.buttonGameP4.setText("Gracz")
            if self.player4.id is None:
                self.buttonLoginP4.setVisible(True)
                self.buttonLogoutP4.setVisible(False)
            else:
                self.buttonLoginP4.setVisible(False)
                self.buttonLogoutP4.setVisible(True)
            self.comboBoxAiDifficulty4.setVisible(False)
        else:
            self.buttonGameP4.setText("Komputer")
            self.buttonLoginP4.setVisible(False)
            self.buttonLogoutP4.setVisible(False)
            self.comboBoxAiDifficulty4.setVisible(True)
        self.buttonGameP4.setVisible(True)
        self.enterNameP4.setVisible(True)
        self.enterNameP4.setText(self.player4.name)

    def hide_p3(self):
        if self.player3 is not None:
            self.player3 = None
        self.buttonGameP3.setVisible(False)
        self.buttonLoginP3.setVisible(False)
        self.comboBoxAiDifficulty3.setVisible(False)
        self.enterNameP3.setVisible(False)

    def hide_p4(self):
        if self.player4 is not None:
            self.player4 = None
        self.buttonGameP4.setVisible(False)
        self.buttonLoginP4.setVisible(False)
        self.comboBoxAiDifficulty4.setVisible(False)
        self.enterNameP4.setVisible(False)

