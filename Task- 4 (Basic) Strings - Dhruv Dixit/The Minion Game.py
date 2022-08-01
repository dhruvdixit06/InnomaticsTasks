def minion_game(string):
    s=0
    k=0
    for i in range(0,len(string)):
        if string[i] not in ('a','e','i','o','u','A','E','I','O','U'):
            s=s+len(string)-i
        else:
            k=k+len(string)-i
    if s>k:
        ans="Stuart "+str(s)
    elif s<k:
        ans="Kevin "+str(k)
    else:
        ans="Draw"
    print (ans)
if __name__ == '__main__':
    s = input()
    minion_game(s)