import math
n, d = map(int, input().split())
x = []
cnt = 0
for i in range(n):
    l = list(map(int, input().split()))
    x.append(l)
for i in range(n-1):
    for j in range(i+1, n):
        di = 0
        for k in range(d):
            di += (x[i][k] - x[j][k]) ** 2
        if math.sqrt(di).is_integer():
            cnt += 1
print(cnt)
