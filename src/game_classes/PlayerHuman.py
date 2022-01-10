"""
package game_classes

"""
from src.game_classes.PlayerAbstract import PlayerAbstract


class PlayerHuman(PlayerAbstract):

    def __init__(self, name):
        from src.gui.game.game_window.GameWindow import GameWindow
        super().__init__(name)
        from src.game_classes.Data import Data
        self.data = Data.instance()

    def move(self):
        check, word = self.check_if_well_placed_and_get_word()
        if check:
            if self.in_dictionary(word):
                x = []
                y = []
                for ele in GameWindow.get_dropped_tiles():
                    x.append(ele[1])
                    y.append(ele[2])
                return min(x), min(y), max(x), max(y), word

    def check_if_well_placed_and_get_word(self):
        x = []
        y = []
        letters = []
        for ele in GameWindow.get_dropped_tiles():
            letters.append(ele[0])
            x.append(ele[1])
            y.append(ele[2])
        x.sort()
        y.sort()

        is_vertical_or_horizontal = 'vertical'
        for i in range(1, len(x)):
            if x[i] != x[i-1]:
                is_vertical_or_horizontal = 'horizontal'
        if is_vertical_or_horizontal == 'horizontal':
            for i in range(1, len(y)):
                if y[i] != y[i-1]:
                    is_vertical_or_horizontal = 'bad'

        word = ''
        if is_vertical_or_horizontal == 'bad':
            return False, ''
        elif is_vertical_or_horizontal == 'vertical':
            for i in range(min(y), max(y)):
                if i in y:
                    word += letters.pop()
                elif self.data.board_pools[x[0]][i] != '':
                    word += self.data.board_pools[x[0]][i]
                else:
                    return False, ''
            return True, word
        elif is_vertical_or_horizontal == 'horizontal':
            for i in range(min(x), max(x)):
                if i in x:
                    word += letters.pop()
                elif self.data.board_pools[i][y[0]] != '':
                    word += self.data.board_pools[i][y[0]]
                else:
                    return False, ''
            return True, word

    def in_dictionary(self, word):
        f = open('src/game_calsses/dict_easy')
        for line in f:
            if word == line.strip():
                break
        else:
            f.close()
            return False
        f.close()
        return True

    def remove_from_pool(self, word):
        for char in word:
            self.player_pool.remove(char)
