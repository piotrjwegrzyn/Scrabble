"""
package game_classes

"""


class Data(object):
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
            from src.game_classes.GamePlayers import GamePlayers
            cls.players = GamePlayers.get_instances()
            cls.board_pools = [[None]*15]*15
            cls.pools_score = [[1]*15 for i in range(15)]
            # Tu trzeba dodać mnożniki do konkretnych pól
            cls.players = []
            cls.letters_you_can_add_to = []
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
