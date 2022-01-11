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

    def start_game(self):
        for player in self.data.players:
            player.player_pool = self.data.draw(7)
        self.start_time = time.time()
        self.main_loop()

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
                move_score += self.data.pools_score[self.data.board_pools[i][y_start]] * self.data.pools_score[i][
                    y_start]
        else:
            for i in range(y_start, y_end):
                move_score += self.data.pools_score[self.data.board_pools[x_start][i]] * self.data.pools_score[x_start][
                    i]
        return move_score

    def put_letter(self, position_x, position_y, letter):
        self.data.board_pools[position_x][position_y] = letter

    def main_loop(self):
        while True:
            player = self.data.players[0]

            if not player.is_human:
                x_start, y_start, x_end, y_end, word = player.move(self.windowManager.game_window)
            else:
                while not self.can_be_placed or not self.in_dict:
                    self.windowManager.show_game_window()
                x_start, y_start, x_end, y_end, word = player.move(self.windowManager.game_window)

                self.data.check_for_letters_you_can_add_to(x_start, y_start, x_end, y_end)
            if x_end > x_start:
                for i in range(x_start, x_end):
                    self.put_letter(i, y_start, word[i - x_start])
            else:
                for i in range(y_start, y_end):
                    self.put_letter(x_start, i, word[i - y_start])
            move_score = self.count_score(x_start, y_start, x_end, y_end)
            player.game_score += move_score

            self.data.players.append(self.data.players.pop(0))

    def start_check_and_in_dict_methods(self):
        self.check_if_well_placed_and_get_word()
        self.in_dictionary()

    def check_if_well_placed_and_get_word(self):
        x = []
        y = []
        letters = []
        for ele in self.windowManager.gameWindow.get_dropped_tiles():
            letters.append(ele[0])
            x.append(ele[1])
            y.append(ele[2])
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

        word = ''
        if is_vertical_or_horizontal == 'bad':
            self.can_be_placed = False
            return
        elif is_vertical_or_horizontal == 'vertical':
            for i in range(min(y), max(y)):
                if i in y:
                    word += letters.pop()
                elif self.data.board_pools[x[0]][i] != '':
                    word += self.data.board_pools[x[0]][i]
                else:
                    self.can_be_placed = False
                    return
            self.can_be_placed = True
            self.data.players[0].word = word
            return
        elif is_vertical_or_horizontal == 'horizontal':
            for i in range(min(x), max(x)):
                if i in x:
                    word += letters.pop()
                elif self.data.board_pools[i][y[0]] != '':
                    word += self.data.board_pools[i][y[0]]
                else:
                    self.can_be_placed = False
                    return
            self.can_be_placed = True
            self.data.players[0].word = word
            return

    def in_dictionary(self):
        f = open('src/game_calsses/dict_easy')
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
