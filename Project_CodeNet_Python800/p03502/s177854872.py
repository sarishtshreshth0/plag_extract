#!/usr/bin/env python3
n = input()
arr = [int(c) for c in n]

if int(n) % sum(arr) == 0:
    print('Yes')
else:
    print('No')