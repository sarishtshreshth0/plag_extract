import sys
from fractions import gcd

N = int(input())
input = sys.stdin.readline().rstrip()
A = list(map(int, input.split()))

L = [0] * N  # 左からi番目までのgcdをメモった配列
R = [0] * N  # 右からi番目までのgcdをメモった配列
L[0] = A[0]
R[0] = A[N - 1]
for i in range(1, N):
    L[i] = gcd(L[i - 1], A[i])
    R[i] = gcd(R[i - 1], A[N - 1 - i])

ans = 0
for i in range(N - 2):
    ans = max(ans, gcd(L[i], R[N - i - 3]))
ans = max(ans, R[N - 2])
ans = max(ans, L[N - 2])
print(ans)