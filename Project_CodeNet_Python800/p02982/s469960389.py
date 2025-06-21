from itertools import combinations
from math import sqrt

n,d = map(int,input().split())
x = [list(map(int,input().split())) for _ in range(n)]

count = 0
for i,j in combinations(range(n),2):
    ans = 0
    for k in range(d):
        ans += (x[i][k]-x[j][k])**2
    if sqrt(ans).is_integer():
        count += 1
print(count)