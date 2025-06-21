#!/usr/bin/env python3
input()
(*a, ) = map(int, input().split())
d = (-1, 0, 1)
ans = [0] * (10**5 + 1)
for i in a:
    for j in d:
        if 0 <= i + j <= 10**5:
            ans[i + j] += 1
print(max(ans))
