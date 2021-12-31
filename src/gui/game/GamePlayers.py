
class GamePlayers(object):
    __instances = []

    def __init__(self, name):
        if GamePlayer(name) not in GamePlayers.__instances:
            GamePlayers.__instances.append(GamePlayer(name))

    @staticmethod
    def delete_instance(name):
        for player in GamePlayers.__instances:
            if player.name == name:
                GamePlayers.__instances.remove(player)

    @staticmethod
    def delete_instances():
        GamePlayers.__instances = []

    @staticmethod
    def get_instance(name):
        for player in GamePlayers.__instances:
            if player.name == name:
                return player
        print(GamePlayers.__instances)
        return None

    @staticmethod
    def get_instances():
        return GamePlayers.__instances


class GamePlayer:
    def __init__(self, name):
        self.realPlayer = True
        self.id = None
        self.difficulty = None
        self.name = name
        self.score = 0
        self.theoreticalScore = 0
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']  # TODO - wyzerowac jak już będzie działać
