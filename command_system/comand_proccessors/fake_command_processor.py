from command_system.command_processor import ICommandProcessor

class FakeCommandProcessor(ICommandProcessor):
    def process_command(self, command_tokens):
        pass