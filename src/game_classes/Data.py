"""
package game_classes

"""
import sys
import random


class Data(object):
    pools_score = [[1] * 15 for i in range(15)]
    theoretical_hard_computer = None
    players = []
    lines = []
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            f = open('src/game_classes/dictionary', encoding='utf-8')
            cls.lines = f.readlines()
            f.close()
            cls.board_pools = [[''] * 15 for i in range(15)]
            for i in range(0, 15):
                for j in range(0, 15):
                    if i == 7 and j == 7:
                        pass
                    elif i % 7 == 0 and j % 7 == 0:
                        cls.pools_score[i][j] = -3
                    elif ((i == 3 or i == 11) and j % 14 == 0) or ((j == 3 or j == 11) and i % 14 == 0):
                        cls.pools_score[i][j] = 2
                    elif (i % 4 == 1 and j % 4 == 1) and not (
                            i == j == 1 or i == j == 13 or (i == 1 and j == 13) or (i == 13 and j == 1)):
                        cls.pools_score[i][j] = 3
                    elif (i == 6 or i == 8) and (j == 6 or j == 8):
                        cls.pools_score[i][j] = 2
            for i in range(1, 5):
                cls.pools_score[i][i] = -2
                cls.pools_score[14 - i][i] = -2
                cls.pools_score[14 - i][14 - i] = -2
                cls.pools_score[i][14 - i] = -2
            for i in range(6, 8):
                cls.pools_score[i][i - 4] = 2
                cls.pools_score[14 - i][14 - (i - 4)] = 2
                cls.pools_score[i - 4][i] = 2
                cls.pools_score[14 - (i - 4)][14 - i] = 2
            cls.pools_score[8][2] = 2
            cls.pools_score[2][8] = 2
            cls.pools_score[12][6] = 2
            cls.pools_score[6][12] = 2
            cls.players = []
            cls.letters_you_can_add_to = []
            from src.game_classes.GamePlayers import GamePlayers
            cls.players = GamePlayers.get_instances()
            from src.game_classes.PlayerAI import PlayerAI
            cls.theoretical_hard_computer = PlayerAI("x")
            cls.theoretical_hard_computer.level = "Hard"
            cls.theoretical_hard_computer.is_real = False
            # cls.game_pool = list("aaaaaaaaaąbbcccćdddeeeeeeeęfgghhiiiiiiiijjkkklllłłmmmnnnnnńooooooóppprrrrsśtttuuwwwwyyyyzzzzzźż")
            cls.game_pool = list(
                "nhucgźoróylwmłńoadpteidcezifpsgaoyićawiplozlżnzwreomakjhoitaarunmiłznśiazrąęekweyceentbyabkajid")
            cls.letters = {
                'a': 1,
                'ą': 5,
                'b': 3,
                'c': 2,
                'ć': 6,
                'd': 2,
                'e': 1,
                'ę': 5,
                'f': 5,
                'g': 3,
                'h': 3,
                'i': 1,
                'j': 3,
                'k': 2,
                'l': 2,
                'ł': 3,
                'm': 2,
                'n': 1,
                'ń': 7,
                'o': 1,
                'ó': 5,
                'p': 2,
                'r': 1,
                's': 1,
                'ś': 5,
                't': 2,
                'u': 3,
                'w': 1,
                'y': 2,
                'z': 1,
                'ź': 9,
                'ż': 5,
            }
        return cls._instance

    def draw(self, how_many):
        if len(self.game_pool) < how_many:
            return ['!']
        draw_pool = []
        for i in range(how_many):
            draw_pool.append(self.game_pool.pop(random.randint(0, len(self.game_pool) - 1)))
        return draw_pool

    def check_for_letters_you_can_add_to(self, x_start, y_start, x_end, y_end):
        for i in range(max(x_start-1, 1), min(x_end+2, 13)):
            for j in range(max(y_start-1, 1), min(y_end+2, 13)):
                if self.board_pools[i][j] != '':
                    self.check_letter(i, j)

    def check_letter(self, x, y):
        if self.board_pools[x+1][y] != '' or self.board_pools[x-1][y] != '':
            for i in range(x-1, x+2):
                if self.board_pools[i][y-1] != '':
                    self.remove_from_letters_you_can_add_to(x, y)
                    return
            for i in range(x-1, x+2):
                if self.board_pools[i][y+1] != '':
                    self.remove_from_letters_you_can_add_to(x, y)
                    return
        elif self.board_pools[x][y+1] != '' or self.board_pools[x][y-1] != '':
            for i in range(y-1, y+2):
                if self.board_pools[x-1][i] != '':
                    self.remove_from_letters_you_can_add_to(x, y)
                    return
            for i in range(y-1, y+2):
                if self.board_pools[x+1][i] != '':
                    self.remove_from_letters_you_can_add_to(x, y)
                    return
        self.add_to_letters_you_can_add_to(x, y)
        return

    def remove_from_letters_you_can_add_to(self, x, y):
        temp = (x, y)
        if temp in self.letters_you_can_add_to:
            self.letters_you_can_add_to.remove(temp)

    def add_to_letters_you_can_add_to(self, x, y):
        temp = (x, y)
        if temp not in self.letters_you_can_add_to:
            self.letters_you_can_add_to.append(temp)