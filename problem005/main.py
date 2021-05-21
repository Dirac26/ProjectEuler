import math

def lcm_n(num):
    """return the least divisable number by all numbers less or equal to num"""
    result = 1
    for n in range(2,num):
        result = int(result *n / math.gcd(n,result))
    return result
    
def main():
    """main funtion"""
    print(lcm_n(20))

if __name__ == "__main__":
    main()