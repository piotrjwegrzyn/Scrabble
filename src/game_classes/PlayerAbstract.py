"""
package game_classes

"""


class PlayerAbstract():
    game_score = 0
    player_pool = []

    def __init__(self, name):
        self.name = name

    def move(self):
        pass
