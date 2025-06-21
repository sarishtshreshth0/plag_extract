from itertools import groupby
n = int(input())
s = input()

gr = groupby(s)
ans = 0
for key, value in gr:
    ans += 1

print(ans)