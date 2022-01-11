"""
package game_classes

"""
from src.game_classes.PlayerAbstract import PlayerAbstract


class PlayerHuman(PlayerAbstract):

    def __init__(self, name):
        super().__init__(name)
        from src.game_classes.Data import Data
        self.data = Data.instance()
        self.is_human = True
        self.word = ''

    def move(self, gameWindow):
            x = []
            y = []
            for ele in gameWindow.get_dropped_tiles():
                x.append(ele[1])
                y.append(ele[2])
            return min(x), min(y), max(x), max(y), self.word

    def remove_from_pool(self, word):
        for char in word:
            self.player_pool.remove(char)
