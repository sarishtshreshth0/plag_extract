import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
A = LI()

from fractions import gcd

L = [0]*N  # L[i] = A[0]からA[i]までの最大公約数
R = [0]*N  # R[i] = A[i]からA[N-1]までの最大公約数

for i in range(N-1):
    if i == 0:
        L[i] = A[i]
        R[N-1-i] = A[N-1-i]
    else:
        L[i] = gcd(L[i-1],A[i])
        R[N-1-i] = gcd(R[N-i],A[N-1-i])

a = max(L[N-2],R[1])

if N == 2:
    print(a)
else:
    print(max(a,max(gcd(L[i],R[i+2]) for i in range(N-2))))