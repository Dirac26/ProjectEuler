def gen_fib_list(num):
    """function to generate fibonacci sequence capped by num for largest element"""
    a, b = 0, 1
    fib_list = [a, b]
    while b < num:
        a, b = b, a + b
        fib_list.append(b)
    return fib_list

def even_fib_list(fib_list):
    """function to filter odd numbers of a list"""
    return [x for x in fib_list if x % 2 == 0]

def sum_list(in_list):
    """function to sum elements of a list"""
    sum = 0
    for elm in in_list:
        sum = sum + elm
    return sum

def main():
    print(sum_list(even_fib_list(gen_fib_list(4000000))))

if __name__ == "__main__":
    main()