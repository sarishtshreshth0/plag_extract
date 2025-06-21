import math


n, d = map(int, input().split())
x = []
for i in range(n):
    x.append(list(map(int, input().split())))

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        y = 0
        for k in range(d):
            y += (x[i][k] - x[j][k])**2

        y = math.sqrt(y)
        if y.is_integer():
            ans += 1
print(ans)
