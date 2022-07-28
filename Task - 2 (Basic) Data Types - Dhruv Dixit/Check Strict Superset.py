A=set(map(int,input().split()))
n=int(input())
res=True
for _ in range(n):
    s=set(map(int,input().split()))
    if A.union(s)==A:
        pass
    else:
        res=False
        break
print(res)