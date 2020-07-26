import logging
import command_provider

from comand_proccessor import command_processor

log = logging.FileLog('prvet_andrey.log')
commandProvider = command_provider.InterractiveCommandProWvider()
commandProcessor = command_processor.CommandProcessor(log)
com = commandProvider.get_command()

while(com[0]):
    commandProcessor.proccess_command(com[0],com[1:])
    com = commandProvider.get_command()

log = logging.ConsoleLog()