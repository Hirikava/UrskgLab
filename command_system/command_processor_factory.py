from command_system.comand_proccessors.graphics_coomand_processor import GraphicsCommandProcessor
from command_system.comand_proccessors.log_command_processor import LogCommandProcessor
from command_system.comand_proccessors.fake_command_processor import FakeCommandProcessor

class ICommandProcessorFactory():
    def get_command_processor(self, command):
        raise NotImplementedError()

class CommandProcessorFactory(ICommandProcessorFactory):
    def __init__(self, log, image):
        self.log = log
        self.image = image

    def get_command_processor(self, command):
        if(command == "log"):
            return LogCommandProcessor(self.log)
        if (command == "graphics"):
            return GraphicsCommandProcessor(self.log, self.image)
        else:
            self.log.Error(str.format("Unknown command: '{0}'",command))
            return FakeCommandProcessor()