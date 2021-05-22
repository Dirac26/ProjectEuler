import sys
import argparse
from functools import reduce

def argparser(arg):
    """ a method to parse arguments """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-input', required=True,type=int, 
                    help='an integer for the accumulator')

    args = parser.parse_args(arg)
    return args

def get_num_divisors(num):
    """ method to return number of divisors for int """
    divisors = 0
    divisor = 2
    division_list = []
    while divisor <= num:
        while num % divisor == 0:
            num = num/divisor
            divisors += 1
        if divisors != 0:
            division_list.append(divisors+1)
        divisor += 1
        divisors = 0
    return reduce(lambda val, elm: val * elm, division_list, 1)

def get_triangle_numbers_divs_over_input(divs_num):
    """ return a the first triangle number that has divs_num divisors """
    triangle_number = 0
    i = 1
    while True:
        triangle_number += i
        i += 1
        if get_num_divisors(triangle_number) > divs_num:
            break
    return triangle_number

def main(args):
    """ main method """
    answer = get_triangle_numbers_divs_over_input(args.input)
    print(answer)




if __name__ == "__main__":
    ARGS = argparser(sys.argv[1:])
    main(ARGS)
