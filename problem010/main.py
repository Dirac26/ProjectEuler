import math

def primes_sum(num):
    """returns the sum of the primes numbers below num"""
    primes_sum = 5
    prime = 4
    while prime < num:
        for n in range(2, int(math.sqrt(prime)+1)):
            if prime % n == 0:
                break
            if n == int(math.sqrt(prime)):
                primes_sum += prime
        prime += 1
    return(primes_sum)

def main():
    """The main function"""
    print(primes_sum(2000000))

if __name__ == "__main__":
    main()