import sys
import math


N, X = map(int, input().split())
A = list(map(int, input().split()))

A.append(X)
A = sorted(A)

anslis = [0]*N
for i in range(N):
    anslis[i] = A[i+1] - A[i]

g = anslis.pop(0)
for c in anslis:
    g = math.gcd(g,c)

print(g)