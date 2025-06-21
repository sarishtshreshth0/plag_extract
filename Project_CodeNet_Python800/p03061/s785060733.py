from fractions import gcd as m_gcd

n = int(input())
a = list(map(int, input().split()))


def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    return m_gcd(a, b)


l = [0] * (n + 2)
r = [0] * (n + 2)
ans = [0] * n

for i in range(1, n+1):
    l[i] = gcd(l[i - 1], a[i - 1])
    r[n - i + 1] = gcd(r[n - i + 2], a[n - i])

for i in range(1, n + 1):
    ans[i-1] = gcd(l[i-1], r[i+1])

print(max(ans))
