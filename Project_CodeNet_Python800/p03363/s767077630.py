n = int(input())
a = list(map(int, input().split()))
ca = [0] * (len(a) + 1)
for i in range(n):
    ca[i + 1] = ca[i] + a[i]


# TLE
# ans = 0
# for i in range(n):
#     # print(a[i], ca[i], ca, ca[i + 1:], ca[i + 1:].count(ca[i]))
#     ans += ca[i + 1:].count(ca[i])
# print(ans)

from collections import Counter

ans = 0
cac = Counter(ca)
# print(cac)
# ca.sort()
for v, c in cac.items():
    if c >= 2:
        ans += c * (c - 1) // 2
print(ans)