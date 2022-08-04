import numpy

arr1=[]
arr2=[]
n,m,p=map(int,input().split())
for i in range(0,int(n)):
    arr1.append(list(map(int,input().split()))[:p])
for i in range(0,int(m)):
    arr2.append(list(map(int,input().split()))[:p])
my_arr1=numpy.array(arr1)
my_arr2=numpy.array(arr2)
print(numpy.concatenate((my_arr1,my_arr2)))