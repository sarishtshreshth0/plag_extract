import sys
from collections import Counter

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

S = [0 for _ in range(N+1)]
for i in range(N):
    S[i+1] = S[i] + A[i]

ans = 0
counter = Counter(S)
for value, count in counter.items():
    ans += count * (count - 1) // 2

print(ans)