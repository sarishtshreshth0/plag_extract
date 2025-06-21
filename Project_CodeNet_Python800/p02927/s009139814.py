M,D = map(int,input().split())
cnt = 0
lists = []
for i in range(1,M+1):
    for j in range(10,D+1):
        if i == j:
            pass
        else:
            m = str(i)
            d = str(j)
            d10 = int(d[0])
            d1 = int(d[-1])
            
            if d1 >= 2 and d10 >= 2 and  int((d1*d10)) == int(m):
                cnt += 1

        
print(cnt)
