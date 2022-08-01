def merge_the_tools(string, k):
     for i in range(0,len(string), k):
        s=string[i:i+k]
        ans= ""
        for i in s:
            if i not in ans:
                ans+=i
        print(ans)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)