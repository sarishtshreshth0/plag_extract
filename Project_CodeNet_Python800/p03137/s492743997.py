#!/usr/bin/env python3

n, m = map(int, input().split())
x = list(map(int, input().split()))

x = sorted(x)
diff = [0 for _ in range(m-1)]
for i in range(m-1):
    diff[i] = x[i+1] - x[i]

diff = sorted(diff, reverse=True)
ans = sum(diff[n-1:])
print(ans)