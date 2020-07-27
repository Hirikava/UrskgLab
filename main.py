from command_system.command_processor_factory import CommandProcessorFactory
from command_system.command_provider import FileCommandProvider, InterractiveCommandProvider
from PIL import Image
from logging_module import ConsoleLog

t()
log = ConsoleLog()
image = Image.new("RGB",(1000,1000),(234,241,123))
command_processor_factory = CommandProcessorFactory(log,image)
command_provider = InterractiveCommandProvider()

com = command_provider.get_command().split()
while(com):
    command_processor = command_processor_factory.get_command_processor(com[0])
    command_processor.process_command(" ".join(com[1:]))
    com = command_provider.get_command().spli