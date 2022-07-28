n,m=input().split()
arr=[]
n=int(n)
h=0
arr = list(map(int, input().split()))
A=set(map(int, input().split()))
B=set(map(int, input().split()))
for i in arr:
    if i in A:
        h=h+1
    elif i in B:
        h=h-1
print(h)