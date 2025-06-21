import sys

def S(): return sys.stdin.readline().rstrip()

A,B = map(int,S().split())

def f(n):  # 0からnまでのxor
    res = 0
    while n % 4 != 3:
        res ^= n
        n -= 1
    return res

print(f(B) ^ f(A-1))