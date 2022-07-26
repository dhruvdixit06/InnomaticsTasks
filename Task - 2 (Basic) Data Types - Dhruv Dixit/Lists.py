if __name__ == '__main__':
    N = int(input())
    res=[]
    for _ in range(0,N):
        command = input()
        arr=command.split(' ')
        if arr[0] == 'insert':
            i = int(arr[1])
            e = int(arr[2])
            res.insert(i,e)
        elif arr[0] == 'print':
            print(res)
        elif arr[0] == 'remove':
            e = int(arr[1])
            res.remove(e)
        elif arr[0] == 'append':
            e = int(arr[1])
            res.append(e)
        elif arr[0] == 'sort':
            res.sort()
        elif arr[0] == 'pop':
            res.pop()
        elif arr[0] == 'reverse':
            res.reverse()