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
            x.append(ele[2])
            y.append(ele[1])
        x_start = min(x)
        x_end = max(x)
        y_start = min(y)
        y_end = max(y)
        if len(x) != len(self.word):
            if min(x) != max(x):
                if min(x) - 1 >= 0:
                    if self.data.board_pools[min(x) - 1][y[0]] != '':
                        x_start = min(x) - 1
                if max(x) + 1 < 15:
                    if self.data.board_pools[max(x) + 1][y[0]] != '':
                        x_end = max(x) + 1
            elif min(y) != max(y):
                if min(y) - 1 >= 0:
                    if self.data.board_pools[x[0]][min(y) - 1] != '':
                        y_start = min(y) - 1
                if max(y) + 1 < 15:
                    if self.data.board_pools[x[0]][max(y) + 1] != '':
                        y_end = max(y) + 1
        return x_start, y_start, x_end, y_end, self.word

    def remove_from_pool(self, word):
        for char in word:
            self.player_pool.remove(char)
