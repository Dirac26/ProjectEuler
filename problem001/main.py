import sys
import argparse

def argparser(arg):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-input', required=True,type=int, 
                    help='an integer for the accumulator')
    args = parser.parse_args(arg)
    return args

def div_by35(num):
    div_list = []
    for n in range(num):
        if n % 3 == 0 or n % 5 == 0:
            div_list.append(n)
    return div_list

def sum_list(in_list):
    sum = 0
    for elm in in_list:
        sum = sum + elm
    return sum

def main(args):
    print(sum_list(div_by35(args.input)))




if __name__ == "__main__":
    ARGS = argparser(sys.argv[1:])
    main(ARGS)

