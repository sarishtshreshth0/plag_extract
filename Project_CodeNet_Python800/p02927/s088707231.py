m,d = map(int,input().split())
ans = 0
for i in range(2,m+1):
    for j in range(22,d+1):
        if j%10 == 1:
            continue
        ans += (i == (j//10)*(j%10))
print(ans)