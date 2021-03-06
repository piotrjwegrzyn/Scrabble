import json
import math

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QColor, QPainter, QBrush
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi

from src.game_classes.Data import Data
from src.game_classes.GamePlayers import GamePlayers
from src.game_classes.PlayerHuman import PlayerHuman
from ...accounts.statistics.mini_statistics_window.MiniStatisticsWindow import MiniStatisticsWindow


class GameWindow(QMainWindow):

    def __init__(self):
        super(GameWindow, self).__init__()
        loadUi("src/gui/game/game_window/game_window.ui", self)
        self.buttonResign.clicked.connect(self.resign)
        self.buttonResetTurn.clicked.connect(self.reset)

        self.settings = self.load_data()
        self.players = GamePlayers.get_instances()
        self.backupItems = []
        self.miniStatistics = None
        self.draggedTileIdx = None

        self.allTilesToExchange = []
        self.allDraggedTiles = []

        self.initialize_tables_labels()  # tableWidgets overall properties

    @staticmethod
    def load_data():
        try:
            with open('data/settings.json', 'r') as f:
                settings = json.load(f)
        except:
            settings = {"tileAppearance": "set_1", "boardAppearance": "set_1", "sortingOrder": "Alfabetycznie"}
            print('error occurred, cannot load data, restoring default values')
        return settings

    def set_board_drop_event(self, event):
        # event.pos()
        x_idx = self.tableBoardArea.columnAt(event.pos().x())
        y_idx = self.tableBoardArea.rowAt(event.pos().y())

        try:
            # copy item <- to tableBoardArea
            tileItem = self.tableTilesArea.item(0, self.draggedTileIdx)  # tile
            item = tileItem.clone()

            # set item on board
            self.tableBoardArea.setItem(y_idx, x_idx, item)

            # delete item <- from tableTilesArea
            self.tableTilesArea.takeItem(0, self.draggedTileIdx)  # tile
            self.allDraggedTiles.append([self.draggedTileIdx, y_idx, x_idx])
        except:
            print("This item no longer exists")
        self.draggedTileIdx = None

    def set_tiles_drag_event(self, event):
        idx = math.floor(event.pos().x()/102)
        self.draggedTileIdx = idx

    def display_data(self):
        self.draw_board()
        self.draw_letters()
        self.draw_labels()
        self.draw_buttons()

    def draw_board(self):
        board = Data.instance().board_pools
        board_paths = self.create_board_paths(board)
        for i in range(0, 15):
            for j in range(0, 15):
                item = QTableWidgetItem()
                item.setData(Qt.DecorationRole, QPixmap(board_paths[i][j]))
                self.tableBoardArea.setItem(j, i, item)

    def create_board_paths(self, board):
        path_empty = "res/board/" + self.settings["boardAppearance"] + "/empty_field.png"
        path_star = "res/board/" + self.settings["boardAppearance"] + "/star.png"
        path_double_letter = "res/board/" + self.settings["boardAppearance"] + "/double_letter.png"
        path_double_word = "res/board/" + self.settings["boardAppearance"] + "/double_word.png"
        path_triple_letter = "res/board/" + self.settings["boardAppearance"] + "/triple_letter.png"
        path_triple_word = "res/board/" + self.settings["boardAppearance"] + "/triple_word.png"
        paths = [None]*15
        for i in range(0, 15):
            paths[i] = [None]*15
        for i in range(0, 15):
            for j in range(0, 15):
                if board[i][j] != '':
                    paths[i][j] = "res/letters/" + self.settings["tileAppearance"] + "/" + board[i][j] + ".png"
                else:
                    if i == 7 and j == 7:
                        paths[i][j] = path_star
                    elif i % 7 == 0 and j % 7 == 0:
                        paths[i][j] = path_triple_word
                    elif ((i == 3 or i == 11) and j % 14 == 0) or ((j == 3 or j == 11) and i % 14 == 0):
                        paths[i][j] = path_double_letter
                    elif (i % 4 == 1 and j % 4 == 1) and not (
                            i == j == 1 or i == j == 13 or (i == 1 and j == 13) or (i == 13 and j == 1)):
                        paths[i][j] = path_triple_letter
                    elif (i == 6 or i == 8) and (j == 6 or j == 8):
                        paths[i][j] = path_double_letter
                    else:
                        paths[i][j] = path_empty
        for i in range(1, 5):
            if board[i][i] == '':
                paths[i][i] = path_double_word
            if board[14 - i][i] == '':
                paths[14 - i][i] = path_double_word
            if board[14 - i][14 - i] == '':
                paths[14 - i][14 - i] = path_double_word
            if board[i][14 - i] == '':
                paths[i][14 - i] = path_double_word
        for i in range(6, 8):
            if board[i][i - 4] == '':
                paths[i][i - 4] = path_double_letter
            if board[14 - i][14 - (i - 4)] == '':
                paths[14 - i][14 - (i - 4)] = path_double_letter
            if board[i - 4][i] == '':
                paths[i - 4][i] = path_double_letter
            if board[14 - (i - 4)][14 - i] == '':
                paths[14 - (i - 4)][14 - i] = path_double_letter
        # brakujace 4, bo nie chcialo mi sie juz myslec
        if board[8][2] == '':
            paths[8][2] = path_double_letter
        if board[2][8] == '':
            paths[2][8] = path_double_letter
        if board[12][6] == '':
            paths[12][6] = path_double_letter
        if board[6][12] == '':
            paths[6][12] = path_double_letter
        return paths

    def draw_letters(self):
        for i in range(0, len(self.players[0].player_pool)):
            item = QTableWidgetItem()
            letterPath = "res/letters/" + self.settings["tileAppearance"] + "/" + (
                self.players[0].player_pool[i]).upper() + ".png"
            item.setData(Qt.DecorationRole, QPixmap(letterPath))
            self.tableTilesArea.setItem(0, i, item)

    def draw_labels(self):
        players = GamePlayers.get_instances()
        self.labelCurrentPlayer.setText(players[0].name)
        if len(players) == 2:
            self.labelOppositePlayer.setText(players[1].name)
        elif len(players) == 3:
            self.labelLeftPlayer.setText(players[1].name)
            self.labelOppositePlayer.setText(players[2].name)
        else:
            self.labelLeftPlayer.setText(players[1].name)
            self.labelOppositePlayer.setText(players[2].name)
            self.labelRightPlayer.setText(players[3].name)

    def initialize_tables_labels(self):
        self.tableBoardArea.dropEvent = self.set_board_drop_event
        self.tableTilesArea.dragEnterEvent = self.set_tiles_drag_event
        self.tableTilesArea.doubleClicked.connect(self.add_to_exchange)

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

    def draw_buttons(self):
        if isinstance(self.players[0], PlayerHuman):
            self.buttonResign.setEnabled(True)
            self.buttonResetTurn.setEnabled(True)
            self.buttonExchange.setEnabled(True)
            self.buttonEndTurn.setEnabled(True)
        else:
            self.buttonResign.setEnabled(False)
            self.buttonResetTurn.setEnabled(False)
            self.buttonExchange.setEnabled(False)
            self.buttonEndTurn.setEnabled(False)

    def add_to_exchange(self):
        index = self.tableTilesArea.currentColumn()
        if index in self.allTilesToExchange:
            self.allTilesToExchange.remove(index)
            try:
                for (storedIndex, storedItem) in self.backupItems:
                    if storedIndex == index:
                        self.tableTilesArea.setItem(0, index, storedItem)
                        self.backupItems.remove([storedIndex, storedItem])
            except:
                print("Error restoring item")
        else:
            self.allTilesToExchange.append(index)
            try:
                item = self.tableTilesArea.item(0, index)
                self.backupItems.append([index, item.clone()])
                pixmap = item.data(Qt.DecorationRole)

                painter = QPainter(pixmap)
                painter.fillRect(QRect(0, 0, pixmap.width(), pixmap.height()), QBrush(QColor(0, 0, 0, 80)))
                painter.end()

                item.setData(Qt.DecorationRole, pixmap)
                self.tableTilesArea.setItem(0, index, item)
            except:
                print("You can't exchange non-existent letter")

    # po zako??czeniu gry
    def display_statistics(self):
        self.buttonResign.setEnabled(True)
        self.miniStatistics = MiniStatisticsWindow(self.players)
        self.miniStatistics.show()
        self.miniStatistics.buttonBack.clicked.connect(self.buttonResign.click)

    def reset(self):
        self.reset_values_to_default()
        self.display_data()

    def reset_values_to_default(self):
        self.backupItems = []
        self.allDraggedTiles = []
        self.allTilesToExchange = []
        self.draggedTileIdx = None

    def resign(self):
        GamePlayers.delete_instances()
        # Data.reset()
        self.close()

    def get_dropped_tiles(self):
        return self.allDraggedTiles

    def get_tiles_to_exchange(self):
        return self.allTilesToExchange
