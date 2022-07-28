t=int(input())
while(t):
    n=int(input())
    A=set(map(int,input().split()))
    m=int(input())
    B=set(map(int,input().split()))
    if A.union(B)==B:
        print(True)
    else:
        print(False)
    t=t-1