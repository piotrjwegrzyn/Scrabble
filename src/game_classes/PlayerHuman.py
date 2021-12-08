"""
package game_classes

"""

class PlayerHuman(PlayerAbstract):

    def __init__(self, id, name, password=""):
        super().__init__(id, name)
        self.password = password

    def put_letter(self, position_x, position_y):
        # TODO("todo")
        pass
