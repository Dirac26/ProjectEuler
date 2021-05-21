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

def main():
    print(sum_list(div_by35(1000)))




if __name__ == "__main__":
    main()

