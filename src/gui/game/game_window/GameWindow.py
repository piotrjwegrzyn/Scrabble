import json

from PyQt5.QtGui import QBrush, QImage
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi

from ..GamePlayers import GamePlayers
from ...accounts.statistics.mini_statistics_window.MiniStatisticsWindow import MiniStatisticsWindow


class GameWindow(QMainWindow):

    def __init__(self):
        super(GameWindow, self).__init__()
        loadUi("src/gui/game/game_window/game_window.ui", self)

        self.buttonResign.clicked.connect(self.resign)
        self.buttonEndTurn.clicked.connect(self.end_turn)
        self.settings = self.load_data()

        self.players = GamePlayers.get_instances()
        self.board = None
        self.miniStatistics = None

        self.initialize_tables_labels()  # tableWidgets overall properties
        self.create_board()  # board consists of paths to images that are currently on board
        self.display_data()  # display actual images on screen

    @staticmethod
    def load_data():
        try:
            with open('data/settings.json', 'r') as f:
                settings = json.load(f)
        except:
            settings = {"tileAppearance": "set_1", "boardAppearance": "set_1", "sortingOrder": "Alfabetycznie"}
            print('error occurred, cannot load data, restoring default values')
        return settings

    def initialize_tables_labels(self):
        self.tableBoardArea.setAcceptDrops(True)
        self.tableBoardArea.setDragEnabled(False)
        self.tableTilesArea.setAcceptDrops(True)
        self.tableTilesArea.setDragEnabled(True)

        for i in range(0, 15):
            self.tableBoardArea.setColumnWidth(i, 102)
            self.tableBoardArea.setRowHeight(i, 102)
        for i in range(0, 7):
            self.tableTilesArea.setColumnWidth(i, 102)
            self.tableTilesArea.setRowHeight(i, 102)

        if len(self.players) == 2:
            self.labelLeftPlayer.setHidden(True)
            self.labelRightPlayer.setHidden(True)
        elif len(self.players) == 3:
            self.labelLeftPlayer.setHidden(False)
            self.labelRightPlayer.setHidden(True)
        else:
            self.labelLeftPlayer.setHidden(False)
            self.labelRightPlayer.setHidden(False)


    def create_board(self):
        path_empty = "res/board/" + self.settings["boardAppearance"] + "/empty_field.png"
        path_star = "res/board/" + self.settings["boardAppearance"] + "/star.png"
        path_double_letter = "res/board/" + self.settings["boardAppearance"] + "/double_letter.png"
        path_double_word = "res/board/" + self.settings["boardAppearance"] + "/double_word.png"
        path_triple_letter = "res/board/" + self.settings["boardAppearance"] + "/triple_letter.png"
        path_triple_word = "res/board/" + self.settings["boardAppearance"] + "/triple_word.png"
        self.board = [None] * 15
        for i in range(0, 15):
            self.board[i] = [None] * 15
            for j in range(0, 15):
                self.board[i][j] = [None]
        for i in range(0, 15):
            for j in range(0, 15):
                if i == 7 and j == 7:
                    self.board[i][j] = path_star
                elif i % 7 == 0 and j % 7 == 0:
                    self.board[i][j] = path_triple_word
                elif ((i == 3 or i == 11) and j % 14 == 0) or ((j == 3 or j == 11) and i % 14 == 0):
                    self.board[i][j] = path_double_letter
                elif (i % 4 == 1 and j % 4 == 1) and not (
                        i == j == 1 or i == j == 13 or (i == 1 and j == 13) or (i == 13 and j == 1)):
                    self.board[i][j] = path_triple_letter
                elif (i == 6 or i == 8) and (j == 6 or j == 8):
                    self.board[i][j] = path_double_letter
                else:
                    self.board[i][j] = path_empty

        for i in range(1, 5):
            self.board[i][i] = path_double_word
            self.board[14 - i][i] = path_double_word
            self.board[14 - i][14 - i] = path_double_word
            self.board[i][14 - i] = path_double_word
        # 8 pol z 5linijek, niby szybciej, ale mozna bylo dac recznie
        for i in range(6, 8):
            self.board[i][i - 4] = path_double_letter
            self.board[14 - i][14 - (i - 4)] = path_double_letter
            self.board[i - 4][i] = path_double_letter
            self.board[14 - (i - 4)][14 - i] = path_double_letter
        # brakujace 4, bo nie chcialo mi sie juz myslec
        self.board[8][2] = path_double_letter
        self.board[2][8] = path_double_letter
        self.board[12][6] = path_double_letter
        self.board[6][12] = path_double_letter

    def display_data(self):
        self.display_board()
        self.display_letters()
        self.display_labels()

    def display_board(self):
        for i in range(0, 15):
            for j in range(0, 15):
                item = QTableWidgetItem()
                image = QImage(self.board[i][j])
                brush = QBrush(image)
                item.setBackground(brush)
                self.tableBoardArea.setItem(i, j, item)

    def display_letters(self):
        for i in range(0, 7):
            item = QTableWidgetItem()
            letter_path = "res/letters/" + self.settings["tileAppearance"] + "/" + (
                self.players[0].letters[i]).upper() + ".png"
            image = QImage(letter_path)
            brush = QBrush(image)
            item.setBackground(brush)
            self.tableTilesArea.setItem(0, i, item)

    def display_labels(self):
        self.labelCurrentPlayer.setText(self.players[0].name)
        if len(self.players) == 2:
            self.labelOppositePlayer.setText(self.players[1].name)
        elif len(self.players) == 3:
            self.labelLeftPlayer.setText(self.players[1].name)
            self.labelOppositePlayer.setText(self.players[2].name)
        else:
            self.labelLeftPlayer.setText(self.players[1].name)
            self.labelOppositePlayer.setText(self.players[2].name)
            self.labelRightPlayer.setText(self.players[3].name)

    def end_turn(self):
        self.players.append(self.players.pop(0))
        print('check view')
        self.display_data()  ### Do testów

    # po zakończeniu gry
    def display_statistics(self):
        self.miniStatistics = MiniStatisticsWindow(self.players)
        self.miniStatistics.show()
        self.miniStatistics.buttonBack.clicked.connect(self.resign)

    def resign(self):
        GamePlayers.delete_instances()
        self.close()
