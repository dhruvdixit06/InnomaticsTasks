n=int(input())
A=set(map(int,input().split()))
N=int(input())
for _ in range(N):
    command=input()
    arr=command.split(' ')
    updset=set(map(int,input().split()))
    if arr[0]=='intersection_update':
        A&=updset
    elif arr[0]=='update':
        A|=updset
    elif arr[0]=='symmetric_difference_update':
        A^=updset
    elif arr[0]=='difference_update':
        A-=updset
print(sum(A))