import itertools
import math
n,d = map(int,input().split())
xl = []
for _ in range(n):
    x = list(map(int,input().split()))
    xl.append(x)

cnt = 0
for v in itertools.combinations(xl,2):
    x, y = v[0], v[1]
    sum = 0
    for i in range(d):
        sum += (x[i]-y[i])**2
    dist = math.sqrt(sum)
    if dist.is_integer():
        cnt += 1
print(cnt)