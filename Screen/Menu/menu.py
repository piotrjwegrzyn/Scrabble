from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class MenuWindow(QMainWindow):

    def __init__(self):
        super(MenuWindow, self).__init__()
        loadUi("Screen/Menu/menuWindow.ui", self)
