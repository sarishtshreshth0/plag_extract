N = int(input())
A = list(map(int, input().split()))

sa = [0 for _ in range(N)]
sa[0] = A[0]
for i in range(1, N):
    sa[i] = sa[i-1] + A[i]

from collections import Counter
ca = Counter(sa)
ans = 0
for k, v in ca.items():
    if k == 0:
        ans += v
    
    if v >= 2:
        ans += v * (v-1) // 2
print(ans)