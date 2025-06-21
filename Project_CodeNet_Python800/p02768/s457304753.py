#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, a, b = map(int, input().split())

MOD = 10**9 + 7
# 二項展開より 2**n - 1 - nCa - nCb を MOD 10**9 + 7 で求めればよい


def combination(n, a):
    # nCk = n! / k! (n-k)! のうち、 n!/(n-k)! を計算する
    res = 1
    div = 1
    for i in range(a):
        res *= n-i
        res %= MOD
        div *= a - i
        div %= MOD

    # print(f'n {n}, a {a}, res {res}, div {div}')
    res = (res * pow(div, MOD-2, MOD)) % MOD
    return res


count = (pow(2, n, MOD) - 1 - combination(n, a) - combination(n, b)) % MOD
print(count)
