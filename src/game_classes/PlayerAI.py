"""
package game_classes

"""

from src.game_classes.Game import Game
from src.game_classes.PlayerAbstract import PlayerAbstract


class PlayerAI(PlayerAbstract):

    def __init__(self, name):
        from Data import Data
        super().__init__("AI " + str(name))
        self.possible_words_position_in_dictionary = []
        self.possible_words = []
        self.level = "Easy"
        self.data = Data.instance()

    def move(self):
        if self.level == "Hard":
            for pos in self.data.letters_you_can_add_to:
                x, y = pos[0], pos[1]
                self.best_word_AI(self.data.board_pools[x][y])
            no_possible_words = len(self.possible_words)
            for i in range(no_possible_words):
                temp = min(self.possible_words_position_in_dictionary)
                ind = self.possible_words_position_in_dictionary.index(temp)
                self.possible_words_position_in_dictionary.pop(ind)
                Game.check_if_word_can_be_placed(x, y, self.possible_words.pop(ind))
            else:
                Game.draw(7)

    def best_word_AI(self, letter):
        temp = self.player_pool.copy()
        temp.append(letter)
        i = 0
        for line in self.data.lines:
            i += 1
            AI_pool_copy = temp.copy()
            found = True
            # usuwanie znaku \n z konca
            line = line.strip()
            for char in line:
                if char in AI_pool_copy:
                    AI_pool_copy.remove(char)
                else:
                    found = False
                    break
            if found:
                self.possible_words.append(line)
                self.possible_words_position_in_dictionary.append(i)
                break
