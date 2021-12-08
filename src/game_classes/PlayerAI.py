"""
package game_classes

"""

class PlayerAI(PlayerAbstract):

    def __init__(self, id, level):
        super().__init__(id, "AI " + str(id))
        self.level = level

    def move(self):
        # TODO("todo")
        print('!!! ALGORYTMY W ZALEZNOŚCI OD POZIOMU') # LOG