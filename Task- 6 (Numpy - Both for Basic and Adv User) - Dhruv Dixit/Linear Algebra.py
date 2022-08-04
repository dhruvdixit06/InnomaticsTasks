import numpy
numpy.set_printoptions(legacy='1.13')
n=int(input())
a=numpy.zeros((n,n),float)
for i in range(n):
    a[i]=numpy.array(input().split(),float)
print(round(numpy.linalg.det(a),2))
