from collections import Counter
import numpy as np
n = int(input())
A = [0] + list(np.cumsum(list(map(int, input().split()))))
a = Counter(A[1:])
ans = 0
for x,y in a.items():
    if x == 0: ans += y
    if y >= 2:
        ans += y*(y-1)//2
print(ans)