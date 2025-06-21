import collections

N = int(input())
A = [int(x) for x in input().split()]

ruiseki = [0]

for a in A:
    ruiseki.append(ruiseki[-1] + a)

c = collections.Counter(ruiseki)

ans = 0
for k in c.keys():
    if c[k] >= 2:
        ans += c[k] * (c[k] - 1) // 2

print(ans)
