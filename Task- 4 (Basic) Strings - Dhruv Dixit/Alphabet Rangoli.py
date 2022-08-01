def print_rangoli(size):
    s= 'abcdefghijklmnopqrstuvwxyz'[0:size]
    for i in range(size-1, -size, -1):
        n = abs(i)
        a=s[size:n:-1]
        b=s[n:size]
        l=a+b
        print ("--"*n+'-'.join(l)+"--"*n)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)