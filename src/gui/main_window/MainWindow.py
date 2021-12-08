from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("src/gui/main_window/main_window.ui", self)
