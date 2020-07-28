from command_system.command_processor import ICommandProcessor
from argument_parser import ArgumentParser
from exceptions import ArgumentException
import argparse


def check_color_variable(value):
    val = int(value)
    if(val < 0 or val > 255):
        raise argparse.ArgumentTypeError("%s RGB componenst should be between 0 and 255" % value)
    return val

def __get_argparse_configuration__():
    parser = ArgumentParser(description="Graphics argument parser", usage=argparse.SUPPRESS)
    parser.add_argument("--shape", "-s", dest="shape", choices=["Circle","Rectangle"], required=True)
    parser.add_argument("--color", "-c", type=check_color_variable, nargs=3, dest="color")
    parser.add_argument("--area", "-a", type=int, nargs=4, dest="area", required=True)
    return parser

class GraphicsCommandProcessor(ICommandProcessor):
    def __init__(self,log,image):
        self.image = image
        self.log = log
        self.parser = __get_argparse_configuration__()

    def process_command(self, command_arguments):
        try:
            arguments = self.parser.parse_args(command_arguments.split())
            print(arguments.color)
        except ArgumentException as e:
            self.log.Error(e.message)
            return

