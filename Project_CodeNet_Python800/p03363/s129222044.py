from itertools import accumulate

n = int(input())
a = [int(i) for i in input().split()]
a_ac = [0] + list(accumulate(a))
d = {}
for i in a_ac:
    d.setdefault(i, 0)
    d[i] += 1

ans = 0
for i in d.values():
    ans += i * (i - 1) // 2
print(ans)