m,d = map(int,input().split())
ans = 0
for i in range(1,m+1):
    for j in range(1,d+1):
        r = list(str(j))
        if len(r) >= 2:
            if int(r[0])*int(r[1]) == i and int(r[0]) >= 2 and int(r[1]) >= 2:
                ans += 1
                #print(i,j)
print(ans)