k=int(input())
rooms=list(map(int,input().split()))
a=set()
b=set()
for i in rooms:
    if i in a:
        b.add(i)
    else:
        a.add(i)
res=a.difference(b)
print(list(res)[0])