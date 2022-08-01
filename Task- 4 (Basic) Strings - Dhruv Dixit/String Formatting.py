def print_formatted(number):
    width=len(bin(number))-2
    for i in range(1,number+1):
        for base in ('d', 'o', 'X', 'b'):
            print("{0:{width}{base}}".format(i, base=base, width=width), end=' ')
        print()
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)