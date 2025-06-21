from fractions import gcd

N = int(input())
A = list(map(int, input().split()))

gcd_from_left = [0] * (N + 1) 
gcd_from_right = [0] * (N + 1)
gcd_from_left[1] = A[0]
for i in range(2, N + 1):
    gcd_from_left[i] = gcd(A[i - 1], gcd_from_left[i - 1])
A = A[::-1]
gcd_from_right[1] = A[0]
for i in range(2, N + 1):
    gcd_from_right[i] = gcd(A[i - 1], gcd_from_right[i - 1])

ans = 0
for i in range(1, N + 1): # 抜かすやつのindex
    if i == 1:
        ans = max(ans, gcd_from_right[N - i])
    elif i == N:
        ans = max(ans, gcd_from_left[i - 1])
    else:
        ans = max(ans, gcd(gcd_from_left[i - 1], gcd_from_right[N - i]))
print(ans)