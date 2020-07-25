import sys
import argparse

argument_parser = argparse.ArgumentParser("Process configuration")
argument_parser.add_argument('--log','-l',metavar='N',default='console', dest="logging")

args = argument_parser.parse_args()
print(args.logging)
