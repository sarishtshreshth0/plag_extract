import math

n, x = list(map(int, input().split()))
a = list(map(int, input().split()))

d =  abs(a[0] - x)

for i in range(1, n):
    d = math.gcd(d, abs(a[i] - x))

print(d)