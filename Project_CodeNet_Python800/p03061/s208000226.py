import math
N = int(input())
A = list(map(int, input().split()))

left = [0]
gcd_left = 0
for a in A:
    gcd_left = math.gcd(gcd_left, a)
    left.append(gcd_left)
right = [0]
gcd_right = 0
for a in reversed(A):
    gcd_right = math.gcd(gcd_right, a)
    right.append(gcd_right)
right.append(0)
right = list(reversed(right))
# print(left)
# print(right)

max_gcd = 0
for i in range(1, N+1):
    sub_gcd = math.gcd(left[i-1], right[i+1])
    max_gcd = max(max_gcd, sub_gcd)
print(max_gcd)
