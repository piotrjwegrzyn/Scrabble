import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QTableWidgetItem, QDialog
from PyQt5.uic import loadUi


class MiniStatisticsWindow(QDialog):

    def __init__(self, players):
        super(MiniStatisticsWindow, self).__init__()
        loadUi('src/gui/accounts/statistics/mini_statistics_window/mini_statistics_window.ui', self)

        self.buttonBack.clicked.connect(self.close)
        self.players = players

        self.update_database()
        self.set_table()
        self.set_table_data()
        self.table.setSortingEnabled(True)
        self.table.sortItems(1, Qt.DescendingOrder)

    def set_table(self):
        self.table.setRowCount(len(self.players))

        self.table.setFont(QFont("MS Shell Dlg 2", 14))  # Cells properties
        self.table.horizontalHeader().setStyleSheet("QHeaderView")
        self.table.verticalHeader().setStyleSheet("QHeaderView")
        self.table.horizontalHeader().setFont(QFont("MS Shell Dlg 2", 22, QFont.Bold))
        self.table.verticalHeader().setFont(QFont("MS Shell Dlg 2", 22, QFont.Bold))

        for i in range(0, 4):
            self.table.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        for i in range(0, len(self.players)):
            self.table.verticalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

    def set_table_data(self):
        row = 0
        for player in self.players:
            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, player.name)
            self.table.setItem(row, 0, item)

            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, player.game_score)
            self.table.setItem(row, 1, item)

            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, player.theoretical_score)
            self.table.setItem(row, 2, item)

            item = QTableWidgetItem()
            if player.theoretical_score != 0:
                ratio = player.game_score / player.theoretical_score * 100
            else:
                ratio = 0
            item.setData(Qt.DisplayRole, ratio)
            self.table.setItem(row, 3, item)
            row = row + 1

    def update_database(self):
        bestScore = 0
        for player in self.players:
            bestScore = max(bestScore, player.game_score)
        for player in self.players:
            if player.id is not None:
                connection = sqlite3.connect('data/Accounts_Statistics.db')
                cursor = connection.cursor()
                if player.game_score == bestScore:
                    query_update_user = "UPDATE statistics SET matches=matches+1, wins=wins+1, points=points+'{1}'," \
                                        "max_points=max_points+'{2}' WHERE ID='{0}'".format(player.id, player.game_score,
                                                                                            player.theoretical_score)
                else:
                    query_update_user = "UPDATE statistics SET matches=matches+1, points=points+'{1}'," \
                                        " max_points=max_points+'{2}' WHERE ID='{0}'".format(player.id, player.game_score,
                                                                                             player.theoretical_score)
                cursor.execute(query_update_user)
                connection.commit()
                cursor.close()
                connection.close()
