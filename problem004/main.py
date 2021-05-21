def is_palindromic(num):
    """Return true if the number is palindromic and false otehrwise"""
    return str(num) == str(num)[::-1]

def dividable_with_indigits(num, digits):
    """Returns true if num is a product of two integers within the digits range"""
    within = range(10 ** digits - 1)
    for n in within[1:]:
        if num % n == 0:
            if num / n <= 10 ** digits - 1:
                return True
    return False

def largest_mult(digits):
    """Returns the largest palindromic number that is the product of two numbers with certain digits number"""
    num = (10 ** digits - 1) ** 2
    found = False
    while not found:
        if is_palindromic(num):
            if dividable_with_indigits(num, digits):
                return num
        num -= 1

def main():
    """main funtion"""
    print(largest_mult(3))

if __name__ == "__main__":
    main()