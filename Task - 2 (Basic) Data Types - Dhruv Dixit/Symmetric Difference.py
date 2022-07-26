M=int(input())
m=set(map(int,input().split()))
N=int(input())
n=set(map(int,input().split()))
un=sorted(m.union(n))
inter=m.intersection(n)
for i in un:
    if i not in inter:
        print (i)