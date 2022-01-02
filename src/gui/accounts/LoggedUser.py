
class LoggedUser(object):
    __instance = None

    def __init__(self, username, userid):
        if LoggedUser.__instance is None:
            LoggedUser.__instance = object.__new__(LoggedUser)
            LoggedUser.uname = username
            LoggedUser.uid = userid

    @staticmethod
    def get_instance():
        if LoggedUser.__instance is not None:
            return LoggedUser.__instance
        else:
            return None

    @staticmethod
    def delete_instance():
        LoggedUser.__instance = None
