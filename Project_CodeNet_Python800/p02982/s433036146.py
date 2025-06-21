import itertools
import math
n,d = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]
m = 0
for h in itertools.combinations(x, 2):
    num = 0
    for j in range(d):
        num += (h[0][j]-h[1][j])**2
    if math.sqrt(num).is_integer() == True:
        m += 1
print(m)