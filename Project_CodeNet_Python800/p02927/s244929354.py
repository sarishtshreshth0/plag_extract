m,n = map(int,input().split())

cnt = 0
for i in range(1,m+1):
    for j in range(10,n+1):
        num = 1
        d = str(j)
        l = len(d)
        
        for k in range(l):
            if int(d[k]) < 2:
                num =1
                break
            else:
                num *=int(d[k])
        if num == i and num !=1:
            cnt +=1
print(cnt)