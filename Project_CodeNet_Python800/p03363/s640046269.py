from collections import Counter
from math import factorial

N = int(input())
A = list(map(int, input().split()))
memo = [0]*(N+1)
for i in range(1, N+1):
    memo[i] = memo[i-1] + A[i-1]

cnt = 0
C = Counter(memo)

for c in C.values():
    if c > 1:
        cnt += (factorial(c)/(2*factorial(c-2)))

print(int(cnt))