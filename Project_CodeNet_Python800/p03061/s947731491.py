import fractions

n = int(input())
a = list(map(int, input().split()))
b = a[::-1]

left = [0, a[0]]
right = [0, b[0]]
l = a[0]
r = b[0]
for i in range(1, n):
    l = fractions.gcd(l, a[i])
    r = fractions.gcd(r, b[i])
    left.append(l)
    right.append(r)

gcd_max = 0
for i in range(n+1):
    gcd_tmp = fractions.gcd(left[i], right[n-i-1])
    if gcd_tmp > gcd_max:
        gcd_max = gcd_tmp

print(gcd_max)
