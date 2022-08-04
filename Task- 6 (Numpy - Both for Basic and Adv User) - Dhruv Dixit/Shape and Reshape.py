import numpy

arr=list(map(int,input().split()))
my_array = numpy.array(arr)
print(numpy.reshape(my_array,(3,3)))
