# A - Zero-Sum Ranges
import numpy as np

N = int(input())
A = list(map(int, input().split()))
S = np.zeros(N+1)
ans = 0

for i in range(N):
    S[i+1] = S[i] + A[i]

S.sort()
tmp = 1

for i in range(N):
    if S[i]==S[i+1]:
        tmp += 1
    else:
        ans += tmp * (tmp-1) // 2
        tmp = 1
ans += tmp * (tmp-1) // 2

print(ans)