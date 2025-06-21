from collections import Counter
n = int(input())
ns = list(map(int, input().split()))
cum = []
a = 0
for i in ns:
    a += i
    cum.append(a)
c = Counter(cum)
ans = 0
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result
for value in c.values():
    if value > 1:
        ans += cmb(value, 2)
print(ans + c[0])
