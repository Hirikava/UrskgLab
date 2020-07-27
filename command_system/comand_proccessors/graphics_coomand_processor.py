from  command_system.command_processor import ICommandProcessor
import argparse

def __get_argoarse_configuration__():
    parser = argparse.ArgumentParser(description="Graphics argument parser")
    parser.add_argument("--shape", "-s", dest="shape")
    return parser

class GraphicsCommandProcessor(ICommandProcessor):
    def __init__(self,log,image):
        self.image = image
        self.log = log

    def process_command(self, command_tokens):
        self.image.show()
