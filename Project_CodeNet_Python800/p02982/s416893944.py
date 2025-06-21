import math

n, d = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
c = 0
for i in range(n):
    for j in range(n):
        x = 0
        for k in range(d):
            x += (l[i][k] - l[j][k])**2
        y = math.sqrt(x)
        if y != 0 and y.is_integer():
            c += 1
print(c//2)