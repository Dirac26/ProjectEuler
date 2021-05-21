import math

def primes_list(num):
    """returns Nth prime number"""
    primes_list = [2, 3]
    prime = 4
    while len(primes_list) != num:
        for n in range(2, int(math.sqrt(prime)+1)):
            if prime % n == 0:
                break
            if n == int(math.sqrt(prime)):
                primes_list.append(prime)
        prime += 1
    return(primes_list[num-1])

def main():
    """The main function"""
    print(primes_list(10001))

if __name__ == "__main__":
    main()