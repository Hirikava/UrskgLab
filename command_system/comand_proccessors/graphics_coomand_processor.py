from command_system.command_processor import ICommandProcessor
from argument_parser import ArgumentParser
from exceptions import ArgumentException
from utils import check_color_variable
from PIL import ImageDraw
import argparse


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
            image_draw = ImageDraw.Draw(self.image)
            shape = self.create_shape(arguments.area)
            color = self.create_color(arguments.color)
            if(arguments.shape == "Circle"):
                image_draw.ellipse(shape,fill=color)
                self.image.show()
            if (arguments.shape == "Rectangle"):
                image_draw.rectangle(shape, fill=color)
                self.image.show()

        except ArgumentException as e:
            self.log.Error(e.message)
            return

    def create_shape(self, shape_tokens):
        return [(shape_tokens[0],shape_tokens[1]),(shape_tokens[0] + shape_tokens[2],shape_tokens[1] + shape_tokens[3])]

    def create_color(self, color_tokens):
        return (color_tokens[0],color_tokens[1],color_tokens[2])

