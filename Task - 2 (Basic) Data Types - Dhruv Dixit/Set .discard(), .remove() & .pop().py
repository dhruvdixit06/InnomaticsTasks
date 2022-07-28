n = int(input())
s = set(map(int, input().split()))
N=int(input())
for _ in range(N):
    command=input()
    arr=command.split(' ')
    if(arr[0]=="pop"):
        s.pop()
    elif(arr[0]=="remove"):
        s.remove(int(arr[1]))
    elif(arr[0]=="discard"):
        s.discard(int(arr[1]))
print(sum(s))
