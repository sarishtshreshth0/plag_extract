from fractions import gcd

N = int(input())
A = tuple(map(int, input().split()))

gcd_left, gcd_right = [0] * N, [0] * N
gcd_left[0] = A[0]
gcd_right[-1] = A[-1]
for i in range(1, N):
    gcd_left[i] = gcd(gcd_left[i - 1], A[i])
for i in range(N - 2, -1, -1):
    gcd_right[i] = gcd(gcd_right[i + 1], A[i])

gcd_left = [gcd_right[-1]] + gcd_left
gcd_right = gcd_right + [gcd_left[1]]
ans = 1
for i in range(N):
    ans = max(ans, gcd(gcd_left[i], gcd_right[i + 1]))
print(ans)
