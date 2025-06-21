import sys
from fractions import gcd
sys.setrecursionlimit(500000)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def main():
    N = ii()
    A = list(mi())

    L = [0]*N
    R = [0]*N
    L[1] = A[0]
    R[N-2] = A[N-1]

    M = [0]*N

    for i in range(N-2):
        L[i+2] = gcd(L[i+1], A[i+1])
    for i in range(N-2, 0, -1):
        R[i-1] = gcd(R[i], A[i])

    for i in range(N):
        if L[i] == 0:
            M[i] = R[i]
        elif R[i] == 0:
            M[i] = L[i]
        else:
            M[i] = gcd(R[i], L[i])
    
    print(max(M))



if __name__ == '__main__':
    main()
