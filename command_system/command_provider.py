import exceptions

class ICommandProvider:
    def get_command(self):
        raise NotImplementedError()

class FileCommandProvider(ICommandProvider):
    def __init__(self, file_name):
        try:
            self.file = open(file_name,'r')
        except IOError:
            raise exceptions.FailedToInitComponentExceptuion()

    def get_command(self):
        return self.file.readline()


class InterractiveCommandProvider(ICommandProvider):
    def get_command(self):
        return input()

