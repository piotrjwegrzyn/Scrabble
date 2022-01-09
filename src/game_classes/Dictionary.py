"""
package game_classes

"""

class Dictionary(object):
    _instance = None
    letters = dict()

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.letters = {
                'a' : 1,
                'ą' : 1,
                'b' : 3,
                'c' : 2,
                'ć' : 6,
                'd' : 2,
                'e' : 1,
                'ę' : 5,
                'f' : 5,
                'g' : 3,
                'h' : 3,
                'i' : 1,
                'j' : 3,
                'k' : 2,
                'l' : 2,
                'ł' : 3,
                'm' : 2,
                'n' : 1,
                'ń' : 7,
                'o' : 1,
                'ó' : 5,
                'p' : 2,
                'r' : 1,
                's' : 1,
                'ś' : 5,
                't' : 2,
                'u' : 3,
                'w' : 1,
                'y' : 2,
                'z' : 1,
                'ź' : 9,
                'ż' : 5,
            }
        return cls._instance


    def count_points(self, word):
        # TODO("todo")
        return 0
