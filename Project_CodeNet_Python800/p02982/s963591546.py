import math

n,d = map(int,input().split())
ans = 0
li=[list(map(int,input().split())) for i in range(n)]

for i in range(n-1):
    for j in range(i+1,n):
        cnt = 0
        for k in range(d):
            cnt += (li[i][k] - li[j][k])**2
        if math.sqrt(cnt).is_integer():
            ans += 1

print(ans)