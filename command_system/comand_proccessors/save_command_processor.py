from command_system.command_processor import ICommandProcessor
from argument_parser import ArgumentParser
from exceptions import ArgumentException
import sys
import argparse

def __get_argparse_configuration__():
    parser = ArgumentParser(description="Save argument parser", usage=argparse.SUPPRESS)
    parser.add_argument("--file","-f", type=str, dest="file", required=False)
    return parser


class SaveCommandProcessor(ICommandProcessor):
    def __init__(self,image,log):
        self.image = image
        self.parser = __get_argparse_configuration__()
        self.log = log

    def process_command(self, command_arguments):
        try:
            arguments = self.parser.parse_args(command_arguments.split())
            self.image.save(arguments.file)
        except ArgumentException as e:
            self.log.Error(e)
        except:
            e = sys.exc_info()[0]
            self.log.Error(str(e))


