def gcd(a, b):
    if a < b:
        return gcd(b, a)
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())
a = list(map(int, input().split()))
l = a[:]
r = a[:]

for i in range(n-1):
    l[i+1] = gcd(l[i], l[i+1])
    r[-i-2] = gcd(r[-i-1], r[-i-2])

max_val = max(l[-2], r[1])
for i in range(1, n-1):
    max_val = max(max_val, gcd(l[i-1], r[i+1]))
print(max_val)

