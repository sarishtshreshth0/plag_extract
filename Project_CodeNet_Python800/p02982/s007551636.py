def distance(a,b):
    return abs((a-b)**2)

import math

n,d = map(int,input().split())
x = []
for i in range(n):
    x.append(list(map(int,input().split())))
ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        current = 0
        for k in range(d):
            current += distance(x[i][k],x[j][k])
        current = math.sqrt(current)
        if float.is_integer(current):
            ans += 1
print(ans)