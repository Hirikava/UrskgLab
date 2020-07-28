from exceptions import ArgumentException
from argument_parser import ArgumentParser
from command_system.command_processor import ICommandProcessor
import argparse

def __get_argparse_configuration__():
    parser = ArgumentParser(description="Log argument parser", usage=argparse.SUPPRESS)
    parser.add_argument("--level", "-l", dest="level", default="Debug", required=False, choices=['Warn', 'Info', 'Debug', 'Error'])
    parser.add_argument("--message", "-m", nargs='+', dest="message", required=True)
    return parser

def __format__(message):
    return " ".join(message)

class LogCommandProcessor(ICommandProcessor):
    def __init__(self, log):
        self.log = log
        self.parser = __get_argparse_configuration__()

    def process_command(self, command_arguments):
        try:
            args = self.parser.parse_args(command_arguments.split())
            if(args.level):
                if(args.level == "Warn"):
                    self.log.Warn(__format__(args.message))
                elif (args.level == "Info"):
                    self.log.Info(__format__(args.message))
                elif (args.level == "Error"):
                    self.log.Error(__format__(args.message))
                elif (args.level == "Debug"):
                    self.log.Debug(__format__(args.message))
                else:
                    self.log.Info(__format__(args.message))
        except ArgumentException as e:
            self.log.Error(e.message)

