import sys
import numpy as np


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


input = sys.stdin.buffer.readline
N = int(input())
A = np.array(sorted(list(map(int, input().split()))))
# print(f'{A=}')

L = [0] * (N + 1)
R = [0] * (N + 1)
M = [0] * N

for i in range(N):
    L[i + 1] = gcd(L[i], A[i])
# print(f'{L=}')

for i in range(N - 1, -1, -1):
    R[i] = gcd(R[i + 1], A[i])
# print(f'{R=}')

for i in range(N):
    M[i] = gcd(L[i], R[i + 1])
# print(f'{M=}')
ans = max(M)
print(ans)
