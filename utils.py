import argparse

def check_color_variable(value):
    val = int(value)
    if(val < 0 or val > 255):
        raise argparse.ArgumentTypeError("%s RGB componenst should be between 0 and 255" % value)
    return val


def check_size(value):
    val = int(value)
    if(val < 0):
        raise argparse.ArgumentTypeError("%s Image size should be positive" % value)
    return val
