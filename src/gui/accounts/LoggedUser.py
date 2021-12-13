
class LoggedUser:
    __instance = None

    @staticmethod
    def get_instance():
        if LoggedUser.__instance is not None:
            return LoggedUser.__instance
        else:
            return None

    @staticmethod
    def delete_instance():
        if LoggedUser.__instance is not None:
            LoggedUser.__instance = None

    def __init__(self, userid, username):
        if LoggedUser.__instance is None:
            LoggedUser.__instance = self
            LoggedUser.__instance.uid = userid
            LoggedUser.__instance.uname = username
        else:
            raise Exception("Second instance of singleton!")