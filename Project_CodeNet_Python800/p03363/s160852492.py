from collections import Counter


def comb(n, r):
    ans = 1
    for i in range(1, r+1):
        ans = ans * ((n + 1 - i) / i)

    return int(ans)


n = int(input())

a = list(map(int, input().split()))

d = [0]

for i in range(n):
    d.append(d[i]+a[i])

d.sort()

cd = Counter(d)
ans = 0
for k in cd.keys():
    if cd[k] >= 2:
        ans += comb(cd[k], 2)

print(ans)
