def sum_num(num):
    """retur the sum of integers from 1 to num"""
    return num*(num+1)/2

def sum_squar(num):
    """retur the sum of the squar of the integers from 1 to num"""
    return num*(num+1)*(2*num+1)/6
def main():
    """main funtion"""
    result = (sum_num(100) ** 2) - sum_squar(100) 
    print(result)
if __name__ == "__main__":
    main()