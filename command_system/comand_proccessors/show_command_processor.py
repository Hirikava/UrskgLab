from command_system.command_processor import ICommandProcessor

class ShowCommandProcessor(ICommandProcessor):
    def __init__(self,image):
        self.image = image
    def process_command(self, command_arguments):
        self.image.show()
