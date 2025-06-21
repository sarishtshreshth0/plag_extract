n = int(input())
d = list(map(int, input().split()))
dist = [0]*n

for i in range(n):
    dist[d[i]] += 1

ans = 1

if d[0]!=0:
    ans = 0
elif dist[0] != 1:
    ans = 0
else:
    for i in range(2,n):
        if dist[i-1]==0 and dist[i]!=0:
            ans = 0
            break
        elif dist[i] == 0:
            continue
        else:
            for j in range(dist[i]):
                ans *= dist[i-1]
            if ans > 998244353:
                ans %= 998244353

print(ans)
