import sys
from command_system.command_processor import ICommandProcessor
import argparse

def __get_argoarse_configuration__():
    parser = argparse.ArgumentParser(description="Log argument parser")
    parser.add_argument("--level", "-l", dest="level")
    parser.add_argument("--message", "-m", nargs='+', dest="message")
    return parser

def __format__(message):
    return " ".join(message)


class LogCommandProcessor(ICommandProcessor):
    def __init__(self, log):
        self.log = log
        self.parser = __get_argoarse_configuration__()

    def process_command(self, command_arguments):
        args = self.parser.parse_args(command_arguments.split())
        try:
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
            else:
                self.log.Info(__format__(args.message))
        except:
            e = sys.exc_info()[0]
            self.log.Error(e)

