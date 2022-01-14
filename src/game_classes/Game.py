"""
package game_classes

"""
import time


class Game:

    def __init__(self, windowManager):
        from src.game_classes.Data import Data
        self.start_time = None
        self.data = Data.instance()
        self.data.players = Data.players
        self.windowManager = windowManager
        self.can_be_placed = False
        self.in_dict = False

    def start_game(self):
        from src.game_classes.Data import Data
        self.data = Data.instance()
        self.data.board_pools = [[''] * 15 for i in range(15)]
        self.data.game_pool = list("nhucgźoróylwmłńoadpteidcezifpsgaoyićawiplozlżnzwreomakjhoitaarunmiłznśiazrąęekweyceentbyabkajid")
        from src.game_classes.GamePlayers import GamePlayers
        self.data.players = GamePlayers.get_instances()
        self.data.letters_you_can_add_to = []
        for player in self.data.players:
            player.player_pool = self.data.draw(7)
        self.start_time = time.time()
        self.windowManager.game_window.reset()

    def end_game(self):
        self.windowManager.qTimer.stop()
        self.windowManager.game_window.display_statistics()

    def count_score(self, x_start, y_start, x_end, y_end, word):
        move_score = 0
        double_word_multiplier = False
        triple_word_multiplier = False
        if x_end > x_start:
            for i in range(x_start, x_end + 1):
                multiplier = self.data.pools_score[i][y_start]
                if multiplier == -2:
                    multiplier = 1
                    double_word_multiplier = True
                elif multiplier == -3:
                    multiplier = 1
                    triple_word_multiplier = True
                move_score += self.data.letters[word[i-x_start]] * multiplier
        else:
            for i in range(y_start, y_end + 1):
                multiplier = self.data.pools_score[x_start][i]
                if multiplier == -2:
                    multiplier = 1
                    double_word_multiplier = True
                elif multiplier == -3:
                    multiplier = 1
                    triple_word_multiplier = True
                move_score += self.data.letters[word[i-y_start]] * multiplier
        if double_word_multiplier:
            move_score = move_score * 2
        elif triple_word_multiplier:
            move_score = move_score * 3
        return move_score

    def put_letter(self, position_x, position_y, letter):
        self.data.board_pools[position_x][position_y] = letter

    def exchange_clicked(self):
        self.exchange()
        if not self.data.players[0].is_human:
            self.make_move()
        else:
            self.windowManager.game_window.reset()
            self.windowManager.show_blackscreen_window()

    def exchange(self):
        if len(self.windowManager.game_window.get_tiles_to_exchange()) == 0:
            return
        letters_to_throw_away = []
        for ele in self.windowManager.game_window.get_tiles_to_exchange():
            letters_to_throw_away.append(self.data.players[0].player_pool[ele])
        self.data.game_pool.extend(letters_to_throw_away)
        for letter in letters_to_throw_away:
            self.data.players[0].player_pool.remove(letter)
        self.data.players[0].player_pool.extend(self.data.draw(len(letters_to_throw_away)))
        if '!' in self.data.players[0].player_pool:
            self.end_game()
        self.windowManager.game_window.reset()
        self.data.players.append(self.data.players.pop(0))

    def automatic_move_if_computer(self):
        if not self.data.players[0].is_human:
            self.make_move()

    def make_move(self):
        player = self.data.players[0]
        if player.is_human:
            self.check_if_well_placed_and_get_word()
            self.in_dictionary()
            if self.can_be_placed and self.in_dict:
                self.data.theoretical_hard_computer.player_pool = player.player_pool.copy()
                x_start, y_start, x_end, y_end, word = self.data.theoretical_hard_computer.move(self.windowManager.game_window)
                player.theoretical_score += self.count_score(x_start, y_start, x_end, y_end, word)
                x_start, y_start, x_end, y_end, word = player.move(self.windowManager.game_window)
                self.make_actuall_move(x_start, y_start, x_end, y_end, word)
            else:
                player.letters_that_were_on_board.clear()
                self.windowManager.game_window.reset()
                return
        else:
            self.data.theoretical_hard_computer.player_pool = player.player_pool.copy()
            x_start, y_start, x_end, y_end, word = player.move(self.windowManager.game_window)
            if word == '!' or player.how_many_times_in_row_exchanged >= 3:
                self.end_game()
            if word != '':
                self.make_actuall_move(x_start, y_start, x_end, y_end, word)
                if player.level == "Hard":
                    player.theoretical_score = player.game_score
                else:
                    x_start, y_start, x_end, y_end, word = self.data.theoretical_hard_computer.move(self.windowManager.game_window)
                    player.theoretical_score += self.count_score(x_start, y_start, x_end, y_end, word) + 2
                self.windowManager.game_window.reset()
        self.data.players.append(self.data.players.pop(0))
        if self.data.players[0].is_human:
            self.windowManager.game_window.reset()
            self.windowManager.show_blackscreen_window()

    def make_actuall_move(self, x_start, y_start, x_end, y_end, word):
        player = self.data.players[0]
        if x_end > x_start:
            for i in range(x_start, x_end + 1):
                self.put_letter(i, y_start, word[i - x_start])
        else:
            for i in range(y_start, y_end + 1):
                self.put_letter(x_start, i, word[i - y_start])
        self.data.check_for_letters_you_can_add_to(x_start, y_start, x_end, y_end)
        move_score = self.count_score(x_start, y_start, x_end, y_end, word)
        player.game_score += move_score
        for letter in word:
            if letter not in player.letters_that_were_on_board:
                player.player_pool.remove(letter)
        player.player_pool.extend(self.data.draw(7 - len(player.player_pool)))
        if '!' in player.player_pool:
            self.end_game()
        player.letters_that_were_on_board.clear()

    def check_if_well_placed_and_get_word(self):
        x = []
        y = []
        letters = []
        for ele in self.windowManager.game_window.get_dropped_tiles():
            letters.append(self.data.players[0].player_pool[ele[0]])
            x.append(ele[2])
            y.append(ele[1])
        x.sort()
        y.sort()
        if self.data.board_pools[7][7] == '':
            if 7 not in x or 7 not in y:
                self.can_be_placed = False
                return

        is_vertical_or_horizontal = 'vertical'
        for i in range(1, len(x)):
            if x[i] != x[i - 1]:
                is_vertical_or_horizontal = 'horizontal'
        if is_vertical_or_horizontal == 'horizontal':
            for i in range(1, len(y)):
                if y[i] != y[i - 1]:
                    is_vertical_or_horizontal = 'bad'
        if len(x) <= 1:
            is_vertical_or_horizontal = 'bad'
        if len(x) == 1:
            if min(y) - 1 >= 0:
                if self.data.board_pools[x[0]][min(y) - 1] != '':
                    is_vertical_or_horizontal = 'vertical'
            if max(y) + 1 < 15:
                if self.data.board_pools[x[0]][max(y) + 1] != '':
                    is_vertical_or_horizontal = 'vertical'
            if min(x) - 1 >= 0:
                if self.data.board_pools[min(x) - 1][y[0]] != '':
                    is_vertical_or_horizontal = 'horizontal'
            if max(x) + 1 < 15:
                if self.data.board_pools[max(x) + 1][y[0]] != '':
                    is_vertical_or_horizontal = 'horizontal'
        word = ''
        if is_vertical_or_horizontal == 'bad':
            self.can_be_placed = False
            self.data.players[0].word = word
            return
        elif is_vertical_or_horizontal == 'vertical':
            y_start = min(y)
            y_end = max(y)
            if min(y) - 1 >= 0:
                if self.data.board_pools[x[0]][min(y) - 1] != '':
                    y_start = min(y) - 1
            if max(y) + 1 < 15:
                if self.data.board_pools[x[0]][max(y) + 1] != '':
                    y_end = max(y) + 1
            for i in range(y_start, y_end + 1):
                if i in y:
                    word += letters.pop(0)
                elif self.data.board_pools[x[0]][i] != '':
                    self.data.players[0].letters_that_were_on_board.append(self.data.board_pools[x[0]][i])
                    word += self.data.board_pools[x[0]][i]
                else:
                    self.can_be_placed = False
                    self.data.players[0].word = word
                    return
            self.can_be_placed = True
            self.data.players[0].word = word
            return
        elif is_vertical_or_horizontal == 'horizontal':
            x_start = min(x)
            x_end = max(x)
            if min(x) - 1 >= 0:
                if self.data.board_pools[min(x) - 1][y[0]] != '':
                    x_start = min(x) - 1
            if max(x) + 1 < 15:
                if self.data.board_pools[max(x) + 1][y[0]] != '':
                    x_end = max(x) + 1
            for i in range(x_start, x_end + 1):
                if i in x:
                    word += letters.pop(0)
                elif self.data.board_pools[i][y[0]] != '':
                    self.data.players[0].letters_that_were_on_board.append(self.data.board_pools[i][y[0]])
                    word += self.data.board_pools[i][y[0]]
                else:
                    self.can_be_placed = False
                    self.data.players[0].word = word
                    return
            self.can_be_placed = True
            self.data.players[0].word = word
            return

    def in_dictionary(self):
        if self.data.players[0].word == '':
            self.in_dict = False
            return
        f = open('src/game_classes/dict_easy', encoding='utf-8')
        for line in f:
            if self.data.players[0].word == line.strip():
                break
        else:
            f.close()
            self.in_dict = False
            return
        f.close()
        self.in_dict = True
        return
