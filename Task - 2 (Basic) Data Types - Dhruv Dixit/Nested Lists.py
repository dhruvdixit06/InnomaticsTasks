if __name__ == '__main__':
    res=[]
    coll=[]
    sc=set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        coll.append([name,score])
        sc.add(score)
    sc=sorted(sc)
    slowest=sc[1]
    for name,score in coll:
        if(score==slowest):
            res.append(name)
    res=sorted(res)
    for name in res:
        print(name)