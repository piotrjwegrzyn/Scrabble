
class LoggedUser(object):
    __instance = None

    @staticmethod
    def getInstance():
        if LoggedUser.__instance is not None:
            return LoggedUser.__instance

    def __init__(self, currentUserId):
        if LoggedUser.__instance is None:
            LoggedUser.__instance = self
            LoggedUser.__instance.uid = currentUserId
