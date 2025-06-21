import math

N = int(input())
a = list(input().split())
A = [int(a[i])for i in range(N)]

L = [0 for i in range(N+1)]
R = [0 for i in range(N+1)]

for i in range(N):
    L[i+1] = math.gcd(L[i], A[i])
    R[N - (i+1)] = math.gcd(R[N - i], A[N - (i+1)])

print(max([math.gcd(L[i], R[i+1]) for i in range(N)]))