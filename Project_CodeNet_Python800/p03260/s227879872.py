# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

A, B = lr()
bl = (A*B)&1
print('Yes' if bl else 'No')
