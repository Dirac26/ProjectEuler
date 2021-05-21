def largest_prime(input_num):
    """returns the largest prime factor of a num"""
    largest = None
    num = input_num
    n = 2
    while n ** 2 <= input_num:
        while num % n == 0:
            num = num / n
            largest = n
        n += 1
    if largest is None: return input_num
    return largest
def main():
    print(largest_prime(600851475143))

if __name__ == "__main__":
    main()