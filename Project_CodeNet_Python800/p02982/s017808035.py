n, d = map(int, input().split())
ans = 0
a = [list(map(int, input().split())) for i in range(n)]
import math
for i in range(n-1):
    for j in range(i+1, n):
        dist = math.sqrt(sum([(a[i][k]-a[j][k])**2 for k in range(d)]))
        if (int(dist) == dist):
            ans += 1
print(ans)