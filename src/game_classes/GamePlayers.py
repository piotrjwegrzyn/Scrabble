from src.game_classes.PlayerHuman import PlayerHuman
from src.game_classes.PlayerAI import PlayerAI


class GamePlayers(object):
    __instances = []

    def __init__(self, name, playerType):
        if playerType == "AI":
            if PlayerAI(name) not in GamePlayers.__instances:
                GamePlayers.__instances.append(PlayerAI(name))
        else:
            if PlayerHuman(name) not in GamePlayers.__instances:
                GamePlayers.__instances.append(PlayerHuman(name))

    @staticmethod
    def delete_instance(play3r):
        if play3r in GamePlayers.__instances:
            GamePlayers.__instances.remove(play3r)

    @staticmethod
    def delete_instances():
        GamePlayers.__instances = []

    @staticmethod
    def get_instance(name):
        for player in GamePlayers.__instances:
            if player.name == name:
                return player
        return None

    @staticmethod
    def get_instances():
        return GamePlayers.__instances
