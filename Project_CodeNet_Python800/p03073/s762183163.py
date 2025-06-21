#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

S = input()

count = 0
for i, s in enumerate(S):
    if i % 2 and s == S[0]:
        count += 1
    if i % 2 == 0 and s != S[0]:
        count += 1

if count > len(S):
    count = len(S) - count

print(count)

