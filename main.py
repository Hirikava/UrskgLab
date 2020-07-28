from command_system.command_processor_factory import CommandProcessorFactory
from command_system.command_provider import FileCommandProvider, InterractiveCommandProvider
from exceptions import FailedToInitComponentExceptuion
import argparse
from PIL import Image
from logging_module import ConsoleLog, FileLog
from utils import check_color_variable, check_size

def get_log_cfg(log_argument):
    if(log_argument == "console"):
        return ConsoleLog()
    try:
        return FileLog(log_argument)
    except FailedToInitComponentExceptuion as e:
        print("Failed to init file log:%0 use default consol log" % log_argument)
        return ConsoleLog

def get_image_cfg(size_tokens,color_tokens):
    size = (size_tokens[0],size_tokens[1])
    color = (color_tokens[0],color_tokens[1],color_tokens[2])
    return Image.new("RGB",size,color)

def get_command_provider_cfg(input_argument):
    if(input_argument == "console"):
        return InterractiveCommandProvider()
    try:
        return FileCommandProvider(input_argument)
    except FailedToInitComponentExceptuion as e:
        print("Failed to open file:%0 " % input_argument)
        raise


parser = argparse.ArgumentParser(description="Configuration")
parser.add_argument("-l", "--log", dest="log", type=str, default="console", required=False)
parser.add_argument("-i","--input", dest="input", type=str, default="console", required=False)
parser.add_argument("-c","--color", dest="color", type=check_color_variable, default=[255,255,255], nargs=3, required=False)
parser.add_argument("-s","--size", dest="size", type=check_size,default=[800,600], nargs=2, required=False)
cfg_arguments = parser.parse_args()

log = get_log_cfg(cfg_arguments.log)
image = get_image_cfg(cfg_arguments.size, cfg_arguments.color)
command_provider = get_command_provider_cfg(cfg_arguments.input)

command_processor_factory = CommandProcessorFactory(log,image)
com = command_provider.get_command().split()
while(com):
    command_processor = command_processor_factory.get_command_processor(com[0])
    command_processor.process_command(" ".join(com[1:]))
    com = command_provider.get_command().split()