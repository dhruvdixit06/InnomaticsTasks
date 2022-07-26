if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    arr2=[]
    m=max(arr)
    for i in arr:
        if(i!=m):
            arr2.append(i)
    print(max(arr2))