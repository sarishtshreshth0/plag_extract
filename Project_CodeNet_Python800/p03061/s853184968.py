n = int(input())
a = list(map(int, input().split()))
l = [0 for _ in range(n)]
r = [0 for _ in range(n)]
def gcd(x, y):
    x, y = max(x, y), min(x, y)
    while y:
        x, y = y, x % y
    return x
for i in range(n):
    if i == 0:
        l[0] = a[0]
    else:
        l[i] = gcd(l[i-1], a[i])
    j = n - 1 - i
    if j == n - 1:
        r[n-1] = a[n-1]
    else:
        r[j] = gcd(r[j+1], a[j])
m = [0 for _ in range(n)]
for i in range(n):
    if i == 0:
        m[0] = r[1]
    elif i == n - 1:
        m[n-1] = l[n-2]
    else:
        m[i] = gcd(l[i-1], r[i+1])
print(max(m))