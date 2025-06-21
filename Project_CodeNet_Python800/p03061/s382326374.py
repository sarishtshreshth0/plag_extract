# -*- coding: utf-8 -*-
#C - GCD on Blackboard
import sys 
from math import gcd
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
A = [0] + list(map(int, readline().split()))
# L(i) := A1, A2, ..., Ai-1の最大公約数
# R(i) := Ai, Ai+1, ..., ANの最大公約数
L = [0]*(N+1)
L[0] = 0
R = [0]*(N+2)
R[N+1] = 0

for i in range(1,N+1):
    L[i] = gcd(L[i-1],A[i])
for i in range(N,-1,-1):
    R[i] = gcd(R[i+1],A[i])

ans = 1
for i in range(N):
    m = gcd(L[i],R[i+2])
    ans = max(m,ans)
print(ans)