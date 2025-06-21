import numpy as np
import math
n,d = map(int, input().split())
x = np.array(list(input().split() for _ in range(n)), dtype=int)
ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        s = math.sqrt(sum((x[i]-x[j])**2))
        if s.is_integer():
            ans += 1
print(ans)