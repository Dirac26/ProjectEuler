import sys
import argparse
from math import comb

def argparser(arg):
    """ a method to parse arguments """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-input_x', required=True, type=int,
                    help='grids in x')
    parser.add_argument('-input_y', required=True, type=int,
                    help='grids in ')

    args = parser.parse_args(arg)
    return args

def calc_grid_paths(x, y):
    """ return x*y grid in for of list """
    perm_len = x + y
    return comb(perm_len, x)


def main(args):
    """ main method """
    print(calc_grid_paths(args.input_x, args.input_y))





if __name__ == "__main__":
    ARGS = argparser(sys.argv[1:])
    main(ARGS)
