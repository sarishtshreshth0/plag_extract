import math
def distance(x, y):
    b = 0
    for k in range(d):
        b += (x[k] - y[k]) ** 2
    return float(math.sqrt(b))

n, d = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]
a = 0
for j in range(n - 1):
    for i in range(j + 1):
        if distance(x[i], x[j + 1]) == math.floor(distance(x[i], x[j + 1])):
            a += 1
print(int(a))