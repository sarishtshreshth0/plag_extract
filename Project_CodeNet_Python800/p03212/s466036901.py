N = int(input())

L = len(str(N))

import math
import itertools

ans = 0

for now_L in range(3, L):
    for a in list(itertools.product([3,5,7], repeat=now_L)):
        num = int("".join(map(str, a)))

        if set(a) == set([3,5,7]):
            ans += 1
        
for a in list(itertools.product([3,5,7], repeat=L)):
    num = int("".join(map(str, a)))
    if num > N:
        break

    if set(a) == set([3,5,7]):
        ans += 1

print(ans)