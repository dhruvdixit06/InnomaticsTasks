import numpy

a=numpy.array(input().split(),float)
x=int(input())
print(numpy.polyval(a,x))