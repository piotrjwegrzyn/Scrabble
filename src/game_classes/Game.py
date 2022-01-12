"""
package game_classes

"""
import sys
import time
import random


class Game:

    def __init__(self, windowManager):
        from src.game_classes.Data import Data
        self.start_time = None
        self.data = Data.instance()
        self.data.players = Data.players
        self.windowManager = windowManager
        self.can_be_placed = False
        self.in_dict = False
        self.human_moved = False

    def start_game(self):
        for player in self.data.players:
            player.player_pool = self.data.draw(7)
        self.start_time = time.time()

    def pause_game(self):
        # TODO
        print('!!! POKAŻ JAKIEŚ OKIENKO I ZATRZYMAJ GRE !!!')

    def resume_game(self):
        # TODO
        print('!!! UKRYJ OKIENKO I KONTYNUUJ GRE !!!')

    def end_game(self):
        # TODO("Refactor")
        print('!!! DODAJ DO STATYSTYK I WYJDZ DO MAIN MENU !!!')
        czas_gry = time.time() - self.start_time
        sec = czas_gry % 60
        czas_gry = czas_gry // 60
        min = czas_gry % 60
        godz = czas_gry // 60
        print('Czas gry to {}H {}M {}S'.format(godz, min, sec))

    def count_score(self, x_start, y_start, x_end, y_end):
        move_score = 0
        if x_end > x_start:
            for i in range(x_start, x_end):
                move_score += self.data.letters[self.data.board_pools[i][y_start]] * self.data.pools_score[i][
                    y_start]
        else:
            for i in range(y_start, y_end):
                move_score += self.data.letters[self.data.board_pools[x_start][i]] * self.data.pools_score[x_start][
                    i]
        return move_score

    def put_letter(self, position_x, position_y, letter):
        self.data.board_pools[position_x][position_y] = letter

    def make_move(self):
        while not self.human_moved or not self.data.players[0].is_human:
            player = self.data.players[0]
            if player.is_human:
                self.check_if_well_placed_and_get_word()
                self.in_dictionary()
                if self.can_be_placed and self.in_dict:
                    x_start, y_start, x_end, y_end, word = player.move(self.windowManager.game_window)
                    self.make_actuall_move(x_start, y_start, x_end, y_end, word)
                    self.human_moved = True
                else:
                    # TODO oczyścić planszę z ostatniego ruchu -> wczytac jeszcze raz z board_pools w data
                    return
            else:
                x_start, y_start, x_end, y_end, word = player.move(self.windowManager.game_window)
                self.make_actuall_move(x_start, y_start, x_end, y_end, word)
        self.human_moved = False

    def make_actuall_move(self, x_start, y_start, x_end, y_end, word):
        player = self.data.players[0]
        if x_end > x_start:
            for i in range(x_start, x_end + 1):
                self.put_letter(i, y_start, word[i - x_start])
        else:
            for i in range(y_start, y_end + 1):
                self.put_letter(x_start, i, word[i - y_start])
        self.data.check_for_letters_you_can_add_to(x_start, y_start, x_end, y_end)
        move_score = self.count_score(x_start, y_start, x_end, y_end)
        player.game_score += move_score
        self.data.players.append(self.data.players.pop(0))
        for letter in word:
            player.player_pool.remove(letter)
        player.player_pool.extend(self.data.draw(len(word)))

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
        word = ''
        if is_vertical_or_horizontal == 'bad':
            self.can_be_placed = False
            self.data.players[0].word = word
            return
        elif is_vertical_or_horizontal == 'vertical':
            for i in range(min(y), max(y) + 1):
                if i in y:
                    word += letters.pop(0)
                elif self.data.board_pools[x[0]][i] != '':
                    word += self.data.board_pools[x[0]][i]
                else:
                    self.can_be_placed = False
                    self.data.players[0].word = word
                    return
            self.can_be_placed = True
            self.data.players[0].word = word
            return
        elif is_vertical_or_horizontal == 'horizontal':
            for i in range(min(x), max(x) + 1):
                if i in x:
                    word += letters.pop(0)
                elif self.data.board_pools[i][y[0]] != '':
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
