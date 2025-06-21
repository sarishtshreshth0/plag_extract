import math

N = int(input())
A = [int(n) for n in input().split()]

gcd_l = [0]
gcd_r = [0]


for i in range(N):
    gcd_l.append(math.gcd(gcd_l[i], A[i]))
    gcd_r.append(math.gcd(gcd_r[i], A[-(i+1)]))

gcd_r = gcd_r[::-1]

max_gcd = 0
for i in range(N):
    max_gcd = max(max_gcd, math.gcd(gcd_l[i], gcd_r[i+1]))

print(max_gcd)