def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


n = int(input())
A = list(map(int, input().split()))

gcd_from_left = [0]*n
gcd_from_right = [0]*n

for i in range(1, n):
    gcd_from_left[i] = gcd(A[i-1], gcd_from_left[i-1])
    gcd_from_right[n-i-1] = gcd(A[n-i], gcd_from_right[n-i])

ans = 0

for a, b in zip(gcd_from_left, gcd_from_right):
    x = gcd(a, b)
    if ans < x:
        ans = x

print(ans)
