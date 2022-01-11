"""
package game_classes

"""
import sys
import time
import random


class Game:

    def __init__(self):
        from src.game_classes.Data import Data
        from src.gui.game.game_window.GameWindow import GameWindow
        self.start_time = None
        self.data = Data.instance()
        self.data.players = Data.players
        self.window = GameWindow()

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

            self.window.display_data()

            # self.window.buttonEndTurn.clicked.connect()
            if not player.is_human:
                x_start, y_start, x_end, y_end, word, exit_code = player.move(self.window)
            else:
                x_start, y_start, x_end, y_end, word, exit_code = 0, 0, 0, 0, '', 3
            while exit_code != 0:

                x_start, y_start, x_end, y_end, word, exit_code = player.move(self.window)
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
