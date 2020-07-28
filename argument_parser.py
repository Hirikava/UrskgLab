import argparse
from exceptions import ArgumentException

class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentException(message)