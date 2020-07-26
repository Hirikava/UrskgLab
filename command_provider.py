import exceptions

class ICommandProvider:
    def get_command(self):
        raise NotImplementedError()

class FileCommandProvider(ICommandProvider):

    def __init__(self, file_name, log):
        try:
            self.file = open(file_name,'r')
        except IOError:
            log.error(str.format('failed to open file {0}', file_name))
            self.file = None
            raise exceptions.FailedToInitComponentExceptuion()

    def get_command(self):
        return self.file.readline()


class InterractiveCommandProWvider(ICommandProvider):
    def get_command(self):
        return input().split(' ')

