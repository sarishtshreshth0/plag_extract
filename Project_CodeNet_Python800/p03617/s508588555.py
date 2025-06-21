import sys, math
from functools import lru_cache
sys.setrecursionlimit(10**9)
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

Q, H, S, D = mi()
N = ii()

x = min(
    8*Q, 6*Q+H, 4*Q+2*H, 2*Q+3*H, 4*H,
    4*Q+S, 2*Q+H+S, 2*H+S, 2*S, D
)
y = min(4*Q, 2*Q+H, 2*H, S)

if N%2 == 0:
    print(x*(N//2))
else:
    print(x*(N//2)+y)


