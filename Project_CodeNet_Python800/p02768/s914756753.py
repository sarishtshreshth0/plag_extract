import sys
import itertools
# import numpy as np
import time
import math

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MAX = 2 * 10 ** 5 + 5
MOD = 10 ** 9 + 7

fac = [0 for i in range(MAX)]
finv = [0 for i in range(MAX)]
inv = [0 for i in range(MAX)]

def comInit(mod):
    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod

def com(mod, n, k):
    numerator = 1
    for i in range(1, k + 1):
        numerator *= (n - i + 1)
        numerator %= mod
    return (numerator * finv[k] % mod)
comInit(MOD)

n, a, b = map(int, readline().split())
nb = n
x = 2
y = 1
while n > 1:
    if n % 2 == 1:
        y *= x
        n -= 1
    else:
        x *= x
        n //= 2
    x %= MOD
    y %= MOD
ans = (x * y % MOD) - 1
print((ans - com(MOD, nb, a) - com(MOD, nb, b)) % MOD)