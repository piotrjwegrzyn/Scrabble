"""
package game_classes

"""

import Board
import time

class Game():

    players = list()

    def __init__(self, id, players_human, players_ai=list()):
        self.start_time = 0
        self.current_state = 0
        self.board = Board()
        self.players.extend(players_human).extend(players_ai)


    def start_game(self):
        # TODO("To Do")
        self.start_time = time.time()


    def pause_game(self):
        # TODO("To Do")
        print('!!! POKAŻ JAKIEŚ OKIENKO I ZATRZYMAJ GRE !!!')


    def resume_game(self):
        # TODO("To Do")
        print('!!! UKRYJ OKIENKO I KONTYNUUJ GRE !!!')


    def end_game(self):
        # TODO("Refactor")
        print('!!! DODAJ DO STATYSTYK I WYJDZ DO MAIN MENU !!!')
        czas_gry = time.time() - self.start_time
        sec = czas_gry%60
        czas_gry = czas_gry//60
        min = czas_gry%60
        godz = czas_gry//60
        print('Czas gry to {}H {}M {}S'.format(godz, min, sec))
