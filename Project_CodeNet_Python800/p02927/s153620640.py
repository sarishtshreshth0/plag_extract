def resolve():
    m,d=map(int, input().split())
    cnt=0
    for i in range(1,m+1):
        for j in range(22,d+1):
            jstr=str(j)
            j10=int(jstr[0])
            j1=int(jstr[1])
            if j1>=2 and j10>=2 and i==j1*j10:
                cnt+=1
    print(cnt)
resolve()