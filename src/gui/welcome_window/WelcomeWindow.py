from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class WelcomeWindow(QMainWindow):

    def __init__(self):
        super(WelcomeWindow, self).__init__()
        loadUi("src/gui/welcome_window/welcome_window.ui", self)

        self.buttonLogin.clicked.connect(self.close)
        self.buttonRegister.clicked.connect(self.close)
