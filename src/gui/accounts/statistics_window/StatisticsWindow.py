import sqlite3

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class StatisticsWindow(QMainWindow):

    def __init__(self):
        super(StatisticsWindow, self).__init__()
        loadUi('src/gui/accounts/statistics_window/statistics_window.ui')

        self.buttonBack.clicked.connect(self.close)

        self.set_column_sizes()
        # index: 1: a->Z; 2: games count 3: wins count
        # 4: win% 5: pts_gained 6: theoretical_max 7: points%
        #? self.dropdownListSortingOrder.SelectedIndex = 1
        #? self.dropdownListSortingOrder.currentIndexChanged.connect(self.change_sorting_order)
        #? self.insert_users_statistics_into_table()

    def set_column_sizes(self):
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(0, 50)

    def change_sorting_order(self):
        print('change order')

    def insert_users_statistics_into_table(self):

        connection = sqlite3.connect('data/Accounts_Statistics.db')
        cursor = connection.cursor()

        # TODO
        query_users = "SELECT username FROM users ORDER BY username" # ID, username
        cursor.execute(query_users)
        users = cursor.fetchall()
        query_statistics = "SELECT ID, matches, wins, points, max_points FROM statistics" # ID, matches, wins, points, max_points
        cursor.execute(query_statistics)
        statistics = cursor.fetchall()
        """
        row = 0
        for user in users:
            self.table.setItem(row, 0, QTableWidgetItem(user[])) # matches
            self.table.setItem(row, 0 ) # won_matches
            self.table.setItem(row, 0 ) # won_matches_%
            self.table.setItem(row, 0 ) # points
            self.table.setItem(row, 0 ) # max_points
            self.table.setItem(row, 0 ) # points / max_points
            row = row + 1
        """
        print('TODO')

        cursor.close()
        connection.close()
