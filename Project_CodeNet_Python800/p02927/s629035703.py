m,d = map(int,input().split())
ans = 0
for i in range(1,m+1):
    for j in range(10,d+1):
        k = str(j)
        if int(k[0]) >= 2 and int(k[1]) >= 2:
            if i == int(k[0])*int(k[1]):
                ans += 1
print(ans)