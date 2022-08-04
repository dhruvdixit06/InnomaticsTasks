import numpy

n,m=map(int,input().split())
a=numpy.zeros((n,m),int)
for i in range(n):
    a[i]=numpy.array(input().split(),int)
print(numpy.mean(a,axis=1))
print(numpy.var(a,axis=0))
print(round(numpy.std(a),11))