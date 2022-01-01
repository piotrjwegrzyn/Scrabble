import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog, QTableWidget
from PyQt5.uic import loadUi


class MiniStatisticsWindow(QDialog):

    def __init__(self, players):
        super(MiniStatisticsWindow, self).__init__()
        loadUi('src/gui/accounts/statistics/mini_statistics_window/mini_statistics_window.ui', self)

        self.buttonBack.clicked.connect(self.close)
        self.players = players

        self.set_columns()
        self.set_table_data()
        self.table.setSortingEnabled(True)
        self.table.sortItems(1)

    def set_columns(self):
        self.table.setRowCount(len(self.players))
        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 240)
        self.table.setColumnWidth(2, 240)
        self.table.setColumnWidth(3, 350)
        for i in range(0, 4):
            self.table.setRowHeight(i, 25)

    def set_table_data(self):
        row = 0
        for player in self.players:
            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, player.name)
            self.table.setItem(row, 0, item)

            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, player.score)
            self.table.setItem(row, 1, item)

            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, player.theoreticalScore)
            self.table.setItem(row, 2, item)

            item = QTableWidgetItem()
            ratio = 10
            item.setData(Qt.DisplayRole, ratio)
            self.table.setItem(row, 3, item)
            row = row + 1
