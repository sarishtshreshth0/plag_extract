import math

n = int(input())
a = list(map(int, input().split()))

gcd_left = []
gcd_right = []
for i in range(n):
    if i == 0:
        gcd_left.append(a[i])
        gcd_right.append(a[n - 1 - i])
    else:
        gcd_left.append(math.gcd(a[i], gcd_left[i - 1]))
        gcd_right.append(math.gcd(a[n - 1 - i], gcd_right[i - 1]))
gcd_right.reverse()

gcd_ex = []
for i in range(n):
    if i == 0:
        gcd_ex.append(gcd_right[i + 1])
    elif i == n - 1:
        gcd_ex.append(gcd_left[i - 1])
    else:
        gcd_ex.append(math.gcd(gcd_left[i - 1], gcd_right[i + 1]))
print(max(gcd_ex))
