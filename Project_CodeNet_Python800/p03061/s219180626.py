from fractions import gcd

n = int(input())
a = list(map(int, input().split()))
left = a[:]
right = a[:]
for i in range(1, n):
  left[i] = gcd(left[i], left[i-1])
  right[n-i-1] = gcd(right[n-i], right[n-i-1])
maximum = max(left[n-2], right[1])
for i in range(n-2):
  common_divisor = gcd(left[i], right[i+2])
  if common_divisor > maximum:
    maximum = common_divisor
print(maximum)