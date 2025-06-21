# -*- coding: utf-8 -*-

S = input()

ans = False
if len(S) >= 4:
    if S[:4] == 'YAKI':
        ans = True

print('Yes' if ans else 'No')
