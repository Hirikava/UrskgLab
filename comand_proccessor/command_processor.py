import exceptions

class ICommandProcessor():
    def proccess_command(self, command, tokens):
        raise NotImplementedError()

class CommandProcessor(ICommandProcessor):
    def __init__(self, log):
        self.log = log

    def proccess_command(self, command, tokens):
        if(command == "log"):
            self.log.Info(" ".join(tokens))
        else:
            self.log.Warn(str.format("Unknown command: '{0}' with arguments: '{1}'",command," ".join(tokens)))
