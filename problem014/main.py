import sys
import argparse

def argparser(arg):
    """ a method to parse arguments """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-input', required=True, type=int, 
                    help='number to calculate longest chain under')

    args = parser.parse_args(arg)
    return args

def apply_odd_equation(num):
    """ apply 3n+1 on num """
    return 3 * num + 1

def apply_even_equation(num):
    """ apply n/2 on num """
    return num/2

def apply_chain_for_num(num):
    """ apply num chain on the num """
    itters = 0
    while num != 1:
        if num % 2 == 0:
            num = apply_even_equation(num)
        else:
            num = apply_odd_equation(num)
        itters += 1
    return itters

def main(args):
    """ main method """
    largest_chain = (0, 0)
    for num in range(1, args.input):
        num_chain = apply_chain_for_num(num)
        if num_chain > largest_chain[1]:
            largest_chain = (num, num_chain)
    print(largest_chain[0], largest_chain[1])







if __name__ == "__main__":
    ARGS = argparser(sys.argv[1:])
    main(ARGS)
