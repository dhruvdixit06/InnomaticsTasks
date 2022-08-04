import numpy

n,m=map(int,input().split())
a=numpy.zeros((n,m),int)
t=[]
for i in range(n):
    a[i]=numpy.array(input().split(),int)
m=1
for i in range(m):
    t.append(numpy.sum(a,axis=0))
print(numpy.prod(t,axis=None))