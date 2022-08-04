import numpy

def arrays(arr):
    a=numpy.array(arr,float)
    a=a[::-1]
    return a
arr = input().strip().split(' ')
result = arrays(arr)
print(result)