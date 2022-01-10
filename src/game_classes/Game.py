"""
package game_classes

"""
import sys
import time
import random


class Game:

    def __init__(self, gameWindow):
        from Data import Data
        self.start_time = None
        self.data = Data.instance()
        self.data.players = Data.players
        self.window = gameWindow

    def start_game(self):
        for player in self.data.players:
            player.player_pool = self.draw(7)
        self.start_time = time.time()
        self.main_loop()

    def pause_game(self):
        # TODO
        print('!!! POKAŻ JAKIEŚ OKIENKO I ZATRZYMAJ GRE !!!')

    def resume_game(self):
        # TODO
        # self.window.buttonEndTurn.clicked.connect(#Twoja_funckja)
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

    def isalpha_and_in_pool(self, pool, word):
        if not (word.isalpha()):
            print("Ya entered some weird stuff")
            return False

        move_score = 0
        player_pool_copy = pool.copy()
        for char in word:
            if char in player_pool_copy:
                player_pool_copy.remove(char)
            else:
                print("character(s) not in your pool")
                return False
        return True

    def in_dictionary(self, word):
        f = open('slownik')
        for line in f:
            if word == line.strip():
                break
        else:
            print("Word not in dictionary")
            f.close()
            return False
        f.close()
        return True

    def remove_from_pool(self, pool, word):
        for char in word:
            pool.remove(char)

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
            # self.data.players[0]

            # self.window.display_data()

            x_start, y_start, x_end, y_end, word = player.move()
            if x_end > x_start:
                for i in range(x_start, x_end):
                    self.put_letter(i, y_start, word[i - x_start])
            else:
                for i in range(y_start, y_end):
                    self.put_letter(x_start, i, word[i - y_start])
            move_score = self.count_score(x_start, y_start, x_end, y_end)
            player.game_score += move_score

            # self.data.players.append(self.data.players.pop(0))
