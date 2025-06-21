N = int(input())
A = list(map(int,input().split()))
C = [0]
for a in A:
    C.append(C[-1] + a)
from collections import Counter
ctr = Counter(C)
ans = 0
for v in ctr.values():
    ans += v*(v-1)//2
print(ans)