from fractions import gcd

n = int(input())
A = list(map(int, input().split()))

left = [0]*n
right = [0]*n

for i in range(n-1):
    left[i+1] = gcd(left[i], A[i])
    right[n-i-2] = gcd(right[n-i-1], A[n-i-1])

ans = 0
for i in range(n):
    ans = max(ans, gcd(left[i], right[i]))
print(ans)
