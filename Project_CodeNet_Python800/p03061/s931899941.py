def gcd(a, b):
    return gcd(b, a % b) if b > 0 else a


n = int(input())
a = list(map(int, input().split()))

al = [0] * (n + 2)
ar = [0] * (n + 2)

for i in range(1, n + 1):
    al[i] = gcd(a[i - 1], al[i - 1])

for j in range(n, 0, -1):
    ar[j] = gcd(a[j - 1], ar[j + 1])

ans = 0

for i in range(n):
    num = gcd(al[i], ar[i + 2])
    ans = max(ans, num)

print(ans)
