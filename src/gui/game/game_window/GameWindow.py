import json

from PyQt5.QtGui import QBrush, QImage
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi


# TODO
class GameWindow(QMainWindow):

    def __init__(self):
        super(GameWindow, self).__init__()
        loadUi("src/gui/game/game_window/game_window.ui", self)

        self.buttonResign.clicked.connect(self.close)
        self.buttonEndTurn.clicked.connect(self.end_turn)
        self.settings = self.load_data()

        self.set_tables()  # tableWidgets overall properties
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

    def set_tables(self):
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

    def create_board(self):
        path_empty = "res/board/" + self.settings["boardAppearance"] + "/empty_field.png"
        path_star = "res/board/" + self.settings["boardAppearance"] + "/star.png"
        path_double_letter = "res/board/" + self.settings["boardAppearance"] + "/double_letter.png"
        path_double_word = "res/board/" + self.settings["boardAppearance"] + "/double_word.png"
        path_triple_letter ="res/board/" + self.settings["boardAppearance"] + "/triple_letter.png"
        path_triple_word = "res/board/" + self.settings["boardAppearance"] + "/triple_word.png"
        self.board = [None]*15
        for i in range(0, 15):
            self.board[i] = [None]*15
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
                else:
                    self.board[i][j] = path_empty

    def display_data(self):
        for i in range(0, 15):
            for j in range(0, 15):
                item = QTableWidgetItem()
                image = QImage(self.board[i][j])
                brush = QBrush(image)
                item.setBackground(brush)
                self.tableBoardArea.setItem(i, j, item)

        letters = ["a", "b", "c", "d", "e", "f", "g"]  # TODO <- wywalic, odniesc do plytek na rece gracza
        for i in range(0,7):
            item = QTableWidgetItem()
            letter_path = "res/letters/" + self.settings["tileAppearance"] + "/" + (letters[i]).upper() + ".png"  # TODO <- o tutaj
            image = QImage(letter_path)
            brush = QBrush(image)
            item.setBackground(brush)
            self.tableTilesArea.setItem(0, i, item)

    def end_turn(self):
        #if action_correct:
        #continue
        #else:
        print('restore view')


