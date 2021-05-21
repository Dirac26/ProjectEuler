import math

def int_pyth_tuple(sum_abc):
    """Returns the prduct of the pythagorean triplet with the sum sum_abc"""
    for a in range(1, sum_abc):
        for b in range(1, sum_abc):
            c = math.sqrt( a** 2 + b ** 2)
            if a + b + c == sum_abc:
                return int(a * b * c)

def main():
    """main funtion"""
    print(int_pyth_tuple(1000))

if __name__ == "__main__":
    main()