#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

A, B = map(int, input().split())
S = input()

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

flag = "Yes"
for i in range(A):
    if S[i] not in num:
        flag = "No"

if S[A] != '-':
    flag = "No"

for j in range(B):
    if S[j+A+1] not in num:
        flag = "No"

print(flag)