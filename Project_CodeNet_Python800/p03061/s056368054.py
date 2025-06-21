from fractions import gcd
n = int(input())
a = list(map(int, input().split()))
sf = [a[0]] * n
for i in range(1, n):
    sf[i] = gcd(sf[i - 1], a[i])
sb = [a[n - 1]] * n
for i in range(n - 2, -1, -1):
    sb[i] = gcd(sb[i + 1], a[i])
ans = 1
for i in range(n):
    if i == 0:
        ans = max(ans, sb[1])
    elif i == n - 1:
        ans = max(ans, sf[n - 2])
    else:
        ans = max(ans, gcd(sf[i - 1], sb[i + 1]))
print(ans)
