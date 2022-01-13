"""
package game_classes

"""


class PlayerAbstract:
    game_score = 0
    player_pool = []
    is_human = False
    letters_that_were_on_board = []
    theoretical_score = 0

    def __init__(self, name):
        self.name = name
        self.id = None

    def move(self, gameWindow):
        pass
