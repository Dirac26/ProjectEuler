import sys
import argparse

def argparser(arg):
    """ a method to parse arguments """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-input', required=True, 
                    help='a file with input numbers to be processed')

    args = parser.parse_args(arg)
    return args

def parse_input_file(path):
    """ a method to parse input file and return list of the numbers """
    numbers_list = []
    with open(path, "r") as input_file:
        for line in input_file:
            numbers_list.append(int(line.strip()))
    return numbers_list

def main(args):
    """ main method """
    numbers = parse_input_file(args.input)
    print(str(sum(numbers))[:10])





if __name__ == "__main__":
    ARGS = argparser(sys.argv[1:])
    main(ARGS)
