def gcd(a, b):
    if a < b:
        tmp = a
        a = b
        b = tmp
    while b != 0:
        a, b = b, a%b
    return a

n = int(input())
a = list(map(int, input().split()))
l = [a[0]] * n
r = [a[n-1]] * n
for i in range(1, n):
    l[i] = gcd(l[i-1], a[i-1])
for i in range(n-2, -1, -1):
    r[i] = gcd(r[i+1], a[i+1])
l[0] = r[0]
r[n-1] = l[n-1]
ans = 0
for i in range(n):
    ans = max(ans, gcd(l[i], r[i]))
print(ans)