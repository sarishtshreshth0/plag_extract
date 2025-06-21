
from math import gcd

N = int(input())
X = list(map(int, input().split()))

left = [0] * (N + 2)
right = [0] * (N + 2)

for i in range(N):
    left[i + 1] = gcd(left[i], X[i])

for i in reversed(range(N)):
    right[i + 1] = gcd(right[i + 2], X[i])

ans = 1
for i in range(N):
    ans = max(ans, gcd(left[i], right[i + 2]))

print(ans)
