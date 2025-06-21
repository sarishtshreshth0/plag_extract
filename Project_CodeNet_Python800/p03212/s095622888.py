N = int(input())
from itertools import product
ans = 0
for i in range(3,len(str(N))+1):
    for ptn in product('753',repeat=i):
        s = ''.join(ptn)
        for c in '753':
            if c not in s:
                break
        else:
            if int(''.join(ptn)) <= N:
                ans += 1
print(ans)