import math
n, d = list(map(int, input().split()))
x = []
for i in range(n):
    x_i = list(map(int, input().split()))
    x.append(x_i)
c = 0
for i in range(n):
    for j in range(i + 1, n):
        d_ij = 0
        for k in range(d):
            d_ij += (x[i][k] - x[j][k]) ** 2
        d_ij = math.sqrt(d_ij)
        if d_ij.is_integer():
            c += 1
print(c)