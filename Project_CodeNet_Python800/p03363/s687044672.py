import collections
import math

n = int(input())
a = list(map(int, input().split(" ")))

s = [0]
for i in range(1, n + 1):
    s.append(s[i-1] + a[i-1] )

ans = 0
for v in collections.Counter(s).values():
    if v >= 2:
        ans += math.factorial(v) // (math.factorial(v - 2) * math.factorial(2))
print(ans)