import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi


class StatisticsWindow(QMainWindow):

    def __init__(self):
        super(StatisticsWindow, self).__init__()
        loadUi('src/gui/accounts/statistics/statistics_window/statistics_window.ui', self)

        self.buttonBack.clicked.connect(self.close)

        self.set_tables()
        self.set_table_data()
        self.table.setSortingEnabled(True)
        self.table.sortItems(0)

    def set_tables(self):
        self.table.setFont(QFont("MS Shell Dlg 2", 10))  # Cells properties
        self.table.horizontalHeader().setStyleSheet("QHeaderView")
        self.table.verticalHeader().setStyleSheet("QHeaderView")
        self.table.horizontalHeader().setFont(QFont("MS Shell Dlg 2", 20, QFont.Bold))
        self.table.verticalHeader().setFont(QFont("MS Shell Dlg 2", 20, QFont.Bold))
        for i in range(0, 7):
            self.table.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

    def set_table_data(self):
        connection = sqlite3.connect('data/Accounts_Statistics.db')
        cursor = connection.cursor()
        query_get_users = "SELECT username FROM users ORDER BY ID"
        users_data = cursor.execute(query_get_users).fetchall()
        query_get_users_statistics = "SELECT matches, wins, points, max_points FROM statistics ORDER BY ID"
        users_statistics = cursor.execute(query_get_users_statistics).fetchall()
        cursor.close()
        connection.close()

        self.table.setRowCount(len(users_data))

        row = 0
        for user in users_data:
            self.table.verticalHeader().setSectionResizeMode(row, QtWidgets.QHeaderView.ResizeToContents)
            self.table.setItem(row, 0, QTableWidgetItem(str(user[0])))
            row = row + 1
        row = 0
        for user_stats in users_statistics:
            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, user_stats[0])
            self.table.setItem(row, 1, item)  # matches

            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, user_stats[1])
            self.table.setItem(row, 2, item)  # wins

            item = QTableWidgetItem()
            if user_stats[0] != 0:
                won_percentage = user_stats[1] / user_stats[0] * 100
            else:
                won_percentage = 0
            item.setData(Qt.DisplayRole, won_percentage)
            self.table.setItem(row, 3, item)  # calculated win%

            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, user_stats[2])
            self.table.setItem(row, 4, item)  # points gained

            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, user_stats[3])
            self.table.setItem(row, 5, item)  # theoretical max points

            item = QTableWidgetItem()
            if user_stats[3] != 0:
                points_percentage = user_stats[2] / user_stats[3] * 100
            else:
                points_percentage = 0
            item.setData(Qt.DisplayRole, points_percentage)
            self.table.setItem(row, 6, item)  # calculated efficiency
            row = row + 1
