# -*- coding: utf-8 -*-
n, a, b = map(int, input().split())
s = list(input())

cnt_a = 0
cnt_b = 0

for p in s:
    if p == 'a':
        if (cnt_a+cnt_b) < (a+b):
            print('Yes')
            cnt_a += 1
        else:
            print('No')
    elif p == 'b':
        if (cnt_a+cnt_b) < (a+b) and cnt_b < b:
            print('Yes')
            cnt_b += 1
        else:
            print('No')
    else:
        print('No')
