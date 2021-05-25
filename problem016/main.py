import sys
import argparse
from functools import reduce

def argparser(arg):
    """ a method to parse arguments """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-input', required=True, type=int,
                    help='input power')
    args = parser.parse_args(arg)
    return args

def add_number_digits(num):
    """ add all digits of a number """
    return reduce(lambda v, n: int(n) + v, str(num), 0)


def main(args):
    """ main method """
    print(add_number_digits(2 ** args.input))





if __name__ == "__main__":
    ARGS = argparser(sys.argv[1:])
    main(ARGS)
