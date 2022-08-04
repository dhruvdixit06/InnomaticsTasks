import numpy

arr=[]
n,m=input().split()
for i in range(int(n)):
    arr.append(list(map(int,input().split())))
my_arr=numpy.array(arr)
print(my_arr.transpose())
print(my_arr.flatten())