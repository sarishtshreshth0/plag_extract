from collections import Counter

N = [int(_) for _ in input().split()][0]
a = [int(_) for _ in input().split()]

s = [0] * (len(a) + 1)
for i in range(len(a)):
    s[i + 1] = s[i] + a[i]

c = Counter()

for i in range(len(s)):
    c[s[i]] += 1

ans = 0
for cnt in c.values():
    if cnt < 2: continue

    ans += (cnt * (cnt - 1)) // 2
print(ans)
