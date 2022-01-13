"""
package game_classes

"""

from src.game_classes.PlayerAbstract import PlayerAbstract


class PlayerAI(PlayerAbstract):

    def __init__(self, name):
        from src.game_classes.Data import Data
        super().__init__("AI " + str(name))
        self.possible_words_position_in_dictionary = []
        self.possible_words = []
        self.positions = []
        self.level = "Easy"
        self.data = Data.instance()
        self.words_found = 0
        self.how_many_times_in_row_exchanged = 0

    def move(self, gameWindow):
        if self.data.board_pools[7][7] == '':
            letter = self.player_pool.pop(0)
            self.best_word_AI(letter, 7, 7)
            if len(self.possible_words) > 0:
                self.data.board_pools[7][7] = letter
                self.letters_that_were_on_board.append(letter)
                word = self.possible_words.pop(0)
                x_start = 7 - word.find(letter)
                x_end = 7 - word.find(letter) + len(word) - 1
                return x_start, 7, x_end, 7, word
            else:
                self.player_pool.append(letter)
        self.positions.clear()
        self.possible_words.clear()
        self.possible_words_position_in_dictionary.clear()
        for pos in self.data.letters_you_can_add_to:
            x, y = pos[0], pos[1]
            temp = self.words_found
            if self.level == "Easy":
                self.not_the_best_word_AI(self.data.board_pools[x][y], x, y)
            elif self.level == "Medium" or self.level == "Hard":
                self.best_word_AI(self.data.board_pools[x][y], x, y)
            if self.words_found > temp:
                self.positions.append(pos)
        no_possible_words = len(self.possible_words)
        if no_possible_words < 1:
            self.data.game_pool.extend(self.player_pool)
            self.player_pool.clear()
            self.player_pool.extend(self.data.draw(7))
            self.how_many_times_in_row_exchanged += 1
            return 0, 0, 0, 0, ''
        else:
            for i in range(no_possible_words):
                word = self.possible_words[i]
                x, y = self.positions[i][0], self.positions[i][1]
                if self.data.board_pools[x - 1][y] != '' or self.data.board_pools[x + 1][y] != '':
                    x_start = x
                    x_end = x
                    letter = self.data.board_pools[x][y]
                    self.letters_that_were_on_board.append(letter)
                    ind = word.find(letter)
                    y_start = y - ind
                    y_end = y - ind + len(word) - 1
                    if y_start >= 0 and y_end < 15:
                        self.how_many_times_in_row_exchanged = 0
                        return x_start, y_start, x_end, y_end, word
                elif self.data.board_pools[x][y - 1] != '' or self.data.board_pools[x][y + 1] != '':
                    y_start = y
                    y_end = y
                    letter = self.data.board_pools[x][y]
                    self.letters_that_were_on_board.append(letter)
                    ind = word.find(letter)
                    x_start = x - ind
                    x_end = x - ind + len(word) - 1
                    if x_start >= 0 and x_end < 15:
                        self.how_many_times_in_row_exchanged = 0
                        return x_start, y_start, x_end, y_end, word

    def check_if_word_can_be_placed(self, x, y, word):
        check = True
        letter = self.data.board_pools[x][y]
        ind = word.find(letter)
        length = len(word)
        if self.data.board_pools[x-1][y] != '' or self.data.board_pools[x+1][y] != '':
            for i in range(max(y-(ind+1), 0), y):
                if self.data.board_pools[x-1][i] != '' or self.data.board_pools[x+1][i] != '':
                    check = False
            for i in range(y+1, min(y+(length-ind+1), 14)):
                if self.data.board_pools[x-1][i] != '' or self.data.board_pools[x+1][i] != '':
                    check = False
            if y-(ind+1) >= 0 and y+(length-ind) < 15:
                if self.data.board_pools[x][y-(ind+1)] != '' or self.data.board_pools[x][y+(length-ind)] != '':
                    check = False

        elif self.data.board_pools[x][y-1] != '' or self.data.board_pools[x][y+1] != '':
            for i in range(max(x-(ind+1), 0), x):
                if self.data.board_pools[i][y-1] != '' or self.data.board_pools[i][y+1] != '':
                    check = False
            for i in range(x+1, min(x+(length-ind+1), 14)):
                if self.data.board_pools[i][y-1] != '' or self.data.board_pools[i][y+1] != '':
                    check = False
            if x-(ind+1) >= 0 and x+(length-ind) < 15:
                if self.data.board_pools[x-(ind+1)][y] != '' or self.data.board_pools[x+(length-ind)][y] != '':
                    check = False

        if check:
            return True
        else:
            return False

    def best_word_AI(self, letter, x, y):
        temp = self.player_pool.copy()
        temp.append(letter)
        i = 0
        for line in self.data.lines:
            if letter in line:
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
                if found and self.check_if_word_can_be_placed(x, y, line):
                    self.possible_words.append(line)
                    self.possible_words_position_in_dictionary.append(i)
                    break

    def not_the_best_word_AI(self, letter, x, y):
        temp = self.player_pool.copy()
        temp.append(letter)
        for line in open('src/game_classes/dict_easy', encoding='utf-8'):
            if letter in line:
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
                if found and self.check_if_word_can_be_placed(x, y, line):
                    self.possible_words.append(line)
                    self.words_found += 1
                    break
