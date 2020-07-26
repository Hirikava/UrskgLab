
class CommandNotFountException(Exception):
    def __init__(self, message):
        self.message = message

class FailedToInitComponentExceptuion(Exception):
    pass

