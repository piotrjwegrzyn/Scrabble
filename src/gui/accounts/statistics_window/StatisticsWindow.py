import sqlite3

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class StatisticsWindow(QMainWindow):

    def __init__(self):
        super(StatisticsWindow, self).__init__()
        loadUi('src/gui/accounts/statistics_window/statistics_window.ui', self)

        self.set_column_sizes()
        self.dropdownListSortingOrder.SelectedIndex = 1
        self.dropdownListSortingOrder.currentIndexChanged.connect(self.change_sorting_order)
        self.insert_users_statistics_into_table()

        self.buttonBack.clicked.connect(self.close)

    def set_column_sizes(self):
        self.table.setColumnWidth(0, 120)
        self.table.setColumnWidth(1, 110)
        self.table.setColumnWidth(2, 160)
        self.table.setColumnWidth(3, 190)
        self.table.setColumnWidth(4, 190)
        self.table.setColumnWidth(5, 260)
        self.table.setColumnWidth(6, 320)

    def change_sorting_order(self):
        index = self.dropdownListSortingOrder.currentIndex()

        # index: 0: a->Z; 1: games count 2: wins count
        # 3: win% 4: pts_gained 5: theoretical_max 6: points% (idx4/idx5)

        connection = sqlite3.connect('data/Accounts_Statistics.db')
        cursor = connection.cursor()
        query_get_users = "SELECT FROM users"

        query_get_users_statistics = "SELECT FROM statistics"
        """
        if index == 1:

        elif index == 2:

        elif index == 3:

        elif index == 4:

        elif index == 5:

        elif index == 6:

        else:
        """

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
