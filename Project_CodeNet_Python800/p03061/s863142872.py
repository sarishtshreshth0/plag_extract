from math import gcd as gcd
import numpy as np
N = int(input())
A = list(map(int,input().split()))

A = [0] + A + [0]

fromleft = np.array([0]*N)
fromright = np.array([0]*N)

for i in range(1,N):
    fromleft[i] = gcd(A[i],fromleft[i-1])
    fromright[-(i+1)] = gcd(A[-(i+1)],fromright[-i])

#print(fromleft)
#print(fromright)

ansgcd = [0]*N

for i in range(N):
    ansgcd[i] = gcd(fromright[i], fromleft[i])

print(max(ansgcd))